from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VcdOrganization")


@_attrs_define
class VcdOrganization:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a VMware Cloud Director organization.
        urn (Union[Unset, str]): URN of a VMware Cloud Director organization. That identifier must be used on working
            with Vcd job configuration.
        name (Union[Unset, str]): Name of a VMware Cloud Director organization.
        vcd_server_uid (Union[Unset, UUID]): UID assigned to a VMware Cloud Director server.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup & Replication server.
        hosted_backup_server (Union[Unset, bool]): Indicates whether an organization VMware Cloud Director server is
            connected to a hosted Veeam Backup & Replication server.
        can_be_mapped_as_hosted_resource (Union[Unset, bool]): Indicates whether a VMware Cloud Director organization
            can be mapped to a company as a hosted resource.
            > `false` value indicates that a VMware Cloud Director organization is not connected to a hosted Veeam Backup &
            Replication server or is already mapped to a company.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    urn: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    vcd_server_uid: Union[Unset, UUID] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    hosted_backup_server: Union[Unset, bool] = UNSET
    can_be_mapped_as_hosted_resource: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        urn = self.urn

        name = self.name

        vcd_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.vcd_server_uid, Unset):
            vcd_server_uid = str(self.vcd_server_uid)

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        hosted_backup_server = self.hosted_backup_server

        can_be_mapped_as_hosted_resource = self.can_be_mapped_as_hosted_resource

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if urn is not UNSET:
            field_dict["urn"] = urn
        if name is not UNSET:
            field_dict["name"] = name
        if vcd_server_uid is not UNSET:
            field_dict["vcdServerUid"] = vcd_server_uid
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if hosted_backup_server is not UNSET:
            field_dict["hostedBackupServer"] = hosted_backup_server
        if can_be_mapped_as_hosted_resource is not UNSET:
            field_dict["canBeMappedAsHostedResource"] = can_be_mapped_as_hosted_resource

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

        name = d.pop("name", UNSET)

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

        hosted_backup_server = d.pop("hostedBackupServer", UNSET)

        can_be_mapped_as_hosted_resource = d.pop("canBeMappedAsHostedResource", UNSET)

        vcd_organization = cls(
            instance_uid=instance_uid,
            urn=urn,
            name=name,
            vcd_server_uid=vcd_server_uid,
            backup_server_uid=backup_server_uid,
            hosted_backup_server=hosted_backup_server,
            can_be_mapped_as_hosted_resource=can_be_mapped_as_hosted_resource,
        )

        vcd_organization.additional_properties = d
        return vcd_organization

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
