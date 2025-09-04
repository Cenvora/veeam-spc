from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanySiteVcdReplicationResourceUsage")


@_attrs_define
class CompanySiteVcdReplicationResourceUsage:
    """
    Attributes:
        data_center_uid (Union[Unset, UUID]): UID assigned to a VMware Cloud Director replication resource.
        company_uid (Union[Unset, UUID]): UID assigned to a company.
        site_uid (Union[Unset, UUID]): UID assigned to a Veeam Cloud Connect server on which a management agent is
            installed.
        cpu_count_consumed (Union[Unset, int]): Number of replicated VMs CPUs.
        memory_usage (Union[Unset, int]): Amount of RAM consumed by company replicas, in bytes.
        storage_usage (Union[Unset, int]): Amount of space consumed by company replicas, in bytes.
    """

    data_center_uid: Union[Unset, UUID] = UNSET
    company_uid: Union[Unset, UUID] = UNSET
    site_uid: Union[Unset, UUID] = UNSET
    cpu_count_consumed: Union[Unset, int] = UNSET
    memory_usage: Union[Unset, int] = UNSET
    storage_usage: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_center_uid: Union[Unset, str] = UNSET
        if not isinstance(self.data_center_uid, Unset):
            data_center_uid = str(self.data_center_uid)

        company_uid: Union[Unset, str] = UNSET
        if not isinstance(self.company_uid, Unset):
            company_uid = str(self.company_uid)

        site_uid: Union[Unset, str] = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        cpu_count_consumed = self.cpu_count_consumed

        memory_usage = self.memory_usage

        storage_usage = self.storage_usage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_center_uid is not UNSET:
            field_dict["dataCenterUid"] = data_center_uid
        if company_uid is not UNSET:
            field_dict["companyUid"] = company_uid
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid
        if cpu_count_consumed is not UNSET:
            field_dict["cpuCountConsumed"] = cpu_count_consumed
        if memory_usage is not UNSET:
            field_dict["memoryUsage"] = memory_usage
        if storage_usage is not UNSET:
            field_dict["storageUsage"] = storage_usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _data_center_uid = d.pop("dataCenterUid", UNSET)
        data_center_uid: Union[Unset, UUID]
        if isinstance(_data_center_uid, Unset):
            data_center_uid = UNSET
        else:
            data_center_uid = UUID(_data_center_uid)

        _company_uid = d.pop("companyUid", UNSET)
        company_uid: Union[Unset, UUID]
        if isinstance(_company_uid, Unset):
            company_uid = UNSET
        else:
            company_uid = UUID(_company_uid)

        _site_uid = d.pop("siteUid", UNSET)
        site_uid: Union[Unset, UUID]
        if isinstance(_site_uid, Unset):
            site_uid = UNSET
        else:
            site_uid = UUID(_site_uid)

        cpu_count_consumed = d.pop("cpuCountConsumed", UNSET)

        memory_usage = d.pop("memoryUsage", UNSET)

        storage_usage = d.pop("storageUsage", UNSET)

        company_site_vcd_replication_resource_usage = cls(
            data_center_uid=data_center_uid,
            company_uid=company_uid,
            site_uid=site_uid,
            cpu_count_consumed=cpu_count_consumed,
            memory_usage=memory_usage,
            storage_usage=storage_usage,
        )

        company_site_vcd_replication_resource_usage.additional_properties = d
        return company_site_vcd_replication_resource_usage

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
