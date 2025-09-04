from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionPlanPublicCloudLicenses")


@_attrs_define
class SubscriptionPlanPublicCloudLicenses:
    """
    Attributes:
        cloud_vm_price (Union[Unset, float]): Monthly charge rate for a licensed cloud VM managed in Veeam Backup for
            Public Cloud. Default: 0.0.
        cloud_file_share_price (Union[Unset, float]): Monthly charge rate for a licensed cloud file share managed in
            Veeam Backup for Public Cloud. Default: 0.0.
        cloud_database_price (Union[Unset, float]): Monthly charge rate for a licensed cloud database managed in Veeam
            Backup for Public Cloud. Default: 0.0.
    """

    cloud_vm_price: Union[Unset, float] = 0.0
    cloud_file_share_price: Union[Unset, float] = 0.0
    cloud_database_price: Union[Unset, float] = 0.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cloud_vm_price = self.cloud_vm_price

        cloud_file_share_price = self.cloud_file_share_price

        cloud_database_price = self.cloud_database_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cloud_vm_price is not UNSET:
            field_dict["cloudVmPrice"] = cloud_vm_price
        if cloud_file_share_price is not UNSET:
            field_dict["cloudFileSharePrice"] = cloud_file_share_price
        if cloud_database_price is not UNSET:
            field_dict["cloudDatabasePrice"] = cloud_database_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cloud_vm_price = d.pop("cloudVmPrice", UNSET)

        cloud_file_share_price = d.pop("cloudFileSharePrice", UNSET)

        cloud_database_price = d.pop("cloudDatabasePrice", UNSET)

        subscription_plan_public_cloud_licenses = cls(
            cloud_vm_price=cloud_vm_price,
            cloud_file_share_price=cloud_file_share_price,
            cloud_database_price=cloud_database_price,
        )

        subscription_plan_public_cloud_licenses.additional_properties = d
        return subscription_plan_public_cloud_licenses

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
