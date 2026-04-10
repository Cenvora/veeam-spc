from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PluginUserLoginDataServiceTimeZone")


@_attrs_define
class PluginUserLoginDataServiceTimeZone:
    """
    Attributes:
        id (Union[Unset, str]): ID assigned to a time zone.
        description (Union[Unset, str]): Description of a time zone.
        utc_offset_in_minutes (Union[Unset, int]): Time zone UTC offset, in minutes.
    """

    id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    utc_offset_in_minutes: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        description = self.description

        utc_offset_in_minutes = self.utc_offset_in_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if utc_offset_in_minutes is not UNSET:
            field_dict["utcOffsetInMinutes"] = utc_offset_in_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        utc_offset_in_minutes = d.pop("utcOffsetInMinutes", UNSET)

        plugin_user_login_data_service_time_zone = cls(
            id=id,
            description=description,
            utc_offset_in_minutes=utc_offset_in_minutes,
        )

        plugin_user_login_data_service_time_zone.additional_properties = d
        return plugin_user_login_data_service_time_zone

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
