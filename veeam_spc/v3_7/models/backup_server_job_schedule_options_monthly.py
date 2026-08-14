from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_job_schedule_options_monthly_day_number_in_month import (
    BackupServerJobScheduleOptionsMonthlyDayNumberInMonth,
)
from ..models.backup_server_job_schedule_options_monthly_day_of_week import (
    BackupServerJobScheduleOptionsMonthlyDayOfWeek,
)
from ..models.backup_server_job_schedule_options_monthly_months_item import (
    BackupServerJobScheduleOptionsMonthlyMonthsItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerJobScheduleOptionsMonthly")


@_attrs_define
class BackupServerJobScheduleOptionsMonthly:
    """
    Attributes:
        time (str | Unset): Time of the day when a job must start.
        time_utc (str | Unset): Time of the day when a job must start, in UTC.
        day_number_in_month (BackupServerJobScheduleOptionsMonthlyDayNumberInMonth | Unset): Ordinal number of the week
            on which a job must start.
        day_of_week (BackupServerJobScheduleOptionsMonthlyDayOfWeek | Unset): Day of the week on which a job must start.
        months (list[BackupServerJobScheduleOptionsMonthlyMonthsItem] | Unset): Array of the monthswhen a job must
            start.
    """

    time: str | Unset = UNSET
    time_utc: str | Unset = UNSET
    day_number_in_month: BackupServerJobScheduleOptionsMonthlyDayNumberInMonth | Unset = UNSET
    day_of_week: BackupServerJobScheduleOptionsMonthlyDayOfWeek | Unset = UNSET
    months: list[BackupServerJobScheduleOptionsMonthlyMonthsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        time_utc = self.time_utc

        day_number_in_month: str | Unset = UNSET
        if not isinstance(self.day_number_in_month, Unset):
            day_number_in_month = self.day_number_in_month.value

        day_of_week: str | Unset = UNSET
        if not isinstance(self.day_of_week, Unset):
            day_of_week = self.day_of_week.value

        months: list[str] | Unset = UNSET
        if not isinstance(self.months, Unset):
            months = []
            for months_item_data in self.months:
                months_item = months_item_data.value
                months.append(months_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if time_utc is not UNSET:
            field_dict["timeUtc"] = time_utc
        if day_number_in_month is not UNSET:
            field_dict["dayNumberInMonth"] = day_number_in_month
        if day_of_week is not UNSET:
            field_dict["dayOfWeek"] = day_of_week
        if months is not UNSET:
            field_dict["months"] = months

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        time_utc = d.pop("timeUtc", UNSET)

        _day_number_in_month = d.pop("dayNumberInMonth", UNSET)
        day_number_in_month: BackupServerJobScheduleOptionsMonthlyDayNumberInMonth | Unset
        if isinstance(_day_number_in_month, Unset):
            day_number_in_month = UNSET
        else:
            day_number_in_month = BackupServerJobScheduleOptionsMonthlyDayNumberInMonth(_day_number_in_month)

        _day_of_week = d.pop("dayOfWeek", UNSET)
        day_of_week: BackupServerJobScheduleOptionsMonthlyDayOfWeek | Unset
        if isinstance(_day_of_week, Unset):
            day_of_week = UNSET
        else:
            day_of_week = BackupServerJobScheduleOptionsMonthlyDayOfWeek(_day_of_week)

        _months = d.pop("months", UNSET)
        months: list[BackupServerJobScheduleOptionsMonthlyMonthsItem] | Unset = UNSET
        if _months is not UNSET:
            months = []
            for months_item_data in _months:
                months_item = BackupServerJobScheduleOptionsMonthlyMonthsItem(months_item_data)

                months.append(months_item)

        backup_server_job_schedule_options_monthly = cls(
            time=time,
            time_utc=time_utc,
            day_number_in_month=day_number_in_month,
            day_of_week=day_of_week,
            months=months,
        )

        backup_server_job_schedule_options_monthly.additional_properties = d
        return backup_server_job_schedule_options_monthly

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
