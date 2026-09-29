from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerVcdVirtualMachine")


@_attrs_define
class BackupServerVcdVirtualMachine:
    """
    Attributes:
        urn (str): VM URN.
        name (str): Name of a VM.
        size (None | str | Unset): Size used by a VM.
        vcd_organization_uid (None | Unset | UUID): UID assigned to a VMware Cloud Director organization.
        vcd_organization_name (None | str | Unset): Name assigned to a VMware Cloud Director organization.
    """

    urn: str
    name: str
    size: None | str | Unset = UNSET
    vcd_organization_uid: None | Unset | UUID = UNSET
    vcd_organization_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        urn = self.urn

        name = self.name

        size: None | str | Unset
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        vcd_organization_uid: None | str | Unset
        if isinstance(self.vcd_organization_uid, Unset):
            vcd_organization_uid = UNSET
        elif isinstance(self.vcd_organization_uid, UUID):
            vcd_organization_uid = str(self.vcd_organization_uid)
        else:
            vcd_organization_uid = self.vcd_organization_uid

        vcd_organization_name: None | str | Unset
        if isinstance(self.vcd_organization_name, Unset):
            vcd_organization_name = UNSET
        else:
            vcd_organization_name = self.vcd_organization_name

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
        if vcd_organization_uid is not UNSET:
            field_dict["vcdOrganizationUid"] = vcd_organization_uid
        if vcd_organization_name is not UNSET:
            field_dict["vcdOrganizationName"] = vcd_organization_name

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

        def _parse_vcd_organization_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                vcd_organization_uid_type_0 = UUID(data)

                return vcd_organization_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        vcd_organization_uid = _parse_vcd_organization_uid(d.pop("vcdOrganizationUid", UNSET))

        def _parse_vcd_organization_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vcd_organization_name = _parse_vcd_organization_name(d.pop("vcdOrganizationName", UNSET))

        backup_server_vcd_virtual_machine = cls(
            urn=urn,
            name=name,
            size=size,
            vcd_organization_uid=vcd_organization_uid,
            vcd_organization_name=vcd_organization_name,
        )

        backup_server_vcd_virtual_machine.additional_properties = d
        return backup_server_vcd_virtual_machine

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
