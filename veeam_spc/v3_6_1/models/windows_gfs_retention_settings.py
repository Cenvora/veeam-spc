from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.windows_gfs_monthly_retention_settings import WindowsGfsMonthlyRetentionSettings
    from ..models.windows_gfs_weekly_retention_settings import WindowsGfsWeeklyRetentionSettings
    from ..models.windows_gfs_yearly_retention_settings import WindowsGfsYearlyRetentionSettings


T = TypeVar("T", bound="WindowsGfsRetentionSettings")


@_attrs_define
class WindowsGfsRetentionSettings:
    """
    Attributes:
        weekly (Union[Unset, WindowsGfsWeeklyRetentionSettings]):
        monthly (Union[Unset, WindowsGfsMonthlyRetentionSettings]):
        yearly (Union[Unset, WindowsGfsYearlyRetentionSettings]):
    """

    weekly: Union[Unset, "WindowsGfsWeeklyRetentionSettings"] = UNSET
    monthly: Union[Unset, "WindowsGfsMonthlyRetentionSettings"] = UNSET
    yearly: Union[Unset, "WindowsGfsYearlyRetentionSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        weekly: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.weekly, Unset):
            weekly = self.weekly.to_dict()

        monthly: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.monthly, Unset):
            monthly = self.monthly.to_dict()

        yearly: Union[Unset, dict[str, Any]] = UNSET
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
        from ..models.windows_gfs_monthly_retention_settings import WindowsGfsMonthlyRetentionSettings
        from ..models.windows_gfs_weekly_retention_settings import WindowsGfsWeeklyRetentionSettings
        from ..models.windows_gfs_yearly_retention_settings import WindowsGfsYearlyRetentionSettings

        d = dict(src_dict)
        _weekly = d.pop("weekly", UNSET)
        weekly: Union[Unset, WindowsGfsWeeklyRetentionSettings]
        if isinstance(_weekly, Unset):
            weekly = UNSET
        else:
            weekly = WindowsGfsWeeklyRetentionSettings.from_dict(_weekly)

        _monthly = d.pop("monthly", UNSET)
        monthly: Union[Unset, WindowsGfsMonthlyRetentionSettings]
        if isinstance(_monthly, Unset):
            monthly = UNSET
        else:
            monthly = WindowsGfsMonthlyRetentionSettings.from_dict(_monthly)

        _yearly = d.pop("yearly", UNSET)
        yearly: Union[Unset, WindowsGfsYearlyRetentionSettings]
        if isinstance(_yearly, Unset):
            yearly = UNSET
        else:
            yearly = WindowsGfsYearlyRetentionSettings.from_dict(_yearly)

        windows_gfs_retention_settings = cls(
            weekly=weekly,
            monthly=monthly,
            yearly=yearly,
        )

        windows_gfs_retention_settings.additional_properties = d
        return windows_gfs_retention_settings

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
