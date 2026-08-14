from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.backup_server_backup_job_configuration import BackupServerBackupJobConfiguration
from ...models.create_backup_server_backup_vm_v_sphere_job_response_200 import (
    CreateBackupServerBackupVmVSphereJobResponse200,
)
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    backup_server_uid: UUID,
    *,
    body: BackupServerBackupJobConfiguration,
    mapped_organization_uid: UUID | Unset = UNSET,
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

    json_mapped_organization_uid: str | Unset = UNSET
    if not isinstance(mapped_organization_uid, Unset):
        json_mapped_organization_uid = str(mapped_organization_uid)
    params["mappedOrganizationUid"] = json_mapped_organization_uid

    params["select"] = select

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/infrastructure/backupServers/{backup_server_uid}/jobs/backupVmJobs/vSphere".format(
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
) -> Any | CreateBackupServerBackupVmVSphereJobResponse200 | ErrorResponse:
    if response.status_code == 200:
        response_200 = CreateBackupServerBackupVmVSphereJobResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateBackupServerBackupVmVSphereJobResponse200 | ErrorResponse]:
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
    body: BackupServerBackupJobConfiguration,
    mapped_organization_uid: UUID | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateBackupServerBackupVmVSphereJobResponse200 | ErrorResponse]:
    """Create VMware vSphere VM Backup Job

     Creates a VMware VSphere VM backup job on a Veeam Backup & Replication server with the specified
    UID.

    Args:
        backup_server_uid (UUID):
        mapped_organization_uid (UUID | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (BackupServerBackupJobConfiguration):  Example: {'instanceUid':
            '1bcb374f-b346-68b3-bd70-2b40cc7ff6ae', 'originalUid':
            '7fa501dc-f769-4d71-83b1-4f6859c43925', 'name': 'Backup Job 23', 'description':
            'Customized Job Configuration', 'isDisabled': False, 'mappedOrganizationUid':
            '3337e028-55e1-453f-800c-3085a43033c6', 'mappedOrganizationName': 'hosted',
            'backupServerUid': '91d5797e-c80b-48e5-bb97-b9df5707f14f', 'backupServerName': 'vbr1',
            'isHighPriority': False, 'virtualMachines': {'includes': [{'inventoryObject': {'hostName':
            'vc1.tech.local', 'name': 'lis-l1-1', 'type': 'VirtualMachine', 'objectId': 'vm-91024'},
            'size': '49.4 GB'}, {'inventoryObject': {'hostName': 'vc1.tech.local', 'name': 'lis-l1-2',
            'type': 'VirtualMachine', 'objectId': 'vm-91025'}, 'size': '49.4 GB'}], 'excludes':
            {'vms': [], 'disks': [{'vmObject': {'hostName': 'vc1.tech.local', 'name': 'lis-l1-1',
            'type': 'VirtualMachine', 'objectId': 'vm-91024'}, 'disksToProcess': 'AllDisks', 'disks':
            [], 'removeFromVMConfiguration': True}, {'vmObject': {'hostName': 'vc1.tech.local',
            'name': 'lis-l1-2', 'type': 'VirtualMachine', 'objectId': 'vm-91025'}, 'disksToProcess':
            'AllDisks', 'disks': [], 'removeFromVMConfiguration': True}], 'templates': {'isEnabled':
            True, 'excludeFromIncremental': True}}}, 'storage': {'backupRepositoryId':
            '88788f9e-d8f5-4eb4-bc4f-9b3f5403bcec', 'backupProxies': {'autoSelection': True,
            'proxyIds': []}, 'retentionPolicy': {'type': 'Days', 'quantity': 7}, 'gfsPolicy':
            {'isEnabled': False, 'weekly': {'isEnabled': False, 'keepForNumberOfWeeks': 1,
            'desiredTime': 'Monday'}, 'monthly': {'isEnabled': False, 'keepForNumberOfMonths': 1,
            'desiredTime': 'First'}, 'yearly': {'isEnabled': False, 'keepForNumberOfYears': 1,
            'desiredTime': 'Jan'}}, 'advancedSettings': {'backupModeType': 'Incremental',
            'syntheticFulls': {'isEnabled': True, 'weekly': {'isEnabled': True, 'days': ['Saturday']},
            'monthly': {'isEnabled': False, 'dayOfWeek': 'Monday', 'dayNumberInMonth': 'First',
            'dayOfMonths': 1, 'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
            'Sep', 'Oct', 'Nov', 'Dec']}}, 'activeFulls': {'isEnabled': False, 'weekly': {'isEnabled':
            True, 'days': ['Saturday']}, 'monthly': {'isEnabled': False, 'dayOfWeek': 'Monday',
            'dayNumberInMonth': 'First', 'dayOfMonths': 1, 'months': ['Jan', 'Feb', 'Mar', 'Apr',
            'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}}, 'backupHealth': {'isEnabled':
            False, 'weekly': {'isEnabled': False, 'days': ['Saturday']}, 'monthly': {'isEnabled':
            True, 'dayOfWeek': 'Saturday', 'dayNumberInMonth': 'Last', 'dayOfMonths': 1, 'months':
            ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}},
            'fullBackupMaintenance': {'removeData': {'isEnabled': False, 'afterDays': 14},
            'defragmentAndCompact': {'isEnabled': False, 'weekly': {'isEnabled': False, 'days':
            ['Saturday']}, 'monthly': {'isEnabled': True, 'dayOfWeek': 'Saturday', 'dayNumberInMonth':
            'Last', 'dayOfMonths': 1, 'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
            'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}}}, 'storageData': {'enableInlineDataDeduplication':
            True, 'excludeSwapFileBlocks': True, 'excludeDeletedFileBlocks': True, 'compressionLevel':
            'Optimal', 'storageOptimization': 'LocalTarget', 'encryption': {'isEnabled': False,
            'encryptionType': 'ByUserPassword', 'encryptionPasswordId': None, 'encryptionPasswordTag':
            None, 'kmsServerId': None}}, 'notifications': {'sendSNMPNotifications': False,
            'emailNotifications': {'isEnabled': False, 'recipients': [], 'notificationType':
            'UseGlobalNotificationSettings', 'customNotificationSettings': None}, 'vmAttribute':
            {'isEnabled': False, 'notes': 'Notes', 'appendToExistingValue': True}}, 'vSphere':
            {'enableVMWareToolsQuiescence': False, 'changedBlockTracking': {'isEnabled': True,
            'enableCbtAutomatically': True, 'resetCbtOnActiveFull': True}}, 'storageIntegration':
            {'isEnabled': True, 'limitProcessedVm': False, 'limitProcessedVmCount': 10,
            'failoverToStandardBackup': False}, 'scripts': {'preCommand': {'isEnabled': False,
            'command': ''}, 'postCommand': {'isEnabled': False, 'command': ''}, 'periodicityType':
            'BackupSessions', 'runScriptEvery': 1, 'dayOfWeek': ['Saturday']}}}, 'guestProcessing':
            {'appAwareProcessing': {'isEnabled': False, 'appSettings': []}, 'guestFSIndexing':
            {'isEnabled': False, 'indexingSettings': []}, 'guestInteractionProxies': {'autoSelection':
            True, 'proxyIds': []}, 'guestCredentials': None}, 'schedule': {'runAutomatically': False,
            'daily': {'isEnabled': True, 'localTime': '10:00', 'dailyKind': 'Everyday', 'days':
            ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']},
            'monthly': {'isEnabled': False, 'localTime': '10:00', 'dayOfWeek': 'Saturday',
            'dayNumberInMonth': 'Fourth', 'dayOfMonth': None, 'months': ['Jan', 'Feb', 'Mar', 'Apr',
            'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}, 'periodically': {'isEnabled':
            False, 'periodicallyKind': 'Hours', 'frequency': 1, 'backupWindow': {'days': [{'day':
            'Sunday', 'hours': '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Monday',
            'hours': '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Tuesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Wednesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Thursday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Friday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Saturday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}]}, 'startTimeWithinAnHour': 0},
            'continuously': {'isEnabled': False, 'backupWindow': {'days': [{'day': 'Sunday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Monday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Tuesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Wednesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Thursday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Friday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Saturday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}]}}, 'afterThisJob': {'isEnabled':
            False, 'jobName': None}, 'retry': {'isEnabled': False, 'retryCount': 3, 'awaitMinutes':
            10}, 'backupWindow': {'isEnabled': False, 'backupWindow': {'days': [{'day': 'Sunday',
            'hours': '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Monday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Tuesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Wednesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Thursday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Friday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Saturday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}]}}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateBackupServerBackupVmVSphereJobResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
        body=body,
        mapped_organization_uid=mapped_organization_uid,
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
    body: BackupServerBackupJobConfiguration,
    mapped_organization_uid: UUID | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateBackupServerBackupVmVSphereJobResponse200 | ErrorResponse | None:
    """Create VMware vSphere VM Backup Job

     Creates a VMware VSphere VM backup job on a Veeam Backup & Replication server with the specified
    UID.

    Args:
        backup_server_uid (UUID):
        mapped_organization_uid (UUID | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (BackupServerBackupJobConfiguration):  Example: {'instanceUid':
            '1bcb374f-b346-68b3-bd70-2b40cc7ff6ae', 'originalUid':
            '7fa501dc-f769-4d71-83b1-4f6859c43925', 'name': 'Backup Job 23', 'description':
            'Customized Job Configuration', 'isDisabled': False, 'mappedOrganizationUid':
            '3337e028-55e1-453f-800c-3085a43033c6', 'mappedOrganizationName': 'hosted',
            'backupServerUid': '91d5797e-c80b-48e5-bb97-b9df5707f14f', 'backupServerName': 'vbr1',
            'isHighPriority': False, 'virtualMachines': {'includes': [{'inventoryObject': {'hostName':
            'vc1.tech.local', 'name': 'lis-l1-1', 'type': 'VirtualMachine', 'objectId': 'vm-91024'},
            'size': '49.4 GB'}, {'inventoryObject': {'hostName': 'vc1.tech.local', 'name': 'lis-l1-2',
            'type': 'VirtualMachine', 'objectId': 'vm-91025'}, 'size': '49.4 GB'}], 'excludes':
            {'vms': [], 'disks': [{'vmObject': {'hostName': 'vc1.tech.local', 'name': 'lis-l1-1',
            'type': 'VirtualMachine', 'objectId': 'vm-91024'}, 'disksToProcess': 'AllDisks', 'disks':
            [], 'removeFromVMConfiguration': True}, {'vmObject': {'hostName': 'vc1.tech.local',
            'name': 'lis-l1-2', 'type': 'VirtualMachine', 'objectId': 'vm-91025'}, 'disksToProcess':
            'AllDisks', 'disks': [], 'removeFromVMConfiguration': True}], 'templates': {'isEnabled':
            True, 'excludeFromIncremental': True}}}, 'storage': {'backupRepositoryId':
            '88788f9e-d8f5-4eb4-bc4f-9b3f5403bcec', 'backupProxies': {'autoSelection': True,
            'proxyIds': []}, 'retentionPolicy': {'type': 'Days', 'quantity': 7}, 'gfsPolicy':
            {'isEnabled': False, 'weekly': {'isEnabled': False, 'keepForNumberOfWeeks': 1,
            'desiredTime': 'Monday'}, 'monthly': {'isEnabled': False, 'keepForNumberOfMonths': 1,
            'desiredTime': 'First'}, 'yearly': {'isEnabled': False, 'keepForNumberOfYears': 1,
            'desiredTime': 'Jan'}}, 'advancedSettings': {'backupModeType': 'Incremental',
            'syntheticFulls': {'isEnabled': True, 'weekly': {'isEnabled': True, 'days': ['Saturday']},
            'monthly': {'isEnabled': False, 'dayOfWeek': 'Monday', 'dayNumberInMonth': 'First',
            'dayOfMonths': 1, 'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
            'Sep', 'Oct', 'Nov', 'Dec']}}, 'activeFulls': {'isEnabled': False, 'weekly': {'isEnabled':
            True, 'days': ['Saturday']}, 'monthly': {'isEnabled': False, 'dayOfWeek': 'Monday',
            'dayNumberInMonth': 'First', 'dayOfMonths': 1, 'months': ['Jan', 'Feb', 'Mar', 'Apr',
            'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}}, 'backupHealth': {'isEnabled':
            False, 'weekly': {'isEnabled': False, 'days': ['Saturday']}, 'monthly': {'isEnabled':
            True, 'dayOfWeek': 'Saturday', 'dayNumberInMonth': 'Last', 'dayOfMonths': 1, 'months':
            ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}},
            'fullBackupMaintenance': {'removeData': {'isEnabled': False, 'afterDays': 14},
            'defragmentAndCompact': {'isEnabled': False, 'weekly': {'isEnabled': False, 'days':
            ['Saturday']}, 'monthly': {'isEnabled': True, 'dayOfWeek': 'Saturday', 'dayNumberInMonth':
            'Last', 'dayOfMonths': 1, 'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
            'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}}}, 'storageData': {'enableInlineDataDeduplication':
            True, 'excludeSwapFileBlocks': True, 'excludeDeletedFileBlocks': True, 'compressionLevel':
            'Optimal', 'storageOptimization': 'LocalTarget', 'encryption': {'isEnabled': False,
            'encryptionType': 'ByUserPassword', 'encryptionPasswordId': None, 'encryptionPasswordTag':
            None, 'kmsServerId': None}}, 'notifications': {'sendSNMPNotifications': False,
            'emailNotifications': {'isEnabled': False, 'recipients': [], 'notificationType':
            'UseGlobalNotificationSettings', 'customNotificationSettings': None}, 'vmAttribute':
            {'isEnabled': False, 'notes': 'Notes', 'appendToExistingValue': True}}, 'vSphere':
            {'enableVMWareToolsQuiescence': False, 'changedBlockTracking': {'isEnabled': True,
            'enableCbtAutomatically': True, 'resetCbtOnActiveFull': True}}, 'storageIntegration':
            {'isEnabled': True, 'limitProcessedVm': False, 'limitProcessedVmCount': 10,
            'failoverToStandardBackup': False}, 'scripts': {'preCommand': {'isEnabled': False,
            'command': ''}, 'postCommand': {'isEnabled': False, 'command': ''}, 'periodicityType':
            'BackupSessions', 'runScriptEvery': 1, 'dayOfWeek': ['Saturday']}}}, 'guestProcessing':
            {'appAwareProcessing': {'isEnabled': False, 'appSettings': []}, 'guestFSIndexing':
            {'isEnabled': False, 'indexingSettings': []}, 'guestInteractionProxies': {'autoSelection':
            True, 'proxyIds': []}, 'guestCredentials': None}, 'schedule': {'runAutomatically': False,
            'daily': {'isEnabled': True, 'localTime': '10:00', 'dailyKind': 'Everyday', 'days':
            ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']},
            'monthly': {'isEnabled': False, 'localTime': '10:00', 'dayOfWeek': 'Saturday',
            'dayNumberInMonth': 'Fourth', 'dayOfMonth': None, 'months': ['Jan', 'Feb', 'Mar', 'Apr',
            'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}, 'periodically': {'isEnabled':
            False, 'periodicallyKind': 'Hours', 'frequency': 1, 'backupWindow': {'days': [{'day':
            'Sunday', 'hours': '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Monday',
            'hours': '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Tuesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Wednesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Thursday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Friday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Saturday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}]}, 'startTimeWithinAnHour': 0},
            'continuously': {'isEnabled': False, 'backupWindow': {'days': [{'day': 'Sunday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Monday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Tuesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Wednesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Thursday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Friday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Saturday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}]}}, 'afterThisJob': {'isEnabled':
            False, 'jobName': None}, 'retry': {'isEnabled': False, 'retryCount': 3, 'awaitMinutes':
            10}, 'backupWindow': {'isEnabled': False, 'backupWindow': {'days': [{'day': 'Sunday',
            'hours': '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Monday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Tuesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Wednesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Thursday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Friday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Saturday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}]}}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateBackupServerBackupVmVSphereJobResponse200 | ErrorResponse
    """

    return sync_detailed(
        backup_server_uid=backup_server_uid,
        client=client,
        body=body,
        mapped_organization_uid=mapped_organization_uid,
        select=select,
        x_request_id=x_request_id,
        x_client_version=x_client_version,
    ).parsed


async def asyncio_detailed(
    backup_server_uid: UUID,
    *,
    client: AuthenticatedClient,
    body: BackupServerBackupJobConfiguration,
    mapped_organization_uid: UUID | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Response[Any | CreateBackupServerBackupVmVSphereJobResponse200 | ErrorResponse]:
    """Create VMware vSphere VM Backup Job

     Creates a VMware VSphere VM backup job on a Veeam Backup & Replication server with the specified
    UID.

    Args:
        backup_server_uid (UUID):
        mapped_organization_uid (UUID | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (BackupServerBackupJobConfiguration):  Example: {'instanceUid':
            '1bcb374f-b346-68b3-bd70-2b40cc7ff6ae', 'originalUid':
            '7fa501dc-f769-4d71-83b1-4f6859c43925', 'name': 'Backup Job 23', 'description':
            'Customized Job Configuration', 'isDisabled': False, 'mappedOrganizationUid':
            '3337e028-55e1-453f-800c-3085a43033c6', 'mappedOrganizationName': 'hosted',
            'backupServerUid': '91d5797e-c80b-48e5-bb97-b9df5707f14f', 'backupServerName': 'vbr1',
            'isHighPriority': False, 'virtualMachines': {'includes': [{'inventoryObject': {'hostName':
            'vc1.tech.local', 'name': 'lis-l1-1', 'type': 'VirtualMachine', 'objectId': 'vm-91024'},
            'size': '49.4 GB'}, {'inventoryObject': {'hostName': 'vc1.tech.local', 'name': 'lis-l1-2',
            'type': 'VirtualMachine', 'objectId': 'vm-91025'}, 'size': '49.4 GB'}], 'excludes':
            {'vms': [], 'disks': [{'vmObject': {'hostName': 'vc1.tech.local', 'name': 'lis-l1-1',
            'type': 'VirtualMachine', 'objectId': 'vm-91024'}, 'disksToProcess': 'AllDisks', 'disks':
            [], 'removeFromVMConfiguration': True}, {'vmObject': {'hostName': 'vc1.tech.local',
            'name': 'lis-l1-2', 'type': 'VirtualMachine', 'objectId': 'vm-91025'}, 'disksToProcess':
            'AllDisks', 'disks': [], 'removeFromVMConfiguration': True}], 'templates': {'isEnabled':
            True, 'excludeFromIncremental': True}}}, 'storage': {'backupRepositoryId':
            '88788f9e-d8f5-4eb4-bc4f-9b3f5403bcec', 'backupProxies': {'autoSelection': True,
            'proxyIds': []}, 'retentionPolicy': {'type': 'Days', 'quantity': 7}, 'gfsPolicy':
            {'isEnabled': False, 'weekly': {'isEnabled': False, 'keepForNumberOfWeeks': 1,
            'desiredTime': 'Monday'}, 'monthly': {'isEnabled': False, 'keepForNumberOfMonths': 1,
            'desiredTime': 'First'}, 'yearly': {'isEnabled': False, 'keepForNumberOfYears': 1,
            'desiredTime': 'Jan'}}, 'advancedSettings': {'backupModeType': 'Incremental',
            'syntheticFulls': {'isEnabled': True, 'weekly': {'isEnabled': True, 'days': ['Saturday']},
            'monthly': {'isEnabled': False, 'dayOfWeek': 'Monday', 'dayNumberInMonth': 'First',
            'dayOfMonths': 1, 'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
            'Sep', 'Oct', 'Nov', 'Dec']}}, 'activeFulls': {'isEnabled': False, 'weekly': {'isEnabled':
            True, 'days': ['Saturday']}, 'monthly': {'isEnabled': False, 'dayOfWeek': 'Monday',
            'dayNumberInMonth': 'First', 'dayOfMonths': 1, 'months': ['Jan', 'Feb', 'Mar', 'Apr',
            'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}}, 'backupHealth': {'isEnabled':
            False, 'weekly': {'isEnabled': False, 'days': ['Saturday']}, 'monthly': {'isEnabled':
            True, 'dayOfWeek': 'Saturday', 'dayNumberInMonth': 'Last', 'dayOfMonths': 1, 'months':
            ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}},
            'fullBackupMaintenance': {'removeData': {'isEnabled': False, 'afterDays': 14},
            'defragmentAndCompact': {'isEnabled': False, 'weekly': {'isEnabled': False, 'days':
            ['Saturday']}, 'monthly': {'isEnabled': True, 'dayOfWeek': 'Saturday', 'dayNumberInMonth':
            'Last', 'dayOfMonths': 1, 'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
            'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}}}, 'storageData': {'enableInlineDataDeduplication':
            True, 'excludeSwapFileBlocks': True, 'excludeDeletedFileBlocks': True, 'compressionLevel':
            'Optimal', 'storageOptimization': 'LocalTarget', 'encryption': {'isEnabled': False,
            'encryptionType': 'ByUserPassword', 'encryptionPasswordId': None, 'encryptionPasswordTag':
            None, 'kmsServerId': None}}, 'notifications': {'sendSNMPNotifications': False,
            'emailNotifications': {'isEnabled': False, 'recipients': [], 'notificationType':
            'UseGlobalNotificationSettings', 'customNotificationSettings': None}, 'vmAttribute':
            {'isEnabled': False, 'notes': 'Notes', 'appendToExistingValue': True}}, 'vSphere':
            {'enableVMWareToolsQuiescence': False, 'changedBlockTracking': {'isEnabled': True,
            'enableCbtAutomatically': True, 'resetCbtOnActiveFull': True}}, 'storageIntegration':
            {'isEnabled': True, 'limitProcessedVm': False, 'limitProcessedVmCount': 10,
            'failoverToStandardBackup': False}, 'scripts': {'preCommand': {'isEnabled': False,
            'command': ''}, 'postCommand': {'isEnabled': False, 'command': ''}, 'periodicityType':
            'BackupSessions', 'runScriptEvery': 1, 'dayOfWeek': ['Saturday']}}}, 'guestProcessing':
            {'appAwareProcessing': {'isEnabled': False, 'appSettings': []}, 'guestFSIndexing':
            {'isEnabled': False, 'indexingSettings': []}, 'guestInteractionProxies': {'autoSelection':
            True, 'proxyIds': []}, 'guestCredentials': None}, 'schedule': {'runAutomatically': False,
            'daily': {'isEnabled': True, 'localTime': '10:00', 'dailyKind': 'Everyday', 'days':
            ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']},
            'monthly': {'isEnabled': False, 'localTime': '10:00', 'dayOfWeek': 'Saturday',
            'dayNumberInMonth': 'Fourth', 'dayOfMonth': None, 'months': ['Jan', 'Feb', 'Mar', 'Apr',
            'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}, 'periodically': {'isEnabled':
            False, 'periodicallyKind': 'Hours', 'frequency': 1, 'backupWindow': {'days': [{'day':
            'Sunday', 'hours': '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Monday',
            'hours': '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Tuesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Wednesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Thursday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Friday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Saturday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}]}, 'startTimeWithinAnHour': 0},
            'continuously': {'isEnabled': False, 'backupWindow': {'days': [{'day': 'Sunday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Monday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Tuesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Wednesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Thursday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Friday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Saturday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}]}}, 'afterThisJob': {'isEnabled':
            False, 'jobName': None}, 'retry': {'isEnabled': False, 'retryCount': 3, 'awaitMinutes':
            10}, 'backupWindow': {'isEnabled': False, 'backupWindow': {'days': [{'day': 'Sunday',
            'hours': '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Monday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Tuesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Wednesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Thursday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Friday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Saturday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}]}}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateBackupServerBackupVmVSphereJobResponse200 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        backup_server_uid=backup_server_uid,
        body=body,
        mapped_organization_uid=mapped_organization_uid,
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
    body: BackupServerBackupJobConfiguration,
    mapped_organization_uid: UUID | Unset = UNSET,
    select: str | Unset = UNSET,
    x_request_id: UUID | Unset = UNSET,
    x_client_version: str | Unset = UNSET,
) -> Any | CreateBackupServerBackupVmVSphereJobResponse200 | ErrorResponse | None:
    """Create VMware vSphere VM Backup Job

     Creates a VMware VSphere VM backup job on a Veeam Backup & Replication server with the specified
    UID.

    Args:
        backup_server_uid (UUID):
        mapped_organization_uid (UUID | Unset):
        select (str | Unset):
        x_request_id (UUID | Unset):
        x_client_version (str | Unset):
        body (BackupServerBackupJobConfiguration):  Example: {'instanceUid':
            '1bcb374f-b346-68b3-bd70-2b40cc7ff6ae', 'originalUid':
            '7fa501dc-f769-4d71-83b1-4f6859c43925', 'name': 'Backup Job 23', 'description':
            'Customized Job Configuration', 'isDisabled': False, 'mappedOrganizationUid':
            '3337e028-55e1-453f-800c-3085a43033c6', 'mappedOrganizationName': 'hosted',
            'backupServerUid': '91d5797e-c80b-48e5-bb97-b9df5707f14f', 'backupServerName': 'vbr1',
            'isHighPriority': False, 'virtualMachines': {'includes': [{'inventoryObject': {'hostName':
            'vc1.tech.local', 'name': 'lis-l1-1', 'type': 'VirtualMachine', 'objectId': 'vm-91024'},
            'size': '49.4 GB'}, {'inventoryObject': {'hostName': 'vc1.tech.local', 'name': 'lis-l1-2',
            'type': 'VirtualMachine', 'objectId': 'vm-91025'}, 'size': '49.4 GB'}], 'excludes':
            {'vms': [], 'disks': [{'vmObject': {'hostName': 'vc1.tech.local', 'name': 'lis-l1-1',
            'type': 'VirtualMachine', 'objectId': 'vm-91024'}, 'disksToProcess': 'AllDisks', 'disks':
            [], 'removeFromVMConfiguration': True}, {'vmObject': {'hostName': 'vc1.tech.local',
            'name': 'lis-l1-2', 'type': 'VirtualMachine', 'objectId': 'vm-91025'}, 'disksToProcess':
            'AllDisks', 'disks': [], 'removeFromVMConfiguration': True}], 'templates': {'isEnabled':
            True, 'excludeFromIncremental': True}}}, 'storage': {'backupRepositoryId':
            '88788f9e-d8f5-4eb4-bc4f-9b3f5403bcec', 'backupProxies': {'autoSelection': True,
            'proxyIds': []}, 'retentionPolicy': {'type': 'Days', 'quantity': 7}, 'gfsPolicy':
            {'isEnabled': False, 'weekly': {'isEnabled': False, 'keepForNumberOfWeeks': 1,
            'desiredTime': 'Monday'}, 'monthly': {'isEnabled': False, 'keepForNumberOfMonths': 1,
            'desiredTime': 'First'}, 'yearly': {'isEnabled': False, 'keepForNumberOfYears': 1,
            'desiredTime': 'Jan'}}, 'advancedSettings': {'backupModeType': 'Incremental',
            'syntheticFulls': {'isEnabled': True, 'weekly': {'isEnabled': True, 'days': ['Saturday']},
            'monthly': {'isEnabled': False, 'dayOfWeek': 'Monday', 'dayNumberInMonth': 'First',
            'dayOfMonths': 1, 'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
            'Sep', 'Oct', 'Nov', 'Dec']}}, 'activeFulls': {'isEnabled': False, 'weekly': {'isEnabled':
            True, 'days': ['Saturday']}, 'monthly': {'isEnabled': False, 'dayOfWeek': 'Monday',
            'dayNumberInMonth': 'First', 'dayOfMonths': 1, 'months': ['Jan', 'Feb', 'Mar', 'Apr',
            'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}}, 'backupHealth': {'isEnabled':
            False, 'weekly': {'isEnabled': False, 'days': ['Saturday']}, 'monthly': {'isEnabled':
            True, 'dayOfWeek': 'Saturday', 'dayNumberInMonth': 'Last', 'dayOfMonths': 1, 'months':
            ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}},
            'fullBackupMaintenance': {'removeData': {'isEnabled': False, 'afterDays': 14},
            'defragmentAndCompact': {'isEnabled': False, 'weekly': {'isEnabled': False, 'days':
            ['Saturday']}, 'monthly': {'isEnabled': True, 'dayOfWeek': 'Saturday', 'dayNumberInMonth':
            'Last', 'dayOfMonths': 1, 'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
            'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}}}, 'storageData': {'enableInlineDataDeduplication':
            True, 'excludeSwapFileBlocks': True, 'excludeDeletedFileBlocks': True, 'compressionLevel':
            'Optimal', 'storageOptimization': 'LocalTarget', 'encryption': {'isEnabled': False,
            'encryptionType': 'ByUserPassword', 'encryptionPasswordId': None, 'encryptionPasswordTag':
            None, 'kmsServerId': None}}, 'notifications': {'sendSNMPNotifications': False,
            'emailNotifications': {'isEnabled': False, 'recipients': [], 'notificationType':
            'UseGlobalNotificationSettings', 'customNotificationSettings': None}, 'vmAttribute':
            {'isEnabled': False, 'notes': 'Notes', 'appendToExistingValue': True}}, 'vSphere':
            {'enableVMWareToolsQuiescence': False, 'changedBlockTracking': {'isEnabled': True,
            'enableCbtAutomatically': True, 'resetCbtOnActiveFull': True}}, 'storageIntegration':
            {'isEnabled': True, 'limitProcessedVm': False, 'limitProcessedVmCount': 10,
            'failoverToStandardBackup': False}, 'scripts': {'preCommand': {'isEnabled': False,
            'command': ''}, 'postCommand': {'isEnabled': False, 'command': ''}, 'periodicityType':
            'BackupSessions', 'runScriptEvery': 1, 'dayOfWeek': ['Saturday']}}}, 'guestProcessing':
            {'appAwareProcessing': {'isEnabled': False, 'appSettings': []}, 'guestFSIndexing':
            {'isEnabled': False, 'indexingSettings': []}, 'guestInteractionProxies': {'autoSelection':
            True, 'proxyIds': []}, 'guestCredentials': None}, 'schedule': {'runAutomatically': False,
            'daily': {'isEnabled': True, 'localTime': '10:00', 'dailyKind': 'Everyday', 'days':
            ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']},
            'monthly': {'isEnabled': False, 'localTime': '10:00', 'dayOfWeek': 'Saturday',
            'dayNumberInMonth': 'Fourth', 'dayOfMonth': None, 'months': ['Jan', 'Feb', 'Mar', 'Apr',
            'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}, 'periodically': {'isEnabled':
            False, 'periodicallyKind': 'Hours', 'frequency': 1, 'backupWindow': {'days': [{'day':
            'Sunday', 'hours': '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Monday',
            'hours': '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Tuesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Wednesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Thursday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Friday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Saturday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}]}, 'startTimeWithinAnHour': 0},
            'continuously': {'isEnabled': False, 'backupWindow': {'days': [{'day': 'Sunday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Monday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Tuesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Wednesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Thursday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Friday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Saturday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}]}}, 'afterThisJob': {'isEnabled':
            False, 'jobName': None}, 'retry': {'isEnabled': False, 'retryCount': 3, 'awaitMinutes':
            10}, 'backupWindow': {'isEnabled': False, 'backupWindow': {'days': [{'day': 'Sunday',
            'hours': '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Monday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Tuesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Wednesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Thursday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Friday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Saturday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}]}}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateBackupServerBackupVmVSphereJobResponse200 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            backup_server_uid=backup_server_uid,
            client=client,
            body=body,
            mapped_organization_uid=mapped_organization_uid,
            select=select,
            x_request_id=x_request_id,
            x_client_version=x_client_version,
        )
    ).parsed
