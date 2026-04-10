import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoicePeriod")


@_attrs_define
class InvoicePeriod:
    """Period for which information about services consumed by each company is included in an invoice.

    Attributes:
        from_date (Union[None, Unset, datetime.datetime]): Start date and time.
        to_date (Union[None, Unset, datetime.datetime]): End date and time.
    """

    from_date: Union[None, Unset, datetime.datetime] = UNSET
    to_date: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_date: Union[None, Unset, str]
        if isinstance(self.from_date, Unset):
            from_date = UNSET
        elif isinstance(self.from_date, datetime.datetime):
            from_date = self.from_date.isoformat()
        else:
            from_date = self.from_date

        to_date: Union[None, Unset, str]
        if isinstance(self.to_date, Unset):
            to_date = UNSET
        elif isinstance(self.to_date, datetime.datetime):
            to_date = self.to_date.isoformat()
        else:
            to_date = self.to_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_date is not UNSET:
            field_dict["fromDate"] = from_date
        if to_date is not UNSET:
            field_dict["toDate"] = to_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_from_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                from_date_type_0 = isoparse(data)

                return from_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        from_date = _parse_from_date(d.pop("fromDate", UNSET))

        def _parse_to_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                to_date_type_0 = isoparse(data)

                return to_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        to_date = _parse_to_date(d.pop("toDate", UNSET))

        invoice_period = cls(
            from_date=from_date,
            to_date=to_date,
        )

        invoice_period.additional_properties = d
        return invoice_period

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
