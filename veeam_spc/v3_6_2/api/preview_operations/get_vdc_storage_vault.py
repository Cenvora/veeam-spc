from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_vdc_storage_vault_response_200 import GetVdcStorageVaultResponse200
from ...models.vdc_storage_vault_expand import VdcStorageVaultExpand
from ...types import UNSET, Response, Unset


def _get_kwargs(
    vault_id: UUID,
    *,
    expand: list[VdcStorageVaultExpand] | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    json_expand: list[str] | Unset = UNSET
    if not isinstance(expand, Unset):
        json_expand = []
        for expand_item_data in expand:
            expand_item = expand_item_data.value
            json_expand.append(expand_item)

    params["expand"] = json_expand

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/vdcVault/storageVaults/{vault_id}".format(
            vault_id=quote(str(vault_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | GetVdcStorageVaultResponse200:
    if response.status_code == 200:
        response_200 = GetVdcStorageVaultResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | GetVdcStorageVaultResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    vault_id: UUID,
    *,
    client: AuthenticatedClient,
    expand: list[VdcStorageVaultExpand] | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetVdcStorageVaultResponse200]:
    """Get Storage Vault

     Returns a resource representation of a storage vault with the specified UID.

    Args:
        vault_id (UUID):
        expand (list[VdcStorageVaultExpand] | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetVdcStorageVaultResponse200]
    """

    kwargs = _get_kwargs(
        vault_id=vault_id,
        expand=expand,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    vault_id: UUID,
    *,
    client: AuthenticatedClient,
    expand: list[VdcStorageVaultExpand] | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetVdcStorageVaultResponse200 | None:
    """Get Storage Vault

     Returns a resource representation of a storage vault with the specified UID.

    Args:
        vault_id (UUID):
        expand (list[VdcStorageVaultExpand] | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetVdcStorageVaultResponse200
    """

    return sync_detailed(
        vault_id=vault_id,
        client=client,
        expand=expand,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    vault_id: UUID,
    *,
    client: AuthenticatedClient,
    expand: list[VdcStorageVaultExpand] | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetVdcStorageVaultResponse200]:
    """Get Storage Vault

     Returns a resource representation of a storage vault with the specified UID.

    Args:
        vault_id (UUID):
        expand (list[VdcStorageVaultExpand] | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetVdcStorageVaultResponse200]
    """

    kwargs = _get_kwargs(
        vault_id=vault_id,
        expand=expand,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    vault_id: UUID,
    *,
    client: AuthenticatedClient,
    expand: list[VdcStorageVaultExpand] | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetVdcStorageVaultResponse200 | None:
    """Get Storage Vault

     Returns a resource representation of a storage vault with the specified UID.

    Args:
        vault_id (UUID):
        expand (list[VdcStorageVaultExpand] | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetVdcStorageVaultResponse200
    """

    return (
        await asyncio_detailed(
            vault_id=vault_id,
            client=client,
            expand=expand,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
