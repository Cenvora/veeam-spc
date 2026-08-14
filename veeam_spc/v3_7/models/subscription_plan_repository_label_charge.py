from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subscription_plan_repository_label_charge_free_of_charge_measure import (
    SubscriptionPlanRepositoryLabelChargeFreeOfChargeMeasure,
)
from ..models.subscription_plan_repository_label_charge_price_measure import (
    SubscriptionPlanRepositoryLabelChargePriceMeasure,
)

T = TypeVar("T", bound="SubscriptionPlanRepositoryLabelCharge")


@_attrs_define
class SubscriptionPlanRepositoryLabelCharge:
    """
    Attributes:
        label_uid (UUID): UID assigned to a label.
        price (float): Charge rate for one GB or TB of consumed backup repository space.
        price_measure (SubscriptionPlanRepositoryLabelChargePriceMeasure): Measurement units of consumed backup
            repository space. Default: SubscriptionPlanRepositoryLabelChargePriceMeasure.GB.
        free_of_charge (float): Amount of backup repository space that can be consumed for free.
        free_of_charge_measure (SubscriptionPlanRepositoryLabelChargeFreeOfChargeMeasure): Measurement units of backup
            repository space that can be consumed for free. Default:
            SubscriptionPlanRepositoryLabelChargeFreeOfChargeMeasure.GB.
        chunk_size (int): Chunk size used to round up storage space.
        round_up_per_chunk (bool): Indicates whether consumed storage space must be rounded up.
        enabled (bool): Indicates whether the pricing configuration is enabled.
    """

    label_uid: UUID
    price: float
    free_of_charge: float
    chunk_size: int
    round_up_per_chunk: bool
    enabled: bool
    price_measure: SubscriptionPlanRepositoryLabelChargePriceMeasure = (
        SubscriptionPlanRepositoryLabelChargePriceMeasure.GB
    )
    free_of_charge_measure: SubscriptionPlanRepositoryLabelChargeFreeOfChargeMeasure = (
        SubscriptionPlanRepositoryLabelChargeFreeOfChargeMeasure.GB
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label_uid = str(self.label_uid)

        price = self.price

        price_measure = self.price_measure.value

        free_of_charge = self.free_of_charge

        free_of_charge_measure = self.free_of_charge_measure.value

        chunk_size = self.chunk_size

        round_up_per_chunk = self.round_up_per_chunk

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "labelUid": label_uid,
                "price": price,
                "priceMeasure": price_measure,
                "freeOfCharge": free_of_charge,
                "freeOfChargeMeasure": free_of_charge_measure,
                "chunkSize": chunk_size,
                "roundUpPerChunk": round_up_per_chunk,
                "enabled": enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label_uid = UUID(d.pop("labelUid"))

        price = d.pop("price")

        price_measure = SubscriptionPlanRepositoryLabelChargePriceMeasure(d.pop("priceMeasure"))

        free_of_charge = d.pop("freeOfCharge")

        free_of_charge_measure = SubscriptionPlanRepositoryLabelChargeFreeOfChargeMeasure(d.pop("freeOfChargeMeasure"))

        chunk_size = d.pop("chunkSize")

        round_up_per_chunk = d.pop("roundUpPerChunk")

        enabled = d.pop("enabled")

        subscription_plan_repository_label_charge = cls(
            label_uid=label_uid,
            price=price,
            price_measure=price_measure,
            free_of_charge=free_of_charge,
            free_of_charge_measure=free_of_charge_measure,
            chunk_size=chunk_size,
            round_up_per_chunk=round_up_per_chunk,
            enabled=enabled,
        )

        subscription_plan_repository_label_charge.additional_properties = d
        return subscription_plan_repository_label_charge

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
