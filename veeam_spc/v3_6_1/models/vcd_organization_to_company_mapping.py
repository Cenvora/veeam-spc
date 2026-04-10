from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VcdOrganizationToCompanyMapping")


@_attrs_define
class VcdOrganizationToCompanyMapping:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a mapping of a VMware Cloud Director organization to a
            company.
        company_uid (Union[Unset, UUID]): UID assigned to a company.
        hosted_resource_uid (Union[Unset, UUID]): UID assigned to a company hosted resource.
        vcd_organization_uid (Union[Unset, UUID]): UID assigned to a VMware Cloud Director organization.
        vcd_organization_name (Union[Unset, str]): Name of a VMware Cloud Director organization.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a hosted Veeam Backup & Replication server.
        backup_server_name (Union[Unset, str]): Name of a hosted Veeam Backup & Replication server.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    company_uid: Union[Unset, UUID] = UNSET
    hosted_resource_uid: Union[Unset, UUID] = UNSET
    vcd_organization_uid: Union[Unset, UUID] = UNSET
    vcd_organization_name: Union[Unset, str] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    backup_server_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        company_uid: Union[Unset, str] = UNSET
        if not isinstance(self.company_uid, Unset):
            company_uid = str(self.company_uid)

        hosted_resource_uid: Union[Unset, str] = UNSET
        if not isinstance(self.hosted_resource_uid, Unset):
            hosted_resource_uid = str(self.hosted_resource_uid)

        vcd_organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.vcd_organization_uid, Unset):
            vcd_organization_uid = str(self.vcd_organization_uid)

        vcd_organization_name = self.vcd_organization_name

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        backup_server_name = self.backup_server_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if company_uid is not UNSET:
            field_dict["companyUid"] = company_uid
        if hosted_resource_uid is not UNSET:
            field_dict["hostedResourceUid"] = hosted_resource_uid
        if vcd_organization_uid is not UNSET:
            field_dict["vcdOrganizationUid"] = vcd_organization_uid
        if vcd_organization_name is not UNSET:
            field_dict["vcdOrganizationName"] = vcd_organization_name
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if backup_server_name is not UNSET:
            field_dict["backupServerName"] = backup_server_name

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

        _company_uid = d.pop("companyUid", UNSET)
        company_uid: Union[Unset, UUID]
        if isinstance(_company_uid, Unset):
            company_uid = UNSET
        else:
            company_uid = UUID(_company_uid)

        _hosted_resource_uid = d.pop("hostedResourceUid", UNSET)
        hosted_resource_uid: Union[Unset, UUID]
        if isinstance(_hosted_resource_uid, Unset):
            hosted_resource_uid = UNSET
        else:
            hosted_resource_uid = UUID(_hosted_resource_uid)

        _vcd_organization_uid = d.pop("vcdOrganizationUid", UNSET)
        vcd_organization_uid: Union[Unset, UUID]
        if isinstance(_vcd_organization_uid, Unset):
            vcd_organization_uid = UNSET
        else:
            vcd_organization_uid = UUID(_vcd_organization_uid)

        vcd_organization_name = d.pop("vcdOrganizationName", UNSET)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: Union[Unset, UUID]
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        backup_server_name = d.pop("backupServerName", UNSET)

        vcd_organization_to_company_mapping = cls(
            instance_uid=instance_uid,
            company_uid=company_uid,
            hosted_resource_uid=hosted_resource_uid,
            vcd_organization_uid=vcd_organization_uid,
            vcd_organization_name=vcd_organization_name,
            backup_server_uid=backup_server_uid,
            backup_server_name=backup_server_name,
        )

        vcd_organization_to_company_mapping.additional_properties = d
        return vcd_organization_to_company_mapping

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
