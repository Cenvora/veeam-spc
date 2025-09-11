from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workload_license_usage_by_weight import WorkloadLicenseUsageByWeight


T = TypeVar("T", bound="WorkloadLicenseUsageByPlatform")


@_attrs_define
class WorkloadLicenseUsageByPlatform:
    """
    Attributes:
        type_id (Union[Unset, str]): ID of a workload type and platform.
        description (Union[Unset, str]): Description of a workload type and platform.
        objects_by_weight (Union[Unset, list['WorkloadLicenseUsageByWeight']]): License usage by workloads for each
            number of consumed units.
    """

    type_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    objects_by_weight: Union[Unset, list["WorkloadLicenseUsageByWeight"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_id = self.type_id

        description = self.description

        objects_by_weight: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.objects_by_weight, Unset):
            objects_by_weight = []
            for objects_by_weight_item_data in self.objects_by_weight:
                objects_by_weight_item = objects_by_weight_item_data.to_dict()
                objects_by_weight.append(objects_by_weight_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_id is not UNSET:
            field_dict["typeId"] = type_id
        if description is not UNSET:
            field_dict["description"] = description
        if objects_by_weight is not UNSET:
            field_dict["objectsByWeight"] = objects_by_weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workload_license_usage_by_weight import WorkloadLicenseUsageByWeight

        d = dict(src_dict)
        type_id = d.pop("typeId", UNSET)

        description = d.pop("description", UNSET)

        objects_by_weight = []
        _objects_by_weight = d.pop("objectsByWeight", UNSET)
        for objects_by_weight_item_data in _objects_by_weight or []:
            objects_by_weight_item = WorkloadLicenseUsageByWeight.from_dict(objects_by_weight_item_data)

            objects_by_weight.append(objects_by_weight_item)

        workload_license_usage_by_platform = cls(
            type_id=type_id,
            description=description,
            objects_by_weight=objects_by_weight,
        )

        workload_license_usage_by_platform.additional_properties = d
        return workload_license_usage_by_platform

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
