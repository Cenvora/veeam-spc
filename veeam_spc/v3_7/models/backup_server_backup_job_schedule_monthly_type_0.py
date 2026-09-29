from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_backup_job_day_number_in_month import BackupServerBackupJobDayNumberInMonth
from ..models.days_of_week_nullable import DaysOfWeekNullable
from ..models.month import Month
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerBackupJobScheduleMonthlyType0")


@_attrs_define
class BackupServerBackupJobScheduleMonthlyType0:
    """Monthly job scheduling settings.

    Attributes:
        is_enabled (bool): Indicates whether monthly schedule is enabled. Default: False.
        local_time (None | str | Unset): Local time when a job must start.
        day_of_week (DaysOfWeekNullable | Unset):
        day_number_in_month (BackupServerBackupJobDayNumberInMonth | Unset): Ordinal number of the week on which a job
            must start.
        day_of_month (int | None | Unset): Numerical value of the day of the month on which a job must start.
        months (list[Month] | None | Unset): Array of months when a job must start.
    """

    is_enabled: bool = False
    local_time: None | str | Unset = UNSET
    day_of_week: DaysOfWeekNullable | Unset = UNSET
    day_number_in_month: BackupServerBackupJobDayNumberInMonth | Unset = UNSET
    day_of_month: int | None | Unset = UNSET
    months: list[Month] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        local_time: None | str | Unset
        if isinstance(self.local_time, Unset):
            local_time = UNSET
        else:
            local_time = self.local_time

        day_of_week: str | Unset = UNSET
        if not isinstance(self.day_of_week, Unset):
            day_of_week = self.day_of_week.value

        day_number_in_month: str | Unset = UNSET
        if not isinstance(self.day_number_in_month, Unset):
            day_number_in_month = self.day_number_in_month.value

        day_of_month: int | None | Unset
        if isinstance(self.day_of_month, Unset):
            day_of_month = UNSET
        else:
            day_of_month = self.day_of_month

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

        def _parse_local_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        local_time = _parse_local_time(d.pop("localTime", UNSET))

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

        def _parse_day_of_month(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        day_of_month = _parse_day_of_month(d.pop("dayOfMonth", UNSET))

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

        backup_server_backup_job_schedule_monthly_type_0 = cls(
            is_enabled=is_enabled,
            local_time=local_time,
            day_of_week=day_of_week,
            day_number_in_month=day_number_in_month,
            day_of_month=day_of_month,
            months=months,
        )

        backup_server_backup_job_schedule_monthly_type_0.additional_properties = d
        return backup_server_backup_job_schedule_monthly_type_0

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
