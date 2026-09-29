from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.linux_monthly_schedule_settings_monthly_mode import LinuxMonthlyScheduleSettingsMonthlyMode
from ..models.linux_monthly_schedule_settings_with_time_day_of_week import LinuxMonthlyScheduleSettingsWithTimeDayOfWeek
from ..models.linux_monthly_schedule_settings_with_time_week_day_number import (
    LinuxMonthlyScheduleSettingsWithTimeWeekDayNumber,
)
from ..models.month import Month
from ..types import UNSET, Unset

T = TypeVar("T", bound="LinuxMonthlyScheduleSettingsWithTime")


@_attrs_define
class LinuxMonthlyScheduleSettingsWithTime:
    """
    Attributes:
        monthly_mode (LinuxMonthlyScheduleSettingsMonthlyMode): Monthly schedule type.
        time (str | Unset): Time when a job must start, in the `hh:mm` format. Default: '10:00'.
        week_day_number (LinuxMonthlyScheduleSettingsWithTimeWeekDayNumber | Unset): Ordinal number of the week on which
            a job must start.
        day_of_month (int | None | Unset): Numerical value of the day of the month on which a job must start.
        day_of_week (LinuxMonthlyScheduleSettingsWithTimeDayOfWeek | Unset): Name of the week day.
            > Required for all `WeekDayNumber` options of mouthly schedule except `Every`.
             Default: LinuxMonthlyScheduleSettingsWithTimeDayOfWeek.SUNDAY.
        months (list[Month] | None | Unset): Month.
    """

    monthly_mode: LinuxMonthlyScheduleSettingsMonthlyMode
    time: str | Unset = "10:00"
    week_day_number: LinuxMonthlyScheduleSettingsWithTimeWeekDayNumber | Unset = UNSET
    day_of_month: int | None | Unset = UNSET
    day_of_week: LinuxMonthlyScheduleSettingsWithTimeDayOfWeek | Unset = (
        LinuxMonthlyScheduleSettingsWithTimeDayOfWeek.SUNDAY
    )
    months: list[Month] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monthly_mode = self.monthly_mode.value

        time = self.time

        week_day_number: str | Unset = UNSET
        if not isinstance(self.week_day_number, Unset):
            week_day_number = self.week_day_number.value

        day_of_month: int | None | Unset
        if isinstance(self.day_of_month, Unset):
            day_of_month = UNSET
        else:
            day_of_month = self.day_of_month

        day_of_week: str | Unset = UNSET
        if not isinstance(self.day_of_week, Unset):
            day_of_week = self.day_of_week.value

        months: list[str] | None | Unset
        if isinstance(self.months, Unset):
            months = UNSET
        elif isinstance(self.months, list):
            months = []
            for months_type_0_item_data in self.months:
                months_type_0_item = months_type_0_item_data.value
                months.append(months_type_0_item)

        else:
            months = self.months

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
        monthly_mode = LinuxMonthlyScheduleSettingsMonthlyMode(d.pop("monthlyMode"))

        time = d.pop("time", UNSET)

        _week_day_number = d.pop("weekDayNumber", UNSET)
        week_day_number: LinuxMonthlyScheduleSettingsWithTimeWeekDayNumber | Unset
        if isinstance(_week_day_number, Unset):
            week_day_number = UNSET
        else:
            week_day_number = LinuxMonthlyScheduleSettingsWithTimeWeekDayNumber(_week_day_number)

        def _parse_day_of_month(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        day_of_month = _parse_day_of_month(d.pop("dayOfMonth", UNSET))

        _day_of_week = d.pop("dayOfWeek", UNSET)
        day_of_week: LinuxMonthlyScheduleSettingsWithTimeDayOfWeek | Unset
        if isinstance(_day_of_week, Unset):
            day_of_week = UNSET
        else:
            day_of_week = LinuxMonthlyScheduleSettingsWithTimeDayOfWeek(_day_of_week)

        def _parse_months(data: object) -> list[Month] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                months_type_0 = []
                _months_type_0 = data
                for months_type_0_item_data in _months_type_0:
                    months_type_0_item = Month(months_type_0_item_data)

                    months_type_0.append(months_type_0_item)

                return months_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Month] | None | Unset, data)

        months = _parse_months(d.pop("months", UNSET))

        linux_monthly_schedule_settings_with_time = cls(
            monthly_mode=monthly_mode,
            time=time,
            week_day_number=week_day_number,
            day_of_month=day_of_month,
            day_of_week=day_of_week,
            months=months,
        )

        linux_monthly_schedule_settings_with_time.additional_properties = d
        return linux_monthly_schedule_settings_with_time

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
