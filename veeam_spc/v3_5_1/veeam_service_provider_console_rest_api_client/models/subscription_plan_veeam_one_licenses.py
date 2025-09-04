from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionPlanVeeamOneLicenses")


@_attrs_define
class SubscriptionPlanVeeamOneLicenses:
    """
    Attributes:
        monitored_object_price (Union[Unset, float]): Monthly charge rate for a licensed object monitored in Veeam ONE.
            Default: 0.0.
    """

    monitored_object_price: Union[Unset, float] = 0.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monitored_object_price = self.monitored_object_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if monitored_object_price is not UNSET:
            field_dict["monitoredObjectPrice"] = monitored_object_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        monitored_object_price = d.pop("monitoredObjectPrice", UNSET)

        subscription_plan_veeam_one_licenses = cls(
            monitored_object_price=monitored_object_price,
        )

        subscription_plan_veeam_one_licenses.additional_properties = d
        return subscription_plan_veeam_one_licenses

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
