from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PluginUserLoginDataFormats")


@_attrs_define
class PluginUserLoginDataFormats:
    """
    Attributes:
        net_short_time (Union[Unset, str]): Custom format string for short time in the .NET format.
        net_long_time (Union[Unset, str]): Custom format string for long time in the .NET format.
        net_short_date (Union[Unset, str]): Custom format string for short date in the .NET format.
        short_time (Union[Unset, str]): Custom format string for short time in the PHP format.
        long_time (Union[Unset, str]): Custom format string for long time in the PHP format.
        short_date (Union[Unset, str]): Custom format string for short date in the PHP format.
    """

    net_short_time: Union[Unset, str] = UNSET
    net_long_time: Union[Unset, str] = UNSET
    net_short_date: Union[Unset, str] = UNSET
    short_time: Union[Unset, str] = UNSET
    long_time: Union[Unset, str] = UNSET
    short_date: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        net_short_time = self.net_short_time

        net_long_time = self.net_long_time

        net_short_date = self.net_short_date

        short_time = self.short_time

        long_time = self.long_time

        short_date = self.short_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if net_short_time is not UNSET:
            field_dict["netShortTime"] = net_short_time
        if net_long_time is not UNSET:
            field_dict["netLongTime"] = net_long_time
        if net_short_date is not UNSET:
            field_dict["netShortDate"] = net_short_date
        if short_time is not UNSET:
            field_dict["shortTime"] = short_time
        if long_time is not UNSET:
            field_dict["longTime"] = long_time
        if short_date is not UNSET:
            field_dict["shortDate"] = short_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        net_short_time = d.pop("netShortTime", UNSET)

        net_long_time = d.pop("netLongTime", UNSET)

        net_short_date = d.pop("netShortDate", UNSET)

        short_time = d.pop("shortTime", UNSET)

        long_time = d.pop("longTime", UNSET)

        short_date = d.pop("shortDate", UNSET)

        plugin_user_login_data_formats = cls(
            net_short_time=net_short_time,
            net_long_time=net_long_time,
            net_short_date=net_short_date,
            short_time=short_time,
            long_time=long_time,
            short_date=short_date,
        )

        plugin_user_login_data_formats.additional_properties = d
        return plugin_user_login_data_formats

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
