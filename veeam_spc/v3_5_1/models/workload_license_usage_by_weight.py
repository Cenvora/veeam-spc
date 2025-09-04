from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkloadLicenseUsageByWeight")


@_attrs_define
class WorkloadLicenseUsageByWeight:
    """
    Attributes:
        weight (Union[Unset, float]): Number of license units consumed by a single workload.
        initial_count (Union[Unset, int]): Number of managed Veeam backup agents.
        reported_count (Union[Unset, int]): Number of managed Veeam backup agents in a finalized report.
        new_count (Union[Unset, int]): Number of managed Veeam backup agents that were activated within the current
            calendar month.
        used_points (Union[Unset, float]): Number of license units consumed by all workloads.
    """

    weight: Union[Unset, float] = UNSET
    initial_count: Union[Unset, int] = UNSET
    reported_count: Union[Unset, int] = UNSET
    new_count: Union[Unset, int] = UNSET
    used_points: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        weight = self.weight

        initial_count = self.initial_count

        reported_count = self.reported_count

        new_count = self.new_count

        used_points = self.used_points

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if weight is not UNSET:
            field_dict["weight"] = weight
        if initial_count is not UNSET:
            field_dict["initialCount"] = initial_count
        if reported_count is not UNSET:
            field_dict["reportedCount"] = reported_count
        if new_count is not UNSET:
            field_dict["newCount"] = new_count
        if used_points is not UNSET:
            field_dict["usedPoints"] = used_points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        weight = d.pop("weight", UNSET)

        initial_count = d.pop("initialCount", UNSET)

        reported_count = d.pop("reportedCount", UNSET)

        new_count = d.pop("newCount", UNSET)

        used_points = d.pop("usedPoints", UNSET)

        workload_license_usage_by_weight = cls(
            weight=weight,
            initial_count=initial_count,
            reported_count=reported_count,
            new_count=new_count,
            used_points=used_points,
        )

        workload_license_usage_by_weight.additional_properties = d
        return workload_license_usage_by_weight

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
