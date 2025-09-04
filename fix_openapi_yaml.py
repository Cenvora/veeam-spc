import re
import sys

# Usage: python fix_response_keys.py <input_yaml> <output_yaml>


def fix_response_keys(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()
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
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(fixed)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python fix_response_keys.py <input_yaml> <output_yaml>")
        sys.exit(1)
    fix_response_keys(sys.argv[1], sys.argv[2])
