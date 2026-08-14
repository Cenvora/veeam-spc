from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceChargeExternalChargeInfo")


@_attrs_define
class InvoiceChargeExternalChargeInfo:
    """Details of charges for external plug-in services. The `null` value indicates that the `category` property has the
    value other than `External`.

        Attributes:
            charge_uid (UUID | Unset): UID assigned to an external plug-in charge.
            category_id (str | Unset): ID assigned to an external plugin charge category.
    """

    charge_uid: UUID | Unset = UNSET
    category_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_uid: str | Unset = UNSET
        if not isinstance(self.charge_uid, Unset):
            charge_uid = str(self.charge_uid)

        category_id = self.category_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if charge_uid is not UNSET:
            field_dict["chargeUid"] = charge_uid
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _charge_uid = d.pop("chargeUid", UNSET)
        charge_uid: UUID | Unset
        if isinstance(_charge_uid, Unset):
            charge_uid = UNSET
        else:
            charge_uid = UUID(_charge_uid)

        category_id = d.pop("categoryId", UNSET)

        invoice_charge_external_charge_info = cls(
            charge_uid=charge_uid,
            category_id=category_id,
        )

        invoice_charge_external_charge_info.additional_properties = d
        return invoice_charge_external_charge_info

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
