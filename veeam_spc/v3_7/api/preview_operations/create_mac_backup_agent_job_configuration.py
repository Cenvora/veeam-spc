from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_mac_backup_agent_job_configuration_response_200 import (
    CreateMacBackupAgentJobConfigurationResponse200,
)
from ...models.error_response import ErrorResponse
from ...models.mac_custom_job_configuration import MacCustomJobConfiguration
from ...types import UNSET, Response, Unset


def _get_kwargs(
    backup_agent_uid: UUID,
    *,
    body: MacCustomJobConfiguration,
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
        "url": "/infrastructure/backupAgents/mac/{backup_agent_uid}/jobs/configuration".format(
            backup_agent_uid=quote(str(backup_agent_uid), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateMacBackupAgentJobConfigurationResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CreateMacBackupAgentJobConfigurationResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateMacBackupAgentJobConfigurationResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    backup_agent_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: MacCustomJobConfiguration,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateMacBackupAgentJobConfigurationResponse200 | ErrorResponse]:
    """Create Configuration of Job for Veeam Agent for Mac

     Creates a configuration of a Veeam backup agent job protecting Mac computer with the specified UID.

    Args:
        backup_agent_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (MacCustomJobConfiguration):  Example: {'name': 'ServerEntireCloud_Custom',
            'description': 'Mac Policy', 'operationMode': 'Server',
            'cloudRepositoryConnectionSettings': {'backupResourceUid':
            '28428289-2557-41b5-a51d-95730a24f23a', 'username': 'admin', 'password': None},
            'jobConfiguration': {'backupSource': {'backupDirectlyFromLiveFileSystem': True,
            'includeUsbDrives': False, 'includeDirectories': None, 'inclusionMasks': None,
            'excludeDirectories': None, 'exclusionMasks': None, 'personalFilesAdvancedSettings':
            {'inclusions': ['Desktop', 'Documents', 'Downloads', 'Video', 'Music', 'Pictures',
            'Favorites', 'ApplicationData', 'OtherFilesAndFolders', 'Library'],
            'excludeNetworkAccount': True}}, 'backupTarget': {'targetType': 'CloudRepository',
            'localPath': None, 'sharedFolder': None, 'backupRepository': None,
            'enableDeletedFilesRetention': False, 'removeDeletedItemsDataAfter': 30}, 'backupStorage':
            {'compressionLevel': 'Optimal', 'blockSize': 'Local1Mb', 'encryptionEnabled': False,
            'password': None, 'passwordHint': None}, 'retentionSettings': {'restorePointsCount': None,
            'retentionDays': 7}, 'scheduleSettings': {'scheduleType': 'Daily',
            'dailyScheduleSettings': {'time': '00:30', 'dailyMode': 'Everyday', 'specificDays': None},
            'monthlyScheduleSettings': None, 'periodicallyScheduleSettings': None,
            'activeFullSettings': None, 'retrySettings': {'enabled': False, 'retryTimes': 3,
            'waitTimeoutMinutes': 10}, 'backupHealthCheckScheduleSettings': None,
            'syntheticFullSettings': None}, 'gfsRetentionSettings': None}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateMacBackupAgentJobConfigurationResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        backup_agent_uid=backup_agent_uid,
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
    backup_agent_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: MacCustomJobConfiguration,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateMacBackupAgentJobConfigurationResponse200 | ErrorResponse | None:
    """Create Configuration of Job for Veeam Agent for Mac

     Creates a configuration of a Veeam backup agent job protecting Mac computer with the specified UID.

    Args:
        backup_agent_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (MacCustomJobConfiguration):  Example: {'name': 'ServerEntireCloud_Custom',
            'description': 'Mac Policy', 'operationMode': 'Server',
            'cloudRepositoryConnectionSettings': {'backupResourceUid':
            '28428289-2557-41b5-a51d-95730a24f23a', 'username': 'admin', 'password': None},
            'jobConfiguration': {'backupSource': {'backupDirectlyFromLiveFileSystem': True,
            'includeUsbDrives': False, 'includeDirectories': None, 'inclusionMasks': None,
            'excludeDirectories': None, 'exclusionMasks': None, 'personalFilesAdvancedSettings':
            {'inclusions': ['Desktop', 'Documents', 'Downloads', 'Video', 'Music', 'Pictures',
            'Favorites', 'ApplicationData', 'OtherFilesAndFolders', 'Library'],
            'excludeNetworkAccount': True}}, 'backupTarget': {'targetType': 'CloudRepository',
            'localPath': None, 'sharedFolder': None, 'backupRepository': None,
            'enableDeletedFilesRetention': False, 'removeDeletedItemsDataAfter': 30}, 'backupStorage':
            {'compressionLevel': 'Optimal', 'blockSize': 'Local1Mb', 'encryptionEnabled': False,
            'password': None, 'passwordHint': None}, 'retentionSettings': {'restorePointsCount': None,
            'retentionDays': 7}, 'scheduleSettings': {'scheduleType': 'Daily',
            'dailyScheduleSettings': {'time': '00:30', 'dailyMode': 'Everyday', 'specificDays': None},
            'monthlyScheduleSettings': None, 'periodicallyScheduleSettings': None,
            'activeFullSettings': None, 'retrySettings': {'enabled': False, 'retryTimes': 3,
            'waitTimeoutMinutes': 10}, 'backupHealthCheckScheduleSettings': None,
            'syntheticFullSettings': None}, 'gfsRetentionSettings': None}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateMacBackupAgentJobConfigurationResponse200 | ErrorResponse
    """

    return sync_detailed(
        backup_agent_uid=backup_agent_uid,
        client=client,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    backup_agent_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: MacCustomJobConfiguration,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateMacBackupAgentJobConfigurationResponse200 | ErrorResponse]:
    """Create Configuration of Job for Veeam Agent for Mac

     Creates a configuration of a Veeam backup agent job protecting Mac computer with the specified UID.

    Args:
        backup_agent_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (MacCustomJobConfiguration):  Example: {'name': 'ServerEntireCloud_Custom',
            'description': 'Mac Policy', 'operationMode': 'Server',
            'cloudRepositoryConnectionSettings': {'backupResourceUid':
            '28428289-2557-41b5-a51d-95730a24f23a', 'username': 'admin', 'password': None},
            'jobConfiguration': {'backupSource': {'backupDirectlyFromLiveFileSystem': True,
            'includeUsbDrives': False, 'includeDirectories': None, 'inclusionMasks': None,
            'excludeDirectories': None, 'exclusionMasks': None, 'personalFilesAdvancedSettings':
            {'inclusions': ['Desktop', 'Documents', 'Downloads', 'Video', 'Music', 'Pictures',
            'Favorites', 'ApplicationData', 'OtherFilesAndFolders', 'Library'],
            'excludeNetworkAccount': True}}, 'backupTarget': {'targetType': 'CloudRepository',
            'localPath': None, 'sharedFolder': None, 'backupRepository': None,
            'enableDeletedFilesRetention': False, 'removeDeletedItemsDataAfter': 30}, 'backupStorage':
            {'compressionLevel': 'Optimal', 'blockSize': 'Local1Mb', 'encryptionEnabled': False,
            'password': None, 'passwordHint': None}, 'retentionSettings': {'restorePointsCount': None,
            'retentionDays': 7}, 'scheduleSettings': {'scheduleType': 'Daily',
            'dailyScheduleSettings': {'time': '00:30', 'dailyMode': 'Everyday', 'specificDays': None},
            'monthlyScheduleSettings': None, 'periodicallyScheduleSettings': None,
            'activeFullSettings': None, 'retrySettings': {'enabled': False, 'retryTimes': 3,
            'waitTimeoutMinutes': 10}, 'backupHealthCheckScheduleSettings': None,
            'syntheticFullSettings': None}, 'gfsRetentionSettings': None}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateMacBackupAgentJobConfigurationResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        backup_agent_uid=backup_agent_uid,
        body=body,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    backup_agent_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: MacCustomJobConfiguration,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateMacBackupAgentJobConfigurationResponse200 | ErrorResponse | None:
    """Create Configuration of Job for Veeam Agent for Mac

     Creates a configuration of a Veeam backup agent job protecting Mac computer with the specified UID.

    Args:
        backup_agent_uid (UUID):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (MacCustomJobConfiguration):  Example: {'name': 'ServerEntireCloud_Custom',
            'description': 'Mac Policy', 'operationMode': 'Server',
            'cloudRepositoryConnectionSettings': {'backupResourceUid':
            '28428289-2557-41b5-a51d-95730a24f23a', 'username': 'admin', 'password': None},
            'jobConfiguration': {'backupSource': {'backupDirectlyFromLiveFileSystem': True,
            'includeUsbDrives': False, 'includeDirectories': None, 'inclusionMasks': None,
            'excludeDirectories': None, 'exclusionMasks': None, 'personalFilesAdvancedSettings':
            {'inclusions': ['Desktop', 'Documents', 'Downloads', 'Video', 'Music', 'Pictures',
            'Favorites', 'ApplicationData', 'OtherFilesAndFolders', 'Library'],
            'excludeNetworkAccount': True}}, 'backupTarget': {'targetType': 'CloudRepository',
            'localPath': None, 'sharedFolder': None, 'backupRepository': None,
            'enableDeletedFilesRetention': False, 'removeDeletedItemsDataAfter': 30}, 'backupStorage':
            {'compressionLevel': 'Optimal', 'blockSize': 'Local1Mb', 'encryptionEnabled': False,
            'password': None, 'passwordHint': None}, 'retentionSettings': {'restorePointsCount': None,
            'retentionDays': 7}, 'scheduleSettings': {'scheduleType': 'Daily',
            'dailyScheduleSettings': {'time': '00:30', 'dailyMode': 'Everyday', 'specificDays': None},
            'monthlyScheduleSettings': None, 'periodicallyScheduleSettings': None,
            'activeFullSettings': None, 'retrySettings': {'enabled': False, 'retryTimes': 3,
            'waitTimeoutMinutes': 10}, 'backupHealthCheckScheduleSettings': None,
            'syntheticFullSettings': None}, 'gfsRetentionSettings': None}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateMacBackupAgentJobConfigurationResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            backup_agent_uid=backup_agent_uid,
            client=client,
            body=body,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
