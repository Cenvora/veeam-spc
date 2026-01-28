from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_advanced_settings_type_0 import BackupServerBackupJobAdvancedSettingsType0
    from ..models.backup_server_backup_job_gfs_policy_settings_type_0 import BackupServerBackupJobGFSPolicySettingsType0
    from ..models.backup_server_backup_job_proxies_settings import BackupServerBackupJobProxiesSettings
    from ..models.backup_server_backup_job_retention_policy_settings import BackupServerBackupJobRetentionPolicySettings


T = TypeVar("T", bound="BackupServerBackupJobStorage")


@_attrs_define
class BackupServerBackupJobStorage:
    """Backup repository settings.

    Attributes:
        backup_repository_id (UUID): UID assigned to a backup repository.
        backup_proxies (BackupServerBackupJobProxiesSettings): Backup proxy settings.
        retention_policy (BackupServerBackupJobRetentionPolicySettings): Retention policy settings.
        gfs_policy (Union['BackupServerBackupJobGFSPolicySettingsType0', None, Unset]): Long-term retention policy
            settings.
        advanced_settings (Union['BackupServerBackupJobAdvancedSettingsType0', None, Unset]): Backup job advanced
            settings.
    """

    backup_repository_id: UUID
    backup_proxies: "BackupServerBackupJobProxiesSettings"
    retention_policy: "BackupServerBackupJobRetentionPolicySettings"
    gfs_policy: Union["BackupServerBackupJobGFSPolicySettingsType0", None, Unset] = UNSET
    advanced_settings: Union["BackupServerBackupJobAdvancedSettingsType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.backup_server_backup_job_advanced_settings_type_0 import (
            BackupServerBackupJobAdvancedSettingsType0,
        )
        from ..models.backup_server_backup_job_gfs_policy_settings_type_0 import (
            BackupServerBackupJobGFSPolicySettingsType0,
        )

        backup_repository_id = str(self.backup_repository_id)

        backup_proxies = self.backup_proxies.to_dict()

        retention_policy = self.retention_policy.to_dict()

        gfs_policy: Union[None, Unset, dict[str, Any]]
        if isinstance(self.gfs_policy, Unset):
            gfs_policy = UNSET
        elif isinstance(self.gfs_policy, BackupServerBackupJobGFSPolicySettingsType0):
            gfs_policy = self.gfs_policy.to_dict()
        else:
            gfs_policy = self.gfs_policy

        advanced_settings: Union[None, Unset, dict[str, Any]]
        if isinstance(self.advanced_settings, Unset):
            advanced_settings = UNSET
        elif isinstance(self.advanced_settings, BackupServerBackupJobAdvancedSettingsType0):
            advanced_settings = self.advanced_settings.to_dict()
        else:
            advanced_settings = self.advanced_settings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backupRepositoryId": backup_repository_id,
                "backupProxies": backup_proxies,
                "retentionPolicy": retention_policy,
            }
        )
        if gfs_policy is not UNSET:
            field_dict["gfsPolicy"] = gfs_policy
        if advanced_settings is not UNSET:
            field_dict["advancedSettings"] = advanced_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_backup_job_advanced_settings_type_0 import (
            BackupServerBackupJobAdvancedSettingsType0,
        )
        from ..models.backup_server_backup_job_gfs_policy_settings_type_0 import (
            BackupServerBackupJobGFSPolicySettingsType0,
        )
        from ..models.backup_server_backup_job_proxies_settings import BackupServerBackupJobProxiesSettings
        from ..models.backup_server_backup_job_retention_policy_settings import (
            BackupServerBackupJobRetentionPolicySettings,
        )

        d = dict(src_dict)
        backup_repository_id = UUID(d.pop("backupRepositoryId"))

        backup_proxies = BackupServerBackupJobProxiesSettings.from_dict(d.pop("backupProxies"))

        retention_policy = BackupServerBackupJobRetentionPolicySettings.from_dict(d.pop("retentionPolicy"))

        def _parse_gfs_policy(data: object) -> Union["BackupServerBackupJobGFSPolicySettingsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_gfs_policy_settings_type_0 = (
                    BackupServerBackupJobGFSPolicySettingsType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_gfs_policy_settings_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobGFSPolicySettingsType0", None, Unset], data)

        gfs_policy = _parse_gfs_policy(d.pop("gfsPolicy", UNSET))

        def _parse_advanced_settings(data: object) -> Union["BackupServerBackupJobAdvancedSettingsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_advanced_settings_type_0 = (
                    BackupServerBackupJobAdvancedSettingsType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_advanced_settings_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobAdvancedSettingsType0", None, Unset], data)

        advanced_settings = _parse_advanced_settings(d.pop("advancedSettings", UNSET))

        backup_server_backup_job_storage = cls(
            backup_repository_id=backup_repository_id,
            backup_proxies=backup_proxies,
            retention_policy=retention_policy,
            gfs_policy=gfs_policy,
            advanced_settings=advanced_settings,
        )

        backup_server_backup_job_storage.additional_properties = d
        return backup_server_backup_job_storage

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
