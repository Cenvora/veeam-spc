from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.windows_gfs_monthly_retention_settings_use_weekly_full_backup_for_the_following_week_of_month import (
    WindowsGfsMonthlyRetentionSettingsUseWeeklyFullBackupForTheFollowingWeekOfMonth,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="WindowsGfsMonthlyRetentionSettings")


@_attrs_define
class WindowsGfsMonthlyRetentionSettings:
    """
    Attributes:
        keep_monthly_backups_for_months (int): Number of months during which restore points must not be modified or
            deleted. Default: 1.
        use_weekly_full_backup_for_the_following_week_of_month (Union[Unset,
            WindowsGfsMonthlyRetentionSettingsUseWeeklyFullBackupForTheFollowingWeekOfMonth]): Week when Veeam Backup &
            Replication must assign the monthly GFS flag to a full restore point. Default:
            WindowsGfsMonthlyRetentionSettingsUseWeeklyFullBackupForTheFollowingWeekOfMonth.FIRST.
    """

    keep_monthly_backups_for_months: int = 1
    use_weekly_full_backup_for_the_following_week_of_month: Union[
        Unset, WindowsGfsMonthlyRetentionSettingsUseWeeklyFullBackupForTheFollowingWeekOfMonth
    ] = WindowsGfsMonthlyRetentionSettingsUseWeeklyFullBackupForTheFollowingWeekOfMonth.FIRST
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keep_monthly_backups_for_months = self.keep_monthly_backups_for_months

        use_weekly_full_backup_for_the_following_week_of_month: Union[Unset, str] = UNSET
        if not isinstance(self.use_weekly_full_backup_for_the_following_week_of_month, Unset):
            use_weekly_full_backup_for_the_following_week_of_month = (
                self.use_weekly_full_backup_for_the_following_week_of_month.value
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keepMonthlyBackupsForMonths": keep_monthly_backups_for_months,
            }
        )
        if use_weekly_full_backup_for_the_following_week_of_month is not UNSET:
            field_dict["useWeeklyFullBackupForTheFollowingWeekOfMonth"] = (
                use_weekly_full_backup_for_the_following_week_of_month
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        keep_monthly_backups_for_months = d.pop("keepMonthlyBackupsForMonths")

        _use_weekly_full_backup_for_the_following_week_of_month = d.pop(
            "useWeeklyFullBackupForTheFollowingWeekOfMonth", UNSET
        )
        use_weekly_full_backup_for_the_following_week_of_month: Union[
            Unset, WindowsGfsMonthlyRetentionSettingsUseWeeklyFullBackupForTheFollowingWeekOfMonth
        ]
        if isinstance(_use_weekly_full_backup_for_the_following_week_of_month, Unset):
            use_weekly_full_backup_for_the_following_week_of_month = UNSET
        else:
            use_weekly_full_backup_for_the_following_week_of_month = (
                WindowsGfsMonthlyRetentionSettingsUseWeeklyFullBackupForTheFollowingWeekOfMonth(
                    _use_weekly_full_backup_for_the_following_week_of_month
                )
            )

        windows_gfs_monthly_retention_settings = cls(
            keep_monthly_backups_for_months=keep_monthly_backups_for_months,
            use_weekly_full_backup_for_the_following_week_of_month=use_weekly_full_backup_for_the_following_week_of_month,
        )

        windows_gfs_monthly_retention_settings.additional_properties = d
        return windows_gfs_monthly_retention_settings

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
