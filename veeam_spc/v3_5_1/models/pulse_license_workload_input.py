from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PulseLicenseWorkloadInput")


@_attrs_define
class PulseLicenseWorkloadInput:
    """
    Attributes:
        workload_id (str): ID assigned to a workload type.
        count (int): Number of objects.
    """

    workload_id: str
    count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workload_id = self.workload_id

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workloadId": workload_id,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        workload_id = d.pop("workloadId")

        count = d.pop("count")

        pulse_license_workload_input = cls(
            workload_id=workload_id,
            count=count,
        )

        pulse_license_workload_input.additional_properties = d
        return pulse_license_workload_input

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
