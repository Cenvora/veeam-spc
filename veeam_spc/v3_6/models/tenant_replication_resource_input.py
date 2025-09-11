from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tenant_replication_resource_hardware_plan import TenantReplicationResourceHardwarePlan


T = TypeVar("T", bound="TenantReplicationResourceInput")


@_attrs_define
class TenantReplicationResourceInput:
    """
    Attributes:
        hardware_plans (Union[Unset, list['TenantReplicationResourceHardwarePlan']]): Array of hardware plans.
        is_failover_capabilities_enabled (Union[Unset, bool]): Indicates whether performing failover is available to a
            company. Default: False.
        is_public_allocation_enabled (Union[Unset, bool]): Indicates whether public IP addresses are allocated to a
            company. Default: False.
        number_of_public_ips (Union[Unset, int]): Number of allocated public IP addresses. Default: 0.
    """

    hardware_plans: Union[Unset, list["TenantReplicationResourceHardwarePlan"]] = UNSET
    is_failover_capabilities_enabled: Union[Unset, bool] = False
    is_public_allocation_enabled: Union[Unset, bool] = False
    number_of_public_ips: Union[Unset, int] = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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
        from ..models.tenant_replication_resource_hardware_plan import TenantReplicationResourceHardwarePlan

        d = dict(src_dict)
        hardware_plans = []
        _hardware_plans = d.pop("hardwarePlans", UNSET)
        for hardware_plans_item_data in _hardware_plans or []:
            hardware_plans_item = TenantReplicationResourceHardwarePlan.from_dict(hardware_plans_item_data)

            hardware_plans.append(hardware_plans_item)

        is_failover_capabilities_enabled = d.pop("isFailoverCapabilitiesEnabled", UNSET)

        is_public_allocation_enabled = d.pop("isPublicAllocationEnabled", UNSET)

        number_of_public_ips = d.pop("numberOfPublicIps", UNSET)

        tenant_replication_resource_input = cls(
            hardware_plans=hardware_plans,
            is_failover_capabilities_enabled=is_failover_capabilities_enabled,
            is_public_allocation_enabled=is_public_allocation_enabled,
            number_of_public_ips=number_of_public_ips,
        )

        tenant_replication_resource_input.additional_properties = d
        return tenant_replication_resource_input

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
