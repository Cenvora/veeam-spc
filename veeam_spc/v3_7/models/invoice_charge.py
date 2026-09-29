from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_charge_category import InvoiceChargeCategory
from ..models.invoice_charge_measure import InvoiceChargeMeasure
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_charge_external_charge_info_type_0 import InvoiceChargeExternalChargeInfoType0
    from ..models.invoice_charge_repository_label_info_type_0 import InvoiceChargeRepositoryLabelInfoType0


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
        quantity (float | None | Unset): Amount of consumed service units.
        net (float | None | Unset): Final cost of consumed service.
        gross (float | None | Unset): Cost of consumed service before applying descount and taxes.
        discount (float | None | Unset): Discounted amount.
        tax (float | None | Unset): Sales tax amount.
        category_name (None | str | Unset): Name of a service category.
        display_name (None | str | Unset): Name of an invoice line. For repository usage charged per label, includes the
            label name.
        repository_label_info (InvoiceChargeRepositoryLabelInfoType0 | None | Unset): Details of for repository usage
            charges applied per label. The `null` value indicates that the `category` property has a value other than
            `RepoUsageByLabelRemote` or `RepoUsageByLabelHosted`.
        external_charge_info (InvoiceChargeExternalChargeInfoType0 | None | Unset): Details of charges for external
            plug-in services. The `null` value indicates that the `category` property has the value other than `External`.
    """

    category: InvoiceChargeCategory | Unset = UNSET
    measure: InvoiceChargeMeasure | Unset = UNSET
    quantity: float | None | Unset = UNSET
    net: float | None | Unset = UNSET
    gross: float | None | Unset = UNSET
    discount: float | None | Unset = UNSET
    tax: float | None | Unset = UNSET
    category_name: None | str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    repository_label_info: InvoiceChargeRepositoryLabelInfoType0 | None | Unset = UNSET
    external_charge_info: InvoiceChargeExternalChargeInfoType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.invoice_charge_external_charge_info_type_0 import InvoiceChargeExternalChargeInfoType0
        from ..models.invoice_charge_repository_label_info_type_0 import InvoiceChargeRepositoryLabelInfoType0

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

        category_name: None | str | Unset
        if isinstance(self.category_name, Unset):
            category_name = UNSET
        else:
            category_name = self.category_name

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        repository_label_info: dict[str, Any] | None | Unset
        if isinstance(self.repository_label_info, Unset):
            repository_label_info = UNSET
        elif isinstance(self.repository_label_info, InvoiceChargeRepositoryLabelInfoType0):
            repository_label_info = self.repository_label_info.to_dict()
        else:
            repository_label_info = self.repository_label_info

        external_charge_info: dict[str, Any] | None | Unset
        if isinstance(self.external_charge_info, Unset):
            external_charge_info = UNSET
        elif isinstance(self.external_charge_info, InvoiceChargeExternalChargeInfoType0):
            external_charge_info = self.external_charge_info.to_dict()
        else:
            external_charge_info = self.external_charge_info

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
        from ..models.invoice_charge_external_charge_info_type_0 import InvoiceChargeExternalChargeInfoType0
        from ..models.invoice_charge_repository_label_info_type_0 import InvoiceChargeRepositoryLabelInfoType0

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

        def _parse_category_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_name = _parse_category_name(d.pop("categoryName", UNSET))

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))

        def _parse_repository_label_info(data: object) -> InvoiceChargeRepositoryLabelInfoType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                repository_label_info_type_0 = InvoiceChargeRepositoryLabelInfoType0.from_dict(data)

                return repository_label_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvoiceChargeRepositoryLabelInfoType0 | None | Unset, data)

        repository_label_info = _parse_repository_label_info(d.pop("repositoryLabelInfo", UNSET))

        def _parse_external_charge_info(data: object) -> InvoiceChargeExternalChargeInfoType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                external_charge_info_type_0 = InvoiceChargeExternalChargeInfoType0.from_dict(data)

                return external_charge_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvoiceChargeExternalChargeInfoType0 | None | Unset, data)

        external_charge_info = _parse_external_charge_info(d.pop("externalChargeInfo", UNSET))

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
