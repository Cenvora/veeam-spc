from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_charge_category import InvoiceChargeCategory
from ..models.invoice_charge_measure import InvoiceChargeMeasure
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceCharge")


@_attrs_define
class InvoiceCharge:
    """
    Attributes:
        category (Union[Unset, InvoiceChargeCategory]): Type of consumed service.
        measure (Union[Unset, InvoiceChargeMeasure]): Measurement units of consumed service.
        quantity (Union[Unset, float]): Amount of consumed service units.
        net (Union[Unset, float]): Final cost of consumed service.
        gross (Union[Unset, float]): Cost of consumed service before applying descount and taxes.
        discount (Union[Unset, float]): Discounted amount.
        tax (Union[Unset, float]): Sales tax amount.
    """

    category: Union[Unset, InvoiceChargeCategory] = UNSET
    measure: Union[Unset, InvoiceChargeMeasure] = UNSET
    quantity: Union[Unset, float] = UNSET
    net: Union[Unset, float] = UNSET
    gross: Union[Unset, float] = UNSET
    discount: Union[Unset, float] = UNSET
    tax: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        measure: Union[Unset, str] = UNSET
        if not isinstance(self.measure, Unset):
            measure = self.measure.value

        quantity = self.quantity

        net = self.net

        gross = self.gross

        discount = self.discount

        tax = self.tax

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if measure is not UNSET:
            field_dict["measure"] = measure
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if net is not UNSET:
            field_dict["net"] = net
        if gross is not UNSET:
            field_dict["gross"] = gross
        if discount is not UNSET:
            field_dict["discount"] = discount
        if tax is not UNSET:
            field_dict["tax"] = tax

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _category = d.pop("category", UNSET)
        category: Union[Unset, InvoiceChargeCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = InvoiceChargeCategory(_category)

        _measure = d.pop("measure", UNSET)
        measure: Union[Unset, InvoiceChargeMeasure]
        if isinstance(_measure, Unset):
            measure = UNSET
        else:
            measure = InvoiceChargeMeasure(_measure)

        quantity = d.pop("quantity", UNSET)

        net = d.pop("net", UNSET)

        gross = d.pop("gross", UNSET)

        discount = d.pop("discount", UNSET)

        tax = d.pop("tax", UNSET)

        invoice_charge = cls(
            category=category,
            measure=measure,
            quantity=quantity,
            net=net,
            gross=gross,
            discount=discount,
            tax=tax,
        )

        invoice_charge.additional_properties = d
        return invoice_charge

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
