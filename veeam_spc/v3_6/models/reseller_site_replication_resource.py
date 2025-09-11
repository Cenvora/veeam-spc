from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResellerSiteReplicationResource")


@_attrs_define
class ResellerSiteReplicationResource:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a cloud replication resource.
        site_uid (Union[Unset, UUID]): UID assigned to a Veeam Cloud Connect site.
        reseller_uid (Union[Unset, UUID]): UID assigned to a reseller.
        hardware_plan_uid (Union[Unset, UUID]): UID assigned to a hardware plan.
        tenants_per_plan_quota (Union[Unset, int]): Maximum number of companies that a reseller can subscribe to a
            hardware plan.
        is_wan_acceleration_enabled (Union[Unset, bool]): Indicates whether WAN acceleration is enabled. Default: False.
        wan_accelerator_uid (Union[Unset, UUID]): UID assigned to a WAN accelerator.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    site_uid: Union[Unset, UUID] = UNSET
    reseller_uid: Union[Unset, UUID] = UNSET
    hardware_plan_uid: Union[Unset, UUID] = UNSET
    tenants_per_plan_quota: Union[Unset, int] = UNSET
    is_wan_acceleration_enabled: Union[Unset, bool] = False
    wan_accelerator_uid: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        site_uid: Union[Unset, str] = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        reseller_uid: Union[Unset, str] = UNSET
        if not isinstance(self.reseller_uid, Unset):
            reseller_uid = str(self.reseller_uid)

        hardware_plan_uid: Union[Unset, str] = UNSET
        if not isinstance(self.hardware_plan_uid, Unset):
            hardware_plan_uid = str(self.hardware_plan_uid)

        tenants_per_plan_quota = self.tenants_per_plan_quota

        is_wan_acceleration_enabled = self.is_wan_acceleration_enabled

        wan_accelerator_uid: Union[Unset, str] = UNSET
        if not isinstance(self.wan_accelerator_uid, Unset):
            wan_accelerator_uid = str(self.wan_accelerator_uid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid
        if reseller_uid is not UNSET:
            field_dict["resellerUid"] = reseller_uid
        if hardware_plan_uid is not UNSET:
            field_dict["hardwarePlanUid"] = hardware_plan_uid
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
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _site_uid = d.pop("siteUid", UNSET)
        site_uid: Union[Unset, UUID]
        if isinstance(_site_uid, Unset):
            site_uid = UNSET
        else:
            site_uid = UUID(_site_uid)

        _reseller_uid = d.pop("resellerUid", UNSET)
        reseller_uid: Union[Unset, UUID]
        if isinstance(_reseller_uid, Unset):
            reseller_uid = UNSET
        else:
            reseller_uid = UUID(_reseller_uid)

        _hardware_plan_uid = d.pop("hardwarePlanUid", UNSET)
        hardware_plan_uid: Union[Unset, UUID]
        if isinstance(_hardware_plan_uid, Unset):
            hardware_plan_uid = UNSET
        else:
            hardware_plan_uid = UUID(_hardware_plan_uid)

        tenants_per_plan_quota = d.pop("tenantsPerPlanQuota", UNSET)

        is_wan_acceleration_enabled = d.pop("isWanAccelerationEnabled", UNSET)

        _wan_accelerator_uid = d.pop("wanAcceleratorUid", UNSET)
        wan_accelerator_uid: Union[Unset, UUID]
        if isinstance(_wan_accelerator_uid, Unset):
            wan_accelerator_uid = UNSET
        else:
            wan_accelerator_uid = UUID(_wan_accelerator_uid)

        reseller_site_replication_resource = cls(
            instance_uid=instance_uid,
            site_uid=site_uid,
            reseller_uid=reseller_uid,
            hardware_plan_uid=hardware_plan_uid,
            tenants_per_plan_quota=tenants_per_plan_quota,
            is_wan_acceleration_enabled=is_wan_acceleration_enabled,
            wan_accelerator_uid=wan_accelerator_uid,
        )

        reseller_site_replication_resource.additional_properties = d
        return reseller_site_replication_resource

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
