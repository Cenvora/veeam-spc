from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulse_vdc_workload import PulseVdcWorkload


T = TypeVar("T", bound="PulseTenantVdcUsage")


@_attrs_define
class PulseTenantVdcUsage:
    """
    Attributes:
        tenant_uid (str | Unset): UID assigned to a VCSP Pulse tenant.
        workloads (list[PulseVdcWorkload] | Unset): VDC usage by each workload.
    """

    tenant_uid: str | Unset = UNSET
    workloads: list[PulseVdcWorkload] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tenant_uid = self.tenant_uid

        workloads: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.workloads, Unset):
            workloads = []
            for workloads_item_data in self.workloads:
                workloads_item = workloads_item_data.to_dict()
                workloads.append(workloads_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tenant_uid is not UNSET:
            field_dict["tenantUid"] = tenant_uid
        if workloads is not UNSET:
            field_dict["workloads"] = workloads

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulse_vdc_workload import PulseVdcWorkload

        d = dict(src_dict)
        tenant_uid = d.pop("tenantUid", UNSET)

        _workloads = d.pop("workloads", UNSET)
        workloads: list[PulseVdcWorkload] | Unset = UNSET
        if _workloads is not UNSET:
            workloads = []
            for workloads_item_data in _workloads:
                workloads_item = PulseVdcWorkload.from_dict(workloads_item_data)

                workloads.append(workloads_item)

        pulse_tenant_vdc_usage = cls(
            tenant_uid=tenant_uid,
            workloads=workloads,
        )

        pulse_tenant_vdc_usage.additional_properties = d
        return pulse_tenant_vdc_usage

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
