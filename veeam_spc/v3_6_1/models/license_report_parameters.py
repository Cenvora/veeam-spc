import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.license_report_interval import LicenseReportInterval


T = TypeVar("T", bound="LicenseReportParameters")


@_attrs_define
class LicenseReportParameters:
    """
    Attributes:
        report_id (int): Report ID.
        organization_name (str): Name of a report owner organization.
        organization_uid (UUID): UID assigned to a report owner organization.
        license_company_name (str): Name of a licensee organization.
        generation_date (datetime.date): Date of report generation.
        report_interval (LicenseReportInterval):
    """

    report_id: int
    organization_name: str
    organization_uid: UUID
    license_company_name: str
    generation_date: datetime.date
    report_interval: "LicenseReportInterval"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        report_id = self.report_id

        organization_name = self.organization_name

        organization_uid = str(self.organization_uid)

        license_company_name = self.license_company_name

        generation_date = self.generation_date.isoformat()

        report_interval = self.report_interval.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reportId": report_id,
                "organizationName": organization_name,
                "organizationUid": organization_uid,
                "licenseCompanyName": license_company_name,
                "generationDate": generation_date,
                "reportInterval": report_interval,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.license_report_interval import LicenseReportInterval

        d = dict(src_dict)
        report_id = d.pop("reportId")

        organization_name = d.pop("organizationName")

        organization_uid = UUID(d.pop("organizationUid"))

        license_company_name = d.pop("licenseCompanyName")

        generation_date = isoparse(d.pop("generationDate")).date()

        report_interval = LicenseReportInterval.from_dict(d.pop("reportInterval"))

        license_report_parameters = cls(
            report_id=report_id,
            organization_name=organization_name,
            organization_uid=organization_uid,
            license_company_name=license_company_name,
            generation_date=generation_date,
            report_interval=report_interval,
        )

        license_report_parameters.additional_properties = d
        return license_report_parameters

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
