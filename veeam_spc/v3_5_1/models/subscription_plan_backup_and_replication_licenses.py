from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionPlanBackupAndReplicationLicenses")


@_attrs_define
class SubscriptionPlanBackupAndReplicationLicenses:
    """
    Attributes:
        vm_price (Union[Unset, float]): Monthly charge rate for a licensed VM protected by Veeam Backup & Replication.
            Default: 0.0.
        workstation_price (Union[Unset, float]): Monthly charge rate for a licensed workstation protected by Veeam
            Backup & Replication. Default: 0.0.
        server_price (Union[Unset, float]): Monthly charge rate for a licensed server protected by Veeam Backup &
            Replication. Default: 0.0.
        application_price (Union[Unset, float]): Monthly charge rate for a licensed application protected by Veeam
            Backup & Replication. Default: 0.0.
        file_share_price (Union[Unset, float]): Monthly charge rate for a licensed file share protected by Veeam Backup
            & Replication. Default: 0.0.
        object_storage_price (Union[Unset, float]): Monthly charge rate for a licensed object storage protected by Veeam
            Backup & Replication. Default: 0.0.
    """

    vm_price: Union[Unset, float] = 0.0
    workstation_price: Union[Unset, float] = 0.0
    server_price: Union[Unset, float] = 0.0
    application_price: Union[Unset, float] = 0.0
    file_share_price: Union[Unset, float] = 0.0
    object_storage_price: Union[Unset, float] = 0.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vm_price = self.vm_price

        workstation_price = self.workstation_price

        server_price = self.server_price

        application_price = self.application_price

        file_share_price = self.file_share_price

        object_storage_price = self.object_storage_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vm_price is not UNSET:
            field_dict["vmPrice"] = vm_price
        if workstation_price is not UNSET:
            field_dict["workstationPrice"] = workstation_price
        if server_price is not UNSET:
            field_dict["serverPrice"] = server_price
        if application_price is not UNSET:
            field_dict["applicationPrice"] = application_price
        if file_share_price is not UNSET:
            field_dict["fileSharePrice"] = file_share_price
        if object_storage_price is not UNSET:
            field_dict["objectStoragePrice"] = object_storage_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vm_price = d.pop("vmPrice", UNSET)

        workstation_price = d.pop("workstationPrice", UNSET)

        server_price = d.pop("serverPrice", UNSET)

        application_price = d.pop("applicationPrice", UNSET)

        file_share_price = d.pop("fileSharePrice", UNSET)

        object_storage_price = d.pop("objectStoragePrice", UNSET)

        subscription_plan_backup_and_replication_licenses = cls(
            vm_price=vm_price,
            workstation_price=workstation_price,
            server_price=server_price,
            application_price=application_price,
            file_share_price=file_share_price,
            object_storage_price=object_storage_price,
        )

        subscription_plan_backup_and_replication_licenses.additional_properties = d
        return subscription_plan_backup_and_replication_licenses

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
