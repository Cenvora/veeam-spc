from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_backup_job_backup_mode_type import BackupServerBackupJobBackupModeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_active_full_settings import BackupServerBackupJobActiveFullSettings
    from ..models.backup_server_backup_job_advanced_settings_v_sphere import (
        BackupServerBackupJobAdvancedSettingsVSphere,
    )
    from ..models.backup_server_backup_job_full_backup_maintenance import BackupServerBackupJobFullBackupMaintenance
    from ..models.backup_server_backup_job_health_check_settings import BackupServerBackupJobHealthCheckSettings
    from ..models.backup_server_backup_job_notification_settings import BackupServerBackupJobNotificationSettings
    from ..models.backup_server_backup_job_primary_storage_integration_settings import (
        BackupServerBackupJobPrimaryStorageIntegrationSettings,
    )
    from ..models.backup_server_backup_job_storage_setting import BackupServerBackupJobStorageSetting
    from ..models.backup_server_backup_job_synthetic_full_settings import BackupServerBackupJobSyntheticFullSettings
    from ..models.backup_server_job_scripts_settings import BackupServerJobScriptsSettings


T = TypeVar("T", bound="BackupServerBackupJobAdvancedSettings")


@_attrs_define
class BackupServerBackupJobAdvancedSettings:
    """Backup job advanced settings.

    Attributes:
        backup_mode_type (BackupServerBackupJobBackupModeType | Unset): Backup method.
        synthetic_fulls (BackupServerBackupJobSyntheticFullSettings | Unset): Synthetic full backup settings.
        active_fulls (BackupServerBackupJobActiveFullSettings | Unset): Active full backup settings.
        backup_health (BackupServerBackupJobHealthCheckSettings | Unset): Health check settings for the latest restore
            point in the backup chain.
        full_backup_maintenance (BackupServerBackupJobFullBackupMaintenance | Unset): Maintenance settings for full
            backup files.
        storage_data (BackupServerBackupJobStorageSetting | Unset): Storage settings.
        notifications (BackupServerBackupJobNotificationSettings | Unset): Notification settings.
        v_sphere (BackupServerBackupJobAdvancedSettingsVSphere | Unset): VMware vSphere settings.
        storage_integration (BackupServerBackupJobPrimaryStorageIntegrationSettings | Unset): Backup from Storage
            Snapshots settings.
        scripts (BackupServerJobScriptsSettings | Unset): Script settings.
    """

    backup_mode_type: BackupServerBackupJobBackupModeType | Unset = UNSET
    synthetic_fulls: BackupServerBackupJobSyntheticFullSettings | Unset = UNSET
    active_fulls: BackupServerBackupJobActiveFullSettings | Unset = UNSET
    backup_health: BackupServerBackupJobHealthCheckSettings | Unset = UNSET
    full_backup_maintenance: BackupServerBackupJobFullBackupMaintenance | Unset = UNSET
    storage_data: BackupServerBackupJobStorageSetting | Unset = UNSET
    notifications: BackupServerBackupJobNotificationSettings | Unset = UNSET
    v_sphere: BackupServerBackupJobAdvancedSettingsVSphere | Unset = UNSET
    storage_integration: BackupServerBackupJobPrimaryStorageIntegrationSettings | Unset = UNSET
    scripts: BackupServerJobScriptsSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_mode_type: str | Unset = UNSET
        if not isinstance(self.backup_mode_type, Unset):
            backup_mode_type = self.backup_mode_type.value

        synthetic_fulls: dict[str, Any] | Unset = UNSET
        if not isinstance(self.synthetic_fulls, Unset):
            synthetic_fulls = self.synthetic_fulls.to_dict()

        active_fulls: dict[str, Any] | Unset = UNSET
        if not isinstance(self.active_fulls, Unset):
            active_fulls = self.active_fulls.to_dict()

        backup_health: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_health, Unset):
            backup_health = self.backup_health.to_dict()

        full_backup_maintenance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.full_backup_maintenance, Unset):
            full_backup_maintenance = self.full_backup_maintenance.to_dict()

        storage_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage_data, Unset):
            storage_data = self.storage_data.to_dict()

        notifications: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notifications, Unset):
            notifications = self.notifications.to_dict()

        v_sphere: dict[str, Any] | Unset = UNSET
        if not isinstance(self.v_sphere, Unset):
            v_sphere = self.v_sphere.to_dict()

        storage_integration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage_integration, Unset):
            storage_integration = self.storage_integration.to_dict()

        scripts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scripts, Unset):
            scripts = self.scripts.to_dict()

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
        from ..models.backup_server_backup_job_active_full_settings import BackupServerBackupJobActiveFullSettings
        from ..models.backup_server_backup_job_advanced_settings_v_sphere import (
            BackupServerBackupJobAdvancedSettingsVSphere,
        )
        from ..models.backup_server_backup_job_full_backup_maintenance import BackupServerBackupJobFullBackupMaintenance
        from ..models.backup_server_backup_job_health_check_settings import BackupServerBackupJobHealthCheckSettings
        from ..models.backup_server_backup_job_notification_settings import BackupServerBackupJobNotificationSettings
        from ..models.backup_server_backup_job_primary_storage_integration_settings import (
            BackupServerBackupJobPrimaryStorageIntegrationSettings,
        )
        from ..models.backup_server_backup_job_storage_setting import BackupServerBackupJobStorageSetting
        from ..models.backup_server_backup_job_synthetic_full_settings import BackupServerBackupJobSyntheticFullSettings
        from ..models.backup_server_job_scripts_settings import BackupServerJobScriptsSettings

        d = dict(src_dict)
        _backup_mode_type = d.pop("backupModeType", UNSET)
        backup_mode_type: BackupServerBackupJobBackupModeType | Unset
        if isinstance(_backup_mode_type, Unset):
            backup_mode_type = UNSET
        else:
            backup_mode_type = BackupServerBackupJobBackupModeType(_backup_mode_type)

        _synthetic_fulls = d.pop("syntheticFulls", UNSET)
        synthetic_fulls: BackupServerBackupJobSyntheticFullSettings | Unset
        if isinstance(_synthetic_fulls, Unset):
            synthetic_fulls = UNSET
        else:
            synthetic_fulls = BackupServerBackupJobSyntheticFullSettings.from_dict(_synthetic_fulls)

        _active_fulls = d.pop("activeFulls", UNSET)
        active_fulls: BackupServerBackupJobActiveFullSettings | Unset
        if isinstance(_active_fulls, Unset):
            active_fulls = UNSET
        else:
            active_fulls = BackupServerBackupJobActiveFullSettings.from_dict(_active_fulls)

        _backup_health = d.pop("backupHealth", UNSET)
        backup_health: BackupServerBackupJobHealthCheckSettings | Unset
        if isinstance(_backup_health, Unset):
            backup_health = UNSET
        else:
            backup_health = BackupServerBackupJobHealthCheckSettings.from_dict(_backup_health)

        _full_backup_maintenance = d.pop("fullBackupMaintenance", UNSET)
        full_backup_maintenance: BackupServerBackupJobFullBackupMaintenance | Unset
        if isinstance(_full_backup_maintenance, Unset):
            full_backup_maintenance = UNSET
        else:
            full_backup_maintenance = BackupServerBackupJobFullBackupMaintenance.from_dict(_full_backup_maintenance)

        _storage_data = d.pop("storageData", UNSET)
        storage_data: BackupServerBackupJobStorageSetting | Unset
        if isinstance(_storage_data, Unset):
            storage_data = UNSET
        else:
            storage_data = BackupServerBackupJobStorageSetting.from_dict(_storage_data)

        _notifications = d.pop("notifications", UNSET)
        notifications: BackupServerBackupJobNotificationSettings | Unset
        if isinstance(_notifications, Unset):
            notifications = UNSET
        else:
            notifications = BackupServerBackupJobNotificationSettings.from_dict(_notifications)

        _v_sphere = d.pop("vSphere", UNSET)
        v_sphere: BackupServerBackupJobAdvancedSettingsVSphere | Unset
        if isinstance(_v_sphere, Unset):
            v_sphere = UNSET
        else:
            v_sphere = BackupServerBackupJobAdvancedSettingsVSphere.from_dict(_v_sphere)

        _storage_integration = d.pop("storageIntegration", UNSET)
        storage_integration: BackupServerBackupJobPrimaryStorageIntegrationSettings | Unset
        if isinstance(_storage_integration, Unset):
            storage_integration = UNSET
        else:
            storage_integration = BackupServerBackupJobPrimaryStorageIntegrationSettings.from_dict(_storage_integration)

        _scripts = d.pop("scripts", UNSET)
        scripts: BackupServerJobScriptsSettings | Unset
        if isinstance(_scripts, Unset):
            scripts = UNSET
        else:
            scripts = BackupServerJobScriptsSettings.from_dict(_scripts)

        backup_server_backup_job_advanced_settings = cls(
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

        backup_server_backup_job_advanced_settings.additional_properties = d
        return backup_server_backup_job_advanced_settings

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
