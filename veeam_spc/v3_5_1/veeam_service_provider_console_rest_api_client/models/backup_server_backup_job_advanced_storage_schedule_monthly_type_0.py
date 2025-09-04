from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_backup_job_day_number_in_month_nullable import BackupServerBackupJobDayNumberInMonthNullable
from ..models.days_of_week_nullable import DaysOfWeekNullable
from ..models.month import Month
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerBackupJobAdvancedStorageScheduleMonthlyType0")


@_attrs_define
class BackupServerBackupJobAdvancedStorageScheduleMonthlyType0:
    """Monthly schedule settings.

    Attributes:
        is_enabled (bool): Indicates whether the monthly schedule is enabled.
        day_of_week (Union[Unset, DaysOfWeekNullable]):
        day_number_in_month (Union[Unset, BackupServerBackupJobDayNumberInMonthNullable]): Week day number in a month.
        day_of_months (Union[None, Unset, int]): Numerical value of the day when the operation is performed.
        months (Union[None, Unset, list[Month]]): Months when the operation is performed.
    """

    is_enabled: bool
    day_of_week: Union[Unset, DaysOfWeekNullable] = UNSET
    day_number_in_month: Union[Unset, BackupServerBackupJobDayNumberInMonthNullable] = UNSET
    day_of_months: Union[None, Unset, int] = UNSET
    months: Union[None, Unset, list[Month]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        day_of_week: Union[Unset, str] = UNSET
        if not isinstance(self.day_of_week, Unset):
            day_of_week = self.day_of_week.value

        day_number_in_month: Union[Unset, str] = UNSET
        if not isinstance(self.day_number_in_month, Unset):
            day_number_in_month = self.day_number_in_month.value

        day_of_months: Union[None, Unset, int]
        if isinstance(self.day_of_months, Unset):
            day_of_months = UNSET
        else:
            day_of_months = self.day_of_months

        months: Union[None, Unset, list[str]]
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

        def _parse_day_of_months(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        day_of_months = _parse_day_of_months(d.pop("dayOfMonths", UNSET))

        def _parse_months(data: object) -> Union[None, Unset, list[Month]]:
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
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[Month]], data)

        months = _parse_months(d.pop("months", UNSET))

        backup_server_backup_job_advanced_storage_schedule_monthly_type_0 = cls(
            is_enabled=is_enabled,
            day_of_week=day_of_week,
            day_number_in_month=day_number_in_month,
            day_of_months=day_of_months,
            months=months,
        )

        backup_server_backup_job_advanced_storage_schedule_monthly_type_0.additional_properties = d
        return backup_server_backup_job_advanced_storage_schedule_monthly_type_0

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
