from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResellerSiteReplicationResourceInput")


@_attrs_define
class ResellerSiteReplicationResourceInput:
    """
    Example:
        {'hardwarePlanUid': 'ae61e533-82c7-4cb6-a030-78ae589cf49d', 'tenantsPerPlanQuota': 100,
            'isWanAccelerationEnabled': True, 'wanAcceleratorUid': None}

    Attributes:
        hardware_plan_uid (UUID): UID assigned to a hardware plan.
        tenants_per_plan_quota (int | Unset): Maximum number of companies that a reseller can subscribe to a hardware
            plan.
        is_wan_acceleration_enabled (bool | Unset): Indicates whether WAN acceleration is enabled. Default: False.
        wan_accelerator_uid (UUID | Unset): UID assigned to a WAN accelerator.
    """

    hardware_plan_uid: UUID
    tenants_per_plan_quota: int | Unset = UNSET
    is_wan_acceleration_enabled: bool | Unset = False
    wan_accelerator_uid: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hardware_plan_uid = str(self.hardware_plan_uid)

        tenants_per_plan_quota = self.tenants_per_plan_quota

        is_wan_acceleration_enabled = self.is_wan_acceleration_enabled

        wan_accelerator_uid: str | Unset = UNSET
        if not isinstance(self.wan_accelerator_uid, Unset):
            wan_accelerator_uid = str(self.wan_accelerator_uid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hardwarePlanUid": hardware_plan_uid,
            }
        )
        if tenants_per_plan_quota is not UNSET:
            field_dict["tenantsPerPlanQuota"] = tenants_per_plan_quota
        if is_wan_acceleration_enabled is not UNSET:
            field_dict["isWanAccelerationEnabled"] = is_wan_acceleration_enabled
        if wan_accelerator_uid is not UNSET:
            field_dict["wanAcceleratorUid"] = wan_accelerator_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hardware_plan_uid = UUID(d.pop("hardwarePlanUid"))

        tenants_per_plan_quota = d.pop("tenantsPerPlanQuota", UNSET)

        is_wan_acceleration_enabled = d.pop("isWanAccelerationEnabled", UNSET)

        _wan_accelerator_uid = d.pop("wanAcceleratorUid", UNSET)
        wan_accelerator_uid: UUID | Unset
        if isinstance(_wan_accelerator_uid, Unset):
            wan_accelerator_uid = UNSET
        else:
            wan_accelerator_uid = UUID(_wan_accelerator_uid)

        reseller_site_replication_resource_input = cls(
            hardware_plan_uid=hardware_plan_uid,
            tenants_per_plan_quota=tenants_per_plan_quota,
            is_wan_acceleration_enabled=is_wan_acceleration_enabled,
            wan_accelerator_uid=wan_accelerator_uid,
        )

        reseller_site_replication_resource_input.additional_properties = d
        return reseller_site_replication_resource_input

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
