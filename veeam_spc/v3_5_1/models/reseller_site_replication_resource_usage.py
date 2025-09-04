from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResellerSiteReplicationResourceUsage")


@_attrs_define
class ResellerSiteReplicationResourceUsage:
    """
    Attributes:
        replication_resource_uid (Union[Unset, UUID]): UID assigned to a cloud replication resource.
        reseller_uid (Union[Unset, UUID]): UID assigned to a reseller.
        hardware_plan_uid (Union[Unset, UUID]): UID assigned to a hardware plan.
        tenants_per_plan_usage (Union[Unset, int]): Number of companies that are subscribe to a hardware plan.
    """

    replication_resource_uid: Union[Unset, UUID] = UNSET
    reseller_uid: Union[Unset, UUID] = UNSET
    hardware_plan_uid: Union[Unset, UUID] = UNSET
    tenants_per_plan_usage: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        replication_resource_uid: Union[Unset, str] = UNSET
        if not isinstance(self.replication_resource_uid, Unset):
            replication_resource_uid = str(self.replication_resource_uid)

        reseller_uid: Union[Unset, str] = UNSET
        if not isinstance(self.reseller_uid, Unset):
            reseller_uid = str(self.reseller_uid)

        hardware_plan_uid: Union[Unset, str] = UNSET
        if not isinstance(self.hardware_plan_uid, Unset):
            hardware_plan_uid = str(self.hardware_plan_uid)

        tenants_per_plan_usage = self.tenants_per_plan_usage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if replication_resource_uid is not UNSET:
            field_dict["replicationResourceUid"] = replication_resource_uid
        if reseller_uid is not UNSET:
            field_dict["resellerUid"] = reseller_uid
        if hardware_plan_uid is not UNSET:
            field_dict["hardwarePlanUid"] = hardware_plan_uid
        if tenants_per_plan_usage is not UNSET:
            field_dict["tenantsPerPlanUsage"] = tenants_per_plan_usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _replication_resource_uid = d.pop("replicationResourceUid", UNSET)
        replication_resource_uid: Union[Unset, UUID]
        if isinstance(_replication_resource_uid, Unset):
            replication_resource_uid = UNSET
        else:
            replication_resource_uid = UUID(_replication_resource_uid)

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

        tenants_per_plan_usage = d.pop("tenantsPerPlanUsage", UNSET)

        reseller_site_replication_resource_usage = cls(
            replication_resource_uid=replication_resource_uid,
            reseller_uid=reseller_uid,
            hardware_plan_uid=hardware_plan_uid,
            tenants_per_plan_usage=tenants_per_plan_usage,
        )

        reseller_site_replication_resource_usage.additional_properties = d
        return reseller_site_replication_resource_usage

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
