from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinuxPeriodicallyScheduleSettings")


@_attrs_define
class LinuxPeriodicallyScheduleSettings:
    """
    Attributes:
        interval_in_minutes (Union[Unset, int]): Time interval for a periodically running job, in minutes. Default: 60.
    """

    interval_in_minutes: Union[Unset, int] = 60
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interval_in_minutes = self.interval_in_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interval_in_minutes is not UNSET:
            field_dict["intervalInMinutes"] = interval_in_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        interval_in_minutes = d.pop("intervalInMinutes", UNSET)

        linux_periodically_schedule_settings = cls(
            interval_in_minutes=interval_in_minutes,
        )

        linux_periodically_schedule_settings.additional_properties = d
        return linux_periodically_schedule_settings

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
