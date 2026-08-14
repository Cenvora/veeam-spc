from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_job_operation_mode import BackupJobOperationMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cloud_repository_connection_settings import CloudRepositoryConnectionSettings
    from ..models.linux_backup_job_configuration import LinuxBackupJobConfiguration


T = TypeVar("T", bound="LinuxCustomJobConfiguration")


@_attrs_define
class LinuxCustomJobConfiguration:
    """
    Example:
        {'name': 'ServerEntireCloud_Custom', 'description': 'Linux Policy', 'operationMode': 'Server',
            'cloudRepositoryConnectionSettings': {'backupResourceUid': '28428289-2557-41b5-a51d-06730a24f23a', 'username':
            'admin', 'password': 'Password1'}, 'jobConfiguration': {'backupSource': {'backupMode': 'EntireComputer',
            'volumeLevelOptions': None, 'fileLevelOptions': None}, 'backupTarget': {'targetType': 'CloudRepository',
            'localPath': None, 'sharedFolder': None, 'backupRepository': None, 'enableDeletedFilesRetention': True,
            'removeDeletedItemsDataAfter': 5}, 'backupStorage': {'compressionLevel': 'Optimal', 'blockSize': 'Local1MB',
            'encryptionEnabled': False, 'password': None, 'passwordHint': None, 'isSnapshotRequired': True},
            'indexingSettings': None, 'scriptSettings': {'enabled': False, 'preJobScript': None, 'postJobScript': None,
            'preFreezeScript': None, 'postThawScript': None}, 'retentionSettings': {'restorePointsCount': 10,
            'retentionDays': 7}, 'scheduleSettings': {'scheduleType': 'Daily', 'dailyScheduleSettings': {'time': '03:30',
            'dailyMode': 'Everyday', 'specificDays': None}, 'monthlyScheduleSettings': None, 'periodicallyScheduleSettings':
            None, 'activeFullSettings': {'scheduleType': 'Monthly', 'monthly': {'monthlyMode': 'Day', 'weekDayNumber':
            'First', 'dayOfMonth': 0, 'dayOfWeek': 'Sunday', 'months': []}, 'weeklyOnDays': ['Saturday']}, 'retrySettings':
            {'enabled': True, 'retryTimes': 3, 'waitTimeoutMinutes': 10}, 'backupHealthCheckScheduleSettings': None,
            'syntheticFullSettings': None}, 'applicationAwareProcessingSettings': {'oracleAapSettings': {'processingType':
            'DisableProcess', 'credentials': None, 'truncationConfig': {'truncationMode': 'TruncateDisabled', 'sizeGB': 1,
            'lifeTimeHours': 1}, 'useOracleCredentials': False}, 'mySqlAapSettings': {'processingType': 'DisableProcess',
            'credentials': {'username': 'admin', 'password': 'Password1'}, 'authType': 'MySQLPassword', 'passwordFilePath':
            None}, 'postgreSqlAapSettings': {'processingType': 'DisableProcess', 'credentials': {'username': 'admin',
            'password': 'Password1'}, 'authType': 'PSQLPassword'}}, 'gfsRetentionSettings': {'weekly':
            {'keepWeeklyBackupsForWeeks': 1, 'useFullBackupFrom': 'Tuesday'}, 'monthly': {'keepMonthlyBackupsForMonths': 2,
            'useWeeklyFullBackupForTheFollowingWeekOfMonth': 'Second'}, 'yearly': {'keepYearlyBackupsForYears': 3,
            'useMonthlyFullBackupForTheFollowingMonth': 'Jan'}}}}

    Attributes:
        name (str): Job name.
        operation_mode (BackupJobOperationMode): Backup job operation mode.
        job_configuration (LinuxBackupJobConfiguration):
        description (str | Unset): Job description.
        cloud_repository_connection_settings (CloudRepositoryConnectionSettings | Unset): Settings required to connect a
            cloud repository that is used as a target location for backups.
    """

    name: str
    operation_mode: BackupJobOperationMode
    job_configuration: LinuxBackupJobConfiguration
    description: str | Unset = UNSET
    cloud_repository_connection_settings: CloudRepositoryConnectionSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        operation_mode = self.operation_mode.value

        job_configuration = self.job_configuration.to_dict()

        description = self.description

        cloud_repository_connection_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cloud_repository_connection_settings, Unset):
            cloud_repository_connection_settings = self.cloud_repository_connection_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "operationMode": operation_mode,
                "jobConfiguration": job_configuration,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if cloud_repository_connection_settings is not UNSET:
            field_dict["cloudRepositoryConnectionSettings"] = cloud_repository_connection_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cloud_repository_connection_settings import CloudRepositoryConnectionSettings
        from ..models.linux_backup_job_configuration import LinuxBackupJobConfiguration

        d = dict(src_dict)
        name = d.pop("name")

        operation_mode = BackupJobOperationMode(d.pop("operationMode"))

        job_configuration = LinuxBackupJobConfiguration.from_dict(d.pop("jobConfiguration"))

        description = d.pop("description", UNSET)

        _cloud_repository_connection_settings = d.pop("cloudRepositoryConnectionSettings", UNSET)
        cloud_repository_connection_settings: CloudRepositoryConnectionSettings | Unset
        if isinstance(_cloud_repository_connection_settings, Unset):
            cloud_repository_connection_settings = UNSET
        else:
            cloud_repository_connection_settings = CloudRepositoryConnectionSettings.from_dict(
                _cloud_repository_connection_settings
            )

        linux_custom_job_configuration = cls(
            name=name,
            operation_mode=operation_mode,
            job_configuration=job_configuration,
            description=description,
            cloud_repository_connection_settings=cloud_repository_connection_settings,
        )

        linux_custom_job_configuration.additional_properties = d
        return linux_custom_job_configuration

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
