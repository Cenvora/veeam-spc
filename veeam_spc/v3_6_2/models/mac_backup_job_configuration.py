from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mac_backup_source import MacBackupSource
    from ..models.mac_backup_storage import MacBackupStorage
    from ..models.mac_backup_target import MacBackupTarget
    from ..models.mac_gfs_retention_settings import MacGfsRetentionSettings
    from ..models.mac_job_retention_settings import MacJobRetentionSettings
    from ..models.mac_job_schedule_settings import MacJobScheduleSettings


T = TypeVar("T", bound="MacBackupJobConfiguration")


@_attrs_define
class MacBackupJobConfiguration:
    """
    Attributes:
        backup_source (MacBackupSource):
        backup_target (MacBackupTarget):
        backup_storage (MacBackupStorage | Unset):
        retention_settings (MacJobRetentionSettings | Unset):
        schedule_settings (MacJobScheduleSettings | Unset):
        gfs_retention_settings (MacGfsRetentionSettings | Unset):
    """

    backup_source: MacBackupSource
    backup_target: MacBackupTarget
    backup_storage: MacBackupStorage | Unset = UNSET
    retention_settings: MacJobRetentionSettings | Unset = UNSET
    schedule_settings: MacJobScheduleSettings | Unset = UNSET
    gfs_retention_settings: MacGfsRetentionSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_source = self.backup_source.to_dict()

        backup_target = self.backup_target.to_dict()

        backup_storage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_storage, Unset):
            backup_storage = self.backup_storage.to_dict()

        retention_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retention_settings, Unset):
            retention_settings = self.retention_settings.to_dict()

        schedule_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule_settings, Unset):
            schedule_settings = self.schedule_settings.to_dict()

        gfs_retention_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gfs_retention_settings, Unset):
            gfs_retention_settings = self.gfs_retention_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backupSource": backup_source,
                "backupTarget": backup_target,
            }
        )
        if backup_storage is not UNSET:
            field_dict["backupStorage"] = backup_storage
        if retention_settings is not UNSET:
            field_dict["retentionSettings"] = retention_settings
        if schedule_settings is not UNSET:
            field_dict["scheduleSettings"] = schedule_settings
        if gfs_retention_settings is not UNSET:
            field_dict["gfsRetentionSettings"] = gfs_retention_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mac_backup_source import MacBackupSource
        from ..models.mac_backup_storage import MacBackupStorage
        from ..models.mac_backup_target import MacBackupTarget
        from ..models.mac_gfs_retention_settings import MacGfsRetentionSettings
        from ..models.mac_job_retention_settings import MacJobRetentionSettings
        from ..models.mac_job_schedule_settings import MacJobScheduleSettings

        d = dict(src_dict)
        backup_source = MacBackupSource.from_dict(d.pop("backupSource"))

        backup_target = MacBackupTarget.from_dict(d.pop("backupTarget"))

        _backup_storage = d.pop("backupStorage", UNSET)
        backup_storage: MacBackupStorage | Unset
        if isinstance(_backup_storage, Unset):
            backup_storage = UNSET
        else:
            backup_storage = MacBackupStorage.from_dict(_backup_storage)

        _retention_settings = d.pop("retentionSettings", UNSET)
        retention_settings: MacJobRetentionSettings | Unset
        if isinstance(_retention_settings, Unset):
            retention_settings = UNSET
        else:
            retention_settings = MacJobRetentionSettings.from_dict(_retention_settings)

        _schedule_settings = d.pop("scheduleSettings", UNSET)
        schedule_settings: MacJobScheduleSettings | Unset
        if isinstance(_schedule_settings, Unset):
            schedule_settings = UNSET
        else:
            schedule_settings = MacJobScheduleSettings.from_dict(_schedule_settings)

        _gfs_retention_settings = d.pop("gfsRetentionSettings", UNSET)
        gfs_retention_settings: MacGfsRetentionSettings | Unset
        if isinstance(_gfs_retention_settings, Unset):
            gfs_retention_settings = UNSET
        else:
            gfs_retention_settings = MacGfsRetentionSettings.from_dict(_gfs_retention_settings)

        mac_backup_job_configuration = cls(
            backup_source=backup_source,
            backup_target=backup_target,
            backup_storage=backup_storage,
            retention_settings=retention_settings,
            schedule_settings=schedule_settings,
            gfs_retention_settings=gfs_retention_settings,
        )

        mac_backup_job_configuration.additional_properties = d
        return mac_backup_job_configuration

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
