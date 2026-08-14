from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

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
        kind (BackupServerJobScheduleOptionsDailyKind | Unset): Type of daily schedule.
        days (list[DaysOfWeek] | Unset): Days of the week when a job must start.
        time (str | Unset): Time of the day when a job must start.
        time_utc (str | Unset): Time of the day when a job must start, in UTC.
    """

    kind: BackupServerJobScheduleOptionsDailyKind | Unset = UNSET
    days: list[DaysOfWeek] | Unset = UNSET
    time: str | Unset = UNSET
    time_utc: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        days: list[str] | Unset = UNSET
        if not isinstance(self.days, Unset):
            days = []
            for days_item_data in self.days:
                days_item = days_item_data.value
                days.append(days_item)

        time = self.time

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
        kind: BackupServerJobScheduleOptionsDailyKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = BackupServerJobScheduleOptionsDailyKind(_kind)

        _days = d.pop("days", UNSET)
        days: list[DaysOfWeek] | Unset = UNSET
        if _days is not UNSET:
            days = []
            for days_item_data in _days:
                days_item = DaysOfWeek(days_item_data)

                days.append(days_item)

        time = d.pop("time", UNSET)

        time_utc = d.pop("timeUtc", UNSET)

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
