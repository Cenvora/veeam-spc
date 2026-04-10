from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PluginLoginDataLanguageModel")


@_attrs_define
class PluginLoginDataLanguageModel:
    """
    Attributes:
        native_name (str | Unset):
        prefix (str | Unset):
        predefined (bool | Unset):
    """

    native_name: str | Unset = UNSET
    prefix: str | Unset = UNSET
    predefined: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        native_name = self.native_name

        prefix = self.prefix

        predefined = self.predefined

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if native_name is not UNSET:
            field_dict["nativeName"] = native_name
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if predefined is not UNSET:
            field_dict["predefined"] = predefined

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        native_name = d.pop("nativeName", UNSET)

        prefix = d.pop("prefix", UNSET)

        predefined = d.pop("predefined", UNSET)

        plugin_login_data_language_model = cls(
            native_name=native_name,
            prefix=prefix,
            predefined=predefined,
        )

        plugin_login_data_language_model.additional_properties = d
        return plugin_login_data_language_model

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
