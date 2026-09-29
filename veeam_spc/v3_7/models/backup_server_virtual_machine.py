from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerVirtualMachine")


@_attrs_define
class BackupServerVirtualMachine:
    """
    Attributes:
        urn (str): VM URN.
        name (str): Name of a VM.
        size (None | str | Unset): Size used by a VM.
        host_uid (None | Unset | UUID): UID assigned to a vCenter Server that manages a VM.
        host_name (None | str | Unset): Name of a vCenter Server that manages a VM.
    """

    urn: str
    name: str
    size: None | str | Unset = UNSET
    host_uid: None | Unset | UUID = UNSET
    host_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        urn = self.urn

        name = self.name

        size: None | str | Unset
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        host_uid: None | str | Unset
        if isinstance(self.host_uid, Unset):
            host_uid = UNSET
        elif isinstance(self.host_uid, UUID):
            host_uid = str(self.host_uid)
        else:
            host_uid = self.host_uid

        host_name: None | str | Unset
        if isinstance(self.host_name, Unset):
            host_name = UNSET
        else:
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

        def _parse_size(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        size = _parse_size(d.pop("size", UNSET))

        def _parse_host_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                host_uid_type_0 = UUID(data)

                return host_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        host_uid = _parse_host_uid(d.pop("hostUid", UNSET))

        def _parse_host_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host_name = _parse_host_name(d.pop("hostName", UNSET))

        backup_server_virtual_machine = cls(
            urn=urn,
            name=name,
            size=size,
            host_uid=host_uid,
            host_name=host_name,
        )

        backup_server_virtual_machine.additional_properties = d
        return backup_server_virtual_machine

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
