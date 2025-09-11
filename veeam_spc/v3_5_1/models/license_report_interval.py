import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="LicenseReportInterval")


@_attrs_define
class LicenseReportInterval:
    """
    Attributes:
        start_of_interval (datetime.date): Start date of reporting interval.
        end_of_interval (datetime.date): End date of reporting interval.
    """

    start_of_interval: datetime.date
    end_of_interval: datetime.date
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_of_interval = self.start_of_interval.isoformat()

        end_of_interval = self.end_of_interval.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startOfInterval": start_of_interval,
                "endOfInterval": end_of_interval,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_of_interval = isoparse(d.pop("startOfInterval")).date()

        end_of_interval = isoparse(d.pop("endOfInterval")).date()

        license_report_interval = cls(
            start_of_interval=start_of_interval,
            end_of_interval=end_of_interval,
        )

        license_report_interval.additional_properties = d
        return license_report_interval

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
