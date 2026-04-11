from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

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
        category (InvoiceChargeCategory | Unset): Type of consumed service.
        measure (InvoiceChargeMeasure | Unset): Measurement units of consumed service.
        quantity (float | None | Unset): Amount of consumed service units.
        net (float | None | Unset): Final cost of consumed service.
        gross (float | None | Unset): Cost of consumed service before applying descount and taxes.
        discount (float | None | Unset): Discounted amount.
        tax (float | None | Unset): Sales tax amount.
    """

    category: InvoiceChargeCategory | Unset = UNSET
    measure: InvoiceChargeMeasure | Unset = UNSET
    quantity: float | None | Unset = UNSET
    net: float | None | Unset = UNSET
    gross: float | None | Unset = UNSET
    discount: float | None | Unset = UNSET
    tax: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        measure: str | Unset = UNSET
        if not isinstance(self.measure, Unset):
            measure = self.measure.value

        quantity: float | None | Unset
        if isinstance(self.quantity, Unset):
            quantity = UNSET
        else:
            quantity = self.quantity

        net: float | None | Unset
        if isinstance(self.net, Unset):
            net = UNSET
        else:
            net = self.net

        gross: float | None | Unset
        if isinstance(self.gross, Unset):
            gross = UNSET
        else:
            gross = self.gross

        discount: float | None | Unset
        if isinstance(self.discount, Unset):
            discount = UNSET
        else:
            discount = self.discount

        tax: float | None | Unset
        if isinstance(self.tax, Unset):
            tax = UNSET
        else:
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
        category: InvoiceChargeCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = InvoiceChargeCategory(_category)

        _measure = d.pop("measure", UNSET)
        measure: InvoiceChargeMeasure | Unset
        if isinstance(_measure, Unset):
            measure = UNSET
        else:
            measure = InvoiceChargeMeasure(_measure)

        def _parse_quantity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        quantity = _parse_quantity(d.pop("quantity", UNSET))

        def _parse_net(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        net = _parse_net(d.pop("net", UNSET))

        def _parse_gross(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gross = _parse_gross(d.pop("gross", UNSET))

        def _parse_discount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        discount = _parse_discount(d.pop("discount", UNSET))

        def _parse_tax(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        tax = _parse_tax(d.pop("tax", UNSET))

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
