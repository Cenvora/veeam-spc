from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionPlanVspcLicenses")


@_attrs_define
class SubscriptionPlanVspcLicenses:
    """
    Attributes:
        workstation_price (Union[Unset, float]): Monthly charge rate for a licensed workstation managed in Veeam Service
            Provider Console. Default: 0.0.
        server_price (Union[Unset, float]): Monthly charge rate for a licensed server managed in Veeam Service Provider
            Console. Default: 0.0.
    """

    workstation_price: Union[Unset, float] = 0.0
    server_price: Union[Unset, float] = 0.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workstation_price = self.workstation_price

        server_price = self.server_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workstation_price is not UNSET:
            field_dict["workstationPrice"] = workstation_price
        if server_price is not UNSET:
            field_dict["serverPrice"] = server_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        workstation_price = d.pop("workstationPrice", UNSET)

        server_price = d.pop("serverPrice", UNSET)

        subscription_plan_vspc_licenses = cls(
            workstation_price=workstation_price,
            server_price=server_price,
        )

        subscription_plan_vspc_licenses.additional_properties = d
        return subscription_plan_vspc_licenses

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
