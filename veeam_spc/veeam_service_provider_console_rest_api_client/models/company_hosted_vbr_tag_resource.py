from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyHostedVbrTagResource")


@_attrs_define
class CompanyHostedVbrTagResource:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a company tag resource.
        company_uid (Union[Unset, UUID]): UID assigned to a company.
        hosted_resource_uid (Union[Unset, UUID]): UID assigned to a company hosted resource.
        tag_urn (Union[Unset, str]): URN assigned to a tag.
        tag_name (Union[Unset, str]): Name of a tag.
        virtual_center_uid (Union[Unset, UUID]): UID assigned to a vCenter Server.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    company_uid: Union[Unset, UUID] = UNSET
    hosted_resource_uid: Union[Unset, UUID] = UNSET
    tag_urn: Union[Unset, str] = UNSET
    tag_name: Union[Unset, str] = UNSET
    virtual_center_uid: Union[Unset, UUID] = UNSET
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

        tag_urn = self.tag_urn

        tag_name = self.tag_name

        virtual_center_uid: Union[Unset, str] = UNSET
        if not isinstance(self.virtual_center_uid, Unset):
            virtual_center_uid = str(self.virtual_center_uid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if company_uid is not UNSET:
            field_dict["companyUid"] = company_uid
        if hosted_resource_uid is not UNSET:
            field_dict["hostedResourceUid"] = hosted_resource_uid
        if tag_urn is not UNSET:
            field_dict["tagUrn"] = tag_urn
        if tag_name is not UNSET:
            field_dict["tagName"] = tag_name
        if virtual_center_uid is not UNSET:
            field_dict["virtualCenterUid"] = virtual_center_uid

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

        tag_urn = d.pop("tagUrn", UNSET)

        tag_name = d.pop("tagName", UNSET)

        _virtual_center_uid = d.pop("virtualCenterUid", UNSET)
        virtual_center_uid: Union[Unset, UUID]
        if isinstance(_virtual_center_uid, Unset):
            virtual_center_uid = UNSET
        else:
            virtual_center_uid = UUID(_virtual_center_uid)

        company_hosted_vbr_tag_resource = cls(
            instance_uid=instance_uid,
            company_uid=company_uid,
            hosted_resource_uid=hosted_resource_uid,
            tag_urn=tag_urn,
            tag_name=tag_name,
            virtual_center_uid=virtual_center_uid,
        )

        company_hosted_vbr_tag_resource.additional_properties = d
        return company_hosted_vbr_tag_resource

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
