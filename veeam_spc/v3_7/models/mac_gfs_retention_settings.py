from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mac_gfs_monthly_retention_settings import MacGfsMonthlyRetentionSettings
    from ..models.mac_gfs_weekly_retention_settings import MacGfsWeeklyRetentionSettings
    from ..models.mac_gfs_yearly_retention_settings import MacGfsYearlyRetentionSettings


T = TypeVar("T", bound="MacGfsRetentionSettings")


@_attrs_define
class MacGfsRetentionSettings:
    """
    Attributes:
        weekly (MacGfsWeeklyRetentionSettings | Unset):
        monthly (MacGfsMonthlyRetentionSettings | Unset):
        yearly (MacGfsYearlyRetentionSettings | Unset):
    """

    weekly: MacGfsWeeklyRetentionSettings | Unset = UNSET
    monthly: MacGfsMonthlyRetentionSettings | Unset = UNSET
    yearly: MacGfsYearlyRetentionSettings | Unset = UNSET
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
        from ..models.mac_gfs_monthly_retention_settings import MacGfsMonthlyRetentionSettings
        from ..models.mac_gfs_weekly_retention_settings import MacGfsWeeklyRetentionSettings
        from ..models.mac_gfs_yearly_retention_settings import MacGfsYearlyRetentionSettings

        d = dict(src_dict)
        _weekly = d.pop("weekly", UNSET)
        weekly: MacGfsWeeklyRetentionSettings | Unset
        if isinstance(_weekly, Unset):
            weekly = UNSET
        else:
            weekly = MacGfsWeeklyRetentionSettings.from_dict(_weekly)

        _monthly = d.pop("monthly", UNSET)
        monthly: MacGfsMonthlyRetentionSettings | Unset
        if isinstance(_monthly, Unset):
            monthly = UNSET
        else:
            monthly = MacGfsMonthlyRetentionSettings.from_dict(_monthly)

        _yearly = d.pop("yearly", UNSET)
        yearly: MacGfsYearlyRetentionSettings | Unset
        if isinstance(_yearly, Unset):
            yearly = UNSET
        else:
            yearly = MacGfsYearlyRetentionSettings.from_dict(_yearly)

        mac_gfs_retention_settings = cls(
            weekly=weekly,
            monthly=monthly,
            yearly=yearly,
        )

        mac_gfs_retention_settings.additional_properties = d
        return mac_gfs_retention_settings

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
