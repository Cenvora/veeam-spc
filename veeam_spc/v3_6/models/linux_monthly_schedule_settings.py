from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.linux_monthly_schedule_settings_day_of_week import LinuxMonthlyScheduleSettingsDayOfWeek
from ..models.linux_monthly_schedule_settings_monthly_mode import LinuxMonthlyScheduleSettingsMonthlyMode
from ..models.linux_monthly_schedule_settings_week_day_number import LinuxMonthlyScheduleSettingsWeekDayNumber
from ..models.month import Month
from ..types import UNSET, Unset

T = TypeVar("T", bound="LinuxMonthlyScheduleSettings")


@_attrs_define
class LinuxMonthlyScheduleSettings:
    """
    Attributes:
        monthly_mode (LinuxMonthlyScheduleSettingsMonthlyMode): Monthly schedule type.
        week_day_number (Union[Unset, LinuxMonthlyScheduleSettingsWeekDayNumber]): Counting number of the week day on
            which a job must start.
        day_of_month (Union[Unset, int]): Numerical value of the day of the month on which a job must start.
        day_of_week (Union[Unset, LinuxMonthlyScheduleSettingsDayOfWeek]): Name of the week day on which a job must
            start.
            > Required for all `weekDayNumber` property values except `Every`.
             Default: LinuxMonthlyScheduleSettingsDayOfWeek.SUNDAY.
        months (Union[Unset, list[Month]]): Array of months when a job must start.
    """

    monthly_mode: LinuxMonthlyScheduleSettingsMonthlyMode
    week_day_number: Union[Unset, LinuxMonthlyScheduleSettingsWeekDayNumber] = UNSET
    day_of_month: Union[Unset, int] = UNSET
    day_of_week: Union[Unset, LinuxMonthlyScheduleSettingsDayOfWeek] = LinuxMonthlyScheduleSettingsDayOfWeek.SUNDAY
    months: Union[Unset, list[Month]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monthly_mode = self.monthly_mode.value

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
        monthly_mode = LinuxMonthlyScheduleSettingsMonthlyMode(d.pop("monthlyMode"))

        _week_day_number = d.pop("weekDayNumber", UNSET)
        week_day_number: Union[Unset, LinuxMonthlyScheduleSettingsWeekDayNumber]
        if isinstance(_week_day_number, Unset):
            week_day_number = UNSET
        else:
            week_day_number = LinuxMonthlyScheduleSettingsWeekDayNumber(_week_day_number)

        day_of_month = d.pop("dayOfMonth", UNSET)

        _day_of_week = d.pop("dayOfWeek", UNSET)
        day_of_week: Union[Unset, LinuxMonthlyScheduleSettingsDayOfWeek]
        if isinstance(_day_of_week, Unset):
            day_of_week = UNSET
        else:
            day_of_week = LinuxMonthlyScheduleSettingsDayOfWeek(_day_of_week)

        months = []
        _months = d.pop("months", UNSET)
        for months_item_data in _months or []:
            months_item = Month(months_item_data)

            months.append(months_item)

        linux_monthly_schedule_settings = cls(
            monthly_mode=monthly_mode,
            week_day_number=week_day_number,
            day_of_month=day_of_month,
            day_of_week=day_of_week,
            months=months,
        )

        linux_monthly_schedule_settings.additional_properties = d
        return linux_monthly_schedule_settings

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
