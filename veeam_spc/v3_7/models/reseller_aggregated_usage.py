from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aggregated_usage import AggregatedUsage


T = TypeVar("T", bound="ResellerAggregatedUsage")


@_attrs_define
class ResellerAggregatedUsage:
    """
    Attributes:
        reseller_uid (UUID | Unset): UID assigned to a reseller.
        date (datetime.date | Unset): Date of data aggregation.
        counters (list[AggregatedUsage] | Unset): Managed services counters.
    """

    reseller_uid: UUID | Unset = UNSET
    date: datetime.date | Unset = UNSET
    counters: list[AggregatedUsage] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reseller_uid: str | Unset = UNSET
        if not isinstance(self.reseller_uid, Unset):
            reseller_uid = str(self.reseller_uid)

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        counters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.counters, Unset):
            counters = []
            for counters_item_data in self.counters:
                counters_item = counters_item_data.to_dict()
                counters.append(counters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reseller_uid is not UNSET:
            field_dict["resellerUid"] = reseller_uid
        if date is not UNSET:
            field_dict["date"] = date
        if counters is not UNSET:
            field_dict["counters"] = counters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aggregated_usage import AggregatedUsage

        d = dict(src_dict)
        _reseller_uid = d.pop("resellerUid", UNSET)
        reseller_uid: UUID | Unset
        if isinstance(_reseller_uid, Unset):
            reseller_uid = UNSET
        else:
            reseller_uid = UUID(_reseller_uid)

        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        _counters = d.pop("counters", UNSET)
        counters: list[AggregatedUsage] | Unset = UNSET
        if _counters is not UNSET:
            counters = []
            for counters_item_data in _counters:
                counters_item = AggregatedUsage.from_dict(counters_item_data)

                counters.append(counters_item)

        reseller_aggregated_usage = cls(
            reseller_uid=reseller_uid,
            date=date,
            counters=counters,
        )

        reseller_aggregated_usage.additional_properties = d
        return reseller_aggregated_usage

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
