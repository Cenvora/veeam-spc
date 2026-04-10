from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365OrganizationToCompanyMapping")


@_attrs_define
class Vb365OrganizationToCompanyMapping:
    """
    Attributes:
        vb_365_organization_uid (UUID): UID assigned to a Microsoft organization.
        company_uid (UUID): UID assigned to a company.
        instance_uid (Union[Unset, UUID]): UID assigned to a mapping.
        vb_365_organization_name (Union[Unset, str]): Name of a Microsoft organization.
        vb_365_server_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup for Microsoft 365 server.
        vb_365_server_name (Union[Unset, str]): Name of a Veeam Backup for Microsoft 365 server.
        company_name (Union[Unset, str]): Name of a company.
    """

    vb_365_organization_uid: UUID
    company_uid: UUID
    instance_uid: Union[Unset, UUID] = UNSET
    vb_365_organization_name: Union[Unset, str] = UNSET
    vb_365_server_uid: Union[Unset, UUID] = UNSET
    vb_365_server_name: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vb_365_organization_uid = str(self.vb_365_organization_uid)

        company_uid = str(self.company_uid)

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        vb_365_organization_name = self.vb_365_organization_name

        vb_365_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.vb_365_server_uid, Unset):
            vb_365_server_uid = str(self.vb_365_server_uid)

        vb_365_server_name = self.vb_365_server_name

        company_name = self.company_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vb365OrganizationUid": vb_365_organization_uid,
                "companyUid": company_uid,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if vb_365_organization_name is not UNSET:
            field_dict["vb365OrganizationName"] = vb_365_organization_name
        if vb_365_server_uid is not UNSET:
            field_dict["vb365ServerUid"] = vb_365_server_uid
        if vb_365_server_name is not UNSET:
            field_dict["vb365ServerName"] = vb_365_server_name
        if company_name is not UNSET:
            field_dict["companyName"] = company_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vb_365_organization_uid = UUID(d.pop("vb365OrganizationUid"))

        company_uid = UUID(d.pop("companyUid"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        vb_365_organization_name = d.pop("vb365OrganizationName", UNSET)

        _vb_365_server_uid = d.pop("vb365ServerUid", UNSET)
        vb_365_server_uid: Union[Unset, UUID]
        if isinstance(_vb_365_server_uid, Unset):
            vb_365_server_uid = UNSET
        else:
            vb_365_server_uid = UUID(_vb_365_server_uid)

        vb_365_server_name = d.pop("vb365ServerName", UNSET)

        company_name = d.pop("companyName", UNSET)

        vb_365_organization_to_company_mapping = cls(
            vb_365_organization_uid=vb_365_organization_uid,
            company_uid=company_uid,
            instance_uid=instance_uid,
            vb_365_organization_name=vb_365_organization_name,
            vb_365_server_uid=vb_365_server_uid,
            vb_365_server_name=vb_365_server_name,
            company_name=company_name,
        )

        vb_365_organization_to_company_mapping.additional_properties = d
        return vb_365_organization_to_company_mapping

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
