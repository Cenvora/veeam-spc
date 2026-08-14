from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_windows_backup_policy_response_200 import CreateWindowsBackupPolicyResponse200
from ...models.error_response import ErrorResponse
from ...models.windows_backup_policy_input import WindowsBackupPolicyInput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: WindowsBackupPolicyInput | Unset = UNSET,
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
        "url": "/configuration/backupPolicies/windows",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateWindowsBackupPolicyResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CreateWindowsBackupPolicyResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateWindowsBackupPolicyResponse200 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: WindowsBackupPolicyInput | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateWindowsBackupPolicyResponse200 | ErrorResponse]:
    r"""Create Backup Policy for Windows Computers

     Creates a backup policy for Microsoft Windows computers.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (WindowsBackupPolicyInput | Unset):  Example: {'name': 'WWrkstEntireCloud',
            'description': 'temp description', 'operationMode': 'Workstation', 'accessMode': 'Public',
            'createSubtenants': True, 'createSubFolders': False, 'unlimitedSubtenantQuota': False,
            'repositoryQuotaGb': 1, 'jobConfiguration': {'backupSource': {'backupMode':
            'EntireComputer', 'computerLevelOptions': {'includeUsbDrives': True},
            'volumeLevelOptions': None, 'fileLevelOptions': None}, 'backupTarget': {'targetType':
            'CloudRepository', 'localPath': None, 'sharedFolder': None, 'backupRepository': None,
            'cloudRepository': {'backupCacheSettings': {'location': 'C:\\string', 'maximumSizeGb':
            1}}}, 'serverModeSettings': {'retentionSettings': {'retentionMode': 'RestorePoints',
            'retentionCount': 7}, 'scheduleSetting': {'scheduleType': 'Daily',
            'dailyScheduleSettings': {'time': '00:30', 'dailyMode': 'Everyday', 'specificDays': None},
            'monthlyScheduleSettings': None, 'periodicalScheduleSettings': None,
            'continuousScheduleSettings': {'backupWindowSettings': {'scheduleWindow': None,
            'shiftForMinutes': 0}}, 'retrySettings': {'enabled': True, 'retryTimes': 3,
            'waitTimeoutMinutes': 10}, 'backupWindow': None}, 'indexingSettings': None,
            'applicationAwareProcessingSettings': {'enabled': False, 'transactionLogProcessingMode':
            'ProcessTransactionLogsWithJob', 'sqlServerTransactionLogHandlingSettings': None,
            'oracleTransactionLogHandlingSettings': None, 'sharePointAccountSettings': None,
            'scriptSettings': None}}, 'workstationModeSettings': {'scheduleSetting':
            {'periodicalScheduleEnabled': True, 'periodicalScheduleSettings':
            {'dailyScheduleSettings': {'time': '00:30', 'dailyMode': 'Everyday', 'specificDays':
            None}, 'shutdownAction': 'SkipBackup', 'finalizingAction': 'KeepRunning'},
            'eventTriggerSettings': {'backupOnLock': False, 'backupOnLogOff': False,
            'backupOnTargetConnection': False, 'ejectTargetOnBackupComplete': False, 'backupNotOften':
            3, 'notOftenTimeUnit': 'Hours'}}, 'retentionSettings': {'retentionDays': 7}},
            'advancedSettings': {'backupStorage': {'compressionLevel': 'Optimal',
            'storageOptimization': 'Local1MB', 'encryptionEnabled': False, 'password': None,
            'passwordHint': None}, 'scheduleSettings': None, 'maintenanceSettings': None},
            'gfsRetentionSettings': None}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateWindowsBackupPolicyResponse200 | ErrorResponse]
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
    body: WindowsBackupPolicyInput | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateWindowsBackupPolicyResponse200 | ErrorResponse | None:
    r"""Create Backup Policy for Windows Computers

     Creates a backup policy for Microsoft Windows computers.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (WindowsBackupPolicyInput | Unset):  Example: {'name': 'WWrkstEntireCloud',
            'description': 'temp description', 'operationMode': 'Workstation', 'accessMode': 'Public',
            'createSubtenants': True, 'createSubFolders': False, 'unlimitedSubtenantQuota': False,
            'repositoryQuotaGb': 1, 'jobConfiguration': {'backupSource': {'backupMode':
            'EntireComputer', 'computerLevelOptions': {'includeUsbDrives': True},
            'volumeLevelOptions': None, 'fileLevelOptions': None}, 'backupTarget': {'targetType':
            'CloudRepository', 'localPath': None, 'sharedFolder': None, 'backupRepository': None,
            'cloudRepository': {'backupCacheSettings': {'location': 'C:\\string', 'maximumSizeGb':
            1}}}, 'serverModeSettings': {'retentionSettings': {'retentionMode': 'RestorePoints',
            'retentionCount': 7}, 'scheduleSetting': {'scheduleType': 'Daily',
            'dailyScheduleSettings': {'time': '00:30', 'dailyMode': 'Everyday', 'specificDays': None},
            'monthlyScheduleSettings': None, 'periodicalScheduleSettings': None,
            'continuousScheduleSettings': {'backupWindowSettings': {'scheduleWindow': None,
            'shiftForMinutes': 0}}, 'retrySettings': {'enabled': True, 'retryTimes': 3,
            'waitTimeoutMinutes': 10}, 'backupWindow': None}, 'indexingSettings': None,
            'applicationAwareProcessingSettings': {'enabled': False, 'transactionLogProcessingMode':
            'ProcessTransactionLogsWithJob', 'sqlServerTransactionLogHandlingSettings': None,
            'oracleTransactionLogHandlingSettings': None, 'sharePointAccountSettings': None,
            'scriptSettings': None}}, 'workstationModeSettings': {'scheduleSetting':
            {'periodicalScheduleEnabled': True, 'periodicalScheduleSettings':
            {'dailyScheduleSettings': {'time': '00:30', 'dailyMode': 'Everyday', 'specificDays':
            None}, 'shutdownAction': 'SkipBackup', 'finalizingAction': 'KeepRunning'},
            'eventTriggerSettings': {'backupOnLock': False, 'backupOnLogOff': False,
            'backupOnTargetConnection': False, 'ejectTargetOnBackupComplete': False, 'backupNotOften':
            3, 'notOftenTimeUnit': 'Hours'}}, 'retentionSettings': {'retentionDays': 7}},
            'advancedSettings': {'backupStorage': {'compressionLevel': 'Optimal',
            'storageOptimization': 'Local1MB', 'encryptionEnabled': False, 'password': None,
            'passwordHint': None}, 'scheduleSettings': None, 'maintenanceSettings': None},
            'gfsRetentionSettings': None}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateWindowsBackupPolicyResponse200 | ErrorResponse
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
    body: WindowsBackupPolicyInput | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateWindowsBackupPolicyResponse200 | ErrorResponse]:
    r"""Create Backup Policy for Windows Computers

     Creates a backup policy for Microsoft Windows computers.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (WindowsBackupPolicyInput | Unset):  Example: {'name': 'WWrkstEntireCloud',
            'description': 'temp description', 'operationMode': 'Workstation', 'accessMode': 'Public',
            'createSubtenants': True, 'createSubFolders': False, 'unlimitedSubtenantQuota': False,
            'repositoryQuotaGb': 1, 'jobConfiguration': {'backupSource': {'backupMode':
            'EntireComputer', 'computerLevelOptions': {'includeUsbDrives': True},
            'volumeLevelOptions': None, 'fileLevelOptions': None}, 'backupTarget': {'targetType':
            'CloudRepository', 'localPath': None, 'sharedFolder': None, 'backupRepository': None,
            'cloudRepository': {'backupCacheSettings': {'location': 'C:\\string', 'maximumSizeGb':
            1}}}, 'serverModeSettings': {'retentionSettings': {'retentionMode': 'RestorePoints',
            'retentionCount': 7}, 'scheduleSetting': {'scheduleType': 'Daily',
            'dailyScheduleSettings': {'time': '00:30', 'dailyMode': 'Everyday', 'specificDays': None},
            'monthlyScheduleSettings': None, 'periodicalScheduleSettings': None,
            'continuousScheduleSettings': {'backupWindowSettings': {'scheduleWindow': None,
            'shiftForMinutes': 0}}, 'retrySettings': {'enabled': True, 'retryTimes': 3,
            'waitTimeoutMinutes': 10}, 'backupWindow': None}, 'indexingSettings': None,
            'applicationAwareProcessingSettings': {'enabled': False, 'transactionLogProcessingMode':
            'ProcessTransactionLogsWithJob', 'sqlServerTransactionLogHandlingSettings': None,
            'oracleTransactionLogHandlingSettings': None, 'sharePointAccountSettings': None,
            'scriptSettings': None}}, 'workstationModeSettings': {'scheduleSetting':
            {'periodicalScheduleEnabled': True, 'periodicalScheduleSettings':
            {'dailyScheduleSettings': {'time': '00:30', 'dailyMode': 'Everyday', 'specificDays':
            None}, 'shutdownAction': 'SkipBackup', 'finalizingAction': 'KeepRunning'},
            'eventTriggerSettings': {'backupOnLock': False, 'backupOnLogOff': False,
            'backupOnTargetConnection': False, 'ejectTargetOnBackupComplete': False, 'backupNotOften':
            3, 'notOftenTimeUnit': 'Hours'}}, 'retentionSettings': {'retentionDays': 7}},
            'advancedSettings': {'backupStorage': {'compressionLevel': 'Optimal',
            'storageOptimization': 'Local1MB', 'encryptionEnabled': False, 'password': None,
            'passwordHint': None}, 'scheduleSettings': None, 'maintenanceSettings': None},
            'gfsRetentionSettings': None}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateWindowsBackupPolicyResponse200 | ErrorResponse]
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
    body: WindowsBackupPolicyInput | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateWindowsBackupPolicyResponse200 | ErrorResponse | None:
    r"""Create Backup Policy for Windows Computers

     Creates a backup policy for Microsoft Windows computers.

    Args:
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (WindowsBackupPolicyInput | Unset):  Example: {'name': 'WWrkstEntireCloud',
            'description': 'temp description', 'operationMode': 'Workstation', 'accessMode': 'Public',
            'createSubtenants': True, 'createSubFolders': False, 'unlimitedSubtenantQuota': False,
            'repositoryQuotaGb': 1, 'jobConfiguration': {'backupSource': {'backupMode':
            'EntireComputer', 'computerLevelOptions': {'includeUsbDrives': True},
            'volumeLevelOptions': None, 'fileLevelOptions': None}, 'backupTarget': {'targetType':
            'CloudRepository', 'localPath': None, 'sharedFolder': None, 'backupRepository': None,
            'cloudRepository': {'backupCacheSettings': {'location': 'C:\\string', 'maximumSizeGb':
            1}}}, 'serverModeSettings': {'retentionSettings': {'retentionMode': 'RestorePoints',
            'retentionCount': 7}, 'scheduleSetting': {'scheduleType': 'Daily',
            'dailyScheduleSettings': {'time': '00:30', 'dailyMode': 'Everyday', 'specificDays': None},
            'monthlyScheduleSettings': None, 'periodicalScheduleSettings': None,
            'continuousScheduleSettings': {'backupWindowSettings': {'scheduleWindow': None,
            'shiftForMinutes': 0}}, 'retrySettings': {'enabled': True, 'retryTimes': 3,
            'waitTimeoutMinutes': 10}, 'backupWindow': None}, 'indexingSettings': None,
            'applicationAwareProcessingSettings': {'enabled': False, 'transactionLogProcessingMode':
            'ProcessTransactionLogsWithJob', 'sqlServerTransactionLogHandlingSettings': None,
            'oracleTransactionLogHandlingSettings': None, 'sharePointAccountSettings': None,
            'scriptSettings': None}}, 'workstationModeSettings': {'scheduleSetting':
            {'periodicalScheduleEnabled': True, 'periodicalScheduleSettings':
            {'dailyScheduleSettings': {'time': '00:30', 'dailyMode': 'Everyday', 'specificDays':
            None}, 'shutdownAction': 'SkipBackup', 'finalizingAction': 'KeepRunning'},
            'eventTriggerSettings': {'backupOnLock': False, 'backupOnLogOff': False,
            'backupOnTargetConnection': False, 'ejectTargetOnBackupComplete': False, 'backupNotOften':
            3, 'notOftenTimeUnit': 'Hours'}}, 'retentionSettings': {'retentionDays': 7}},
            'advancedSettings': {'backupStorage': {'compressionLevel': 'Optimal',
            'storageOptimization': 'Local1MB', 'encryptionEnabled': False, 'password': None,
            'passwordHint': None}, 'scheduleSettings': None, 'maintenanceSettings': None},
            'gfsRetentionSettings': None}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateWindowsBackupPolicyResponse200 | ErrorResponse
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
