from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.linux_vbr_upgrade_configuration import LinuxVbrUpgradeConfiguration
from ...models.upgrade_linux_backup_server_response_200 import UpgradeLinuxBackupServerResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    backup_server_uid: UUID,
    *,
    body: LinuxVbrUpgradeConfiguration,
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
        "url": "/infrastructure/backupServers/{backup_server_uid}/upgradeLinux".format(
            backup_server_uid=quote(str(backup_server_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | UpgradeLinuxBackupServerResponse200:
    if response.status_code == 200:
        response_200 = UpgradeLinuxBackupServerResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorResponse | UpgradeLinuxBackupServerResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    backup_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: LinuxVbrUpgradeConfiguration,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | UpgradeLinuxBackupServerResponse200]:
    """Update Veeam Backup & Replication on Linux Server

     Installs updates on a Linux Veeam Backup & Replication server with the specified UID using
    VeeamUpdater.
    > To track the installation progress, you can use the `WaitDeploymentTask` operation.

    Args:
        backup_server_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (LinuxVbrUpgradeConfiguration): Configuration for upgrading Veeam Backup &
            Replication on a Linux server. Example: {'updateIds':
            ['3f8a9c41-2d57-4e0b-9a1c-6b2f8d3e7a04', 'c1d4e9b2-7a36-4f81-b5e0-9d2a6c4f1e83'],
            'stopAllActivities': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | UpgradeLinuxBackupServerResponse200]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
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
    backup_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: LinuxVbrUpgradeConfiguration,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | UpgradeLinuxBackupServerResponse200 | None:
    """Update Veeam Backup & Replication on Linux Server

     Installs updates on a Linux Veeam Backup & Replication server with the specified UID using
    VeeamUpdater.
    > To track the installation progress, you can use the `WaitDeploymentTask` operation.

    Args:
        backup_server_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (LinuxVbrUpgradeConfiguration): Configuration for upgrading Veeam Backup &
            Replication on a Linux server. Example: {'updateIds':
            ['3f8a9c41-2d57-4e0b-9a1c-6b2f8d3e7a04', 'c1d4e9b2-7a36-4f81-b5e0-9d2a6c4f1e83'],
            'stopAllActivities': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | UpgradeLinuxBackupServerResponse200
    """

    return sync_detailed(
        backup_server_uid=backup_server_uid,
        client=client,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    backup_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: LinuxVbrUpgradeConfiguration,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | UpgradeLinuxBackupServerResponse200]:
    """Update Veeam Backup & Replication on Linux Server

     Installs updates on a Linux Veeam Backup & Replication server with the specified UID using
    VeeamUpdater.
    > To track the installation progress, you can use the `WaitDeploymentTask` operation.

    Args:
        backup_server_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (LinuxVbrUpgradeConfiguration): Configuration for upgrading Veeam Backup &
            Replication on a Linux server. Example: {'updateIds':
            ['3f8a9c41-2d57-4e0b-9a1c-6b2f8d3e7a04', 'c1d4e9b2-7a36-4f81-b5e0-9d2a6c4f1e83'],
            'stopAllActivities': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | UpgradeLinuxBackupServerResponse200]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    backup_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: LinuxVbrUpgradeConfiguration,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | ErrorResponse | UpgradeLinuxBackupServerResponse200 | None:
    """Update Veeam Backup & Replication on Linux Server

     Installs updates on a Linux Veeam Backup & Replication server with the specified UID using
    VeeamUpdater.
    > To track the installation progress, you can use the `WaitDeploymentTask` operation.

    Args:
        backup_server_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (LinuxVbrUpgradeConfiguration): Configuration for upgrading Veeam Backup &
            Replication on a Linux server. Example: {'updateIds':
            ['3f8a9c41-2d57-4e0b-9a1c-6b2f8d3e7a04', 'c1d4e9b2-7a36-4f81-b5e0-9d2a6c4f1e83'],
            'stopAllActivities': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | UpgradeLinuxBackupServerResponse200
    """

    return (
        await asyncio_detailed(
            backup_server_uid=backup_server_uid,
            client=client,
            body=body,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
