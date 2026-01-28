from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monthly_or_weekly_schedule_with_day_settings import MonthlyOrWeeklyScheduleWithDaySettings


T = TypeVar("T", bound="WindowsAdvancedScheduleSettings")


@_attrs_define
class WindowsAdvancedScheduleSettings:
    """
    Attributes:
        synthetic_full_settings (Union[Unset, MonthlyOrWeeklyScheduleWithDaySettings]):
        active_full_settings (Union[Unset, MonthlyOrWeeklyScheduleWithDaySettings]):
    """

    synthetic_full_settings: Union[Unset, "MonthlyOrWeeklyScheduleWithDaySettings"] = UNSET
    active_full_settings: Union[Unset, "MonthlyOrWeeklyScheduleWithDaySettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        synthetic_full_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.synthetic_full_settings, Unset):
            synthetic_full_settings = self.synthetic_full_settings.to_dict()

        active_full_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.active_full_settings, Unset):
            active_full_settings = self.active_full_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if synthetic_full_settings is not UNSET:
            field_dict["syntheticFullSettings"] = synthetic_full_settings
        if active_full_settings is not UNSET:
            field_dict["activeFullSettings"] = active_full_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monthly_or_weekly_schedule_with_day_settings import MonthlyOrWeeklyScheduleWithDaySettings

        d = dict(src_dict)
        _synthetic_full_settings = d.pop("syntheticFullSettings", UNSET)
        synthetic_full_settings: Union[Unset, MonthlyOrWeeklyScheduleWithDaySettings]
        if isinstance(_synthetic_full_settings, Unset):
            synthetic_full_settings = UNSET
        else:
            synthetic_full_settings = MonthlyOrWeeklyScheduleWithDaySettings.from_dict(_synthetic_full_settings)

        _active_full_settings = d.pop("activeFullSettings", UNSET)
        active_full_settings: Union[Unset, MonthlyOrWeeklyScheduleWithDaySettings]
        if isinstance(_active_full_settings, Unset):
            active_full_settings = UNSET
        else:
            active_full_settings = MonthlyOrWeeklyScheduleWithDaySettings.from_dict(_active_full_settings)

        windows_advanced_schedule_settings = cls(
            synthetic_full_settings=synthetic_full_settings,
            active_full_settings=active_full_settings,
        )

        windows_advanced_schedule_settings.additional_properties = d
        return windows_advanced_schedule_settings

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
