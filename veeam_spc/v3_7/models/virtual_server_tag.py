from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VirtualServerTag")


@_attrs_define
class VirtualServerTag:
    """
    Attributes:
        urn (str): Tag URN.
        name (str): Name of a tag.
        size (str | Unset): Size used by a tag.
        host_uid (UUID | Unset): UID assigned to a vCenter Server to which a tag belongs.
        host_name (str | Unset): Name of a vCenter Server to which a tag belongs.
    """

    urn: str
    name: str
    size: str | Unset = UNSET
    host_uid: UUID | Unset = UNSET
    host_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        urn = self.urn

        name = self.name

        size = self.size

        host_uid: str | Unset = UNSET
        if not isinstance(self.host_uid, Unset):
            host_uid = str(self.host_uid)

        host_name = self.host_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "urn": urn,
                "name": name,
            }
        )
        if size is not UNSET:
            field_dict["size"] = size
        if host_uid is not UNSET:
            field_dict["hostUid"] = host_uid
        if host_name is not UNSET:
            field_dict["hostName"] = host_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        urn = d.pop("urn")

        name = d.pop("name")

        size = d.pop("size", UNSET)

        _host_uid = d.pop("hostUid", UNSET)
        host_uid: UUID | Unset
        if isinstance(_host_uid, Unset):
            host_uid = UNSET
        else:
            host_uid = UUID(_host_uid)

        host_name = d.pop("hostName", UNSET)

        virtual_server_tag = cls(
            urn=urn,
            name=name,
            size=size,
            host_uid=host_uid,
            host_name=host_name,
        )

        virtual_server_tag.additional_properties = d
        return virtual_server_tag

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
