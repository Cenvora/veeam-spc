from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.total_product_license_usage import TotalProductLicenseUsage


T = TypeVar("T", bound="LicenseReportSummary")


@_attrs_define
class LicenseReportSummary:
    """
    Attributes:
        total_points (float): Number of report owner license points used by managed organizations.
        products_usage (list['TotalProductLicenseUsage']): License usage for each product.
    """

    total_points: float
    products_usage: list["TotalProductLicenseUsage"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_points = self.total_points

        products_usage = []
        for products_usage_item_data in self.products_usage:
            products_usage_item = products_usage_item_data.to_dict()
            products_usage.append(products_usage_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalPoints": total_points,
                "productsUsage": products_usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.total_product_license_usage import TotalProductLicenseUsage

        d = dict(src_dict)
        total_points = d.pop("totalPoints")

        products_usage = []
        _products_usage = d.pop("productsUsage")
        for products_usage_item_data in _products_usage:
            products_usage_item = TotalProductLicenseUsage.from_dict(products_usage_item_data)

            products_usage.append(products_usage_item)

        license_report_summary = cls(
            total_points=total_points,
            products_usage=products_usage,
        )

        license_report_summary.additional_properties = d
        return license_report_summary

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
