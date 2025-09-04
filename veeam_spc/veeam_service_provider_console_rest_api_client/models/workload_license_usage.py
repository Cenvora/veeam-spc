from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workload_license_usage_workload_type import WorkloadLicenseUsageWorkloadType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workload_license_usage_by_platform import WorkloadLicenseUsageByPlatform


T = TypeVar("T", bound="WorkloadLicenseUsage")


@_attrs_define
class WorkloadLicenseUsage:
    """
    Attributes:
        workload_type (Union[Unset, WorkloadLicenseUsageWorkloadType]): Workload type.
        description (Union[Unset, str]): Workload description.
        initial_count (Union[Unset, int]): Number of managed agents.
        reported_count (Union[Unset, int]): Number of managed agents after report finalization.
        new_count (Union[Unset, int]): Number of managed agents that were activated within the current calendar month.
        weight (Union[Unset, float]): Number of points a single workload uses.
        used_points (Union[Unset, float]): Number of points used by all managed agents of the same type.
        workloads_by_platform (Union[Unset, list['WorkloadLicenseUsageByPlatform']]): License usage by workloads for
            each platform.
    """

    workload_type: Union[Unset, WorkloadLicenseUsageWorkloadType] = UNSET
    description: Union[Unset, str] = UNSET
    initial_count: Union[Unset, int] = UNSET
    reported_count: Union[Unset, int] = UNSET
    new_count: Union[Unset, int] = UNSET
    weight: Union[Unset, float] = UNSET
    used_points: Union[Unset, float] = UNSET
    workloads_by_platform: Union[Unset, list["WorkloadLicenseUsageByPlatform"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workload_type: Union[Unset, str] = UNSET
        if not isinstance(self.workload_type, Unset):
            workload_type = self.workload_type.value

        description = self.description

        initial_count = self.initial_count

        reported_count = self.reported_count

        new_count = self.new_count

        weight = self.weight

        used_points = self.used_points

        workloads_by_platform: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.workloads_by_platform, Unset):
            workloads_by_platform = []
            for workloads_by_platform_item_data in self.workloads_by_platform:
                workloads_by_platform_item = workloads_by_platform_item_data.to_dict()
                workloads_by_platform.append(workloads_by_platform_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workload_type is not UNSET:
            field_dict["workloadType"] = workload_type
        if description is not UNSET:
            field_dict["description"] = description
        if initial_count is not UNSET:
            field_dict["initialCount"] = initial_count
        if reported_count is not UNSET:
            field_dict["reportedCount"] = reported_count
        if new_count is not UNSET:
            field_dict["newCount"] = new_count
        if weight is not UNSET:
            field_dict["weight"] = weight
        if used_points is not UNSET:
            field_dict["usedPoints"] = used_points
        if workloads_by_platform is not UNSET:
            field_dict["workloadsByPlatform"] = workloads_by_platform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workload_license_usage_by_platform import WorkloadLicenseUsageByPlatform

        d = dict(src_dict)
        _workload_type = d.pop("workloadType", UNSET)
        workload_type: Union[Unset, WorkloadLicenseUsageWorkloadType]
        if isinstance(_workload_type, Unset):
            workload_type = UNSET
        else:
            workload_type = WorkloadLicenseUsageWorkloadType(_workload_type)

        description = d.pop("description", UNSET)

        initial_count = d.pop("initialCount", UNSET)

        reported_count = d.pop("reportedCount", UNSET)

        new_count = d.pop("newCount", UNSET)

        weight = d.pop("weight", UNSET)

        used_points = d.pop("usedPoints", UNSET)

        workloads_by_platform = []
        _workloads_by_platform = d.pop("workloadsByPlatform", UNSET)
        for workloads_by_platform_item_data in _workloads_by_platform or []:
            workloads_by_platform_item = WorkloadLicenseUsageByPlatform.from_dict(workloads_by_platform_item_data)

            workloads_by_platform.append(workloads_by_platform_item)

        workload_license_usage = cls(
            workload_type=workload_type,
            description=description,
            initial_count=initial_count,
            reported_count=reported_count,
            new_count=new_count,
            weight=weight,
            used_points=used_points,
            workloads_by_platform=workloads_by_platform,
        )

        workload_license_usage.additional_properties = d
        return workload_license_usage

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
