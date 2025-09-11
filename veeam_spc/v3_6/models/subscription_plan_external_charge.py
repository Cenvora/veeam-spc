from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.measure_unit_type import MeasureUnitType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionPlanExternalCharge")


@_attrs_define
class SubscriptionPlanExternalCharge:
    """
    Attributes:
        charge_uid (Union[Unset, UUID]): UID assigned to a charge rate.
        measure_type (Union[Unset, MeasureUnitType]): Measurement units of provided services.
        price (Union[Unset, float]): Charge rate.
    """

    charge_uid: Union[Unset, UUID] = UNSET
    measure_type: Union[Unset, MeasureUnitType] = UNSET
    price: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_uid: Union[Unset, str] = UNSET
        if not isinstance(self.charge_uid, Unset):
            charge_uid = str(self.charge_uid)

        measure_type: Union[Unset, str] = UNSET
        if not isinstance(self.measure_type, Unset):
            measure_type = self.measure_type.value

        price = self.price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if charge_uid is not UNSET:
            field_dict["chargeUid"] = charge_uid
        if measure_type is not UNSET:
            field_dict["measureType"] = measure_type
        if price is not UNSET:
            field_dict["price"] = price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _charge_uid = d.pop("chargeUid", UNSET)
        charge_uid: Union[Unset, UUID]
        if isinstance(_charge_uid, Unset):
            charge_uid = UNSET
        else:
            charge_uid = UUID(_charge_uid)

        _measure_type = d.pop("measureType", UNSET)
        measure_type: Union[Unset, MeasureUnitType]
        if isinstance(_measure_type, Unset):
            measure_type = UNSET
        else:
            measure_type = MeasureUnitType(_measure_type)

        price = d.pop("price", UNSET)

        subscription_plan_external_charge = cls(
            charge_uid=charge_uid,
            measure_type=measure_type,
            price=price,
        )

        subscription_plan_external_charge.additional_properties = d
        return subscription_plan_external_charge

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
