from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_job_schedule_options_daily_kind import BackupServerJobScheduleOptionsDailyKind
from ..models.days_of_week import DaysOfWeek
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerJobScheduleOptionsDaily")


@_attrs_define
class BackupServerJobScheduleOptionsDaily:
    """
    Attributes:
        kind (Union[Unset, BackupServerJobScheduleOptionsDailyKind]): Type of daily schedule.
        days (Union[None, Unset, list[DaysOfWeek]]): Days of the week when a job must start.
        time (Union[None, Unset, str]): Time of the day when a job must start.
        time_utc (Union[None, Unset, str]): Time of the day when a job must start, in UTC.
    """

    kind: Union[Unset, BackupServerJobScheduleOptionsDailyKind] = UNSET
    days: Union[None, Unset, list[DaysOfWeek]] = UNSET
    time: Union[None, Unset, str] = UNSET
    time_utc: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        days: Union[None, Unset, list[str]]
        if isinstance(self.days, Unset):
            days = UNSET
        elif isinstance(self.days, list):
            days = []
            for days_type_0_item_data in self.days:
                days_type_0_item = days_type_0_item_data.value
                days.append(days_type_0_item)

        else:
            days = self.days

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if days is not UNSET:
            field_dict["days"] = days
        if time is not UNSET:
            field_dict["time"] = time
        if time_utc is not UNSET:
            field_dict["timeUtc"] = time_utc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, BackupServerJobScheduleOptionsDailyKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = BackupServerJobScheduleOptionsDailyKind(_kind)

        def _parse_days(data: object) -> Union[None, Unset, list[DaysOfWeek]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                days_type_0 = []
                _days_type_0 = data
                for days_type_0_item_data in _days_type_0:
                    days_type_0_item = DaysOfWeek(days_type_0_item_data)

                    days_type_0.append(days_type_0_item)

                return days_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[DaysOfWeek]], data)

        days = _parse_days(d.pop("days", UNSET))

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

        backup_server_job_schedule_options_daily = cls(
            kind=kind,
            days=days,
            time=time,
            time_utc=time_utc,
        )

        backup_server_job_schedule_options_daily.additional_properties = d
        return backup_server_job_schedule_options_daily

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
