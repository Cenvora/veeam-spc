from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyHostedVbrResource")


@_attrs_define
class CompanyHostedVbrResource:
    """
    Attributes:
        server_uid (UUID): UID assigned to a Veeam Backup & Replication server that provides resources to a company.
        friendly_name (str): Friendly name of a company hosted resource.
        instance_uid (Union[Unset, UUID]): UID assigned to a company hosted resource.
        company_uid (Union[None, UUID, Unset]): UID assigned to a company.
    """

    server_uid: UUID
    friendly_name: str
    instance_uid: Union[Unset, UUID] = UNSET
    company_uid: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_uid = str(self.server_uid)

        friendly_name = self.friendly_name

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        company_uid: Union[None, Unset, str]
        if isinstance(self.company_uid, Unset):
            company_uid = UNSET
        elif isinstance(self.company_uid, UUID):
            company_uid = str(self.company_uid)
        else:
            company_uid = self.company_uid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serverUid": server_uid,
                "friendlyName": friendly_name,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if company_uid is not UNSET:
            field_dict["companyUid"] = company_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        server_uid = UUID(d.pop("serverUid"))

        friendly_name = d.pop("friendlyName")

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        def _parse_company_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                company_uid_type_0 = UUID(data)

                return company_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        company_uid = _parse_company_uid(d.pop("companyUid", UNSET))

        company_hosted_vbr_resource = cls(
            server_uid=server_uid,
            friendly_name=friendly_name,
            instance_uid=instance_uid,
            company_uid=company_uid,
        )

        company_hosted_vbr_resource.additional_properties = d
        return company_hosted_vbr_resource

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
