from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VdcStorageVaultFolders")


@_attrs_define
class VdcStorageVaultFolders:
    """
    Attributes:
        container_name (str | Unset): Name of a container.
        folders (list[str] | Unset): Array of storage folders.
    """

    container_name: str | Unset = UNSET
    folders: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        container_name = self.container_name

        folders: list[str] | Unset = UNSET
        if not isinstance(self.folders, Unset):
            folders = self.folders

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if container_name is not UNSET:
            field_dict["containerName"] = container_name
        if folders is not UNSET:
            field_dict["folders"] = folders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        container_name = d.pop("containerName", UNSET)

        folders = cast(list[str], d.pop("folders", UNSET))

        vdc_storage_vault_folders = cls(
            container_name=container_name,
            folders=folders,
        )

        vdc_storage_vault_folders.additional_properties = d
        return vdc_storage_vault_folders

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
