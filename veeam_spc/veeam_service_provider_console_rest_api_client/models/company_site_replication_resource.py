from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_site_replication_resource_hardware_plan import CompanySiteReplicationResourceHardwarePlan


T = TypeVar("T", bound="CompanySiteReplicationResource")


@_attrs_define
class CompanySiteReplicationResource:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a cloud replication resource.
        company_uid (Union[Unset, UUID]): UID assigned to a company.
        site_uid (Union[Unset, UUID]): UID assigned to a Veeam Cloud Connect site.
        hardware_plans (Union[Unset, list['CompanySiteReplicationResourceHardwarePlan']]): Array of hardware plans.
        is_failover_capabilities_enabled (Union[Unset, bool]): Indicates whether performing failover is available to a
            company. Default: False.
        is_public_allocation_enabled (Union[Unset, bool]): Indicates whether public IP addresses are allocated to a
            company. Default: False.
        number_of_public_ips (Union[Unset, int]): Number of allocated public IP addresses. Default: 0.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    company_uid: Union[Unset, UUID] = UNSET
    site_uid: Union[Unset, UUID] = UNSET
    hardware_plans: Union[Unset, list["CompanySiteReplicationResourceHardwarePlan"]] = UNSET
    is_failover_capabilities_enabled: Union[Unset, bool] = False
    is_public_allocation_enabled: Union[Unset, bool] = False
    number_of_public_ips: Union[Unset, int] = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        company_uid: Union[Unset, str] = UNSET
        if not isinstance(self.company_uid, Unset):
            company_uid = str(self.company_uid)

        site_uid: Union[Unset, str] = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        hardware_plans: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.hardware_plans, Unset):
            hardware_plans = []
            for hardware_plans_item_data in self.hardware_plans:
                hardware_plans_item = hardware_plans_item_data.to_dict()
                hardware_plans.append(hardware_plans_item)

        is_failover_capabilities_enabled = self.is_failover_capabilities_enabled

        is_public_allocation_enabled = self.is_public_allocation_enabled

        number_of_public_ips = self.number_of_public_ips

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if company_uid is not UNSET:
            field_dict["companyUid"] = company_uid
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid
        if hardware_plans is not UNSET:
            field_dict["hardwarePlans"] = hardware_plans
        if is_failover_capabilities_enabled is not UNSET:
            field_dict["isFailoverCapabilitiesEnabled"] = is_failover_capabilities_enabled
        if is_public_allocation_enabled is not UNSET:
            field_dict["isPublicAllocationEnabled"] = is_public_allocation_enabled
        if number_of_public_ips is not UNSET:
            field_dict["numberOfPublicIps"] = number_of_public_ips

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_site_replication_resource_hardware_plan import CompanySiteReplicationResourceHardwarePlan

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

        _site_uid = d.pop("siteUid", UNSET)
        site_uid: Union[Unset, UUID]
        if isinstance(_site_uid, Unset):
            site_uid = UNSET
        else:
            site_uid = UUID(_site_uid)

        hardware_plans = []
        _hardware_plans = d.pop("hardwarePlans", UNSET)
        for hardware_plans_item_data in _hardware_plans or []:
            hardware_plans_item = CompanySiteReplicationResourceHardwarePlan.from_dict(hardware_plans_item_data)

            hardware_plans.append(hardware_plans_item)

        is_failover_capabilities_enabled = d.pop("isFailoverCapabilitiesEnabled", UNSET)

        is_public_allocation_enabled = d.pop("isPublicAllocationEnabled", UNSET)

        number_of_public_ips = d.pop("numberOfPublicIps", UNSET)

        company_site_replication_resource = cls(
            instance_uid=instance_uid,
            company_uid=company_uid,
            site_uid=site_uid,
            hardware_plans=hardware_plans,
            is_failover_capabilities_enabled=is_failover_capabilities_enabled,
            is_public_allocation_enabled=is_public_allocation_enabled,
            number_of_public_ips=number_of_public_ips,
        )

        company_site_replication_resource.additional_properties = d
        return company_site_replication_resource

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
