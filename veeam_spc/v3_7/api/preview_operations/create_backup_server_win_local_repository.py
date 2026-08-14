from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.backup_server_win_local_repository import BackupServerWinLocalRepository
from ...models.create_backup_server_win_local_repository_response_200 import (
    CreateBackupServerWinLocalRepositoryResponse200,
)
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    backup_server_uid: UUID,
    *,
    body: BackupServerWinLocalRepository,
    overwrite_owner: bool | Unset = UNSET,
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

    params["overwriteOwner"] = overwrite_owner

    params["select"] = select

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/infrastructure/backupServers/{backup_server_uid}/repositories/winLocal".format(
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
) -> Any | CreateBackupServerWinLocalRepositoryResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CreateBackupServerWinLocalRepositoryResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateBackupServerWinLocalRepositoryResponse200 | ErrorResponse]:
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
    body: BackupServerWinLocalRepository,
    overwrite_owner: bool | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateBackupServerWinLocalRepositoryResponse200 | ErrorResponse]:
    r"""Create Windows Local Backup Repository Connected to Backup Server

     Creates a Windows local backup repository connected to a Veeam Backup & Replication server with the
    specified UID.

    Args:
        backup_server_uid (UUID):
        overwrite_owner (bool | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (BackupServerWinLocalRepository):  Example: {'description': 'Created by MyCompany
            admin', 'name': 'LocalRepo2', 'hostId': '6d18e5fe-20e5-4248-a87f-29a109a44b80',
            'importBackup': False, 'importIndex': False, 'repository': {'maxTaskCount': 10, 'path':
            '\\Backups', 'readWriteLimitEnabled': False, 'readWriteRate': 0, 'taskLimitEnabled':
            False, 'advancedSettings': {'alignDataBlocks': False, 'decompressBeforeStoring': False,
            'perVmBackup': False, 'rotatedDriveCleanupMode': 'Disabled', 'rotatedDrives': False}},
            'mountServer': {'type': 'Windows', 'windows': {'mountServerId':
            'b3f66f04-5524-4eaa-9219-d73e9427f30d', 'vPowerNFSEnabled': True, 'writeCacheFolder':
            'C:\\ProgramData\\Veeam\\Backup\\IRCache\\', 'vPowerNFSPortSettings': {'mountPort': 443,
            'vPowerNFSPort': 443}}, 'linux': {'mountServerId': '92856fe0-7ea4-49ea-be90-19642626ceb4',
            'vPowerNFSEnabled': True, 'writeCacheFolder': 'C:\\ProgramData\\Veeam\\Backup\\IRCache\\',
            'vPowerNFSPortSettings': {'mountPort': 443, 'vPowerNFSPort': 443}}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateBackupServerWinLocalRepositoryResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
        body=body,
        overwrite_owner=overwrite_owner,
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
    body: BackupServerWinLocalRepository,
    overwrite_owner: bool | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateBackupServerWinLocalRepositoryResponse200 | ErrorResponse | None:
    r"""Create Windows Local Backup Repository Connected to Backup Server

     Creates a Windows local backup repository connected to a Veeam Backup & Replication server with the
    specified UID.

    Args:
        backup_server_uid (UUID):
        overwrite_owner (bool | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (BackupServerWinLocalRepository):  Example: {'description': 'Created by MyCompany
            admin', 'name': 'LocalRepo2', 'hostId': '6d18e5fe-20e5-4248-a87f-29a109a44b80',
            'importBackup': False, 'importIndex': False, 'repository': {'maxTaskCount': 10, 'path':
            '\\Backups', 'readWriteLimitEnabled': False, 'readWriteRate': 0, 'taskLimitEnabled':
            False, 'advancedSettings': {'alignDataBlocks': False, 'decompressBeforeStoring': False,
            'perVmBackup': False, 'rotatedDriveCleanupMode': 'Disabled', 'rotatedDrives': False}},
            'mountServer': {'type': 'Windows', 'windows': {'mountServerId':
            'b3f66f04-5524-4eaa-9219-d73e9427f30d', 'vPowerNFSEnabled': True, 'writeCacheFolder':
            'C:\\ProgramData\\Veeam\\Backup\\IRCache\\', 'vPowerNFSPortSettings': {'mountPort': 443,
            'vPowerNFSPort': 443}}, 'linux': {'mountServerId': '92856fe0-7ea4-49ea-be90-19642626ceb4',
            'vPowerNFSEnabled': True, 'writeCacheFolder': 'C:\\ProgramData\\Veeam\\Backup\\IRCache\\',
            'vPowerNFSPortSettings': {'mountPort': 443, 'vPowerNFSPort': 443}}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateBackupServerWinLocalRepositoryResponse200 | ErrorResponse
    """

    return sync_detailed(
        backup_server_uid=backup_server_uid,
        client=client,
        body=body,
        overwrite_owner=overwrite_owner,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    backup_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: BackupServerWinLocalRepository,
    overwrite_owner: bool | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateBackupServerWinLocalRepositoryResponse200 | ErrorResponse]:
    r"""Create Windows Local Backup Repository Connected to Backup Server

     Creates a Windows local backup repository connected to a Veeam Backup & Replication server with the
    specified UID.

    Args:
        backup_server_uid (UUID):
        overwrite_owner (bool | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (BackupServerWinLocalRepository):  Example: {'description': 'Created by MyCompany
            admin', 'name': 'LocalRepo2', 'hostId': '6d18e5fe-20e5-4248-a87f-29a109a44b80',
            'importBackup': False, 'importIndex': False, 'repository': {'maxTaskCount': 10, 'path':
            '\\Backups', 'readWriteLimitEnabled': False, 'readWriteRate': 0, 'taskLimitEnabled':
            False, 'advancedSettings': {'alignDataBlocks': False, 'decompressBeforeStoring': False,
            'perVmBackup': False, 'rotatedDriveCleanupMode': 'Disabled', 'rotatedDrives': False}},
            'mountServer': {'type': 'Windows', 'windows': {'mountServerId':
            'b3f66f04-5524-4eaa-9219-d73e9427f30d', 'vPowerNFSEnabled': True, 'writeCacheFolder':
            'C:\\ProgramData\\Veeam\\Backup\\IRCache\\', 'vPowerNFSPortSettings': {'mountPort': 443,
            'vPowerNFSPort': 443}}, 'linux': {'mountServerId': '92856fe0-7ea4-49ea-be90-19642626ceb4',
            'vPowerNFSEnabled': True, 'writeCacheFolder': 'C:\\ProgramData\\Veeam\\Backup\\IRCache\\',
            'vPowerNFSPortSettings': {'mountPort': 443, 'vPowerNFSPort': 443}}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateBackupServerWinLocalRepositoryResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
        body=body,
        overwrite_owner=overwrite_owner,
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
    body: BackupServerWinLocalRepository,
    overwrite_owner: bool | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateBackupServerWinLocalRepositoryResponse200 | ErrorResponse | None:
    r"""Create Windows Local Backup Repository Connected to Backup Server

     Creates a Windows local backup repository connected to a Veeam Backup & Replication server with the
    specified UID.

    Args:
        backup_server_uid (UUID):
        overwrite_owner (bool | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (BackupServerWinLocalRepository):  Example: {'description': 'Created by MyCompany
            admin', 'name': 'LocalRepo2', 'hostId': '6d18e5fe-20e5-4248-a87f-29a109a44b80',
            'importBackup': False, 'importIndex': False, 'repository': {'maxTaskCount': 10, 'path':
            '\\Backups', 'readWriteLimitEnabled': False, 'readWriteRate': 0, 'taskLimitEnabled':
            False, 'advancedSettings': {'alignDataBlocks': False, 'decompressBeforeStoring': False,
            'perVmBackup': False, 'rotatedDriveCleanupMode': 'Disabled', 'rotatedDrives': False}},
            'mountServer': {'type': 'Windows', 'windows': {'mountServerId':
            'b3f66f04-5524-4eaa-9219-d73e9427f30d', 'vPowerNFSEnabled': True, 'writeCacheFolder':
            'C:\\ProgramData\\Veeam\\Backup\\IRCache\\', 'vPowerNFSPortSettings': {'mountPort': 443,
            'vPowerNFSPort': 443}}, 'linux': {'mountServerId': '92856fe0-7ea4-49ea-be90-19642626ceb4',
            'vPowerNFSEnabled': True, 'writeCacheFolder': 'C:\\ProgramData\\Veeam\\Backup\\IRCache\\',
            'vPowerNFSPortSettings': {'mountPort': 443, 'vPowerNFSPort': 443}}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateBackupServerWinLocalRepositoryResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            backup_server_uid=backup_server_uid,
            client=client,
            body=body,
            overwrite_owner=overwrite_owner,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
