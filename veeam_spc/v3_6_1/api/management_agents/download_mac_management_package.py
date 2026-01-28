from http import HTTPStatus
from io import BytesIO
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.download_mac_management_package_package_type import DownloadMacManagementPackagePackageType
from ...models.error_response import ErrorResponse
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    *,
    organization_uid: Union[Unset, UUID] = UNSET,
    location_uid: Union[Unset, UUID] = UNSET,
    cloud_tenant_uid: Union[Unset, UUID] = UNSET,
    token_expiry_period_days: Union[Unset, int] = 365,
    package_type: Union[Unset, DownloadMacManagementPackagePackageType] = DownloadMacManagementPackagePackageType.ZIP,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    json_organization_uid: Union[Unset, str] = UNSET
    if not isinstance(organization_uid, Unset):
        json_organization_uid = str(organization_uid)
    params["organizationUid"] = json_organization_uid

    json_location_uid: Union[Unset, str] = UNSET
    if not isinstance(location_uid, Unset):
        json_location_uid = str(location_uid)
    params["locationUid"] = json_location_uid

    json_cloud_tenant_uid: Union[Unset, str] = UNSET
    if not isinstance(cloud_tenant_uid, Unset):
        json_cloud_tenant_uid = str(cloud_tenant_uid)
    params["cloudTenantUid"] = json_cloud_tenant_uid

    params["tokenExpiryPeriodDays"] = token_expiry_period_days

    json_package_type: Union[Unset, str] = UNSET
    if not isinstance(package_type, Unset):
        json_package_type = package_type.value

    params["packageType"] = json_package_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/infrastructure/managementAgents/packages/mac",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, ErrorResponse, File]:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 520:
        response_520 = ErrorResponse.from_dict(response.json())

        return response_520

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorResponse, File]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    organization_uid: Union[Unset, UUID] = UNSET,
    location_uid: Union[Unset, UUID] = UNSET,
    cloud_tenant_uid: Union[Unset, UUID] = UNSET,
    token_expiry_period_days: Union[Unset, int] = 365,
    package_type: Union[Unset, DownloadMacManagementPackagePackageType] = DownloadMacManagementPackagePackageType.ZIP,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, File]]:
    """Download Management Agent Setup File for macOS.

     Returns a download link to a management agent setup file in the shell script format for macOS
    computers.

    Args:
        organization_uid (Union[Unset, UUID]):
        location_uid (Union[Unset, UUID]):
        cloud_tenant_uid (Union[Unset, UUID]):
        token_expiry_period_days (Union[Unset, int]):  Default: 365.
        package_type (Union[Unset, DownloadMacManagementPackagePackageType]):  Default:
            DownloadMacManagementPackagePackageType.ZIP.
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, File]]
    """

    kwargs = _get_kwargs(
        organization_uid=organization_uid,
        location_uid=location_uid,
        cloud_tenant_uid=cloud_tenant_uid,
        token_expiry_period_days=token_expiry_period_days,
        package_type=package_type,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    organization_uid: Union[Unset, UUID] = UNSET,
    location_uid: Union[Unset, UUID] = UNSET,
    cloud_tenant_uid: Union[Unset, UUID] = UNSET,
    token_expiry_period_days: Union[Unset, int] = 365,
    package_type: Union[Unset, DownloadMacManagementPackagePackageType] = DownloadMacManagementPackagePackageType.ZIP,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, File]]:
    """Download Management Agent Setup File for macOS.

     Returns a download link to a management agent setup file in the shell script format for macOS
    computers.

    Args:
        organization_uid (Union[Unset, UUID]):
        location_uid (Union[Unset, UUID]):
        cloud_tenant_uid (Union[Unset, UUID]):
        token_expiry_period_days (Union[Unset, int]):  Default: 365.
        package_type (Union[Unset, DownloadMacManagementPackagePackageType]):  Default:
            DownloadMacManagementPackagePackageType.ZIP.
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, File]
    """

    return sync_detailed(
        client=client,
        organization_uid=organization_uid,
        location_uid=location_uid,
        cloud_tenant_uid=cloud_tenant_uid,
        token_expiry_period_days=token_expiry_period_days,
        package_type=package_type,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    organization_uid: Union[Unset, UUID] = UNSET,
    location_uid: Union[Unset, UUID] = UNSET,
    cloud_tenant_uid: Union[Unset, UUID] = UNSET,
    token_expiry_period_days: Union[Unset, int] = 365,
    package_type: Union[Unset, DownloadMacManagementPackagePackageType] = DownloadMacManagementPackagePackageType.ZIP,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, File]]:
    """Download Management Agent Setup File for macOS.

     Returns a download link to a management agent setup file in the shell script format for macOS
    computers.

    Args:
        organization_uid (Union[Unset, UUID]):
        location_uid (Union[Unset, UUID]):
        cloud_tenant_uid (Union[Unset, UUID]):
        token_expiry_period_days (Union[Unset, int]):  Default: 365.
        package_type (Union[Unset, DownloadMacManagementPackagePackageType]):  Default:
            DownloadMacManagementPackagePackageType.ZIP.
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, File]]
    """

    kwargs = _get_kwargs(
        organization_uid=organization_uid,
        location_uid=location_uid,
        cloud_tenant_uid=cloud_tenant_uid,
        token_expiry_period_days=token_expiry_period_days,
        package_type=package_type,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    organization_uid: Union[Unset, UUID] = UNSET,
    location_uid: Union[Unset, UUID] = UNSET,
    cloud_tenant_uid: Union[Unset, UUID] = UNSET,
    token_expiry_period_days: Union[Unset, int] = 365,
    package_type: Union[Unset, DownloadMacManagementPackagePackageType] = DownloadMacManagementPackagePackageType.ZIP,
    x_request_id: Union[Unset, UUID] = UNSET,
    x_client_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, File]]:
    """Download Management Agent Setup File for macOS.

     Returns a download link to a management agent setup file in the shell script format for macOS
    computers.

    Args:
        organization_uid (Union[Unset, UUID]):
        location_uid (Union[Unset, UUID]):
        cloud_tenant_uid (Union[Unset, UUID]):
        token_expiry_period_days (Union[Unset, int]):  Default: 365.
        package_type (Union[Unset, DownloadMacManagementPackagePackageType]):  Default:
            DownloadMacManagementPackagePackageType.ZIP.
        x_request_id (Union[Unset, UUID]):
        x_client_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, File]
    """

    return (
        await asyncio_detailed(
            client=client,
            organization_uid=organization_uid,
            location_uid=location_uid,
            cloud_tenant_uid=cloud_tenant_uid,
            token_expiry_period_days=token_expiry_period_days,
            package_type=package_type,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
