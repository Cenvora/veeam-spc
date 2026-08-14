from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alarm_schedule_days_item import AlarmScheduleDaysItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alarm_schedule_time_window import AlarmScheduleTimeWindow


T = TypeVar("T", bound="AlarmSchedule")


@_attrs_define
class AlarmSchedule:
    """Defines when an alarm is active. The alarm is suppressed (its detection skipped)
    at any moment that falls outside the configured days/time window. An empty schedule
    (the resource itself is null) means "always active".

        Attributes:
            is_enabled (bool): Indicates whether the schedule is active.
            days (list[AlarmScheduleDaysItem]): Days of the week during which the alarm is active.
            time_window (AlarmScheduleTimeWindow): A time window within a day defined by start and end time in HH:mm format.
                Overnight windows are supported (e.g. startTime 22:00 with endTime 06:00).
            time_zone_id (str | Unset): IANA / Windows time-zone id used to interpret days and the time window. If
                null or unrecognized, the service-local time zone is used.
    """

    is_enabled: bool
    days: list[AlarmScheduleDaysItem]
    time_window: AlarmScheduleTimeWindow
    time_zone_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        days = []
        for days_item_data in self.days:
            days_item = days_item_data.value
            days.append(days_item)

        time_window = self.time_window.to_dict()

        time_zone_id = self.time_zone_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isEnabled": is_enabled,
                "days": days,
                "timeWindow": time_window,
            }
        )
        if time_zone_id is not UNSET:
            field_dict["timeZoneId"] = time_zone_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alarm_schedule_time_window import AlarmScheduleTimeWindow

        d = dict(src_dict)
        is_enabled = d.pop("isEnabled")

        days = []
        _days = d.pop("days")
        for days_item_data in _days:
            days_item = AlarmScheduleDaysItem(days_item_data)

            days.append(days_item)

        time_window = AlarmScheduleTimeWindow.from_dict(d.pop("timeWindow"))

        time_zone_id = d.pop("timeZoneId", UNSET)

        alarm_schedule = cls(
            is_enabled=is_enabled,
            days=days,
            time_window=time_window,
            time_zone_id=time_zone_id,
        )

        alarm_schedule.additional_properties = d
        return alarm_schedule

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
