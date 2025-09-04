from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinuxMonthlyScheduleSettings")


@_attrs_define
class LinuxMonthlyScheduleSettings:
    """
    Attributes:
        time (Union[Unset, str]): Timestamp of a job start in the `hh:mm` format. Default: '10:00'.
        day_of_month (Union[Unset, int]): Day of the month. Default: 1.
    """

    time: Union[Unset, str] = "10:00"
    day_of_month: Union[Unset, int] = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        day_of_month = self.day_of_month

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if day_of_month is not UNSET:
            field_dict["dayOfMonth"] = day_of_month

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        day_of_month = d.pop("dayOfMonth", UNSET)

        linux_monthly_schedule_settings = cls(
            time=time,
            day_of_month=day_of_month,
        )

        linux_monthly_schedule_settings.additional_properties = d
        return linux_monthly_schedule_settings

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
