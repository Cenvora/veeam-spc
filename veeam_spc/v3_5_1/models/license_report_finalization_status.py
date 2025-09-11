from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.license_report_finalization_status_report_approval_status import (
    LicenseReportFinalizationStatusReportApprovalStatus,
)

T = TypeVar("T", bound="LicenseReportFinalizationStatus")


@_attrs_define
class LicenseReportFinalizationStatus:
    """
    Attributes:
        report_approval_status (LicenseReportFinalizationStatusReportApprovalStatus): Report finalization status.
        message (str): Message.
    """

    report_approval_status: LicenseReportFinalizationStatusReportApprovalStatus
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        report_approval_status = self.report_approval_status.value

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reportApprovalStatus": report_approval_status,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        report_approval_status = LicenseReportFinalizationStatusReportApprovalStatus(d.pop("reportApprovalStatus"))

        message = d.pop("message")

        license_report_finalization_status = cls(
            report_approval_status=report_approval_status,
            message=message,
        )

        license_report_finalization_status.additional_properties = d
        return license_report_finalization_status

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
