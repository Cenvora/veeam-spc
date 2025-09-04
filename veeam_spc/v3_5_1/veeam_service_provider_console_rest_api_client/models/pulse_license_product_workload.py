from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulseLicenseProductWorkload")


@_attrs_define
class PulseLicenseProductWorkload:
    """
    Attributes:
        workload_id (Union[Unset, str]): ID addigned to a workload.
        name (Union[Unset, str]): Name of a workload.
        multiplier (Union[Unset, float]): License unit multiplier for the workload type.
    """

    workload_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    multiplier: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workload_id = self.workload_id

        name = self.name

        multiplier = self.multiplier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workload_id is not UNSET:
            field_dict["workloadId"] = workload_id
        if name is not UNSET:
            field_dict["name"] = name
        if multiplier is not UNSET:
            field_dict["multiplier"] = multiplier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        workload_id = d.pop("workloadId", UNSET)

        name = d.pop("name", UNSET)

        multiplier = d.pop("multiplier", UNSET)

        pulse_license_product_workload = cls(
            workload_id=workload_id,
            name=name,
            multiplier=multiplier,
        )

        pulse_license_product_workload.additional_properties = d
        return pulse_license_product_workload

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
