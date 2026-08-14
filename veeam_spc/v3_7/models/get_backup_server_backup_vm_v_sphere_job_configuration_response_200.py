from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_configuration import BackupServerBackupJobConfiguration
    from ..models.response_error import ResponseError
    from ..models.response_metadata import ResponseMetadata


T = TypeVar("T", bound="GetBackupServerBackupVmVSphereJobConfigurationResponse200")


@_attrs_define
class GetBackupServerBackupVmVSphereJobConfigurationResponse200:
    """
    Attributes:
        data (BackupServerBackupJobConfiguration):  Example: {'instanceUid': '1bcb374f-b346-68b3-bd70-2b40cc7ff6ae',
            'originalUid': '7fa501dc-f769-4d71-83b1-4f6859c43925', 'name': 'Backup Job 23', 'description': 'Customized Job
            Configuration', 'isDisabled': False, 'mappedOrganizationUid': '3337e028-55e1-453f-800c-3085a43033c6',
            'mappedOrganizationName': 'hosted', 'backupServerUid': '91d5797e-c80b-48e5-bb97-b9df5707f14f',
            'backupServerName': 'vbr1', 'isHighPriority': False, 'virtualMachines': {'includes': [{'inventoryObject':
            {'hostName': 'vc1.tech.local', 'name': 'lis-l1-1', 'type': 'VirtualMachine', 'objectId': 'vm-91024'}, 'size':
            '49.4 GB'}, {'inventoryObject': {'hostName': 'vc1.tech.local', 'name': 'lis-l1-2', 'type': 'VirtualMachine',
            'objectId': 'vm-91025'}, 'size': '49.4 GB'}], 'excludes': {'vms': [], 'disks': [{'vmObject': {'hostName':
            'vc1.tech.local', 'name': 'lis-l1-1', 'type': 'VirtualMachine', 'objectId': 'vm-91024'}, 'disksToProcess':
            'AllDisks', 'disks': [], 'removeFromVMConfiguration': True}, {'vmObject': {'hostName': 'vc1.tech.local', 'name':
            'lis-l1-2', 'type': 'VirtualMachine', 'objectId': 'vm-91025'}, 'disksToProcess': 'AllDisks', 'disks': [],
            'removeFromVMConfiguration': True}], 'templates': {'isEnabled': True, 'excludeFromIncremental': True}}},
            'storage': {'backupRepositoryId': '88788f9e-d8f5-4eb4-bc4f-9b3f5403bcec', 'backupProxies': {'autoSelection':
            True, 'proxyIds': []}, 'retentionPolicy': {'type': 'Days', 'quantity': 7}, 'gfsPolicy': {'isEnabled': False,
            'weekly': {'isEnabled': False, 'keepForNumberOfWeeks': 1, 'desiredTime': 'Monday'}, 'monthly': {'isEnabled':
            False, 'keepForNumberOfMonths': 1, 'desiredTime': 'First'}, 'yearly': {'isEnabled': False,
            'keepForNumberOfYears': 1, 'desiredTime': 'Jan'}}, 'advancedSettings': {'backupModeType': 'Incremental',
            'syntheticFulls': {'isEnabled': True, 'weekly': {'isEnabled': True, 'days': ['Saturday']}, 'monthly':
            {'isEnabled': False, 'dayOfWeek': 'Monday', 'dayNumberInMonth': 'First', 'dayOfMonths': 1, 'months': ['Jan',
            'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}}, 'activeFulls': {'isEnabled':
            False, 'weekly': {'isEnabled': True, 'days': ['Saturday']}, 'monthly': {'isEnabled': False, 'dayOfWeek':
            'Monday', 'dayNumberInMonth': 'First', 'dayOfMonths': 1, 'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}}, 'backupHealth': {'isEnabled': False, 'weekly': {'isEnabled': False,
            'days': ['Saturday']}, 'monthly': {'isEnabled': True, 'dayOfWeek': 'Saturday', 'dayNumberInMonth': 'Last',
            'dayOfMonths': 1, 'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov',
            'Dec']}}, 'fullBackupMaintenance': {'removeData': {'isEnabled': False, 'afterDays': 14}, 'defragmentAndCompact':
            {'isEnabled': False, 'weekly': {'isEnabled': False, 'days': ['Saturday']}, 'monthly': {'isEnabled': True,
            'dayOfWeek': 'Saturday', 'dayNumberInMonth': 'Last', 'dayOfMonths': 1, 'months': ['Jan', 'Feb', 'Mar', 'Apr',
            'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}}}, 'storageData': {'enableInlineDataDeduplication':
            True, 'excludeSwapFileBlocks': True, 'excludeDeletedFileBlocks': True, 'compressionLevel': 'Optimal',
            'storageOptimization': 'LocalTarget', 'encryption': {'isEnabled': False, 'encryptionType': 'ByUserPassword',
            'encryptionPasswordId': None, 'encryptionPasswordTag': None, 'kmsServerId': None}}, 'notifications':
            {'sendSNMPNotifications': False, 'emailNotifications': {'isEnabled': False, 'recipients': [],
            'notificationType': 'UseGlobalNotificationSettings', 'customNotificationSettings': None}, 'vmAttribute':
            {'isEnabled': False, 'notes': 'Notes', 'appendToExistingValue': True}}, 'vSphere':
            {'enableVMWareToolsQuiescence': False, 'changedBlockTracking': {'isEnabled': True, 'enableCbtAutomatically':
            True, 'resetCbtOnActiveFull': True}}, 'storageIntegration': {'isEnabled': True, 'limitProcessedVm': False,
            'limitProcessedVmCount': 10, 'failoverToStandardBackup': False}, 'scripts': {'preCommand': {'isEnabled': False,
            'command': ''}, 'postCommand': {'isEnabled': False, 'command': ''}, 'periodicityType': 'BackupSessions',
            'runScriptEvery': 1, 'dayOfWeek': ['Saturday']}}}, 'guestProcessing': {'appAwareProcessing': {'isEnabled':
            False, 'appSettings': []}, 'guestFSIndexing': {'isEnabled': False, 'indexingSettings': []},
            'guestInteractionProxies': {'autoSelection': True, 'proxyIds': []}, 'guestCredentials': None}, 'schedule':
            {'runAutomatically': False, 'daily': {'isEnabled': True, 'localTime': '10:00', 'dailyKind': 'Everyday', 'days':
            ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']}, 'monthly': {'isEnabled': False,
            'localTime': '10:00', 'dayOfWeek': 'Saturday', 'dayNumberInMonth': 'Fourth', 'dayOfMonth': None, 'months':
            ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}, 'periodically':
            {'isEnabled': False, 'periodicallyKind': 'Hours', 'frequency': 1, 'backupWindow': {'days': [{'day': 'Sunday',
            'hours': '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Monday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Tuesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Wednesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Thursday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Friday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Saturday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}]}, 'startTimeWithinAnHour': 0}, 'continuously': {'isEnabled':
            False, 'backupWindow': {'days': [{'day': 'Sunday', 'hours': '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'},
            {'day': 'Monday', 'hours': '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Tuesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Wednesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Thursday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Friday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Saturday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}]}}, 'afterThisJob': {'isEnabled': False, 'jobName': None},
            'retry': {'isEnabled': False, 'retryCount': 3, 'awaitMinutes': 10}, 'backupWindow': {'isEnabled': False,
            'backupWindow': {'days': [{'day': 'Sunday', 'hours': '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day':
            'Monday', 'hours': '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Tuesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Wednesday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Thursday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Friday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}, {'day': 'Saturday', 'hours':
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}]}}}}.
        meta (ResponseMetadata | Unset):
        errors (list[ResponseError] | Unset):
    """

    data: BackupServerBackupJobConfiguration
    meta: ResponseMetadata | Unset = UNSET
    errors: list[ResponseError] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if meta is not UNSET:
            field_dict["meta"] = meta
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_backup_job_configuration import BackupServerBackupJobConfiguration
        from ..models.response_error import ResponseError
        from ..models.response_metadata import ResponseMetadata

        d = dict(src_dict)
        data = BackupServerBackupJobConfiguration.from_dict(d.pop("data"))

        _meta = d.pop("meta", UNSET)
        meta: ResponseMetadata | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ResponseMetadata.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[ResponseError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = ResponseError.from_dict(errors_item_data)

                errors.append(errors_item)

        get_backup_server_backup_vm_v_sphere_job_configuration_response_200 = cls(
            data=data,
            meta=meta,
            errors=errors,
        )

        get_backup_server_backup_vm_v_sphere_job_configuration_response_200.additional_properties = d
        return get_backup_server_backup_vm_v_sphere_job_configuration_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
