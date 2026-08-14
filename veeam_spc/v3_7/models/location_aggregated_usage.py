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


T = TypeVar("T", bound="LocationAggregatedUsage")


@_attrs_define
class LocationAggregatedUsage:
    """
    Attributes:
        company_uid (UUID | Unset): UID assigned to a company.
        reseller_uid (UUID | Unset): UID assigned to a reseller.
        location_uid (UUID | Unset): UID assigned to a location.
        date (datetime.date | Unset): Date of data aggregation.
        counters (list[AggregatedUsage] | Unset): Managed services counters.
    """

    company_uid: UUID | Unset = UNSET
    reseller_uid: UUID | Unset = UNSET
    location_uid: UUID | Unset = UNSET
    date: datetime.date | Unset = UNSET
    counters: list[AggregatedUsage] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_uid: str | Unset = UNSET
        if not isinstance(self.company_uid, Unset):
            company_uid = str(self.company_uid)

        reseller_uid: str | Unset = UNSET
        if not isinstance(self.reseller_uid, Unset):
            reseller_uid = str(self.reseller_uid)

        location_uid: str | Unset = UNSET
        if not isinstance(self.location_uid, Unset):
            location_uid = str(self.location_uid)

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
        if company_uid is not UNSET:
            field_dict["companyUid"] = company_uid
        if reseller_uid is not UNSET:
            field_dict["resellerUid"] = reseller_uid
        if location_uid is not UNSET:
            field_dict["locationUid"] = location_uid
        if date is not UNSET:
            field_dict["date"] = date
        if counters is not UNSET:
            field_dict["counters"] = counters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aggregated_usage import AggregatedUsage

        d = dict(src_dict)
        _company_uid = d.pop("companyUid", UNSET)
        company_uid: UUID | Unset
        if isinstance(_company_uid, Unset):
            company_uid = UNSET
        else:
            company_uid = UUID(_company_uid)

        _reseller_uid = d.pop("resellerUid", UNSET)
        reseller_uid: UUID | Unset
        if isinstance(_reseller_uid, Unset):
            reseller_uid = UNSET
        else:
            reseller_uid = UUID(_reseller_uid)

        _location_uid = d.pop("locationUid", UNSET)
        location_uid: UUID | Unset
        if isinstance(_location_uid, Unset):
            location_uid = UNSET
        else:
            location_uid = UUID(_location_uid)

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

        location_aggregated_usage = cls(
            company_uid=company_uid,
            reseller_uid=reseller_uid,
            location_uid=location_uid,
            date=date,
            counters=counters,
        )

        location_aggregated_usage.additional_properties = d
        return location_aggregated_usage

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
