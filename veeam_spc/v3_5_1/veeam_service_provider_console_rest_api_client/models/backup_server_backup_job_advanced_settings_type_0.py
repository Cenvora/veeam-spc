from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_backup_job_backup_mode_type import BackupServerBackupJobBackupModeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_active_full_settings_type_0 import (
        BackupServerBackupJobActiveFullSettingsType0,
    )
    from ..models.backup_server_backup_job_advanced_settings_v_sphere_type_0 import (
        BackupServerBackupJobAdvancedSettingsVSphereType0,
    )
    from ..models.backup_server_backup_job_full_backup_maintenance_type_0 import (
        BackupServerBackupJobFullBackupMaintenanceType0,
    )
    from ..models.backup_server_backup_job_health_check_settings_type_0 import (
        BackupServerBackupJobHealthCheckSettingsType0,
    )
    from ..models.backup_server_backup_job_notification_settings_type_0 import (
        BackupServerBackupJobNotificationSettingsType0,
    )
    from ..models.backup_server_backup_job_primary_storage_integration_settings_type_0 import (
        BackupServerBackupJobPrimaryStorageIntegrationSettingsType0,
    )
    from ..models.backup_server_backup_job_storage_setting_type_0 import BackupServerBackupJobStorageSettingType0
    from ..models.backup_server_backup_job_synthetic_full_settings_type_0 import (
        BackupServerBackupJobSyntheticFullSettingsType0,
    )
    from ..models.backup_server_job_scripts_settings_type_0 import BackupServerJobScriptsSettingsType0


T = TypeVar("T", bound="BackupServerBackupJobAdvancedSettingsType0")


@_attrs_define
class BackupServerBackupJobAdvancedSettingsType0:
    """Backup job advanced settings.

    Attributes:
        backup_mode_type (Union[Unset, BackupServerBackupJobBackupModeType]): Backup method.
        synthetic_fulls (Union['BackupServerBackupJobSyntheticFullSettingsType0', None, Unset]): Synthetic full backup
            settings.
        active_fulls (Union['BackupServerBackupJobActiveFullSettingsType0', None, Unset]): Active full backup settings.
        backup_health (Union['BackupServerBackupJobHealthCheckSettingsType0', None, Unset]): Health check settings for
            the latest restore point in the backup chain.
        full_backup_maintenance (Union['BackupServerBackupJobFullBackupMaintenanceType0', None, Unset]): Maintenance
            settings for full backup files.
        storage_data (Union['BackupServerBackupJobStorageSettingType0', None, Unset]): Storage settings.
        notifications (Union['BackupServerBackupJobNotificationSettingsType0', None, Unset]): Notification settings.
        v_sphere (Union['BackupServerBackupJobAdvancedSettingsVSphereType0', None, Unset]): VMware vSphere settings.
        storage_integration (Union['BackupServerBackupJobPrimaryStorageIntegrationSettingsType0', None, Unset]): Backup
            from Storage Snapshots settings.
        scripts (Union['BackupServerJobScriptsSettingsType0', None, Unset]): Script settings.
    """

    backup_mode_type: Union[Unset, BackupServerBackupJobBackupModeType] = UNSET
    synthetic_fulls: Union["BackupServerBackupJobSyntheticFullSettingsType0", None, Unset] = UNSET
    active_fulls: Union["BackupServerBackupJobActiveFullSettingsType0", None, Unset] = UNSET
    backup_health: Union["BackupServerBackupJobHealthCheckSettingsType0", None, Unset] = UNSET
    full_backup_maintenance: Union["BackupServerBackupJobFullBackupMaintenanceType0", None, Unset] = UNSET
    storage_data: Union["BackupServerBackupJobStorageSettingType0", None, Unset] = UNSET
    notifications: Union["BackupServerBackupJobNotificationSettingsType0", None, Unset] = UNSET
    v_sphere: Union["BackupServerBackupJobAdvancedSettingsVSphereType0", None, Unset] = UNSET
    storage_integration: Union["BackupServerBackupJobPrimaryStorageIntegrationSettingsType0", None, Unset] = UNSET
    scripts: Union["BackupServerJobScriptsSettingsType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.backup_server_backup_job_active_full_settings_type_0 import (
            BackupServerBackupJobActiveFullSettingsType0,
        )
        from ..models.backup_server_backup_job_advanced_settings_v_sphere_type_0 import (
            BackupServerBackupJobAdvancedSettingsVSphereType0,
        )
        from ..models.backup_server_backup_job_full_backup_maintenance_type_0 import (
            BackupServerBackupJobFullBackupMaintenanceType0,
        )
        from ..models.backup_server_backup_job_health_check_settings_type_0 import (
            BackupServerBackupJobHealthCheckSettingsType0,
        )
        from ..models.backup_server_backup_job_notification_settings_type_0 import (
            BackupServerBackupJobNotificationSettingsType0,
        )
        from ..models.backup_server_backup_job_primary_storage_integration_settings_type_0 import (
            BackupServerBackupJobPrimaryStorageIntegrationSettingsType0,
        )
        from ..models.backup_server_backup_job_storage_setting_type_0 import BackupServerBackupJobStorageSettingType0
        from ..models.backup_server_backup_job_synthetic_full_settings_type_0 import (
            BackupServerBackupJobSyntheticFullSettingsType0,
        )
        from ..models.backup_server_job_scripts_settings_type_0 import BackupServerJobScriptsSettingsType0

        backup_mode_type: Union[Unset, str] = UNSET
        if not isinstance(self.backup_mode_type, Unset):
            backup_mode_type = self.backup_mode_type.value

        synthetic_fulls: Union[None, Unset, dict[str, Any]]
        if isinstance(self.synthetic_fulls, Unset):
            synthetic_fulls = UNSET
        elif isinstance(self.synthetic_fulls, BackupServerBackupJobSyntheticFullSettingsType0):
            synthetic_fulls = self.synthetic_fulls.to_dict()
        else:
            synthetic_fulls = self.synthetic_fulls

        active_fulls: Union[None, Unset, dict[str, Any]]
        if isinstance(self.active_fulls, Unset):
            active_fulls = UNSET
        elif isinstance(self.active_fulls, BackupServerBackupJobActiveFullSettingsType0):
            active_fulls = self.active_fulls.to_dict()
        else:
            active_fulls = self.active_fulls

        backup_health: Union[None, Unset, dict[str, Any]]
        if isinstance(self.backup_health, Unset):
            backup_health = UNSET
        elif isinstance(self.backup_health, BackupServerBackupJobHealthCheckSettingsType0):
            backup_health = self.backup_health.to_dict()
        else:
            backup_health = self.backup_health

        full_backup_maintenance: Union[None, Unset, dict[str, Any]]
        if isinstance(self.full_backup_maintenance, Unset):
            full_backup_maintenance = UNSET
        elif isinstance(self.full_backup_maintenance, BackupServerBackupJobFullBackupMaintenanceType0):
            full_backup_maintenance = self.full_backup_maintenance.to_dict()
        else:
            full_backup_maintenance = self.full_backup_maintenance

        storage_data: Union[None, Unset, dict[str, Any]]
        if isinstance(self.storage_data, Unset):
            storage_data = UNSET
        elif isinstance(self.storage_data, BackupServerBackupJobStorageSettingType0):
            storage_data = self.storage_data.to_dict()
        else:
            storage_data = self.storage_data

        notifications: Union[None, Unset, dict[str, Any]]
        if isinstance(self.notifications, Unset):
            notifications = UNSET
        elif isinstance(self.notifications, BackupServerBackupJobNotificationSettingsType0):
            notifications = self.notifications.to_dict()
        else:
            notifications = self.notifications

        v_sphere: Union[None, Unset, dict[str, Any]]
        if isinstance(self.v_sphere, Unset):
            v_sphere = UNSET
        elif isinstance(self.v_sphere, BackupServerBackupJobAdvancedSettingsVSphereType0):
            v_sphere = self.v_sphere.to_dict()
        else:
            v_sphere = self.v_sphere

        storage_integration: Union[None, Unset, dict[str, Any]]
        if isinstance(self.storage_integration, Unset):
            storage_integration = UNSET
        elif isinstance(self.storage_integration, BackupServerBackupJobPrimaryStorageIntegrationSettingsType0):
            storage_integration = self.storage_integration.to_dict()
        else:
            storage_integration = self.storage_integration

        scripts: Union[None, Unset, dict[str, Any]]
        if isinstance(self.scripts, Unset):
            scripts = UNSET
        elif isinstance(self.scripts, BackupServerJobScriptsSettingsType0):
            scripts = self.scripts.to_dict()
        else:
            scripts = self.scripts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_mode_type is not UNSET:
            field_dict["backupModeType"] = backup_mode_type
        if synthetic_fulls is not UNSET:
            field_dict["syntheticFulls"] = synthetic_fulls
        if active_fulls is not UNSET:
            field_dict["activeFulls"] = active_fulls
        if backup_health is not UNSET:
            field_dict["backupHealth"] = backup_health
        if full_backup_maintenance is not UNSET:
            field_dict["fullBackupMaintenance"] = full_backup_maintenance
        if storage_data is not UNSET:
            field_dict["storageData"] = storage_data
        if notifications is not UNSET:
            field_dict["notifications"] = notifications
        if v_sphere is not UNSET:
            field_dict["vSphere"] = v_sphere
        if storage_integration is not UNSET:
            field_dict["storageIntegration"] = storage_integration
        if scripts is not UNSET:
            field_dict["scripts"] = scripts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_backup_job_active_full_settings_type_0 import (
            BackupServerBackupJobActiveFullSettingsType0,
        )
        from ..models.backup_server_backup_job_advanced_settings_v_sphere_type_0 import (
            BackupServerBackupJobAdvancedSettingsVSphereType0,
        )
        from ..models.backup_server_backup_job_full_backup_maintenance_type_0 import (
            BackupServerBackupJobFullBackupMaintenanceType0,
        )
        from ..models.backup_server_backup_job_health_check_settings_type_0 import (
            BackupServerBackupJobHealthCheckSettingsType0,
        )
        from ..models.backup_server_backup_job_notification_settings_type_0 import (
            BackupServerBackupJobNotificationSettingsType0,
        )
        from ..models.backup_server_backup_job_primary_storage_integration_settings_type_0 import (
            BackupServerBackupJobPrimaryStorageIntegrationSettingsType0,
        )
        from ..models.backup_server_backup_job_storage_setting_type_0 import BackupServerBackupJobStorageSettingType0
        from ..models.backup_server_backup_job_synthetic_full_settings_type_0 import (
            BackupServerBackupJobSyntheticFullSettingsType0,
        )
        from ..models.backup_server_job_scripts_settings_type_0 import BackupServerJobScriptsSettingsType0

        d = dict(src_dict)
        _backup_mode_type = d.pop("backupModeType", UNSET)
        backup_mode_type: Union[Unset, BackupServerBackupJobBackupModeType]
        if isinstance(_backup_mode_type, Unset):
            backup_mode_type = UNSET
        else:
            backup_mode_type = BackupServerBackupJobBackupModeType(_backup_mode_type)

        def _parse_synthetic_fulls(
            data: object,
        ) -> Union["BackupServerBackupJobSyntheticFullSettingsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_synthetic_full_settings_type_0 = (
                    BackupServerBackupJobSyntheticFullSettingsType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_synthetic_full_settings_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobSyntheticFullSettingsType0", None, Unset], data)

        synthetic_fulls = _parse_synthetic_fulls(d.pop("syntheticFulls", UNSET))

        def _parse_active_fulls(data: object) -> Union["BackupServerBackupJobActiveFullSettingsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_active_full_settings_type_0 = (
                    BackupServerBackupJobActiveFullSettingsType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_active_full_settings_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobActiveFullSettingsType0", None, Unset], data)

        active_fulls = _parse_active_fulls(d.pop("activeFulls", UNSET))

        def _parse_backup_health(data: object) -> Union["BackupServerBackupJobHealthCheckSettingsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_health_check_settings_type_0 = (
                    BackupServerBackupJobHealthCheckSettingsType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_health_check_settings_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobHealthCheckSettingsType0", None, Unset], data)

        backup_health = _parse_backup_health(d.pop("backupHealth", UNSET))

        def _parse_full_backup_maintenance(
            data: object,
        ) -> Union["BackupServerBackupJobFullBackupMaintenanceType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_full_backup_maintenance_type_0 = (
                    BackupServerBackupJobFullBackupMaintenanceType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_full_backup_maintenance_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobFullBackupMaintenanceType0", None, Unset], data)

        full_backup_maintenance = _parse_full_backup_maintenance(d.pop("fullBackupMaintenance", UNSET))

        def _parse_storage_data(data: object) -> Union["BackupServerBackupJobStorageSettingType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_storage_setting_type_0 = (
                    BackupServerBackupJobStorageSettingType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_storage_setting_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobStorageSettingType0", None, Unset], data)

        storage_data = _parse_storage_data(d.pop("storageData", UNSET))

        def _parse_notifications(data: object) -> Union["BackupServerBackupJobNotificationSettingsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_notification_settings_type_0 = (
                    BackupServerBackupJobNotificationSettingsType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_notification_settings_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobNotificationSettingsType0", None, Unset], data)

        notifications = _parse_notifications(d.pop("notifications", UNSET))

        def _parse_v_sphere(data: object) -> Union["BackupServerBackupJobAdvancedSettingsVSphereType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_advanced_settings_v_sphere_type_0 = (
                    BackupServerBackupJobAdvancedSettingsVSphereType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_advanced_settings_v_sphere_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobAdvancedSettingsVSphereType0", None, Unset], data)

        v_sphere = _parse_v_sphere(d.pop("vSphere", UNSET))

        def _parse_storage_integration(
            data: object,
        ) -> Union["BackupServerBackupJobPrimaryStorageIntegrationSettingsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_primary_storage_integration_settings_type_0 = (
                    BackupServerBackupJobPrimaryStorageIntegrationSettingsType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_primary_storage_integration_settings_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobPrimaryStorageIntegrationSettingsType0", None, Unset], data)

        storage_integration = _parse_storage_integration(d.pop("storageIntegration", UNSET))

        def _parse_scripts(data: object) -> Union["BackupServerJobScriptsSettingsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_job_scripts_settings_type_0 = (
                    BackupServerJobScriptsSettingsType0.from_dict(data)
                )

                return componentsschemas_backup_server_job_scripts_settings_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerJobScriptsSettingsType0", None, Unset], data)

        scripts = _parse_scripts(d.pop("scripts", UNSET))

        backup_server_backup_job_advanced_settings_type_0 = cls(
            backup_mode_type=backup_mode_type,
            synthetic_fulls=synthetic_fulls,
            active_fulls=active_fulls,
            backup_health=backup_health,
            full_backup_maintenance=full_backup_maintenance,
            storage_data=storage_data,
            notifications=notifications,
            v_sphere=v_sphere,
            storage_integration=storage_integration,
            scripts=scripts,
        )

        backup_server_backup_job_advanced_settings_type_0.additional_properties = d
        return backup_server_backup_job_advanced_settings_type_0

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
