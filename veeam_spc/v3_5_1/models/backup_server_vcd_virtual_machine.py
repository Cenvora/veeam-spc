from collections.abc import Mapping
from typing import Any, TypeVar, Union
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
        size (Union[Unset, str]): Size used by a VM.
        vcd_organization_uid (Union[Unset, UUID]): UID assigned to a VMware Cloud Director organization.
        vcd_organization_name (Union[Unset, str]): Name assigned to a VMware Cloud Director organization.
    """

    urn: str
    name: str
    size: Union[Unset, str] = UNSET
    vcd_organization_uid: Union[Unset, UUID] = UNSET
    vcd_organization_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        urn = self.urn

        name = self.name

        size = self.size

        vcd_organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.vcd_organization_uid, Unset):
            vcd_organization_uid = str(self.vcd_organization_uid)

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

        size = d.pop("size", UNSET)

        _vcd_organization_uid = d.pop("vcdOrganizationUid", UNSET)
        vcd_organization_uid: Union[Unset, UUID]
        if isinstance(_vcd_organization_uid, Unset):
            vcd_organization_uid = UNSET
        else:
            vcd_organization_uid = UUID(_vcd_organization_uid)

        vcd_organization_name = d.pop("vcdOrganizationName", UNSET)

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
