from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_vdc_storage_vault_response_200 import CreateVdcStorageVaultResponse200
from ...models.error_response import ErrorResponse
from ...models.vdc_storage_vault_input import VdcStorageVaultInput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: VdcStorageVaultInput,
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
        "url": "/vdcVault/storageVaults",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateVdcStorageVaultResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CreateVdcStorageVaultResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateVdcStorageVaultResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: VdcStorageVaultInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateVdcStorageVaultResponse200 | ErrorResponse]:
    """Add Storage Vault

     Adds a new storage vault.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VdcStorageVaultInput):  Example: {'tenantUid': '0acf6ffe-
            fa5f-4944-a884-e8aa5dc180b3', 'name': 'dm-vault-temp-e7527', 'dataCenterId': 'westeurope',
            'storageQuota': 1073741824, 'quotaEnforced': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateVdcStorageVaultResponse200 | ErrorResponse]
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
    body: VdcStorageVaultInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateVdcStorageVaultResponse200 | ErrorResponse | None:
    """Add Storage Vault

     Adds a new storage vault.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VdcStorageVaultInput):  Example: {'tenantUid': '0acf6ffe-
            fa5f-4944-a884-e8aa5dc180b3', 'name': 'dm-vault-temp-e7527', 'dataCenterId': 'westeurope',
            'storageQuota': 1073741824, 'quotaEnforced': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateVdcStorageVaultResponse200 | ErrorResponse
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
    body: VdcStorageVaultInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateVdcStorageVaultResponse200 | ErrorResponse]:
    """Add Storage Vault

     Adds a new storage vault.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VdcStorageVaultInput):  Example: {'tenantUid': '0acf6ffe-
            fa5f-4944-a884-e8aa5dc180b3', 'name': 'dm-vault-temp-e7527', 'dataCenterId': 'westeurope',
            'storageQuota': 1073741824, 'quotaEnforced': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateVdcStorageVaultResponse200 | ErrorResponse]
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
    body: VdcStorageVaultInput,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateVdcStorageVaultResponse200 | ErrorResponse | None:
    """Add Storage Vault

     Adds a new storage vault.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (VdcStorageVaultInput):  Example: {'tenantUid': '0acf6ffe-
            fa5f-4944-a884-e8aa5dc180b3', 'name': 'dm-vault-temp-e7527', 'dataCenterId': 'westeurope',
            'storageQuota': 1073741824, 'quotaEnforced': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateVdcStorageVaultResponse200 | ErrorResponse
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
