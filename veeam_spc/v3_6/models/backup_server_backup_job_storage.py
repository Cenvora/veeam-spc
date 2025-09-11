from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_advanced_settings import BackupServerBackupJobAdvancedSettings
    from ..models.backup_server_backup_job_gfs_policy_settings import BackupServerBackupJobGFSPolicySettings
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
        gfs_policy (Union[Unset, BackupServerBackupJobGFSPolicySettings]): Long-term retention policy settings.
        advanced_settings (Union[Unset, BackupServerBackupJobAdvancedSettings]): Backup job advanced settings.
    """

    backup_repository_id: UUID
    backup_proxies: "BackupServerBackupJobProxiesSettings"
    retention_policy: "BackupServerBackupJobRetentionPolicySettings"
    gfs_policy: Union[Unset, "BackupServerBackupJobGFSPolicySettings"] = UNSET
    advanced_settings: Union[Unset, "BackupServerBackupJobAdvancedSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_repository_id = str(self.backup_repository_id)

        backup_proxies = self.backup_proxies.to_dict()

        retention_policy = self.retention_policy.to_dict()

        gfs_policy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.gfs_policy, Unset):
            gfs_policy = self.gfs_policy.to_dict()

        advanced_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.advanced_settings, Unset):
            advanced_settings = self.advanced_settings.to_dict()

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
        from ..models.backup_server_backup_job_advanced_settings import BackupServerBackupJobAdvancedSettings
        from ..models.backup_server_backup_job_gfs_policy_settings import BackupServerBackupJobGFSPolicySettings
        from ..models.backup_server_backup_job_proxies_settings import BackupServerBackupJobProxiesSettings
        from ..models.backup_server_backup_job_retention_policy_settings import (
            BackupServerBackupJobRetentionPolicySettings,
        )

        d = dict(src_dict)
        backup_repository_id = UUID(d.pop("backupRepositoryId"))

        backup_proxies = BackupServerBackupJobProxiesSettings.from_dict(d.pop("backupProxies"))

        retention_policy = BackupServerBackupJobRetentionPolicySettings.from_dict(d.pop("retentionPolicy"))

        _gfs_policy = d.pop("gfsPolicy", UNSET)
        gfs_policy: Union[Unset, BackupServerBackupJobGFSPolicySettings]
        if isinstance(_gfs_policy, Unset):
            gfs_policy = UNSET
        else:
            gfs_policy = BackupServerBackupJobGFSPolicySettings.from_dict(_gfs_policy)

        _advanced_settings = d.pop("advancedSettings", UNSET)
        advanced_settings: Union[Unset, BackupServerBackupJobAdvancedSettings]
        if isinstance(_advanced_settings, Unset):
            advanced_settings = UNSET
        else:
            advanced_settings = BackupServerBackupJobAdvancedSettings.from_dict(_advanced_settings)

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
