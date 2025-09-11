from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PluginVersionInfo")


@_attrs_define
class PluginVersionInfo:
    """
    Attributes:
        plugin_id (Union[Unset, UUID]): ID assigned to a plugin.
        version (Union[Unset, str]): Plugin version.
    """

    plugin_id: Union[Unset, UUID] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plugin_id: Union[Unset, str] = UNSET
        if not isinstance(self.plugin_id, Unset):
            plugin_id = str(self.plugin_id)

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plugin_id is not UNSET:
            field_dict["pluginId"] = plugin_id
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _plugin_id = d.pop("pluginId", UNSET)
        plugin_id: Union[Unset, UUID]
        if isinstance(_plugin_id, Unset):
            plugin_id = UNSET
        else:
            plugin_id = UUID(_plugin_id)

        version = d.pop("version", UNSET)

        plugin_version_info = cls(
            plugin_id=plugin_id,
            version=version,
        )

        plugin_version_info.additional_properties = d
        return plugin_version_info

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
