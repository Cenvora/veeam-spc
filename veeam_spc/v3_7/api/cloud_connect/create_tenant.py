from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.cloud_tenant import CloudTenant
from ...models.create_tenant_response_200 import CreateTenantResponse200
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    site_uid: UUID,
    *,
    body: CloudTenant,
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
        "url": "/infrastructure/sites/{site_uid}/tenants".format(
            site_uid=quote(str(site_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateTenantResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CreateTenantResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateTenantResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    site_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: CloudTenant,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateTenantResponse200 | ErrorResponse]:
    """Create Tenant on Site

     Creates a new tenant on a Veeam Cloud Connect site with the specified UID.

    Args:
        site_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (CloudTenant):  Example: {'type': 'General', 'vCloudOrganizationUid': None,
            'isLeaseExpirationEnabled': False, 'leaseExpirationDate': None, 'credentials':
            {'userName': 'admin', 'password': 'Password1'}, 'description': 'Tenant for Alpha company',
            'isThrottlingEnabled': False, 'throttlingValue': None, 'throttlingUnit': None,
            'maxConcurrentTask': 1, 'isBackupProtectionEnabled': False, 'backupProtectionPeriod':
            None, 'gatewaySelectionType': 'StandaloneGateways', 'gatewayPoolsUids': [],
            'isGatewayFailoverEnabled': False, 'isNativeReplicationResourcesEnabled': False,
            'isVcdReplicationResourcesEnabled': False, 'assignedForCompany': None}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateTenantResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        site_uid=site_uid,
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
    site_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: CloudTenant,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateTenantResponse200 | ErrorResponse | None:
    """Create Tenant on Site

     Creates a new tenant on a Veeam Cloud Connect site with the specified UID.

    Args:
        site_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (CloudTenant):  Example: {'type': 'General', 'vCloudOrganizationUid': None,
            'isLeaseExpirationEnabled': False, 'leaseExpirationDate': None, 'credentials':
            {'userName': 'admin', 'password': 'Password1'}, 'description': 'Tenant for Alpha company',
            'isThrottlingEnabled': False, 'throttlingValue': None, 'throttlingUnit': None,
            'maxConcurrentTask': 1, 'isBackupProtectionEnabled': False, 'backupProtectionPeriod':
            None, 'gatewaySelectionType': 'StandaloneGateways', 'gatewayPoolsUids': [],
            'isGatewayFailoverEnabled': False, 'isNativeReplicationResourcesEnabled': False,
            'isVcdReplicationResourcesEnabled': False, 'assignedForCompany': None}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateTenantResponse200 | ErrorResponse
    """

    return sync_detailed(
        site_uid=site_uid,
        client=client,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    site_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: CloudTenant,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateTenantResponse200 | ErrorResponse]:
    """Create Tenant on Site

     Creates a new tenant on a Veeam Cloud Connect site with the specified UID.

    Args:
        site_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (CloudTenant):  Example: {'type': 'General', 'vCloudOrganizationUid': None,
            'isLeaseExpirationEnabled': False, 'leaseExpirationDate': None, 'credentials':
            {'userName': 'admin', 'password': 'Password1'}, 'description': 'Tenant for Alpha company',
            'isThrottlingEnabled': False, 'throttlingValue': None, 'throttlingUnit': None,
            'maxConcurrentTask': 1, 'isBackupProtectionEnabled': False, 'backupProtectionPeriod':
            None, 'gatewaySelectionType': 'StandaloneGateways', 'gatewayPoolsUids': [],
            'isGatewayFailoverEnabled': False, 'isNativeReplicationResourcesEnabled': False,
            'isVcdReplicationResourcesEnabled': False, 'assignedForCompany': None}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateTenantResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        site_uid=site_uid,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    site_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: CloudTenant,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateTenantResponse200 | ErrorResponse | None:
    """Create Tenant on Site

     Creates a new tenant on a Veeam Cloud Connect site with the specified UID.

    Args:
        site_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (CloudTenant):  Example: {'type': 'General', 'vCloudOrganizationUid': None,
            'isLeaseExpirationEnabled': False, 'leaseExpirationDate': None, 'credentials':
            {'userName': 'admin', 'password': 'Password1'}, 'description': 'Tenant for Alpha company',
            'isThrottlingEnabled': False, 'throttlingValue': None, 'throttlingUnit': None,
            'maxConcurrentTask': 1, 'isBackupProtectionEnabled': False, 'backupProtectionPeriod':
            None, 'gatewaySelectionType': 'StandaloneGateways', 'gatewayPoolsUids': [],
            'isGatewayFailoverEnabled': False, 'isNativeReplicationResourcesEnabled': False,
            'isVcdReplicationResourcesEnabled': False, 'assignedForCompany': None}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateTenantResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            site_uid=site_uid,
            client=client,
            body=body,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
