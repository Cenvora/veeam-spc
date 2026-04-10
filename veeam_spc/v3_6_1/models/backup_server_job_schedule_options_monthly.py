from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_job_schedule_options_monthly_day_number_in_month import (
    BackupServerJobScheduleOptionsMonthlyDayNumberInMonth,
)
from ..models.backup_server_job_schedule_options_monthly_day_of_week import (
    BackupServerJobScheduleOptionsMonthlyDayOfWeek,
)
from ..models.backup_server_job_schedule_options_monthly_months_type_0_item import (
    BackupServerJobScheduleOptionsMonthlyMonthsType0Item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerJobScheduleOptionsMonthly")


@_attrs_define
class BackupServerJobScheduleOptionsMonthly:
    """
    Attributes:
        time (Union[None, Unset, str]): Time of the day when a job must start.
        time_utc (Union[None, Unset, str]): Time of the day when a job must start, in UTC.
        day_number_in_month (Union[Unset, BackupServerJobScheduleOptionsMonthlyDayNumberInMonth]): Ordinal number of the
            week on which a job must start.
        day_of_week (Union[Unset, BackupServerJobScheduleOptionsMonthlyDayOfWeek]): Day of the week on which a job must
            start.
        months (Union[None, Unset, list[BackupServerJobScheduleOptionsMonthlyMonthsType0Item]]): Array of the monthswhen
            a job must start.
    """

    time: Union[None, Unset, str] = UNSET
    time_utc: Union[None, Unset, str] = UNSET
    day_number_in_month: Union[Unset, BackupServerJobScheduleOptionsMonthlyDayNumberInMonth] = UNSET
    day_of_week: Union[Unset, BackupServerJobScheduleOptionsMonthlyDayOfWeek] = UNSET
    months: Union[None, Unset, list[BackupServerJobScheduleOptionsMonthlyMonthsType0Item]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time: Union[None, Unset, str]
        if isinstance(self.time, Unset):
            time = UNSET
        else:
            time = self.time

        time_utc: Union[None, Unset, str]
        if isinstance(self.time_utc, Unset):
            time_utc = UNSET
        else:
            time_utc = self.time_utc

        day_number_in_month: Union[Unset, str] = UNSET
        if not isinstance(self.day_number_in_month, Unset):
            day_number_in_month = self.day_number_in_month.value

        day_of_week: Union[Unset, str] = UNSET
        if not isinstance(self.day_of_week, Unset):
            day_of_week = self.day_of_week.value

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

        def _parse_time(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        time = _parse_time(d.pop("time", UNSET))

        def _parse_time_utc(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        time_utc = _parse_time_utc(d.pop("timeUtc", UNSET))

        _day_number_in_month = d.pop("dayNumberInMonth", UNSET)
        day_number_in_month: Union[Unset, BackupServerJobScheduleOptionsMonthlyDayNumberInMonth]
        if isinstance(_day_number_in_month, Unset):
            day_number_in_month = UNSET
        else:
            day_number_in_month = BackupServerJobScheduleOptionsMonthlyDayNumberInMonth(_day_number_in_month)

        _day_of_week = d.pop("dayOfWeek", UNSET)
        day_of_week: Union[Unset, BackupServerJobScheduleOptionsMonthlyDayOfWeek]
        if isinstance(_day_of_week, Unset):
            day_of_week = UNSET
        else:
            day_of_week = BackupServerJobScheduleOptionsMonthlyDayOfWeek(_day_of_week)

        def _parse_months(
            data: object,
        ) -> Union[None, Unset, list[BackupServerJobScheduleOptionsMonthlyMonthsType0Item]]:
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
                    months_type_0_item = BackupServerJobScheduleOptionsMonthlyMonthsType0Item(months_type_0_item_data)

                    months_type_0.append(months_type_0_item)

                return months_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[BackupServerJobScheduleOptionsMonthlyMonthsType0Item]], data)

        months = _parse_months(d.pop("months", UNSET))

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
