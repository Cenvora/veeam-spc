from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_backup_job_day_number_in_month_nullable import BackupServerBackupJobDayNumberInMonthNullable
from ..models.days_of_week_nullable import DaysOfWeekNullable
from ..models.month import Month
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerBackupJobAdvancedStorageScheduleMonthly")


@_attrs_define
class BackupServerBackupJobAdvancedStorageScheduleMonthly:
    """Monthly schedule settings.

    Attributes:
        is_enabled (bool): Indicates whether the monthly schedule is enabled.
        day_of_week (Union[Unset, DaysOfWeekNullable]):
        day_number_in_month (Union[Unset, BackupServerBackupJobDayNumberInMonthNullable]): Week day number in a month.
        day_of_months (Union[Unset, int]): Numerical value of the day when the operation is performed.
        months (Union[Unset, list[Month]]): Months when the operation is performed.
    """

    is_enabled: bool
    day_of_week: Union[Unset, DaysOfWeekNullable] = UNSET
    day_number_in_month: Union[Unset, BackupServerBackupJobDayNumberInMonthNullable] = UNSET
    day_of_months: Union[Unset, int] = UNSET
    months: Union[Unset, list[Month]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        day_of_week: Union[Unset, str] = UNSET
        if not isinstance(self.day_of_week, Unset):
            day_of_week = self.day_of_week.value

        day_number_in_month: Union[Unset, str] = UNSET
        if not isinstance(self.day_number_in_month, Unset):
            day_number_in_month = self.day_number_in_month.value

        day_of_months = self.day_of_months

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
                "isEnabled": is_enabled,
            }
        )
        if day_of_week is not UNSET:
            field_dict["dayOfWeek"] = day_of_week
        if day_number_in_month is not UNSET:
            field_dict["dayNumberInMonth"] = day_number_in_month
        if day_of_months is not UNSET:
            field_dict["dayOfMonths"] = day_of_months
        if months is not UNSET:
            field_dict["months"] = months

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_enabled = d.pop("isEnabled")

        _day_of_week = d.pop("dayOfWeek", UNSET)
        day_of_week: Union[Unset, DaysOfWeekNullable]
        if isinstance(_day_of_week, Unset):
            day_of_week = UNSET
        else:
            day_of_week = DaysOfWeekNullable(_day_of_week)

        _day_number_in_month = d.pop("dayNumberInMonth", UNSET)
        day_number_in_month: Union[Unset, BackupServerBackupJobDayNumberInMonthNullable]
        if isinstance(_day_number_in_month, Unset):
            day_number_in_month = UNSET
        else:
            day_number_in_month = BackupServerBackupJobDayNumberInMonthNullable(_day_number_in_month)

        day_of_months = d.pop("dayOfMonths", UNSET)

        months = []
        _months = d.pop("months", UNSET)
        for months_item_data in _months or []:
            months_item = Month(months_item_data)

            months.append(months_item)

        backup_server_backup_job_advanced_storage_schedule_monthly = cls(
            is_enabled=is_enabled,
            day_of_week=day_of_week,
            day_number_in_month=day_number_in_month,
            day_of_months=day_of_months,
            months=months,
        )

        backup_server_backup_job_advanced_storage_schedule_monthly.additional_properties = d
        return backup_server_backup_job_advanced_storage_schedule_monthly

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
