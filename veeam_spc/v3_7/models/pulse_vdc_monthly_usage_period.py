from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulse_tenant_vdc_usage import PulseTenantVdcUsage


T = TypeVar("T", bound="PulseVdcMonthlyUsagePeriod")


@_attrs_define
class PulseVdcMonthlyUsagePeriod:
    """
    Attributes:
        month (str | Unset): Reporting month in the `yyyy-MM` format.
        tenants (list[PulseTenantVdcUsage] | Unset): VDC usage by each VCSP Pulse tenant.
    """

    month: str | Unset = UNSET
    tenants: list[PulseTenantVdcUsage] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        month = self.month

        tenants: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tenants, Unset):
            tenants = []
            for tenants_item_data in self.tenants:
                tenants_item = tenants_item_data.to_dict()
                tenants.append(tenants_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if month is not UNSET:
            field_dict["month"] = month
        if tenants is not UNSET:
            field_dict["tenants"] = tenants

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulse_tenant_vdc_usage import PulseTenantVdcUsage

        d = dict(src_dict)
        month = d.pop("month", UNSET)

        _tenants = d.pop("tenants", UNSET)
        tenants: list[PulseTenantVdcUsage] | Unset = UNSET
        if _tenants is not UNSET:
            tenants = []
            for tenants_item_data in _tenants:
                tenants_item = PulseTenantVdcUsage.from_dict(tenants_item_data)

                tenants.append(tenants_item)

        pulse_vdc_monthly_usage_period = cls(
            month=month,
            tenants=tenants,
        )

        pulse_vdc_monthly_usage_period.additional_properties = d
        return pulse_vdc_monthly_usage_period

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
