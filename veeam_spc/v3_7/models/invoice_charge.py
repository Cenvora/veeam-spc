from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_charge_category import InvoiceChargeCategory
from ..models.invoice_charge_measure import InvoiceChargeMeasure
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_charge_external_charge_info import InvoiceChargeExternalChargeInfo
    from ..models.invoice_charge_repository_label_info import InvoiceChargeRepositoryLabelInfo


T = TypeVar("T", bound="InvoiceCharge")


@_attrs_define
class InvoiceCharge:
    """
    Attributes:
        category (InvoiceChargeCategory | Unset): Category of the consumed service.
            >For a charge raised by an external plugin, this property equals `External`. For details, see the
            `externalChargeInfo` property value.
            >For repository usage by each label, this property equals `RepoUsageByLabelRemote` or `RepoUsageByLabelHosted`.
            For details, see the `repositoryLabelInfo` property value.
            >For repository usage not attributed to a specific label, this property equals
            `RepoUsageByLabelRemoteUnspecified` or `RepoUsageByLabelHostedUnspecified`.
        measure (InvoiceChargeMeasure | Unset): Measurement units of consumed service.
        quantity (float | Unset): Amount of consumed service units.
        net (float | Unset): Final cost of consumed service.
        gross (float | Unset): Cost of consumed service before applying descount and taxes.
        discount (float | Unset): Discounted amount.
        tax (float | Unset): Sales tax amount.
        category_name (str | Unset): Name of a service category.
        display_name (str | Unset): Name of an invoice line. For repository usage charged per label, includes the label
            name.
        repository_label_info (InvoiceChargeRepositoryLabelInfo | Unset): Details of for repository usage charges
            applied per label. The `null` value indicates that the `category` property has a value other than
            `RepoUsageByLabelRemote` or `RepoUsageByLabelHosted`.
        external_charge_info (InvoiceChargeExternalChargeInfo | Unset): Details of charges for external plug-in
            services. The `null` value indicates that the `category` property has the value other than `External`.
    """

    category: InvoiceChargeCategory | Unset = UNSET
    measure: InvoiceChargeMeasure | Unset = UNSET
    quantity: float | Unset = UNSET
    net: float | Unset = UNSET
    gross: float | Unset = UNSET
    discount: float | Unset = UNSET
    tax: float | Unset = UNSET
    category_name: str | Unset = UNSET
    display_name: str | Unset = UNSET
    repository_label_info: InvoiceChargeRepositoryLabelInfo | Unset = UNSET
    external_charge_info: InvoiceChargeExternalChargeInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        measure: str | Unset = UNSET
        if not isinstance(self.measure, Unset):
            measure = self.measure.value

        quantity = self.quantity

        net = self.net

        gross = self.gross

        discount = self.discount

        tax = self.tax

        category_name = self.category_name

        display_name = self.display_name

        repository_label_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository_label_info, Unset):
            repository_label_info = self.repository_label_info.to_dict()

        external_charge_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external_charge_info, Unset):
            external_charge_info = self.external_charge_info.to_dict()

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
        if category_name is not UNSET:
            field_dict["categoryName"] = category_name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if repository_label_info is not UNSET:
            field_dict["repositoryLabelInfo"] = repository_label_info
        if external_charge_info is not UNSET:
            field_dict["externalChargeInfo"] = external_charge_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoice_charge_external_charge_info import InvoiceChargeExternalChargeInfo
        from ..models.invoice_charge_repository_label_info import InvoiceChargeRepositoryLabelInfo

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

        quantity = d.pop("quantity", UNSET)

        net = d.pop("net", UNSET)

        gross = d.pop("gross", UNSET)

        discount = d.pop("discount", UNSET)

        tax = d.pop("tax", UNSET)

        category_name = d.pop("categoryName", UNSET)

        display_name = d.pop("displayName", UNSET)

        _repository_label_info = d.pop("repositoryLabelInfo", UNSET)
        repository_label_info: InvoiceChargeRepositoryLabelInfo | Unset
        if isinstance(_repository_label_info, Unset):
            repository_label_info = UNSET
        else:
            repository_label_info = InvoiceChargeRepositoryLabelInfo.from_dict(_repository_label_info)

        _external_charge_info = d.pop("externalChargeInfo", UNSET)
        external_charge_info: InvoiceChargeExternalChargeInfo | Unset
        if isinstance(_external_charge_info, Unset):
            external_charge_info = UNSET
        else:
            external_charge_info = InvoiceChargeExternalChargeInfo.from_dict(_external_charge_info)

        invoice_charge = cls(
            category=category,
            measure=measure,
            quantity=quantity,
            net=net,
            gross=gross,
            discount=discount,
            tax=tax,
            category_name=category_name,
            display_name=display_name,
            repository_label_info=repository_label_info,
            external_charge_info=external_charge_info,
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
