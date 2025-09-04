from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_charge import InvoiceCharge
    from ..models.invoice_period import InvoicePeriod


T = TypeVar("T", bound="InvoiceData")


@_attrs_define
class InvoiceData:
    """Invoice details.

    Attributes:
        period (InvoicePeriod): Period for which information about services consumed by each company is included in an
            invoice.
        charges (Union[Unset, list['InvoiceCharge']]): Detailed information on all consumed services and their costs.
        total_net (Union[Unset, float]): Final cost.
        total_gross (Union[Unset, float]): Total cost before applying discounts and taxes.
        total_discount (Union[Unset, float]): Discounted amount.
        total_tax (Union[Unset, float]): Sales tax amount.
    """

    period: "InvoicePeriod"
    charges: Union[Unset, list["InvoiceCharge"]] = UNSET
    total_net: Union[Unset, float] = UNSET
    total_gross: Union[Unset, float] = UNSET
    total_discount: Union[Unset, float] = UNSET
    total_tax: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        period = self.period.to_dict()

        charges: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.charges, Unset):
            charges = []
            for charges_item_data in self.charges:
                charges_item = charges_item_data.to_dict()
                charges.append(charges_item)

        total_net = self.total_net

        total_gross = self.total_gross

        total_discount = self.total_discount

        total_tax = self.total_tax

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "period": period,
            }
        )
        if charges is not UNSET:
            field_dict["charges"] = charges
        if total_net is not UNSET:
            field_dict["totalNet"] = total_net
        if total_gross is not UNSET:
            field_dict["totalGross"] = total_gross
        if total_discount is not UNSET:
            field_dict["totalDiscount"] = total_discount
        if total_tax is not UNSET:
            field_dict["totalTax"] = total_tax

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoice_charge import InvoiceCharge
        from ..models.invoice_period import InvoicePeriod

        d = dict(src_dict)
        period = InvoicePeriod.from_dict(d.pop("period"))

        charges = []
        _charges = d.pop("charges", UNSET)
        for charges_item_data in _charges or []:
            charges_item = InvoiceCharge.from_dict(charges_item_data)

            charges.append(charges_item)

        total_net = d.pop("totalNet", UNSET)

        total_gross = d.pop("totalGross", UNSET)

        total_discount = d.pop("totalDiscount", UNSET)

        total_tax = d.pop("totalTax", UNSET)

        invoice_data = cls(
            period=period,
            charges=charges,
            total_net=total_net,
            total_gross=total_gross,
            total_discount=total_discount,
            total_tax=total_tax,
        )

        invoice_data.additional_properties = d
        return invoice_data

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
