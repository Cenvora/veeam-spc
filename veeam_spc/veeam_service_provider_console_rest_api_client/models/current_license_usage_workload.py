from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.current_license_usage_workload_unit_type import CurrentLicenseUsageWorkloadUnitType

if TYPE_CHECKING:
    from ..models.current_license_usage_workload_by_platform import CurrentLicenseUsageWorkloadByPlatform


T = TypeVar("T", bound="CurrentLicenseUsageWorkload")


@_attrs_define
class CurrentLicenseUsageWorkload:
    """
    Attributes:
        id (UUID): ID assigned to a workload.
        description (str): Workload description.
        unit_type (CurrentLicenseUsageWorkloadUnitType): License unit type.
        rental_units (float): Number of units with rental licenses installed.
        new_units (float): Number of units that were activated within the current calendar month.
        used_units (float): Number of units that have licenses assigned and are fully managed by Veeam Service Provider
            Console.
        rental_count (int): Number of objects with rental licenses installed.
        new_count (int): Number of objects that were activated within the current calendar month.
        used_count (int): Number of objects that have licenses assigned and are fully managed by Veeam Service Provider
            Console.
        workloads_by_platform (list['CurrentLicenseUsageWorkloadByPlatform']): License usage by workloads for each
            platform.
    """

    id: UUID
    description: str
    unit_type: CurrentLicenseUsageWorkloadUnitType
    rental_units: float
    new_units: float
    used_units: float
    rental_count: int
    new_count: int
    used_count: int
    workloads_by_platform: list["CurrentLicenseUsageWorkloadByPlatform"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        description = self.description

        unit_type = self.unit_type.value

        rental_units = self.rental_units

        new_units = self.new_units

        used_units = self.used_units

        rental_count = self.rental_count

        new_count = self.new_count

        used_count = self.used_count

        workloads_by_platform = []
        for workloads_by_platform_item_data in self.workloads_by_platform:
            workloads_by_platform_item = workloads_by_platform_item_data.to_dict()
            workloads_by_platform.append(workloads_by_platform_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "description": description,
                "unitType": unit_type,
                "rentalUnits": rental_units,
                "newUnits": new_units,
                "usedUnits": used_units,
                "rentalCount": rental_count,
                "newCount": new_count,
                "usedCount": used_count,
                "workloadsByPlatform": workloads_by_platform,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.current_license_usage_workload_by_platform import CurrentLicenseUsageWorkloadByPlatform

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        description = d.pop("description")

        unit_type = CurrentLicenseUsageWorkloadUnitType(d.pop("unitType"))

        rental_units = d.pop("rentalUnits")

        new_units = d.pop("newUnits")

        used_units = d.pop("usedUnits")

        rental_count = d.pop("rentalCount")

        new_count = d.pop("newCount")

        used_count = d.pop("usedCount")

        workloads_by_platform = []
        _workloads_by_platform = d.pop("workloadsByPlatform")
        for workloads_by_platform_item_data in _workloads_by_platform:
            workloads_by_platform_item = CurrentLicenseUsageWorkloadByPlatform.from_dict(
                workloads_by_platform_item_data
            )

            workloads_by_platform.append(workloads_by_platform_item)

        current_license_usage_workload = cls(
            id=id,
            description=description,
            unit_type=unit_type,
            rental_units=rental_units,
            new_units=new_units,
            used_units=used_units,
            rental_count=rental_count,
            new_count=new_count,
            used_count=used_count,
            workloads_by_platform=workloads_by_platform,
        )

        current_license_usage_workload.additional_properties = d
        return current_license_usage_workload

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
