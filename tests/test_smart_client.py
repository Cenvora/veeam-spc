import pytest
from veeam_spc.client import VeeamClient

# These are integration tests - they require a live VSPC instance
# Replace with actual values or use environment variables for real testing

BASE_URL = "https://vspc:1280"
USERNAME = "administrator"
PASSWORD = "password"
TOKEN = "sample_token_here"
API_VERSION = "3.6"


@pytest.mark.asyncio
async def test_veeam_client_init_with_password():
    """Test that VeeamClient can be initialized with username/password"""
    client = VeeamClient(
        host=BASE_URL,
        username=USERNAME,
        password=PASSWORD,
        api_version=API_VERSION,
        verify_ssl=False,
    )
    assert client.host == "https://vspc:1280"
    assert client.username == USERNAME
    assert client.password == PASSWORD
    assert client.token is None
    assert client.api_version == API_VERSION
    assert client.package == "veeam_spc.v3_6"


@pytest.mark.asyncio
async def test_veeam_client_init_with_token():
    """Test that VeeamClient can be initialized with a token"""
    client = VeeamClient(
        host=BASE_URL,
        token=TOKEN,
        api_version=API_VERSION,
        verify_ssl=False,
    )
    assert client.host == "https://vspc:1280"
    assert client.username is None
    assert client.password is None
    assert client.token == TOKEN
    assert client.api_version == API_VERSION
    assert client.package == "veeam_spc.v3_6"


@pytest.mark.asyncio
async def test_veeam_client_missing_credentials():
    """Test that VeeamClient raises an error when no credentials provided"""
    with pytest.raises(ValueError, match="Must provide either 'token' or both 'username' and 'password'"):
        VeeamClient(
            host=BASE_URL,
            api_version=API_VERSION,
            verify_ssl=False,
        )


@pytest.mark.asyncio
async def test_veeam_client_incomplete_credentials():
    """Test that VeeamClient raises an error when only username is provided"""
    with pytest.raises(ValueError, match="Must provide either 'token' or both 'username' and 'password'"):
        VeeamClient(
            host=BASE_URL,
            username=USERNAME,
            api_version=API_VERSION,
            verify_ssl=False,
        )


@pytest.mark.asyncio
async def test_veeam_client_invalid_version():
    """Test that VeeamClient raises an error for invalid API version"""
    with pytest.raises(ValueError, match="Unsupported API version"):
        VeeamClient(
            host=BASE_URL,
            username=USERNAME,
            password=PASSWORD,
            api_version="99.99",
            verify_ssl=False,
        )


@pytest.mark.asyncio
async def test_veeam_client_host_normalization():
    """Test that host URL is normalized correctly"""
    # Test with trailing slash
    client1 = VeeamClient(
        host="https://vspc:1280/",
        username=USERNAME,
        password=PASSWORD,
        api_version=API_VERSION,
        verify_ssl=False,
    )
    assert client1.host == "https://vspc:1280"

    # Test with /api/v3 suffix
    client2 = VeeamClient(
        host="https://vspc:1280/api/v3",
        username=USERNAME,
        password=PASSWORD,
        api_version=API_VERSION,
        verify_ssl=False,
    )
    assert client2.host == "https://vspc:1280"

    # Test with /api suffix
    client3 = VeeamClient(
        host="https://vspc:1280/api",
        username=USERNAME,
        password=PASSWORD,
        api_version=API_VERSION,
        verify_ssl=False,
    )
    assert client3.host == "https://vspc:1280"


@pytest.mark.asyncio
async def test_api_namespace_access():
    """Test that API namespace can be accessed"""
    client = VeeamClient(
        host=BASE_URL,
        username=USERNAME,
        password=PASSWORD,
        api_version=API_VERSION,
        verify_ssl=False,
    )

    # Test namespace access
    namespace = client.api("provider")
    assert namespace is not None
    assert hasattr(namespace, "_client")
    assert hasattr(namespace, "_base")


# Integration tests (these require a live VSPC instance and valid credentials)
# Uncomment and modify when running against a real instance

# @pytest.mark.asyncio
# @pytest.mark.integration
# async def test_veeam_client_connect():
#     """Test connecting to VSPC and getting a token"""
#     client = VeeamClient(
#         host=BASE_URL,
#         username=USERNAME,
#         password=PASSWORD,
#         api_version=API_VERSION,
#         verify_ssl=False,
#     )
#
#     await client.connect()
#
#     assert client._access_token is not None
#     assert client._refresh_token is not None
#     assert client._expires_at is not None
#
#     await client.close()


# @pytest.mark.asyncio
# @pytest.mark.integration
# async def test_veeam_client_call_api():
#     """Test calling an API endpoint through the smart client"""
#     client = VeeamClient(
#         host=BASE_URL,
#         username=USERNAME,
#         password=PASSWORD,
#         api_version=API_VERSION,
#         verify_ssl=False,
#     )
#
#     await client.connect()
#
#     # Call the about API to get version info
#     about_info = await client.call(
#         client.api("about.get_about_information")
#     )
#
#     assert about_info is not None
#     assert hasattr(about_info, "version")
#     assert hasattr(about_info, "title")
#
#     await client.close()


# @pytest.mark.asyncio
# @pytest.mark.integration
# async def test_veeam_client_namespace_api_call():
#     """Test calling an API endpoint using namespace notation"""
#     client = VeeamClient(
#         host=BASE_URL,
#         username=USERNAME,
#         password=PASSWORD,
#         api_version=API_VERSION,
#         verify_ssl=False,
#     )
#
#     await client.connect()
#
#     # Call using namespace
#     about_info = await client.call(
#         client.api("about").get_about_information
#     )
#
#     assert about_info is not None
#     assert hasattr(about_info, "version")
#
#     await client.close()
