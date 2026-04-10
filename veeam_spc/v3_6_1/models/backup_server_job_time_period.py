from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_job_time_period_day import BackupServerJobTimePeriodDay
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerJobTimePeriod")


@_attrs_define
class BackupServerJobTimePeriod:
    """
    Attributes:
        day (Union[Unset, BackupServerJobTimePeriodDay]): Name of the week day.
        hours (Union[None, Unset, list[int]]): Array which contains 24 digits that correspond to hours of the day. `0`
            means that job is permitted to run during the hour. `1` means that job is not permitted to run during the hour.
    """

    day: Union[Unset, BackupServerJobTimePeriodDay] = UNSET
    hours: Union[None, Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day: Union[Unset, str] = UNSET
        if not isinstance(self.day, Unset):
            day = self.day.value

        hours: Union[None, Unset, list[int]]
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
        day: Union[Unset, BackupServerJobTimePeriodDay]
        if isinstance(_day, Unset):
            day = UNSET
        else:
            day = BackupServerJobTimePeriodDay(_day)

        def _parse_hours(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                hours_type_0 = cast(list[int], data)

                return hours_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

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
