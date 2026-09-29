from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TenantReplicationResourceUsage")


@_attrs_define
class TenantReplicationResourceUsage:
    """
    Attributes:
        hardware_plan_uid (UUID | Unset): UID assigned to a hardware plan.
        company_uid (None | Unset | UUID): UID assigned to a company.
        tenant_uid (UUID | Unset): UID assigned to a tenant.
        site_uid (UUID | Unset): UID assigned to a Veeam Cloud Connect server on which a management agent is installed.
        v_cp_us_consumed (int | Unset): Number of replicated VMs vCPUs.
        memory_usage (int | Unset): Amount of RAM consumed by company replicas, in bytes.
        storage_usage (int | Unset): Amount of cloud storage space consumed by company replicas, in bytes.
        hosts_cores_count (int | Unset): Number of physical cores in cloud hosts.
        number_of_vms (int | Unset): Number of replicated VMs.
    """

    hardware_plan_uid: UUID | Unset = UNSET
    company_uid: None | Unset | UUID = UNSET
    tenant_uid: UUID | Unset = UNSET
    site_uid: UUID | Unset = UNSET
    v_cp_us_consumed: int | Unset = UNSET
    memory_usage: int | Unset = UNSET
    storage_usage: int | Unset = UNSET
    hosts_cores_count: int | Unset = UNSET
    number_of_vms: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hardware_plan_uid: str | Unset = UNSET
        if not isinstance(self.hardware_plan_uid, Unset):
            hardware_plan_uid = str(self.hardware_plan_uid)

        company_uid: None | str | Unset
        if isinstance(self.company_uid, Unset):
            company_uid = UNSET
        elif isinstance(self.company_uid, UUID):
            company_uid = str(self.company_uid)
        else:
            company_uid = self.company_uid

        tenant_uid: str | Unset = UNSET
        if not isinstance(self.tenant_uid, Unset):
            tenant_uid = str(self.tenant_uid)

        site_uid: str | Unset = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        v_cp_us_consumed = self.v_cp_us_consumed

        memory_usage = self.memory_usage

        storage_usage = self.storage_usage

        hosts_cores_count = self.hosts_cores_count

        number_of_vms = self.number_of_vms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hardware_plan_uid is not UNSET:
            field_dict["hardwarePlanUid"] = hardware_plan_uid
        if company_uid is not UNSET:
            field_dict["companyUid"] = company_uid
        if tenant_uid is not UNSET:
            field_dict["tenantUid"] = tenant_uid
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid
        if v_cp_us_consumed is not UNSET:
            field_dict["vCPUsConsumed"] = v_cp_us_consumed
        if memory_usage is not UNSET:
            field_dict["memoryUsage"] = memory_usage
        if storage_usage is not UNSET:
            field_dict["storageUsage"] = storage_usage
        if hosts_cores_count is not UNSET:
            field_dict["hostsCoresCount"] = hosts_cores_count
        if number_of_vms is not UNSET:
            field_dict["numberOfVms"] = number_of_vms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _hardware_plan_uid = d.pop("hardwarePlanUid", UNSET)
        hardware_plan_uid: UUID | Unset
        if isinstance(_hardware_plan_uid, Unset):
            hardware_plan_uid = UNSET
        else:
            hardware_plan_uid = UUID(_hardware_plan_uid)

        def _parse_company_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                company_uid_type_0 = UUID(data)

                return company_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        company_uid = _parse_company_uid(d.pop("companyUid", UNSET))

        _tenant_uid = d.pop("tenantUid", UNSET)
        tenant_uid: UUID | Unset
        if isinstance(_tenant_uid, Unset):
            tenant_uid = UNSET
        else:
            tenant_uid = UUID(_tenant_uid)

        _site_uid = d.pop("siteUid", UNSET)
        site_uid: UUID | Unset
        if isinstance(_site_uid, Unset):
            site_uid = UNSET
        else:
            site_uid = UUID(_site_uid)

        v_cp_us_consumed = d.pop("vCPUsConsumed", UNSET)

        memory_usage = d.pop("memoryUsage", UNSET)

        storage_usage = d.pop("storageUsage", UNSET)

        hosts_cores_count = d.pop("hostsCoresCount", UNSET)

        number_of_vms = d.pop("numberOfVms", UNSET)

        tenant_replication_resource_usage = cls(
            hardware_plan_uid=hardware_plan_uid,
            company_uid=company_uid,
            tenant_uid=tenant_uid,
            site_uid=site_uid,
            v_cp_us_consumed=v_cp_us_consumed,
            memory_usage=memory_usage,
            storage_usage=storage_usage,
            hosts_cores_count=hosts_cores_count,
            number_of_vms=number_of_vms,
        )

        tenant_replication_resource_usage.additional_properties = d
        return tenant_replication_resource_usage

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
