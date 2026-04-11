from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeZone")


@_attrs_define
class TimeZone:
    """
    Attributes:
        time_zone_id (str): ID assigned to a time zone.
        display_name (None | str | Unset): Time zone name.
        utc_offset (int | None | Unset): UTC offset, in minutes.
    """

    time_zone_id: str
    display_name: None | str | Unset = UNSET
    utc_offset: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_zone_id = self.time_zone_id

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        utc_offset: int | None | Unset
        if isinstance(self.utc_offset, Unset):
            utc_offset = UNSET
        else:
            utc_offset = self.utc_offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timeZoneId": time_zone_id,
            }
        )
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if utc_offset is not UNSET:
            field_dict["utcOffset"] = utc_offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time_zone_id = d.pop("timeZoneId")

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))

        def _parse_utc_offset(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        utc_offset = _parse_utc_offset(d.pop("utcOffset", UNSET))

        time_zone = cls(
            time_zone_id=time_zone_id,
            display_name=display_name,
            utc_offset=utc_offset,
        )

        time_zone.additional_properties = d
        return time_zone

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
