from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_guest_processing import BackupServerBackupJobGuestProcessing
    from ..models.backup_server_backup_job_schedule import BackupServerBackupJobSchedule
    from ..models.backup_server_backup_job_storage import BackupServerBackupJobStorage
    from ..models.backup_server_backup_job_virtual_machines import BackupServerBackupJobVirtualMachines


T = TypeVar("T", bound="BackupServerBackupJobConfiguration")


@_attrs_define
class BackupServerBackupJobConfiguration:
    """
    Example:
        {'instanceUid': '1bcb374f-b346-68b3-bd70-2b40cc7ff6ae', 'originalUid': '7fa501dc-f769-4d71-83b1-4f6859c43925',
            'name': 'Backup Job 23', 'description': 'Customized Job Configuration', 'isDisabled': False,
            'mappedOrganizationUid': '3337e028-55e1-453f-800c-3085a43033c6', 'mappedOrganizationName': 'hosted',
            'backupServerUid': '91d5797e-c80b-48e5-bb97-b9df5707f14f', 'backupServerName': 'vbr1', 'isHighPriority': False,
            'virtualMachines': {'includes': [{'inventoryObject': {'hostName': 'vc1.tech.local', 'name': 'lis-l1-1', 'type':
            'VirtualMachine', 'objectId': 'vm-91024'}, 'size': '49.4 GB'}, {'inventoryObject': {'hostName':
            'vc1.tech.local', 'name': 'lis-l1-2', 'type': 'VirtualMachine', 'objectId': 'vm-91025'}, 'size': '49.4 GB'}],
            'excludes': {'vms': [], 'disks': [{'vmObject': {'hostName': 'vc1.tech.local', 'name': 'lis-l1-1', 'type':
            'VirtualMachine', 'objectId': 'vm-91024'}, 'disksToProcess': 'AllDisks', 'disks': [],
            'removeFromVMConfiguration': True}, {'vmObject': {'hostName': 'vc1.tech.local', 'name': 'lis-l1-2', 'type':
            'VirtualMachine', 'objectId': 'vm-91025'}, 'disksToProcess': 'AllDisks', 'disks': [],
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
            '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'}]}}}}

    Attributes:
        name (str): Name of a backup job.
        description (str): Description of a backup job.
        is_high_priority (bool): Indicates whether a backup job has a high priority in getting backup resources.
        virtual_machines (BackupServerBackupJobVirtualMachines): Backup scope.
        storage (BackupServerBackupJobStorage): Backup repository settings.
        instance_uid (UUID | Unset): UID assigned to a backup job.
        original_uid (UUID | Unset): UID assigned to a job in Veeam Backup & Replication.
        is_disabled (bool | Unset): Indicates whether a backup job is disabled.
        mapped_organization_uid (UUID | Unset): UID assigned to an organization that is mapped to a backup job on a
            hosted Veeam Backup & Replication server.
        mapped_organization_name (str | Unset): Name of an organization that is mapped to a backup job on a hosted Veeam
            Backup & Replication server.
        backup_server_uid (UUID | Unset): UID of a hosted Veeam Backup & Replication server.
        backup_server_name (str | Unset): Name of a hosted Veeam Backup & Replication server.
        guest_processing (BackupServerBackupJobGuestProcessing | Unset): Guest processing settings.
        schedule (BackupServerBackupJobSchedule | Unset): Job scheduling settings.
    """

    name: str
    description: str
    is_high_priority: bool
    virtual_machines: BackupServerBackupJobVirtualMachines
    storage: BackupServerBackupJobStorage
    instance_uid: UUID | Unset = UNSET
    original_uid: UUID | Unset = UNSET
    is_disabled: bool | Unset = UNSET
    mapped_organization_uid: UUID | Unset = UNSET
    mapped_organization_name: str | Unset = UNSET
    backup_server_uid: UUID | Unset = UNSET
    backup_server_name: str | Unset = UNSET
    guest_processing: BackupServerBackupJobGuestProcessing | Unset = UNSET
    schedule: BackupServerBackupJobSchedule | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        is_high_priority = self.is_high_priority

        virtual_machines = self.virtual_machines.to_dict()

        storage = self.storage.to_dict()

        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        original_uid: str | Unset = UNSET
        if not isinstance(self.original_uid, Unset):
            original_uid = str(self.original_uid)

        is_disabled = self.is_disabled

        mapped_organization_uid: str | Unset = UNSET
        if not isinstance(self.mapped_organization_uid, Unset):
            mapped_organization_uid = str(self.mapped_organization_uid)

        mapped_organization_name = self.mapped_organization_name

        backup_server_uid: str | Unset = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        backup_server_name = self.backup_server_name

        guest_processing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.guest_processing, Unset):
            guest_processing = self.guest_processing.to_dict()

        schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "isHighPriority": is_high_priority,
                "virtualMachines": virtual_machines,
                "storage": storage,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if original_uid is not UNSET:
            field_dict["originalUid"] = original_uid
        if is_disabled is not UNSET:
            field_dict["isDisabled"] = is_disabled
        if mapped_organization_uid is not UNSET:
            field_dict["mappedOrganizationUid"] = mapped_organization_uid
        if mapped_organization_name is not UNSET:
            field_dict["mappedOrganizationName"] = mapped_organization_name
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if backup_server_name is not UNSET:
            field_dict["backupServerName"] = backup_server_name
        if guest_processing is not UNSET:
            field_dict["guestProcessing"] = guest_processing
        if schedule is not UNSET:
            field_dict["schedule"] = schedule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_backup_job_guest_processing import BackupServerBackupJobGuestProcessing
        from ..models.backup_server_backup_job_schedule import BackupServerBackupJobSchedule
        from ..models.backup_server_backup_job_storage import BackupServerBackupJobStorage
        from ..models.backup_server_backup_job_virtual_machines import BackupServerBackupJobVirtualMachines

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        is_high_priority = d.pop("isHighPriority")

        virtual_machines = BackupServerBackupJobVirtualMachines.from_dict(d.pop("virtualMachines"))

        storage = BackupServerBackupJobStorage.from_dict(d.pop("storage"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _original_uid = d.pop("originalUid", UNSET)
        original_uid: UUID | Unset
        if isinstance(_original_uid, Unset):
            original_uid = UNSET
        else:
            original_uid = UUID(_original_uid)

        is_disabled = d.pop("isDisabled", UNSET)

        _mapped_organization_uid = d.pop("mappedOrganizationUid", UNSET)
        mapped_organization_uid: UUID | Unset
        if isinstance(_mapped_organization_uid, Unset):
            mapped_organization_uid = UNSET
        else:
            mapped_organization_uid = UUID(_mapped_organization_uid)

        mapped_organization_name = d.pop("mappedOrganizationName", UNSET)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: UUID | Unset
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        backup_server_name = d.pop("backupServerName", UNSET)

        _guest_processing = d.pop("guestProcessing", UNSET)
        guest_processing: BackupServerBackupJobGuestProcessing | Unset
        if isinstance(_guest_processing, Unset):
            guest_processing = UNSET
        else:
            guest_processing = BackupServerBackupJobGuestProcessing.from_dict(_guest_processing)

        _schedule = d.pop("schedule", UNSET)
        schedule: BackupServerBackupJobSchedule | Unset
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = BackupServerBackupJobSchedule.from_dict(_schedule)

        backup_server_backup_job_configuration = cls(
            name=name,
            description=description,
            is_high_priority=is_high_priority,
            virtual_machines=virtual_machines,
            storage=storage,
            instance_uid=instance_uid,
            original_uid=original_uid,
            is_disabled=is_disabled,
            mapped_organization_uid=mapped_organization_uid,
            mapped_organization_name=mapped_organization_name,
            backup_server_uid=backup_server_uid,
            backup_server_name=backup_server_name,
            guest_processing=guest_processing,
            schedule=schedule,
        )

        backup_server_backup_job_configuration.additional_properties = d
        return backup_server_backup_job_configuration

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
