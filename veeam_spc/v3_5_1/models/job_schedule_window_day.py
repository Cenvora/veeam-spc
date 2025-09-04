from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.job_schedule_window_day_day import JobScheduleWindowDayDay
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobScheduleWindowDay")


@_attrs_define
class JobScheduleWindowDay:
    """
    Attributes:
        day (JobScheduleWindowDayDay): Days when job runs are permitted.
        hours (Union[Unset, list[int]]): Hours when job runs are permitted.
            > Empty array indicates that job runs are denied during the whole day.
    """

    day: JobScheduleWindowDayDay
    hours: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day = self.day.value

        hours: Union[Unset, list[int]] = UNSET
        if not isinstance(self.hours, Unset):
            hours = self.hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "day": day,
            }
        )
        if hours is not UNSET:
            field_dict["hours"] = hours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        day = JobScheduleWindowDayDay(d.pop("day"))

        hours = cast(list[int], d.pop("hours", UNSET))

        job_schedule_window_day = cls(
            day=day,
            hours=hours,
        )

        job_schedule_window_day.additional_properties = d
        return job_schedule_window_day

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
