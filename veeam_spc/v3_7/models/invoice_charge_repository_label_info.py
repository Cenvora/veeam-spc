from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceChargeRepositoryLabelInfo")


@_attrs_define
class InvoiceChargeRepositoryLabelInfo:
    """Details of for repository usage charges applied per label. The `null` value indicates that the `category` property
    has a value other than `RepoUsageByLabelRemote` or `RepoUsageByLabelHosted`.

        Attributes:
            label_uid (UUID | Unset): UID assigned to the label for which the repository usage is charged.
    """

    label_uid: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label_uid: str | Unset = UNSET
        if not isinstance(self.label_uid, Unset):
            label_uid = str(self.label_uid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label_uid is not UNSET:
            field_dict["labelUid"] = label_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _label_uid = d.pop("labelUid", UNSET)
        label_uid: UUID | Unset
        if isinstance(_label_uid, Unset):
            label_uid = UNSET
        else:
            label_uid = UUID(_label_uid)

        invoice_charge_repository_label_info = cls(
            label_uid=label_uid,
        )

        invoice_charge_repository_label_info.additional_properties = d
        return invoice_charge_repository_label_info

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
