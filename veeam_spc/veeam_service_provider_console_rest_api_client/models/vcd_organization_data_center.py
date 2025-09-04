from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VcdOrganizationDataCenter")


@_attrs_define
class VcdOrganizationDataCenter:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to an organization VDC.
        urn (Union[Unset, str]): URN of an organization VDC. That identifier must be used on working with Vcd job
            configuration.
        vcd_organization_uid (Union[Unset, UUID]): UID assigned to a VMware Cloud Director organization.
        vcd_organization_name (Union[Unset, str]): Name of a VMware Cloud Director organization.
        vcd_server_uid (Union[Unset, UUID]): UID assigned to a VMware Cloud Director server.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup & Replication server.
        name (Union[Unset, str]): Name of an organization VDC.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    urn: Union[Unset, str] = UNSET
    vcd_organization_uid: Union[Unset, UUID] = UNSET
    vcd_organization_name: Union[Unset, str] = UNSET
    vcd_server_uid: Union[Unset, UUID] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        urn = self.urn

        vcd_organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.vcd_organization_uid, Unset):
            vcd_organization_uid = str(self.vcd_organization_uid)

        vcd_organization_name = self.vcd_organization_name

        vcd_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.vcd_server_uid, Unset):
            vcd_server_uid = str(self.vcd_server_uid)

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if urn is not UNSET:
            field_dict["urn"] = urn
        if vcd_organization_uid is not UNSET:
            field_dict["vcdOrganizationUid"] = vcd_organization_uid
        if vcd_organization_name is not UNSET:
            field_dict["vcdOrganizationName"] = vcd_organization_name
        if vcd_server_uid is not UNSET:
            field_dict["vcdServerUid"] = vcd_server_uid
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        urn = d.pop("urn", UNSET)

        _vcd_organization_uid = d.pop("vcdOrganizationUid", UNSET)
        vcd_organization_uid: Union[Unset, UUID]
        if isinstance(_vcd_organization_uid, Unset):
            vcd_organization_uid = UNSET
        else:
            vcd_organization_uid = UUID(_vcd_organization_uid)

        vcd_organization_name = d.pop("vcdOrganizationName", UNSET)

        _vcd_server_uid = d.pop("vcdServerUid", UNSET)
        vcd_server_uid: Union[Unset, UUID]
        if isinstance(_vcd_server_uid, Unset):
            vcd_server_uid = UNSET
        else:
            vcd_server_uid = UUID(_vcd_server_uid)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: Union[Unset, UUID]
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        name = d.pop("name", UNSET)

        vcd_organization_data_center = cls(
            instance_uid=instance_uid,
            urn=urn,
            vcd_organization_uid=vcd_organization_uid,
            vcd_organization_name=vcd_organization_name,
            vcd_server_uid=vcd_server_uid,
            backup_server_uid=backup_server_uid,
            name=name,
        )

        vcd_organization_data_center.additional_properties = d
        return vcd_organization_data_center

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
