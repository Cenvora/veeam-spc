from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscription_plan_external_charge import SubscriptionPlanExternalCharge


T = TypeVar("T", bound="SubscriptionPlanExternalPlugin")


@_attrs_define
class SubscriptionPlanExternalPlugin:
    """
    Attributes:
        source_uid (UUID | Unset): UID assigned to an external plugin service.
        charges (list[SubscriptionPlanExternalCharge] | Unset): Array of charge rates.
    """

    source_uid: UUID | Unset = UNSET
    charges: list[SubscriptionPlanExternalCharge] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_uid: str | Unset = UNSET
        if not isinstance(self.source_uid, Unset):
            source_uid = str(self.source_uid)

        charges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.charges, Unset):
            charges = []
            for charges_item_data in self.charges:
                charges_item = charges_item_data.to_dict()
                charges.append(charges_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_uid is not UNSET:
            field_dict["sourceUid"] = source_uid
        if charges is not UNSET:
            field_dict["charges"] = charges

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscription_plan_external_charge import SubscriptionPlanExternalCharge

        d = dict(src_dict)
        _source_uid = d.pop("sourceUid", UNSET)
        source_uid: UUID | Unset
        if isinstance(_source_uid, Unset):
            source_uid = UNSET
        else:
            source_uid = UUID(_source_uid)

        _charges = d.pop("charges", UNSET)
        charges: list[SubscriptionPlanExternalCharge] | Unset = UNSET
        if _charges is not UNSET:
            charges = []
            for charges_item_data in _charges:
                charges_item = SubscriptionPlanExternalCharge.from_dict(charges_item_data)

                charges.append(charges_item)

        subscription_plan_external_plugin = cls(
            source_uid=source_uid,
            charges=charges,
        )

        subscription_plan_external_plugin.additional_properties = d
        return subscription_plan_external_plugin

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
