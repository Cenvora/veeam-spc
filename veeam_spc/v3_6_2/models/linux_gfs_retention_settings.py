from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linux_gfs_monthly_retention_settings import LinuxGfsMonthlyRetentionSettings
    from ..models.linux_gfs_weekly_retention_settings import LinuxGfsWeeklyRetentionSettings
    from ..models.linux_gfs_yearly_retention_settings import LinuxGfsYearlyRetentionSettings


T = TypeVar("T", bound="LinuxGfsRetentionSettings")


@_attrs_define
class LinuxGfsRetentionSettings:
    """
    Attributes:
        weekly (LinuxGfsWeeklyRetentionSettings | Unset):
        monthly (LinuxGfsMonthlyRetentionSettings | Unset):
        yearly (LinuxGfsYearlyRetentionSettings | Unset):
    """

    weekly: LinuxGfsWeeklyRetentionSettings | Unset = UNSET
    monthly: LinuxGfsMonthlyRetentionSettings | Unset = UNSET
    yearly: LinuxGfsYearlyRetentionSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        weekly: dict[str, Any] | Unset = UNSET
        if not isinstance(self.weekly, Unset):
            weekly = self.weekly.to_dict()

        monthly: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monthly, Unset):
            monthly = self.monthly.to_dict()

        yearly: dict[str, Any] | Unset = UNSET
        if not isinstance(self.yearly, Unset):
            yearly = self.yearly.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if weekly is not UNSET:
            field_dict["weekly"] = weekly
        if monthly is not UNSET:
            field_dict["monthly"] = monthly
        if yearly is not UNSET:
            field_dict["yearly"] = yearly

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linux_gfs_monthly_retention_settings import LinuxGfsMonthlyRetentionSettings
        from ..models.linux_gfs_weekly_retention_settings import LinuxGfsWeeklyRetentionSettings
        from ..models.linux_gfs_yearly_retention_settings import LinuxGfsYearlyRetentionSettings

        d = dict(src_dict)
        _weekly = d.pop("weekly", UNSET)
        weekly: LinuxGfsWeeklyRetentionSettings | Unset
        if isinstance(_weekly, Unset):
            weekly = UNSET
        else:
            weekly = LinuxGfsWeeklyRetentionSettings.from_dict(_weekly)

        _monthly = d.pop("monthly", UNSET)
        monthly: LinuxGfsMonthlyRetentionSettings | Unset
        if isinstance(_monthly, Unset):
            monthly = UNSET
        else:
            monthly = LinuxGfsMonthlyRetentionSettings.from_dict(_monthly)

        _yearly = d.pop("yearly", UNSET)
        yearly: LinuxGfsYearlyRetentionSettings | Unset
        if isinstance(_yearly, Unset):
            yearly = UNSET
        else:
            yearly = LinuxGfsYearlyRetentionSettings.from_dict(_yearly)

        linux_gfs_retention_settings = cls(
            weekly=weekly,
            monthly=monthly,
            yearly=yearly,
        )

        linux_gfs_retention_settings.additional_properties = d
        return linux_gfs_retention_settings

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
