import json
import re
import sys
from typing import Any, cast

# Usage: python fix_openapi_yaml.py <input_file> <output_file>
# Supports both YAML and JSON OpenAPI specs.


def add_missing_multi_action_result(data: dict[str, Any]) -> None:
    """Define MultiActionResult when the spec references it without shipping it.

    Veeam's 3.7 document returns ``MultiActionResult`` from three bulk delete endpoints
    (RemoveCloudBackup, DeleteProtectedVirtualMachineBackup,
    DeleteProtectedComputerManagedByBackupServerBackup) but has no such definition, so a
    generator resolving refs stops there.

    The shape below is not invented: it is the response example the same document carries for
    those endpoints, typed against the ``Result`` schema it already defines — the example's
    per-item fields (status, success, message, objectName, objectId) are exactly Result's.
    Added only when it is genuinely absent, so a later release that ships it wins.
    """
    schemas_any = data.get("components", {}).get("schemas")
    if not isinstance(schemas_any, dict):
        return

    schemas = cast(dict[str, Any], schemas_any)
    if "MultiActionResult" in schemas:
        return

    if "#/components/schemas/MultiActionResult" not in json.dumps(data):
        return

    item_schema: dict[str, Any] = (
        {"$ref": "#/components/schemas/Result"}
        if "Result" in schemas
        else {
            "type": "object",
            "properties": {
                "status": {"type": "string"},
                "success": {"type": "boolean"},
                "message": {"type": "string", "nullable": True},
                "objectName": {"type": "string"},
                "objectId": {"type": "string"},
            },
        }
    )

    schemas["MultiActionResult"] = {
        "type": "object",
        "description": (
            "Result of an operation performed on multiple objects. Reconstructed from the "
            "response example in the source document, which references this schema without "
            "defining it."
        ),
        "properties": {
            "results": {"type": "array", "items": item_schema},
            "message": {"type": "string", "nullable": True},
            "status": (
                {"$ref": "#/components/schemas/EActionResultStatus"}
                if "EActionResultStatus" in schemas
                else {"type": "string"}
            ),
            "isMultiActionResult": {"type": "boolean"},
        },
    }


def fix_response_keys(input_path: str, output_path: str) -> None:
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    def redact_secret_text(value: str) -> str:
        # Redact Google OAuth-like secrets and client IDs that trigger push protection.
        redacted = re.sub(r"GOCSPX-[A-Za-z0-9_-]+", "REDACTED_CLIENT_SECRET", value)
        redacted = re.sub(
            r"\b\d{8,}-[A-Za-z0-9-]+\.apps\.googleusercontent\.com\b",
            "REDACTED_CLIENT_ID",
            redacted,
        )
        redacted = re.sub(
            r"(client_id=)[^&\s\"]+",
            r"\1REDACTED_CLIENT_ID",
            redacted,
        )
        return redacted

    content = redact_secret_text(content)

    # For JSON OpenAPI specs, fix schema nodes that are null in schema positions
    # (for example, under properties) because openapi-python-client expects objects.
    if input_path.lower().endswith(".json"):
        data = json.loads(content)

        unsupported_media_types = {
            "application/pdf",
            "application/csv",
            "application/xml",
            "application/binary+base64",
        }

        schema_container_keys = {
            "schema",
            "items",
            "additionalProperties",
            "not",
        }
        schema_array_keys = {"allOf", "anyOf", "oneOf"}

        def fix_null_schema_nodes(node: Any) -> None:
            if isinstance(node, dict):
                node_dict = cast(dict[str, Any], node)

                # Normalize unsupported media types to application/octet-stream
                # so openapi-python-client can keep endpoints instead of dropping them.
                content_any = node_dict.get("content")
                if isinstance(content_any, dict):
                    content_dict = cast(dict[str, Any], content_any)
                    octet_stream = content_dict.get("application/octet-stream")
                    for media_type in list(content_dict.keys()):
                        if media_type in unsupported_media_types:
                            media_def = content_dict.pop(media_type)
                            if octet_stream is None:
                                content_dict["application/octet-stream"] = media_def
                                octet_stream = media_def

                # Replace missing schema ref with an inline fallback schema.
                if (
                    node_dict.get("$ref")
                    == "#/components/schemas/PermissionsEntityType"
                ):
                    node_dict.pop("$ref", None)
                    node_dict["type"] = "string"
                    node_dict["description"] = (
                        "Type of a Veeam Service Provider Console entity."
                    )

                # Collapse JSON Schema nullable unions (e.g. ["string", "null"]) to
                # OpenAPI-compatible representation for openapi-python-client.
                type_any = node_dict.get("type")
                if isinstance(type_any, list):
                    type_list = [t for t in type_any if isinstance(t, str)]
                    if "null" in type_list:
                        non_null_types = [t for t in type_list if t != "null"]
                        if len(non_null_types) == 1:
                            node_dict["type"] = non_null_types[0]
                            node_dict["nullable"] = True

                # Every value in `properties` must be a schema object.
                props_any = node_dict.get("properties")
                if isinstance(props_any, dict):
                    props = cast(dict[str, Any], props_any)
                    for prop_name, prop_schema in props.items():
                        if prop_schema is None:
                            props[prop_name] = {}
                        else:
                            fix_null_schema_nodes(prop_schema)

                for key, value in node_dict.items():
                    if key == "properties":
                        continue

                    if key in schema_container_keys and value is None:
                        node_dict[key] = {}
                        continue

                    if key in schema_container_keys:
                        fix_null_schema_nodes(value)
                        continue

                    if key in schema_array_keys and isinstance(value, list):
                        schemas = cast(list[Any], value)
                        for index, schema in enumerate(schemas):
                            if schema is None:
                                schemas[index] = {}
                            else:
                                fix_null_schema_nodes(schema)
                        continue

                    fix_null_schema_nodes(value)

            elif isinstance(node, list):
                node_list = cast(list[Any], node)
                for item in node_list:
                    fix_null_schema_nodes(item)

        fix_null_schema_nodes(data)

        add_missing_multi_action_result(data)

        # openapi-python-client (0.28.x) can fail on SmtpSettings when the parent
        # object itself is nullable. Keep field-level nullability intact.
        schemas_any = data.get("components", {}).get("schemas", {})
        if isinstance(schemas_any, dict):
            smtp_settings = schemas_any.get("SmtpSettings")
            if isinstance(smtp_settings, dict):
                smtp_settings.pop("nullable", None)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
            f.write("\n")
        return

    # Replace response keys like 'responses:\n    200:' with 'responses:\n    "200":'
    fixed = re.sub(r"(responses:\s*)(\d+):", r'\1"\2":', content)
    # Also fix indented response keys (for nested paths)
    fixed = re.sub(r"(\n\s+)(\d+):", r'\1"\2":', fixed)
    # Replace unsupported content types with application/octet-stream
    fixed = re.sub(
        r"(application/pdf|application/csv|application/xml)",
        "application/octet-stream",
        fixed,
    )
    # Quote version numbers (e.g., version: 3.6, 3.6.1, 3.5.1 to version: "3.6", "3.6.1", "3.5.1")
    fixed = re.sub(r"(version:\s*)([0-9]+(?:\.[0-9]+)+)", r'\1"\2"', fixed)

    def convert_nullable_scalar_type_unions(value: str) -> str:
        scalar_types = {"string", "integer", "number", "boolean"}

        def replace_inline(match: re.Match[str]) -> str:
            indent = match.group("indent")
            first = match.group("first")
            second = match.group("second")
            comment = match.group("comment") or ""
            items = [first, second]
            primitive = next((item for item in items if item in scalar_types), None)
            if primitive is None or "null" not in items:
                return match.group(0)
            return f"{indent}type: {primitive}{comment}\n{indent}nullable: true"

        inline_pattern = re.compile(
            r"^(?P<indent>\s*)type:\s*\[\s*(?P<first>string|integer|number|boolean|null)\s*,\s*(?P<second>string|integer|number|boolean|null)\s*\]\s*(?P<comment>#.*)?$",
            flags=re.MULTILINE,
        )
        value = inline_pattern.sub(replace_inline, value)

        def replace_multiline(match: re.Match[str]) -> str:
            indent = match.group("indent")
            first = match.group("first")
            second = match.group("second")
            items = [first, second]
            primitive = next((item for item in items if item in scalar_types), None)
            if primitive is None or "null" not in items:
                return match.group(0)
            return f"{indent}type: {primitive}\n{indent}nullable: true"

        multiline_pattern = re.compile(
            r"^(?P<indent>\s*)type:\s*(?:#.*)?\n"
            r"(?P<item_indent>\s+)-\s*(?P<first>string|integer|number|boolean|null)\s*(?:#.*)?\n"
            r"(?P=item_indent)-\s*(?P<second>string|integer|number|boolean|null)\s*(?:#.*)?$",
            flags=re.MULTILINE,
        )
        return multiline_pattern.sub(replace_multiline, value)

    # Convert YAML type unions like `type: [string, null]` into OpenAPI style
    # while preserving nullability semantics for common scalar unions.
    fixed = convert_nullable_scalar_type_unions(fixed)
    fixed = redact_secret_text(fixed)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(fixed)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python fix_openapi_yaml.py <input_file> <output_file>")
        sys.exit(1)
    fix_response_keys(sys.argv[1], sys.argv[2])
