from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VcdOrganizationUser")


@_attrs_define
class VcdOrganizationUser:
    """
    Attributes:
        instance_uid (Union[Unset, str]): UID assigned to a VMware Cloud Director organization user.
        vcd_organization_uid (Union[Unset, UUID]): UID assigned to a VMware Cloud Director organization.
        name (Union[Unset, str]): Name of a VMware Cloud Director organization user.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup & Replication server.
    """

    instance_uid: Union[Unset, str] = UNSET
    vcd_organization_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid = self.instance_uid

        vcd_organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.vcd_organization_uid, Unset):
            vcd_organization_uid = str(self.vcd_organization_uid)

        name = self.name

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if vcd_organization_uid is not UNSET:
            field_dict["vcdOrganizationUid"] = vcd_organization_uid
        if name is not UNSET:
            field_dict["name"] = name
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        instance_uid = d.pop("instanceUid", UNSET)

        _vcd_organization_uid = d.pop("vcdOrganizationUid", UNSET)
        vcd_organization_uid: Union[Unset, UUID]
        if isinstance(_vcd_organization_uid, Unset):
            vcd_organization_uid = UNSET
        else:
            vcd_organization_uid = UUID(_vcd_organization_uid)

        name = d.pop("name", UNSET)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: Union[Unset, UUID]
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        vcd_organization_user = cls(
            instance_uid=instance_uid,
            vcd_organization_uid=vcd_organization_uid,
            name=name,
            backup_server_uid=backup_server_uid,
        )

        vcd_organization_user.additional_properties = d
        return vcd_organization_user

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
