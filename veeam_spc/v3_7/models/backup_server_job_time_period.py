from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_job_time_period_day import BackupServerJobTimePeriodDay
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerJobTimePeriod")


@_attrs_define
class BackupServerJobTimePeriod:
    """
    Attributes:
        day (BackupServerJobTimePeriodDay | Unset): Name of the week day.
        hours (list[int] | None | Unset): Array which contains 24 digits that correspond to hours of the day. `0` means
            that job is permitted to run during the hour. `1` means that job is not permitted to run during the hour.
    """

    day: BackupServerJobTimePeriodDay | Unset = UNSET
    hours: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day: str | Unset = UNSET
        if not isinstance(self.day, Unset):
            day = self.day.value

        hours: list[int] | None | Unset
        if isinstance(self.hours, Unset):
            hours = UNSET
        elif isinstance(self.hours, list):
            hours = self.hours

        else:
            hours = self.hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if day is not UNSET:
            field_dict["day"] = day
        if hours is not UNSET:
            field_dict["hours"] = hours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _day = d.pop("day", UNSET)
        day: BackupServerJobTimePeriodDay | Unset
        if isinstance(_day, Unset):
            day = UNSET
        else:
            day = BackupServerJobTimePeriodDay(_day)

        def _parse_hours(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                hours_type_0 = cast(list[int], data)

                return hours_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        hours = _parse_hours(d.pop("hours", UNSET))

        backup_server_job_time_period = cls(
            day=day,
            hours=hours,
        )

        backup_server_job_time_period.additional_properties = d
        return backup_server_job_time_period

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
