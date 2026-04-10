from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.windows_gfs_weekly_retention_settings_use_full_backup_from import (
    WindowsGfsWeeklyRetentionSettingsUseFullBackupFrom,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="WindowsGfsWeeklyRetentionSettings")


@_attrs_define
class WindowsGfsWeeklyRetentionSettings:
    """
    Attributes:
        keep_weekly_backups_for_weeks (int): Number of weeks during which restore points must not be modified or
            deleted. Default: 1.
        use_full_backup_from (Union[Unset, WindowsGfsWeeklyRetentionSettingsUseFullBackupFrom]): Week day when Veeam
            Backup & Replication must assign the weekly GFS flag to a full restore point. Default:
            WindowsGfsWeeklyRetentionSettingsUseFullBackupFrom.SUNDAY.
    """

    keep_weekly_backups_for_weeks: int = 1
    use_full_backup_from: Union[Unset, WindowsGfsWeeklyRetentionSettingsUseFullBackupFrom] = (
        WindowsGfsWeeklyRetentionSettingsUseFullBackupFrom.SUNDAY
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keep_weekly_backups_for_weeks = self.keep_weekly_backups_for_weeks

        use_full_backup_from: Union[Unset, str] = UNSET
        if not isinstance(self.use_full_backup_from, Unset):
            use_full_backup_from = self.use_full_backup_from.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keepWeeklyBackupsForWeeks": keep_weekly_backups_for_weeks,
            }
        )
        if use_full_backup_from is not UNSET:
            field_dict["useFullBackupFrom"] = use_full_backup_from

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        keep_weekly_backups_for_weeks = d.pop("keepWeeklyBackupsForWeeks")

        _use_full_backup_from = d.pop("useFullBackupFrom", UNSET)
        use_full_backup_from: Union[Unset, WindowsGfsWeeklyRetentionSettingsUseFullBackupFrom]
        if isinstance(_use_full_backup_from, Unset):
            use_full_backup_from = UNSET
        else:
            use_full_backup_from = WindowsGfsWeeklyRetentionSettingsUseFullBackupFrom(_use_full_backup_from)

        windows_gfs_weekly_retention_settings = cls(
            keep_weekly_backups_for_weeks=keep_weekly_backups_for_weeks,
            use_full_backup_from=use_full_backup_from,
        )

        windows_gfs_weekly_retention_settings.additional_properties = d
        return windows_gfs_weekly_retention_settings

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
