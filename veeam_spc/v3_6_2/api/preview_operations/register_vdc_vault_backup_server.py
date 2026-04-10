from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.register_vdc_vault_backup_server_response_200 import RegisterVdcVaultBackupServerResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    backup_server_uid: UUID,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-id"] = x_request_id

    if not isinstance(x_client_version, Unset):
        headers["X-Client-Version"] = x_client_version

    params: dict[str, Any] = {}

    json_backup_server_uid = str(backup_server_uid)
    params["backupServerUid"] = json_backup_server_uid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/vdcVault/registeredBackupServers",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | RegisterVdcVaultBackupServerResponse200:
    if response.status_code == 200:
        response_200 = RegisterVdcVaultBackupServerResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | RegisterVdcVaultBackupServerResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    backup_server_uid: UUID,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | RegisterVdcVaultBackupServerResponse200]:
    """Register Veeam Backup & Replication Server in Veeam Data Cloud Vault

     Registers a specified Veeam Backup & Replication server in Veeam Data Cloud Vault.

    Args:
        backup_server_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | RegisterVdcVaultBackupServerResponse200]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
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
    backup_server_uid: UUID,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | RegisterVdcVaultBackupServerResponse200 | None:
    """Register Veeam Backup & Replication Server in Veeam Data Cloud Vault

     Registers a specified Veeam Backup & Replication server in Veeam Data Cloud Vault.

    Args:
        backup_server_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | RegisterVdcVaultBackupServerResponse200
    """

    return sync_detailed(
        client=client,
        backup_server_uid=backup_server_uid,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    backup_server_uid: UUID,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | RegisterVdcVaultBackupServerResponse200]:
    """Register Veeam Backup & Replication Server in Veeam Data Cloud Vault

     Registers a specified Veeam Backup & Replication server in Veeam Data Cloud Vault.

    Args:
        backup_server_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | RegisterVdcVaultBackupServerResponse200]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    backup_server_uid: UUID,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | RegisterVdcVaultBackupServerResponse200 | None:
    """Register Veeam Backup & Replication Server in Veeam Data Cloud Vault

     Registers a specified Veeam Backup & Replication server in Veeam Data Cloud Vault.

    Args:
        backup_server_uid (UUID):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | RegisterVdcVaultBackupServerResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            backup_server_uid=backup_server_uid,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
