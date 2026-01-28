from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mac_backup_health_check_monthly_schedule_day_of_week import MacBackupHealthCheckMonthlyScheduleDayOfWeek
from ..models.mac_backup_health_check_monthly_schedule_week_day_number import (
    MacBackupHealthCheckMonthlyScheduleWeekDayNumber,
)
from ..models.month import Month

T = TypeVar("T", bound="MacBackupHealthCheckMonthlySchedule")


@_attrs_define
class MacBackupHealthCheckMonthlySchedule:
    """
    Attributes:
        week_day_number (MacBackupHealthCheckMonthlyScheduleWeekDayNumber): Ordinal number of the week on which a job
            must start.
        day_of_week (MacBackupHealthCheckMonthlyScheduleDayOfWeek): Name of the week day on which a job must start.
        months (list[Month]): Array of the months when a job must start.
    """

    week_day_number: MacBackupHealthCheckMonthlyScheduleWeekDayNumber
    day_of_week: MacBackupHealthCheckMonthlyScheduleDayOfWeek
    months: list[Month]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        week_day_number = self.week_day_number.value

        day_of_week = self.day_of_week.value

        months = []
        for months_item_data in self.months:
            months_item = months_item_data.value
            months.append(months_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "weekDayNumber": week_day_number,
                "dayOfWeek": day_of_week,
                "months": months,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        week_day_number = MacBackupHealthCheckMonthlyScheduleWeekDayNumber(d.pop("weekDayNumber"))

        day_of_week = MacBackupHealthCheckMonthlyScheduleDayOfWeek(d.pop("dayOfWeek"))

        months = []
        _months = d.pop("months")
        for months_item_data in _months:
            months_item = Month(months_item_data)

            months.append(months_item)

        mac_backup_health_check_monthly_schedule = cls(
            week_day_number=week_day_number,
            day_of_week=day_of_week,
            months=months,
        )

        mac_backup_health_check_monthly_schedule.additional_properties = d
        return mac_backup_health_check_monthly_schedule

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
