"""Tests for the 3.7 package.

Two things are worth pinning for this version specifically.

Veeam shipped 3.7 as a Swagger 2.0 document rather than the OpenAPI 3 one every earlier
version came as, so the package is generated from a converted spec — these assert the
conversion produced a package shaped like its predecessors.

And that document references a MultiActionResult schema it never defines. fix_openapi_yaml.py
reconstructs it from the response example alongside it, so the three endpoints returning it
parse rather than failing on an unresolved model.
"""

import importlib

import pytest

from veeam_spc.client import VeeamClient
from veeam_spc.versions import VERSION_TO_PACKAGE

API_VERSION = "3.7"
PACKAGE = "veeam_spc.v3_7"


def test_the_version_is_routable():
    assert VERSION_TO_PACKAGE[API_VERSION] == PACKAGE

    client = VeeamClient(
        host="https://vspc.example.com:1280",
        token="token",  # noqa: S106 - placeholder, no connection is made
        api_version=API_VERSION,
    )

    assert client.package == PACKAGE


@pytest.mark.parametrize(
    "module",
    ["client", "types", "errors", "models", "api"],
)
def test_the_package_has_the_same_shape_as_its_predecessors(module):
    """The spec arrived in a different format; the generated package should not differ."""
    assert importlib.import_module(f"{PACKAGE}.{module}")


def test_about_reports_the_console_version():
    """The endpoint version detection depends on, and the one the smart client documents."""
    from veeam_spc.v3_7.api.about import get_about_information
    from veeam_spc.v3_7.models import About

    assert hasattr(get_about_information, "asyncio")
    assert hasattr(get_about_information, "sync")

    about = About.from_dict(
        {
            "serverVersion": "9.3.0.35057",
            "installationId": "0b47bb94-fd6c-4dda-8143-0f5c0bd65405",
        }
    )

    assert about.server_version == "9.3.0.35057"


def test_x_client_version_is_still_a_parameter():
    """VSPC negotiates by header rather than by URL, so every operation takes this."""
    from veeam_spc.v3_7.api.about import get_about_information

    import inspect

    signature = inspect.signature(get_about_information.asyncio)

    assert "x_client_version" in signature.parameters


# ---------------------------------------------------------------------------
# MultiActionResult: referenced by the source document, never defined in it
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "module",
    [
        "cloud_connect.remove_cloud_backup",
        "protected_workloads.delete_protected_virtual_machine_backup",
        "protected_workloads.delete_protected_computer_managed_by_backup_server_backup",
    ],
)
def test_the_bulk_delete_endpoints_exist(module):
    """Without the reconstructed schema these three would have been dropped."""
    operation = importlib.import_module(f"{PACKAGE}.api.{module}")

    assert hasattr(operation, "asyncio")


def test_a_multi_action_response_parses():
    """Shaped exactly like the response example Veeam ships for these endpoints."""
    from veeam_spc.v3_7.models import RemoveCloudBackupResponse200

    response = RemoveCloudBackupResponse200.from_dict(
        {
            "data": {
                "results": [
                    {
                        "status": "success",
                        "success": True,
                        "message": "The backup was successfully deleted.",
                        "objectName": "Backup Job_vbr01.tech.local",
                        "objectId": "8f3a1d2e-6b47-4c9a-bf12-2a7c9e4d3b18",
                    }
                ],
                "message": None,
                "status": "success",
                "isMultiActionResult": True,
            }
        }
    )

    assert response.data.is_multi_action_result is True
    result = response.data.results[0]
    assert result.success is True
    assert result.object_name == "Backup Job_vbr01.tech.local"


def test_a_multi_action_result_tolerates_a_null_message():
    """The example itself reports message: null on success."""
    from veeam_spc.v3_7.models import MultiActionResult

    parsed = MultiActionResult.from_dict({"results": [], "message": None})

    assert parsed.results == []


def test_the_results_are_typed_as_the_shared_result_schema():
    """The reconstruction reuses Result rather than inventing a parallel shape."""
    from veeam_spc.v3_7.models import MultiActionResult, Result

    parsed = MultiActionResult.from_dict(
        {"results": [{"status": "success", "success": True}]}
    )

    assert isinstance(parsed.results[0], Result)


# ---------------------------------------------------------------------------
# What 3.7 adds over 3.6.2
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "module",
    [
        "labels.create_label",
        "preview_operations.create_webhook",
        "configuration.create_syslog_target",
    ],
)
def test_operations_new_in_3_7_are_present(module):
    """A conversion that silently dropped paths would still import; these would not exist."""
    assert importlib.import_module(f"{PACKAGE}.api.{module}")
