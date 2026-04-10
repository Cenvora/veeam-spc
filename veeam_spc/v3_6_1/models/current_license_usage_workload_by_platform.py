from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CurrentLicenseUsageWorkloadByPlatform")


@_attrs_define
class CurrentLicenseUsageWorkloadByPlatform:
    """
    Attributes:
        type_id (str): ID assigned to a workload type.
        description (str): Workload description.
        weight (float): Number of license units consumed by a single workload.
        rental_units (float): Number of units with rental licenses installed.
        new_units (float): Number of units that were activated within the current calendar month.
        used_units (float): Number of units that have licenses assigned and are fully managed by Veeam Service Provider
            Console.
        rental_count (int): Number of objects with rental licenses installed.
        new_count (int): Number of objects that were activated within the current calendar month.
        used_count (int): Number of objects that have licenses assigned and are fully managed by Veeam Service Provider
            Console.
    """

    type_id: str
    description: str
    weight: float
    rental_units: float
    new_units: float
    used_units: float
    rental_count: int
    new_count: int
    used_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_id = self.type_id

        description = self.description

        weight = self.weight

        rental_units = self.rental_units

        new_units = self.new_units

        used_units = self.used_units

        rental_count = self.rental_count

        new_count = self.new_count

        used_count = self.used_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "typeId": type_id,
                "description": description,
                "weight": weight,
                "rentalUnits": rental_units,
                "newUnits": new_units,
                "usedUnits": used_units,
                "rentalCount": rental_count,
                "newCount": new_count,
                "usedCount": used_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_id = d.pop("typeId")

        description = d.pop("description")

        weight = d.pop("weight")

        rental_units = d.pop("rentalUnits")

        new_units = d.pop("newUnits")

        used_units = d.pop("usedUnits")

        rental_count = d.pop("rentalCount")

        new_count = d.pop("newCount")

        used_count = d.pop("usedCount")

        current_license_usage_workload_by_platform = cls(
            type_id=type_id,
            description=description,
            weight=weight,
            rental_units=rental_units,
            new_units=new_units,
            used_units=used_units,
            rental_count=rental_count,
            new_count=new_count,
            used_count=used_count,
        )

        current_license_usage_workload_by_platform.additional_properties = d
        return current_license_usage_workload_by_platform

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
