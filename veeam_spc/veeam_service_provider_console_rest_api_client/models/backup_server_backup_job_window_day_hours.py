from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.days_of_week import DaysOfWeek

T = TypeVar("T", bound="BackupServerBackupJobWindowDayHours")


@_attrs_define
class BackupServerBackupJobWindowDayHours:
    """Daily scheme.

    Attributes:
        day (DaysOfWeek):
        hours (str): String that represents 24 hours where `1` is an hour when job run is permitted and *0* is an hour
            when job run is denied.
    """

    day: DaysOfWeek
    hours: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day = self.day.value

        hours = self.hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "day": day,
                "hours": hours,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        day = DaysOfWeek(d.pop("day"))

        hours = d.pop("hours")

        backup_server_backup_job_window_day_hours = cls(
            day=day,
            hours=hours,
        )

        backup_server_backup_job_window_day_hours.additional_properties = d
        return backup_server_backup_job_window_day_hours

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
