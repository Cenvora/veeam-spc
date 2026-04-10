from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_backup_job_day_number_in_month import BackupServerBackupJobDayNumberInMonth
from ..models.days_of_week_nullable import DaysOfWeekNullable
from ..models.month import Month
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerBackupJobScheduleMonthly")


@_attrs_define
class BackupServerBackupJobScheduleMonthly:
    """Monthly job scheduling settings.

    Attributes:
        is_enabled (bool): Indicates whether monthly schedule is enabled. Default: False.
        local_time (str | Unset): Local time when a job must start.
        day_of_week (DaysOfWeekNullable | Unset):
        day_number_in_month (BackupServerBackupJobDayNumberInMonth | Unset): Ordinal number of the week on which a job
            must start.
        day_of_month (int | Unset): Numerical value of the day of the month on which a job must start.
        months (list[Month] | Unset): Array of months when a job must start.
    """

    is_enabled: bool = False
    local_time: str | Unset = UNSET
    day_of_week: DaysOfWeekNullable | Unset = UNSET
    day_number_in_month: BackupServerBackupJobDayNumberInMonth | Unset = UNSET
    day_of_month: int | Unset = UNSET
    months: list[Month] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        local_time = self.local_time

        day_of_week: str | Unset = UNSET
        if not isinstance(self.day_of_week, Unset):
            day_of_week = self.day_of_week.value

        day_number_in_month: str | Unset = UNSET
        if not isinstance(self.day_number_in_month, Unset):
            day_number_in_month = self.day_number_in_month.value

        day_of_month = self.day_of_month

        months: list[str] | Unset = UNSET
        if not isinstance(self.months, Unset):
            months = []
            for months_item_data in self.months:
                months_item = months_item_data.value
                months.append(months_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isEnabled": is_enabled,
            }
        )
        if local_time is not UNSET:
            field_dict["localTime"] = local_time
        if day_of_week is not UNSET:
            field_dict["dayOfWeek"] = day_of_week
        if day_number_in_month is not UNSET:
            field_dict["dayNumberInMonth"] = day_number_in_month
        if day_of_month is not UNSET:
            field_dict["dayOfMonth"] = day_of_month
        if months is not UNSET:
            field_dict["months"] = months

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_enabled = d.pop("isEnabled")

        local_time = d.pop("localTime", UNSET)

        _day_of_week = d.pop("dayOfWeek", UNSET)
        day_of_week: DaysOfWeekNullable | Unset
        if isinstance(_day_of_week, Unset):
            day_of_week = UNSET
        else:
            day_of_week = DaysOfWeekNullable(_day_of_week)

        _day_number_in_month = d.pop("dayNumberInMonth", UNSET)
        day_number_in_month: BackupServerBackupJobDayNumberInMonth | Unset
        if isinstance(_day_number_in_month, Unset):
            day_number_in_month = UNSET
        else:
            day_number_in_month = BackupServerBackupJobDayNumberInMonth(_day_number_in_month)

        day_of_month = d.pop("dayOfMonth", UNSET)

        _months = d.pop("months", UNSET)
        months: list[Month] | Unset = UNSET
        if _months is not UNSET:
            months = []
            for months_item_data in _months:
                months_item = Month(months_item_data)

                months.append(months_item)

        backup_server_backup_job_schedule_monthly = cls(
            is_enabled=is_enabled,
            local_time=local_time,
            day_of_week=day_of_week,
            day_number_in_month=day_number_in_month,
            day_of_month=day_of_month,
            months=months,
        )

        backup_server_backup_job_schedule_monthly.additional_properties = d
        return backup_server_backup_job_schedule_monthly

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
