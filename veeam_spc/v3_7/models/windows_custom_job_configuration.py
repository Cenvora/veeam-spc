from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_job_operation_mode import BackupJobOperationMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cloud_repository_connection_settings_type_0 import CloudRepositoryConnectionSettingsType0
    from ..models.windows_backup_job_configuration import WindowsBackupJobConfiguration


T = TypeVar("T", bound="WindowsCustomJobConfiguration")


@_attrs_define
class WindowsCustomJobConfiguration:
    r"""
    Example:
        {'name': 'Windows workstation - Personal files - winsrv2', 'description': 'This policy processes user profile
            folder including all user settings and data.', 'operationMode': 'Workstation',
            'cloudRepositoryConnectionSettings': {'backupResourceUid': 'ae61e533-82c7-4cb6-a030-78ae589cf49d', 'username':
            'vspc\\admin', 'password': None}, 'jobConfiguration': {'backupSource': {'backupMode': 'FilesFolders',
            'computerLevelOptions': None, 'volumeLevelOptions': None, 'fileLevelOptions': {'includeDirectories': None,
            'excludeDirectories': None, 'inclusionMasks': None, 'exclusionMasks': None, 'osfilesIncluded': False,
            'excludeOneDriveFolders': False, 'personalFilesIncluded': True, 'personalFilesAdvancedSettings': {'inclusions':
            ['Desktop', 'Documents', 'Pictures', 'Video', 'Music', 'Favorites', 'Downloads', 'ApplicationData',
            'OtherFilesAndFolders'], 'excludeNetworkAccount': False}}}, 'backupTarget': {'targetType': 'CloudRepository',
            'localPath': None, 'sharedFolder': None, 'backupRepository': None, 'cloudRepository': None},
            'serverModeSettings': None, 'workstationModeSettings': {'scheduleSetting': {'periodicalScheduleEnabled': True,
            'periodicalScheduleSettings': {'dailyScheduleSettings': {'time': '00:30', 'dailyMode': 'Everyday',
            'specificDays': None}, 'shutdownAction': 'BackupOncePoweredOn', 'finalizingAction': 'KeepRunning'},
            'eventTriggerSettings': {'backupOnLock': False, 'backupOnLogOff': False, 'backupOnTargetConnection': False,
            'ejectTargetOnBackupComplete': False, 'backupNotOften': 2, 'notOftenTimeUnit': 'Hours'}}, 'retentionSettings':
            {'retentionDays': 7}}, 'advancedSettings': {'backupStorage': {'compressionLevel': 'Optimal',
            'storageOptimization': 'Lan512KB', 'encryptionEnabled': False, 'password': None, 'passwordHint': None},
            'scheduleSettings': {'syntheticFullSettings': None, 'activeFullSettings': None}, 'maintenanceSettings':
            {'backupHealthCheckSettings': None, 'fullBackupFileMaintenanceSettings': {'enableDeletedFilesRetention': False,
            'removeDeletedItemsDataAfter': 30, 'defragmentAndCompactFullBackupFileSettings': None}, 'fullHealthCheck':
            False}}, 'gfsRetentionSettings': None}}

    Attributes:
        name (str): Job name.
        operation_mode (BackupJobOperationMode): Backup job operation mode.
        job_configuration (WindowsBackupJobConfiguration):
        description (None | str | Unset): Job description.
        cloud_repository_connection_settings (CloudRepositoryConnectionSettingsType0 | None | Unset): Settings required
            to connect a cloud repository that is used as a target location for backups.
    """

    name: str
    operation_mode: BackupJobOperationMode
    job_configuration: WindowsBackupJobConfiguration
    description: None | str | Unset = UNSET
    cloud_repository_connection_settings: CloudRepositoryConnectionSettingsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cloud_repository_connection_settings_type_0 import CloudRepositoryConnectionSettingsType0

        name = self.name

        operation_mode = self.operation_mode.value

        job_configuration = self.job_configuration.to_dict()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        cloud_repository_connection_settings: dict[str, Any] | None | Unset
        if isinstance(self.cloud_repository_connection_settings, Unset):
            cloud_repository_connection_settings = UNSET
        elif isinstance(self.cloud_repository_connection_settings, CloudRepositoryConnectionSettingsType0):
            cloud_repository_connection_settings = self.cloud_repository_connection_settings.to_dict()
        else:
            cloud_repository_connection_settings = self.cloud_repository_connection_settings

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
        from ..models.cloud_repository_connection_settings_type_0 import CloudRepositoryConnectionSettingsType0
        from ..models.windows_backup_job_configuration import WindowsBackupJobConfiguration

        d = dict(src_dict)
        name = d.pop("name")

        operation_mode = BackupJobOperationMode(d.pop("operationMode"))

        job_configuration = WindowsBackupJobConfiguration.from_dict(d.pop("jobConfiguration"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_cloud_repository_connection_settings(
            data: object,
        ) -> CloudRepositoryConnectionSettingsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_cloud_repository_connection_settings_type_0 = (
                    CloudRepositoryConnectionSettingsType0.from_dict(data)
                )

                return componentsschemas_cloud_repository_connection_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CloudRepositoryConnectionSettingsType0 | None | Unset, data)

        cloud_repository_connection_settings = _parse_cloud_repository_connection_settings(
            d.pop("cloudRepositoryConnectionSettings", UNSET)
        )

        windows_custom_job_configuration = cls(
            name=name,
            operation_mode=operation_mode,
            job_configuration=job_configuration,
            description=description,
            cloud_repository_connection_settings=cloud_repository_connection_settings,
        )

        windows_custom_job_configuration.additional_properties = d
        return windows_custom_job_configuration

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
