from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.product_license_usage_product_type import ProductLicenseUsageProductType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workload_license_usage import WorkloadLicenseUsage


T = TypeVar("T", bound="ProductLicenseUsage")


@_attrs_define
class ProductLicenseUsage:
    """
    Attributes:
        license_id (Union[None, Unset, str]): License ID.
        product_type (Union[Unset, ProductLicenseUsageProductType]): Product type.
        license_edition (Union[None, Unset, str]): License edition.
        used_points (Union[Unset, float]): Number of license points used by an organization.
        workload_usage (Union[Unset, list['WorkloadLicenseUsage']]): License usage for each workload type.
    """

    license_id: Union[None, Unset, str] = UNSET
    product_type: Union[Unset, ProductLicenseUsageProductType] = UNSET
    license_edition: Union[None, Unset, str] = UNSET
    used_points: Union[Unset, float] = UNSET
    workload_usage: Union[Unset, list["WorkloadLicenseUsage"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        license_id: Union[None, Unset, str]
        if isinstance(self.license_id, Unset):
            license_id = UNSET
        else:
            license_id = self.license_id

        product_type: Union[Unset, str] = UNSET
        if not isinstance(self.product_type, Unset):
            product_type = self.product_type.value

        license_edition: Union[None, Unset, str]
        if isinstance(self.license_edition, Unset):
            license_edition = UNSET
        else:
            license_edition = self.license_edition

        used_points = self.used_points

        workload_usage: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.workload_usage, Unset):
            workload_usage = []
            for workload_usage_item_data in self.workload_usage:
                workload_usage_item = workload_usage_item_data.to_dict()
                workload_usage.append(workload_usage_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if license_id is not UNSET:
            field_dict["licenseId"] = license_id
        if product_type is not UNSET:
            field_dict["productType"] = product_type
        if license_edition is not UNSET:
            field_dict["licenseEdition"] = license_edition
        if used_points is not UNSET:
            field_dict["usedPoints"] = used_points
        if workload_usage is not UNSET:
            field_dict["workloadUsage"] = workload_usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workload_license_usage import WorkloadLicenseUsage

        d = dict(src_dict)

        def _parse_license_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        license_id = _parse_license_id(d.pop("licenseId", UNSET))

        _product_type = d.pop("productType", UNSET)
        product_type: Union[Unset, ProductLicenseUsageProductType]
        if isinstance(_product_type, Unset):
            product_type = UNSET
        else:
            product_type = ProductLicenseUsageProductType(_product_type)

        def _parse_license_edition(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        license_edition = _parse_license_edition(d.pop("licenseEdition", UNSET))

        used_points = d.pop("usedPoints", UNSET)

        workload_usage = []
        _workload_usage = d.pop("workloadUsage", UNSET)
        for workload_usage_item_data in _workload_usage or []:
            workload_usage_item = WorkloadLicenseUsage.from_dict(workload_usage_item_data)

            workload_usage.append(workload_usage_item)

        product_license_usage = cls(
            license_id=license_id,
            product_type=product_type,
            license_edition=license_edition,
            used_points=used_points,
            workload_usage=workload_usage,
        )

        product_license_usage.additional_properties = d
        return product_license_usage

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
