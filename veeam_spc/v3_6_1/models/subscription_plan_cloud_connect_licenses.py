from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionPlanCloudConnectLicenses")


@_attrs_define
class SubscriptionPlanCloudConnectLicenses:
    """
    Attributes:
        vm_backup_price (Union[Unset, float]): Monthly charge rate for a licensed VM backup managed in Veeam Cloud
            Connect. Default: 0.0.
        vm_replica_price (Union[Unset, float]): Monthly charge rate for a licensed VM replica managed in Veeam Cloud
            Connect. Default: 0.0.
        workstation_backup_price (Union[Unset, float]): Monthly charge rate for a licensed workstation backup managed in
            Veeam Cloud Connect. Default: 0.0.
        server_backup_price (Union[Unset, float]): Monthly charge rate for a licensed server backup managed in Veeam
            Cloud Connect. Default: 0.0.
    """

    vm_backup_price: Union[Unset, float] = 0.0
    vm_replica_price: Union[Unset, float] = 0.0
    workstation_backup_price: Union[Unset, float] = 0.0
    server_backup_price: Union[Unset, float] = 0.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vm_backup_price = self.vm_backup_price

        vm_replica_price = self.vm_replica_price

        workstation_backup_price = self.workstation_backup_price

        server_backup_price = self.server_backup_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vm_backup_price is not UNSET:
            field_dict["vmBackupPrice"] = vm_backup_price
        if vm_replica_price is not UNSET:
            field_dict["vmReplicaPrice"] = vm_replica_price
        if workstation_backup_price is not UNSET:
            field_dict["workstationBackupPrice"] = workstation_backup_price
        if server_backup_price is not UNSET:
            field_dict["serverBackupPrice"] = server_backup_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vm_backup_price = d.pop("vmBackupPrice", UNSET)

        vm_replica_price = d.pop("vmReplicaPrice", UNSET)

        workstation_backup_price = d.pop("workstationBackupPrice", UNSET)

        server_backup_price = d.pop("serverBackupPrice", UNSET)

        subscription_plan_cloud_connect_licenses = cls(
            vm_backup_price=vm_backup_price,
            vm_replica_price=vm_replica_price,
            workstation_backup_price=workstation_backup_price,
            server_backup_price=server_backup_price,
        )

        subscription_plan_cloud_connect_licenses.additional_properties = d
        return subscription_plan_cloud_connect_licenses

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
