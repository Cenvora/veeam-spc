import pytest
from veeam_spc.v3_6 import AuthenticatedClient
from veeam_spc.v3_6.api.about import get_about_information

BASE_URL = "https://vspc/api/v3"
API_TOKEN = "TOKEN_HERE"  # Replace with a valid token for real tests


@pytest.fixture
def client():
    return AuthenticatedClient(base_url=BASE_URL, token=API_TOKEN)


def test_get_about_information_sync(client):
    response = get_about_information.sync(client=client)
    assert response is not None
    # Optionally check for expected keys/values in response
    assert hasattr(response, "version")
    assert hasattr(response, "title")


def test_get_about_information_sync_detailed(client):
    detailed = get_about_information.sync_detailed(client=client)
    assert detailed is not None
    assert detailed.status_code == 200
    assert detailed.parsed is not None
    assert hasattr(detailed.parsed, "version")
    assert hasattr(detailed.parsed, "title")


# For async tests, you can use pytest-asyncio
# import pytest_asyncio
# @pytest.mark.asyncio
# async def test_get_about_information_async(client):
#     response = await get_about_information.asyncio(client=client)
#     assert response is not None
#     assert hasattr(response, "version")
#     assert hasattr(response, "title")
