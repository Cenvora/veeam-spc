from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
        hardware_plans (list[TenantReplicationResourceHardwarePlan] | Unset): Array of hardware plans.
        is_failover_capabilities_enabled (bool | Unset): Indicates whether performing failover is available to a
            company. Default: False.
        is_public_allocation_enabled (bool | None | Unset): Indicates whether public IP addresses are allocated to a
            company. Default: False.
        number_of_public_ips (int | None | Unset): Number of allocated public IP addresses. Default: 0.
    """

    hardware_plans: list[TenantReplicationResourceHardwarePlan] | Unset = UNSET
    is_failover_capabilities_enabled: bool | Unset = False
    is_public_allocation_enabled: bool | None | Unset = False
    number_of_public_ips: int | None | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hardware_plans: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hardware_plans, Unset):
            hardware_plans = []
            for hardware_plans_item_data in self.hardware_plans:
                hardware_plans_item = hardware_plans_item_data.to_dict()
                hardware_plans.append(hardware_plans_item)

        is_failover_capabilities_enabled = self.is_failover_capabilities_enabled

        is_public_allocation_enabled: bool | None | Unset
        if isinstance(self.is_public_allocation_enabled, Unset):
            is_public_allocation_enabled = UNSET
        else:
            is_public_allocation_enabled = self.is_public_allocation_enabled

        number_of_public_ips: int | None | Unset
        if isinstance(self.number_of_public_ips, Unset):
            number_of_public_ips = UNSET
        else:
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
        _hardware_plans = d.pop("hardwarePlans", UNSET)
        hardware_plans: list[TenantReplicationResourceHardwarePlan] | Unset = UNSET
        if _hardware_plans is not UNSET:
            hardware_plans = []
            for hardware_plans_item_data in _hardware_plans:
                hardware_plans_item = TenantReplicationResourceHardwarePlan.from_dict(hardware_plans_item_data)

                hardware_plans.append(hardware_plans_item)

        is_failover_capabilities_enabled = d.pop("isFailoverCapabilitiesEnabled", UNSET)

        def _parse_is_public_allocation_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_public_allocation_enabled = _parse_is_public_allocation_enabled(d.pop("isPublicAllocationEnabled", UNSET))

        def _parse_number_of_public_ips(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number_of_public_ips = _parse_number_of_public_ips(d.pop("numberOfPublicIps", UNSET))

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
