from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulseVdcWorkload")


@_attrs_define
class PulseVdcWorkload:
    """
    Attributes:
        product_code (str | Unset): Identifier of a Veeam product.
        product_name (str | Unset): Name of a Veeam product.
        unit_type (str | Unset): Type of a billing unit.
        used_units (float | Unset): Number of consumed billing units.
        total_units (float | Unset): Total number of billing units.
        weight (float | Unset): Price of a billing unit in points.
        used_points (float | Unset): Number of consumed license points.
        min_commit_qty (float | Unset): Minimum committed quantity.
        min_commit_enforcement (float | Unset): Enforced minimum committed quantity.
        location (str | Unset): Usage location.
    """

    product_code: str | Unset = UNSET
    product_name: str | Unset = UNSET
    unit_type: str | Unset = UNSET
    used_units: float | Unset = UNSET
    total_units: float | Unset = UNSET
    weight: float | Unset = UNSET
    used_points: float | Unset = UNSET
    min_commit_qty: float | Unset = UNSET
    min_commit_enforcement: float | Unset = UNSET
    location: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_code = self.product_code

        product_name = self.product_name

        unit_type = self.unit_type

        used_units = self.used_units

        total_units = self.total_units

        weight = self.weight

        used_points = self.used_points

        min_commit_qty = self.min_commit_qty

        min_commit_enforcement = self.min_commit_enforcement

        location = self.location

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_code is not UNSET:
            field_dict["productCode"] = product_code
        if product_name is not UNSET:
            field_dict["productName"] = product_name
        if unit_type is not UNSET:
            field_dict["unitType"] = unit_type
        if used_units is not UNSET:
            field_dict["usedUnits"] = used_units
        if total_units is not UNSET:
            field_dict["totalUnits"] = total_units
        if weight is not UNSET:
            field_dict["weight"] = weight
        if used_points is not UNSET:
            field_dict["usedPoints"] = used_points
        if min_commit_qty is not UNSET:
            field_dict["minCommitQty"] = min_commit_qty
        if min_commit_enforcement is not UNSET:
            field_dict["minCommitEnforcement"] = min_commit_enforcement
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_code = d.pop("productCode", UNSET)

        product_name = d.pop("productName", UNSET)

        unit_type = d.pop("unitType", UNSET)

        used_units = d.pop("usedUnits", UNSET)

        total_units = d.pop("totalUnits", UNSET)

        weight = d.pop("weight", UNSET)

        used_points = d.pop("usedPoints", UNSET)

        min_commit_qty = d.pop("minCommitQty", UNSET)

        min_commit_enforcement = d.pop("minCommitEnforcement", UNSET)

        location = d.pop("location", UNSET)

        pulse_vdc_workload = cls(
            product_code=product_code,
            product_name=product_name,
            unit_type=unit_type,
            used_units=used_units,
            total_units=total_units,
            weight=weight,
            used_points=used_points,
            min_commit_qty=min_commit_qty,
            min_commit_enforcement=min_commit_enforcement,
            location=location,
        )

        pulse_vdc_workload.additional_properties = d
        return pulse_vdc_workload

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
