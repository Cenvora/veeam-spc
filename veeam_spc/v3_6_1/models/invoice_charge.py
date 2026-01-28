from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

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
        quantity (Union[None, Unset, float]): Amount of consumed service units.
        net (Union[None, Unset, float]): Final cost of consumed service.
        gross (Union[None, Unset, float]): Cost of consumed service before applying descount and taxes.
        discount (Union[None, Unset, float]): Discounted amount.
        tax (Union[None, Unset, float]): Sales tax amount.
    """

    category: Union[Unset, InvoiceChargeCategory] = UNSET
    measure: Union[Unset, InvoiceChargeMeasure] = UNSET
    quantity: Union[None, Unset, float] = UNSET
    net: Union[None, Unset, float] = UNSET
    gross: Union[None, Unset, float] = UNSET
    discount: Union[None, Unset, float] = UNSET
    tax: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        measure: Union[Unset, str] = UNSET
        if not isinstance(self.measure, Unset):
            measure = self.measure.value

        quantity: Union[None, Unset, float]
        if isinstance(self.quantity, Unset):
            quantity = UNSET
        else:
            quantity = self.quantity

        net: Union[None, Unset, float]
        if isinstance(self.net, Unset):
            net = UNSET
        else:
            net = self.net

        gross: Union[None, Unset, float]
        if isinstance(self.gross, Unset):
            gross = UNSET
        else:
            gross = self.gross

        discount: Union[None, Unset, float]
        if isinstance(self.discount, Unset):
            discount = UNSET
        else:
            discount = self.discount

        tax: Union[None, Unset, float]
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

        def _parse_quantity(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        quantity = _parse_quantity(d.pop("quantity", UNSET))

        def _parse_net(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        net = _parse_net(d.pop("net", UNSET))

        def _parse_gross(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        gross = _parse_gross(d.pop("gross", UNSET))

        def _parse_discount(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        discount = _parse_discount(d.pop("discount", UNSET))

        def _parse_tax(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

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
