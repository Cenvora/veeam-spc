import pytest
from veeam_spc.v3_5_1 import AuthenticatedClient
from veeam_spc.v3_5_1.api.about import get_about_information

BASE_URL = "https://server:1280/api/v3"
API_TOKEN = "SuperSecretKey"  # Replace with a valid token for real tests


@pytest.fixture
def client():
    return AuthenticatedClient(base_url=BASE_URL, token=API_TOKEN)


def test_get_about_information_sync(client):
    response = get_about_information.sync(client=client)
    print("Response:", response)
    assert response is not None
    assert response.data is not None
    assert getattr(response.data, "server_version", None)


def test_get_about_information_sync_detailed(client):
    detailed = get_about_information.sync_detailed(client=client)
    print("Detailed Response:", detailed)
    assert detailed is not None
    assert detailed.status_code == 200
    assert detailed.parsed is not None
    assert detailed.parsed.data is not None
    assert getattr(detailed.parsed.data, "server_version", None)
    assert getattr(detailed.parsed.data, "installation_id", None)
    assert getattr(detailed.parsed.data, "installation_date", None)
    assert getattr(detailed.parsed.data, "actual_vaw_version", None)
    assert getattr(detailed.parsed.data, "actual_val_version", None)
    assert getattr(detailed.parsed.data, "actual_vam_version", None)
    assert getattr(detailed.parsed.data, "windows_management_agent_version", None)
    assert getattr(detailed.parsed.data, "linux_management_agent_version", None)
    assert getattr(detailed.parsed.data, "mac_management_agent_version", None)


# For async tests, you can use pytest-asyncio
# import pytest_asyncio
# @pytest.mark.asyncio
# async def test_get_about_information_async(client):
#     response = await get_about_information.asyncio(client=client)
#     assert response is not None
#     assert hasattr(response, "version")
#     assert hasattr(response, "title")
