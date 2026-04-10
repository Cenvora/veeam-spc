from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyHostedVbrResourceInput")


@_attrs_define
class CompanyHostedVbrResourceInput:
    """
    Attributes:
        server_uid (UUID): UID assigned to a Veeam Backup & Replication server that will provide resources to a company.
        friendly_name (str): Friendly name of a company hosted resource.
        instance_uid (Union[Unset, UUID]): UID assigned to a company hosted resource.
        is_job_scheduling_enabled (Union[Unset, bool]): Defines whether job schedule can be enabled. Default: False.
        company_uid (Union[Unset, UUID]): UID assigned to a company.
    """

    server_uid: UUID
    friendly_name: str
    instance_uid: Union[Unset, UUID] = UNSET
    is_job_scheduling_enabled: Union[Unset, bool] = False
    company_uid: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_uid = str(self.server_uid)

        friendly_name = self.friendly_name

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        is_job_scheduling_enabled = self.is_job_scheduling_enabled

        company_uid: Union[Unset, str] = UNSET
        if not isinstance(self.company_uid, Unset):
            company_uid = str(self.company_uid)

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
        if is_job_scheduling_enabled is not UNSET:
            field_dict["isJobSchedulingEnabled"] = is_job_scheduling_enabled
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

        is_job_scheduling_enabled = d.pop("isJobSchedulingEnabled", UNSET)

        _company_uid = d.pop("companyUid", UNSET)
        company_uid: Union[Unset, UUID]
        if isinstance(_company_uid, Unset):
            company_uid = UNSET
        else:
            company_uid = UUID(_company_uid)

        company_hosted_vbr_resource_input = cls(
            server_uid=server_uid,
            friendly_name=friendly_name,
            instance_uid=instance_uid,
            is_job_scheduling_enabled=is_job_scheduling_enabled,
            company_uid=company_uid,
        )

        company_hosted_vbr_resource_input.additional_properties = d
        return company_hosted_vbr_resource_input

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
