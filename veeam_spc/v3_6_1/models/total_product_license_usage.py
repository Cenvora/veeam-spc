from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.total_product_license_usage_product_type import TotalProductLicenseUsageProductType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workload_license_usage import WorkloadLicenseUsage


T = TypeVar("T", bound="TotalProductLicenseUsage")


@_attrs_define
class TotalProductLicenseUsage:
    """
    Attributes:
        product_type (Union[Unset, TotalProductLicenseUsageProductType]): Product type.
        total_points (Union[Unset, float]): Number of used license points.
        license_edition (Union[Unset, str]): License edition.
        workload_usage (Union[Unset, list['WorkloadLicenseUsage']]): License usage for each workload type.
    """

    product_type: Union[Unset, TotalProductLicenseUsageProductType] = UNSET
    total_points: Union[Unset, float] = UNSET
    license_edition: Union[Unset, str] = UNSET
    workload_usage: Union[Unset, list["WorkloadLicenseUsage"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_type: Union[Unset, str] = UNSET
        if not isinstance(self.product_type, Unset):
            product_type = self.product_type.value

        total_points = self.total_points

        license_edition = self.license_edition

        workload_usage: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.workload_usage, Unset):
            workload_usage = []
            for workload_usage_item_data in self.workload_usage:
                workload_usage_item = workload_usage_item_data.to_dict()
                workload_usage.append(workload_usage_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_type is not UNSET:
            field_dict["productType"] = product_type
        if total_points is not UNSET:
            field_dict["totalPoints"] = total_points
        if license_edition is not UNSET:
            field_dict["licenseEdition"] = license_edition
        if workload_usage is not UNSET:
            field_dict["workloadUsage"] = workload_usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workload_license_usage import WorkloadLicenseUsage

        d = dict(src_dict)
        _product_type = d.pop("productType", UNSET)
        product_type: Union[Unset, TotalProductLicenseUsageProductType]
        if isinstance(_product_type, Unset):
            product_type = UNSET
        else:
            product_type = TotalProductLicenseUsageProductType(_product_type)

        total_points = d.pop("totalPoints", UNSET)

        license_edition = d.pop("licenseEdition", UNSET)

        workload_usage = []
        _workload_usage = d.pop("workloadUsage", UNSET)
        for workload_usage_item_data in _workload_usage or []:
            workload_usage_item = WorkloadLicenseUsage.from_dict(workload_usage_item_data)

            workload_usage.append(workload_usage_item)

        total_product_license_usage = cls(
            product_type=product_type,
            total_points=total_points,
            license_edition=license_edition,
            workload_usage=workload_usage,
        )

        total_product_license_usage.additional_properties = d
        return total_product_license_usage

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
