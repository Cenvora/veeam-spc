from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mac_monthly_schedule_settings_day_of_week import MacMonthlyScheduleSettingsDayOfWeek
from ..models.mac_monthly_schedule_settings_monthly_mode import MacMonthlyScheduleSettingsMonthlyMode
from ..models.mac_monthly_schedule_settings_week_day_number import MacMonthlyScheduleSettingsWeekDayNumber
from ..models.month import Month
from ..types import UNSET, Unset

T = TypeVar("T", bound="MacMonthlyScheduleSettings")


@_attrs_define
class MacMonthlyScheduleSettings:
    """
    Attributes:
        monthly_mode (MacMonthlyScheduleSettingsMonthlyMode): Type of the monthly schedule. Default:
            MacMonthlyScheduleSettingsMonthlyMode.DAY.
        time (Union[Unset, str]): Time when a job must start, in the `hh:mm` format. Default: '10:00'.
        week_day_number (Union[Unset, MacMonthlyScheduleSettingsWeekDayNumber]): Counting number of the week day on
            which a job must start.
        day_of_month (Union[Unset, int]): Numerical value of the day of the month on which a job must start.
        day_of_week (Union[Unset, MacMonthlyScheduleSettingsDayOfWeek]): Name of the week day on which a job must start.
            Required for all `WeekDayNumber` property values except `Every`. Default:
            MacMonthlyScheduleSettingsDayOfWeek.SUNDAY.
        months (Union[Unset, list[Month]]): Array of months when a job must start.
    """

    monthly_mode: MacMonthlyScheduleSettingsMonthlyMode = MacMonthlyScheduleSettingsMonthlyMode.DAY
    time: Union[Unset, str] = "10:00"
    week_day_number: Union[Unset, MacMonthlyScheduleSettingsWeekDayNumber] = UNSET
    day_of_month: Union[Unset, int] = UNSET
    day_of_week: Union[Unset, MacMonthlyScheduleSettingsDayOfWeek] = MacMonthlyScheduleSettingsDayOfWeek.SUNDAY
    months: Union[Unset, list[Month]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monthly_mode = self.monthly_mode.value

        time = self.time

        week_day_number: Union[Unset, str] = UNSET
        if not isinstance(self.week_day_number, Unset):
            week_day_number = self.week_day_number.value

        day_of_month = self.day_of_month

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
                "monthlyMode": monthly_mode,
            }
        )
        if time is not UNSET:
            field_dict["time"] = time
        if week_day_number is not UNSET:
            field_dict["weekDayNumber"] = week_day_number
        if day_of_month is not UNSET:
            field_dict["dayOfMonth"] = day_of_month
        if day_of_week is not UNSET:
            field_dict["dayOfWeek"] = day_of_week
        if months is not UNSET:
            field_dict["months"] = months

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        monthly_mode = MacMonthlyScheduleSettingsMonthlyMode(d.pop("monthlyMode"))

        time = d.pop("time", UNSET)

        _week_day_number = d.pop("weekDayNumber", UNSET)
        week_day_number: Union[Unset, MacMonthlyScheduleSettingsWeekDayNumber]
        if isinstance(_week_day_number, Unset):
            week_day_number = UNSET
        else:
            week_day_number = MacMonthlyScheduleSettingsWeekDayNumber(_week_day_number)

        day_of_month = d.pop("dayOfMonth", UNSET)

        _day_of_week = d.pop("dayOfWeek", UNSET)
        day_of_week: Union[Unset, MacMonthlyScheduleSettingsDayOfWeek]
        if isinstance(_day_of_week, Unset):
            day_of_week = UNSET
        else:
            day_of_week = MacMonthlyScheduleSettingsDayOfWeek(_day_of_week)

        months = []
        _months = d.pop("months", UNSET)
        for months_item_data in _months or []:
            months_item = Month(months_item_data)

            months.append(months_item)

        mac_monthly_schedule_settings = cls(
            monthly_mode=monthly_mode,
            time=time,
            week_day_number=week_day_number,
            day_of_month=day_of_month,
            day_of_week=day_of_week,
            months=months,
        )

        mac_monthly_schedule_settings.additional_properties = d
        return mac_monthly_schedule_settings

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
