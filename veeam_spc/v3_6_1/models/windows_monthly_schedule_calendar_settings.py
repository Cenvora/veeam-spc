from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.windows_monthly_schedule_calendar_settings_day_of_week import (
    WindowsMonthlyScheduleCalendarSettingsDayOfWeek,
)
from ..models.windows_monthly_schedule_calendar_settings_months_item import (
    WindowsMonthlyScheduleCalendarSettingsMonthsItem,
)
from ..models.windows_monthly_schedule_calendar_settings_week_day_number import (
    WindowsMonthlyScheduleCalendarSettingsWeekDayNumber,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="WindowsMonthlyScheduleCalendarSettings")


@_attrs_define
class WindowsMonthlyScheduleCalendarSettings:
    """
    Attributes:
        week_day_number (WindowsMonthlyScheduleCalendarSettingsWeekDayNumber): Ordinal number of the week.
        day_of_week (Union[Unset, WindowsMonthlyScheduleCalendarSettingsDayOfWeek]): Name of the week day. Default:
            WindowsMonthlyScheduleCalendarSettingsDayOfWeek.SUNDAY.
        months (Union[Unset, list[WindowsMonthlyScheduleCalendarSettingsMonthsItem]]): Month.
    """

    week_day_number: WindowsMonthlyScheduleCalendarSettingsWeekDayNumber
    day_of_week: Union[Unset, WindowsMonthlyScheduleCalendarSettingsDayOfWeek] = (
        WindowsMonthlyScheduleCalendarSettingsDayOfWeek.SUNDAY
    )
    months: Union[Unset, list[WindowsMonthlyScheduleCalendarSettingsMonthsItem]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        week_day_number = self.week_day_number.value

        day_of_week: Union[Unset, str] = UNSET
        if not isinstance(self.day_of_week, Unset):
            day_of_week = self.day_of_week.value

        months: Union[Unset, list[str]] = UNSET
        if not isinstance(self.months, Unset):
            months = []
            for months_item_data in self.months:
                months_item = months_item_data.value
                months.append(months_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "weekDayNumber": week_day_number,
            }
        )
        if day_of_week is not UNSET:
            field_dict["dayOfWeek"] = day_of_week
        if months is not UNSET:
            field_dict["months"] = months

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        week_day_number = WindowsMonthlyScheduleCalendarSettingsWeekDayNumber(d.pop("weekDayNumber"))

        _day_of_week = d.pop("dayOfWeek", UNSET)
        day_of_week: Union[Unset, WindowsMonthlyScheduleCalendarSettingsDayOfWeek]
        if isinstance(_day_of_week, Unset):
            day_of_week = UNSET
        else:
            day_of_week = WindowsMonthlyScheduleCalendarSettingsDayOfWeek(_day_of_week)

        months = []
        _months = d.pop("months", UNSET)
        for months_item_data in _months or []:
            months_item = WindowsMonthlyScheduleCalendarSettingsMonthsItem(months_item_data)

            months.append(months_item)

        windows_monthly_schedule_calendar_settings = cls(
            week_day_number=week_day_number,
            day_of_week=day_of_week,
            months=months,
        )

        windows_monthly_schedule_calendar_settings.additional_properties = d
        return windows_monthly_schedule_calendar_settings

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
