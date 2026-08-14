from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_reseller_response_200 import CreateResellerResponse200
from ...models.error_response import ErrorResponse
from ...models.reseller_input import ResellerInput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ResellerInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    params["select"] = select

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/organizations/resellers",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateResellerResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CreateResellerResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateResellerResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ResellerInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateResellerResponse200 | ErrorResponse]:
    """Create Reseller

     Creates a new reseller with specific properties.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (ResellerInput):  Example: {'description': None, 'proPartnerId': None,
            'organizationInput': {'name': 'Atrium Solutions', 'alias': 'atrium', 'taxId': '34598',
            'legalName': 'Atrium Solutions LLC', 'email': 'd.baker@atriumsol.com', 'phone':
            '606-932-3427', 'country': 1, 'state': 38, 'countryName': 'USA', 'regionName': None,
            'city': 'South Shore', 'street': '464 Hinkle Deegan Lake Road', 'locationAdmin0Code':
            'us', 'locationAdmin1Code': 'us-ma', 'locationAdmin2Code': None, 'notes': 'Basic
            configuration', 'zipCode': '41175', 'domain': 'atriumsol.com', 'website':
            'www.atriumsol.com', 'veeamTenantId': '11', 'companyId': None}, 'resellerServices':
            {'hostedServices': {'backupResourcesEnabled': False, 'vb365ManagementEnabled': False,
            'vbPublicCloudManagementEnabled': False}, 'remoteServices': {'backupAgentsManagement':
            {'workstationAgentsQuota': None, 'serverAgentsQuota': None}, 'vb365ManagementEnabled':
            False, 'backupServersManagementEnabled': False, 'vbPublicCloudManagementEnabled': False},
            'cloudConnectQuota': None, 'cloudConnectManagementEnabled': False,
            'isFileLevelRestoreEnabled': False}, 'ownerCredentials': {'userName':
            'ResVcdExternalOwner', 'password': 'Password1'}, 'isRestAccessEnabled': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateResellerResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ResellerInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateResellerResponse200 | ErrorResponse | None:
    """Create Reseller

     Creates a new reseller with specific properties.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (ResellerInput):  Example: {'description': None, 'proPartnerId': None,
            'organizationInput': {'name': 'Atrium Solutions', 'alias': 'atrium', 'taxId': '34598',
            'legalName': 'Atrium Solutions LLC', 'email': 'd.baker@atriumsol.com', 'phone':
            '606-932-3427', 'country': 1, 'state': 38, 'countryName': 'USA', 'regionName': None,
            'city': 'South Shore', 'street': '464 Hinkle Deegan Lake Road', 'locationAdmin0Code':
            'us', 'locationAdmin1Code': 'us-ma', 'locationAdmin2Code': None, 'notes': 'Basic
            configuration', 'zipCode': '41175', 'domain': 'atriumsol.com', 'website':
            'www.atriumsol.com', 'veeamTenantId': '11', 'companyId': None}, 'resellerServices':
            {'hostedServices': {'backupResourcesEnabled': False, 'vb365ManagementEnabled': False,
            'vbPublicCloudManagementEnabled': False}, 'remoteServices': {'backupAgentsManagement':
            {'workstationAgentsQuota': None, 'serverAgentsQuota': None}, 'vb365ManagementEnabled':
            False, 'backupServersManagementEnabled': False, 'vbPublicCloudManagementEnabled': False},
            'cloudConnectQuota': None, 'cloudConnectManagementEnabled': False,
            'isFileLevelRestoreEnabled': False}, 'ownerCredentials': {'userName':
            'ResVcdExternalOwner', 'password': 'Password1'}, 'isRestAccessEnabled': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateResellerResponse200 | ErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ResellerInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateResellerResponse200 | ErrorResponse]:
    """Create Reseller

     Creates a new reseller with specific properties.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (ResellerInput):  Example: {'description': None, 'proPartnerId': None,
            'organizationInput': {'name': 'Atrium Solutions', 'alias': 'atrium', 'taxId': '34598',
            'legalName': 'Atrium Solutions LLC', 'email': 'd.baker@atriumsol.com', 'phone':
            '606-932-3427', 'country': 1, 'state': 38, 'countryName': 'USA', 'regionName': None,
            'city': 'South Shore', 'street': '464 Hinkle Deegan Lake Road', 'locationAdmin0Code':
            'us', 'locationAdmin1Code': 'us-ma', 'locationAdmin2Code': None, 'notes': 'Basic
            configuration', 'zipCode': '41175', 'domain': 'atriumsol.com', 'website':
            'www.atriumsol.com', 'veeamTenantId': '11', 'companyId': None}, 'resellerServices':
            {'hostedServices': {'backupResourcesEnabled': False, 'vb365ManagementEnabled': False,
            'vbPublicCloudManagementEnabled': False}, 'remoteServices': {'backupAgentsManagement':
            {'workstationAgentsQuota': None, 'serverAgentsQuota': None}, 'vb365ManagementEnabled':
            False, 'backupServersManagementEnabled': False, 'vbPublicCloudManagementEnabled': False},
            'cloudConnectQuota': None, 'cloudConnectManagementEnabled': False,
            'isFileLevelRestoreEnabled': False}, 'ownerCredentials': {'userName':
            'ResVcdExternalOwner', 'password': 'Password1'}, 'isRestAccessEnabled': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateResellerResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ResellerInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateResellerResponse200 | ErrorResponse | None:
    """Create Reseller

     Creates a new reseller with specific properties.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (ResellerInput):  Example: {'description': None, 'proPartnerId': None,
            'organizationInput': {'name': 'Atrium Solutions', 'alias': 'atrium', 'taxId': '34598',
            'legalName': 'Atrium Solutions LLC', 'email': 'd.baker@atriumsol.com', 'phone':
            '606-932-3427', 'country': 1, 'state': 38, 'countryName': 'USA', 'regionName': None,
            'city': 'South Shore', 'street': '464 Hinkle Deegan Lake Road', 'locationAdmin0Code':
            'us', 'locationAdmin1Code': 'us-ma', 'locationAdmin2Code': None, 'notes': 'Basic
            configuration', 'zipCode': '41175', 'domain': 'atriumsol.com', 'website':
            'www.atriumsol.com', 'veeamTenantId': '11', 'companyId': None}, 'resellerServices':
            {'hostedServices': {'backupResourcesEnabled': False, 'vb365ManagementEnabled': False,
            'vbPublicCloudManagementEnabled': False}, 'remoteServices': {'backupAgentsManagement':
            {'workstationAgentsQuota': None, 'serverAgentsQuota': None}, 'vb365ManagementEnabled':
            False, 'backupServersManagementEnabled': False, 'vbPublicCloudManagementEnabled': False},
            'cloudConnectQuota': None, 'cloudConnectManagementEnabled': False,
            'isFileLevelRestoreEnabled': False}, 'ownerCredentials': {'userName':
            'ResVcdExternalOwner', 'password': 'Password1'}, 'isRestAccessEnabled': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateResellerResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
