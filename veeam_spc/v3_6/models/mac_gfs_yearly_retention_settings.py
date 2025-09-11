from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mac_gfs_yearly_retention_settings_use_monthly_full_backup_for_the_following_month import (
    MacGfsYearlyRetentionSettingsUseMonthlyFullBackupForTheFollowingMonth,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MacGfsYearlyRetentionSettings")


@_attrs_define
class MacGfsYearlyRetentionSettings:
    """
    Attributes:
        keep_yearly_backups_for_years (int): Number of years during which restore points must not be modified or
            deleted. Default: 1.
        use_monthly_full_backup_for_the_following_month (Union[Unset,
            MacGfsYearlyRetentionSettingsUseMonthlyFullBackupForTheFollowingMonth]): Month when Veeam Backup & Replication
            must assign the yearly GFS flag to a full restore point. Default:
            MacGfsYearlyRetentionSettingsUseMonthlyFullBackupForTheFollowingMonth.JAN.
    """

    keep_yearly_backups_for_years: int = 1
    use_monthly_full_backup_for_the_following_month: Union[
        Unset, MacGfsYearlyRetentionSettingsUseMonthlyFullBackupForTheFollowingMonth
    ] = MacGfsYearlyRetentionSettingsUseMonthlyFullBackupForTheFollowingMonth.JAN
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keep_yearly_backups_for_years = self.keep_yearly_backups_for_years

        use_monthly_full_backup_for_the_following_month: Union[Unset, str] = UNSET
        if not isinstance(self.use_monthly_full_backup_for_the_following_month, Unset):
            use_monthly_full_backup_for_the_following_month = self.use_monthly_full_backup_for_the_following_month.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keepYearlyBackupsForYears": keep_yearly_backups_for_years,
            }
        )
        if use_monthly_full_backup_for_the_following_month is not UNSET:
            field_dict["useMonthlyFullBackupForTheFollowingMonth"] = use_monthly_full_backup_for_the_following_month

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        keep_yearly_backups_for_years = d.pop("keepYearlyBackupsForYears")

        _use_monthly_full_backup_for_the_following_month = d.pop("useMonthlyFullBackupForTheFollowingMonth", UNSET)
        use_monthly_full_backup_for_the_following_month: Union[
            Unset, MacGfsYearlyRetentionSettingsUseMonthlyFullBackupForTheFollowingMonth
        ]
        if isinstance(_use_monthly_full_backup_for_the_following_month, Unset):
            use_monthly_full_backup_for_the_following_month = UNSET
        else:
            use_monthly_full_backup_for_the_following_month = (
                MacGfsYearlyRetentionSettingsUseMonthlyFullBackupForTheFollowingMonth(
                    _use_monthly_full_backup_for_the_following_month
                )
            )

        mac_gfs_yearly_retention_settings = cls(
            keep_yearly_backups_for_years=keep_yearly_backups_for_years,
            use_monthly_full_backup_for_the_following_month=use_monthly_full_backup_for_the_following_month,
        )

        mac_gfs_yearly_retention_settings.additional_properties = d
        return mac_gfs_yearly_retention_settings

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
