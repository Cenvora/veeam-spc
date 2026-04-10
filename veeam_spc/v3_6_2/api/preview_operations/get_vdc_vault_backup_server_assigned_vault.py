from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_vdc_vault_backup_server_assigned_vault_response_200 import (
    GetVdcVaultBackupServerAssignedVaultResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    backup_server_uid: UUID,
    vault_id: UUID,
    *,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/vdcVault/registeredBackupServers/{backup_server_uid}/assignedVaults/{vault_id}".format(
            backup_server_uid=quote(str(backup_server_uid), safe=""),
            vault_id=quote(str(vault_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | GetVdcVaultBackupServerAssignedVaultResponse200:
    if response.status_code == 200:
        response_200 = GetVdcVaultBackupServerAssignedVaultResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | GetVdcVaultBackupServerAssignedVaultResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    backup_server_uid: UUID,
    vault_id: UUID,
    *,
    client: AuthenticatedClient,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetVdcVaultBackupServerAssignedVaultResponse200]:
    """Get Storage Vault Assigned to Veeam Backup & Replication Server

     Returns a resource representation of a storage vault with the specified UID that is assigned to a
    Veeam Backup & Replication server.

    Args:
        backup_server_uid (UUID):
        vault_id (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetVdcVaultBackupServerAssignedVaultResponse200]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
        vault_id=vault_id,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    backup_server_uid: UUID,
    vault_id: UUID,
    *,
    client: AuthenticatedClient,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetVdcVaultBackupServerAssignedVaultResponse200 | None:
    """Get Storage Vault Assigned to Veeam Backup & Replication Server

     Returns a resource representation of a storage vault with the specified UID that is assigned to a
    Veeam Backup & Replication server.

    Args:
        backup_server_uid (UUID):
        vault_id (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetVdcVaultBackupServerAssignedVaultResponse200
    """

    return sync_detailed(
        backup_server_uid=backup_server_uid,
        vault_id=vault_id,
        client=client,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    backup_server_uid: UUID,
    vault_id: UUID,
    *,
    client: AuthenticatedClient,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | GetVdcVaultBackupServerAssignedVaultResponse200]:
    """Get Storage Vault Assigned to Veeam Backup & Replication Server

     Returns a resource representation of a storage vault with the specified UID that is assigned to a
    Veeam Backup & Replication server.

    Args:
        backup_server_uid (UUID):
        vault_id (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | GetVdcVaultBackupServerAssignedVaultResponse200]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
        vault_id=vault_id,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    backup_server_uid: UUID,
    vault_id: UUID,
    *,
    client: AuthenticatedClient,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | GetVdcVaultBackupServerAssignedVaultResponse200 | None:
    """Get Storage Vault Assigned to Veeam Backup & Replication Server

     Returns a resource representation of a storage vault with the specified UID that is assigned to a
    Veeam Backup & Replication server.

    Args:
        backup_server_uid (UUID):
        vault_id (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | GetVdcVaultBackupServerAssignedVaultResponse200
    """

    return (
        await asyncio_detailed(
            backup_server_uid=backup_server_uid,
            vault_id=vault_id,
            client=client,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
