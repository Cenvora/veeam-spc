from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_job_schedule_options_periodically_kind import BackupServerJobScheduleOptionsPeriodicallyKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_job_time_period import BackupServerJobTimePeriod


T = TypeVar("T", bound="BackupServerJobScheduleOptionsPeriodically")


@_attrs_define
class BackupServerJobScheduleOptionsPeriodically:
    """
    Attributes:
        kind (BackupServerJobScheduleOptionsPeriodicallyKind | Unset): Measurement units of the intervals between
            periodical job runs.
        full_period (int | Unset): Numerical value of the intervals between periodical job runs.
        schedule (list[BackupServerJobTimePeriod] | Unset): Permitted time window of a job.
    """

    kind: BackupServerJobScheduleOptionsPeriodicallyKind | Unset = UNSET
    full_period: int | Unset = UNSET
    schedule: list[BackupServerJobTimePeriod] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        full_period = self.full_period

        schedule: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = []
            for schedule_item_data in self.schedule:
                schedule_item = schedule_item_data.to_dict()
                schedule.append(schedule_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if full_period is not UNSET:
            field_dict["fullPeriod"] = full_period
        if schedule is not UNSET:
            field_dict["schedule"] = schedule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_job_time_period import BackupServerJobTimePeriod

        d = dict(src_dict)
        _kind = d.pop("kind", UNSET)
        kind: BackupServerJobScheduleOptionsPeriodicallyKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = BackupServerJobScheduleOptionsPeriodicallyKind(_kind)

        full_period = d.pop("fullPeriod", UNSET)

        _schedule = d.pop("schedule", UNSET)
        schedule: list[BackupServerJobTimePeriod] | Unset = UNSET
        if _schedule is not UNSET:
            schedule = []
            for schedule_item_data in _schedule:
                schedule_item = BackupServerJobTimePeriod.from_dict(schedule_item_data)

                schedule.append(schedule_item)

        backup_server_job_schedule_options_periodically = cls(
            kind=kind,
            full_period=full_period,
            schedule=schedule,
        )

        backup_server_job_schedule_options_periodically.additional_properties = d
        return backup_server_job_schedule_options_periodically

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
