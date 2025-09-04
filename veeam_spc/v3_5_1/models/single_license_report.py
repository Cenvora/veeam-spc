from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.single_license_report_report_status import SingleLicenseReportReportStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.license_report_appendix import LicenseReportAppendix
    from ..models.license_report_parameters import LicenseReportParameters
    from ..models.license_report_summary import LicenseReportSummary
    from ..models.organization_license_usage import OrganizationLicenseUsage
    from ..models.organization_usage_of_licenses_with_same_support_id import (
        OrganizationUsageOfLicensesWithSameSupportId,
    )


T = TypeVar("T", bound="SingleLicenseReport")


@_attrs_define
class SingleLicenseReport:
    """
    Attributes:
        report_status (Union[Unset, SingleLicenseReportReportStatus]): License usage report status.
        report_paremeters (Union[Unset, LicenseReportParameters]):
        report_summary (Union[Unset, LicenseReportSummary]):
        organizations_usage (Union[Unset, list['OrganizationLicenseUsage']]): Number of license points used by managed
            organizations.
        not_collected_cloud_servers (Union[Unset, list[str]]): Array of Veeam Cloud Connect servers from which Veeam
            Service Provider Console could not collect the license usage data.
        cloned_cloud_servers (Union[Unset, list[str]]): Array of cloned Veeam Cloud Connect servers.
        unsupported_cloud_servers (Union[Unset, list[str]]): Array of unsupported Veeam Cloud Connect servers.
        usage_details (Union[Unset, list['OrganizationUsageOfLicensesWithSameSupportId']]): Usage of licenses with the
            same support ID.
        appendices (Union[Unset, list['LicenseReportAppendix']]): Usage of licenses issued to organizations other than
            report owner.
    """

    report_status: Union[Unset, SingleLicenseReportReportStatus] = UNSET
    report_paremeters: Union[Unset, "LicenseReportParameters"] = UNSET
    report_summary: Union[Unset, "LicenseReportSummary"] = UNSET
    organizations_usage: Union[Unset, list["OrganizationLicenseUsage"]] = UNSET
    not_collected_cloud_servers: Union[Unset, list[str]] = UNSET
    cloned_cloud_servers: Union[Unset, list[str]] = UNSET
    unsupported_cloud_servers: Union[Unset, list[str]] = UNSET
    usage_details: Union[Unset, list["OrganizationUsageOfLicensesWithSameSupportId"]] = UNSET
    appendices: Union[Unset, list["LicenseReportAppendix"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        report_status: Union[Unset, str] = UNSET
        if not isinstance(self.report_status, Unset):
            report_status = self.report_status.value

        report_paremeters: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.report_paremeters, Unset):
            report_paremeters = self.report_paremeters.to_dict()

        report_summary: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.report_summary, Unset):
            report_summary = self.report_summary.to_dict()

        organizations_usage: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.organizations_usage, Unset):
            organizations_usage = []
            for organizations_usage_item_data in self.organizations_usage:
                organizations_usage_item = organizations_usage_item_data.to_dict()
                organizations_usage.append(organizations_usage_item)

        not_collected_cloud_servers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.not_collected_cloud_servers, Unset):
            not_collected_cloud_servers = self.not_collected_cloud_servers

        cloned_cloud_servers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cloned_cloud_servers, Unset):
            cloned_cloud_servers = self.cloned_cloud_servers

        unsupported_cloud_servers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.unsupported_cloud_servers, Unset):
            unsupported_cloud_servers = self.unsupported_cloud_servers

        usage_details: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.usage_details, Unset):
            usage_details = []
            for usage_details_item_data in self.usage_details:
                usage_details_item = usage_details_item_data.to_dict()
                usage_details.append(usage_details_item)

        appendices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.appendices, Unset):
            appendices = []
            for appendices_item_data in self.appendices:
                appendices_item = appendices_item_data.to_dict()
                appendices.append(appendices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if report_status is not UNSET:
            field_dict["reportStatus"] = report_status
        if report_paremeters is not UNSET:
            field_dict["reportParemeters"] = report_paremeters
        if report_summary is not UNSET:
            field_dict["reportSummary"] = report_summary
        if organizations_usage is not UNSET:
            field_dict["organizationsUsage"] = organizations_usage
        if not_collected_cloud_servers is not UNSET:
            field_dict["notCollectedCloudServers"] = not_collected_cloud_servers
        if cloned_cloud_servers is not UNSET:
            field_dict["clonedCloudServers"] = cloned_cloud_servers
        if unsupported_cloud_servers is not UNSET:
            field_dict["unsupportedCloudServers"] = unsupported_cloud_servers
        if usage_details is not UNSET:
            field_dict["usageDetails"] = usage_details
        if appendices is not UNSET:
            field_dict["appendices"] = appendices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.license_report_appendix import LicenseReportAppendix
        from ..models.license_report_parameters import LicenseReportParameters
        from ..models.license_report_summary import LicenseReportSummary
        from ..models.organization_license_usage import OrganizationLicenseUsage
        from ..models.organization_usage_of_licenses_with_same_support_id import (
            OrganizationUsageOfLicensesWithSameSupportId,
        )

        d = dict(src_dict)
        _report_status = d.pop("reportStatus", UNSET)
        report_status: Union[Unset, SingleLicenseReportReportStatus]
        if isinstance(_report_status, Unset):
            report_status = UNSET
        else:
            report_status = SingleLicenseReportReportStatus(_report_status)

        _report_paremeters = d.pop("reportParemeters", UNSET)
        report_paremeters: Union[Unset, LicenseReportParameters]
        if isinstance(_report_paremeters, Unset):
            report_paremeters = UNSET
        else:
            report_paremeters = LicenseReportParameters.from_dict(_report_paremeters)

        _report_summary = d.pop("reportSummary", UNSET)
        report_summary: Union[Unset, LicenseReportSummary]
        if isinstance(_report_summary, Unset):
            report_summary = UNSET
        else:
            report_summary = LicenseReportSummary.from_dict(_report_summary)

        organizations_usage = []
        _organizations_usage = d.pop("organizationsUsage", UNSET)
        for organizations_usage_item_data in _organizations_usage or []:
            organizations_usage_item = OrganizationLicenseUsage.from_dict(organizations_usage_item_data)

            organizations_usage.append(organizations_usage_item)

        not_collected_cloud_servers = cast(list[str], d.pop("notCollectedCloudServers", UNSET))

        cloned_cloud_servers = cast(list[str], d.pop("clonedCloudServers", UNSET))

        unsupported_cloud_servers = cast(list[str], d.pop("unsupportedCloudServers", UNSET))

        usage_details = []
        _usage_details = d.pop("usageDetails", UNSET)
        for usage_details_item_data in _usage_details or []:
            usage_details_item = OrganizationUsageOfLicensesWithSameSupportId.from_dict(usage_details_item_data)

            usage_details.append(usage_details_item)

        appendices = []
        _appendices = d.pop("appendices", UNSET)
        for appendices_item_data in _appendices or []:
            appendices_item = LicenseReportAppendix.from_dict(appendices_item_data)

            appendices.append(appendices_item)

        single_license_report = cls(
            report_status=report_status,
            report_paremeters=report_paremeters,
            report_summary=report_summary,
            organizations_usage=organizations_usage,
            not_collected_cloud_servers=not_collected_cloud_servers,
            cloned_cloud_servers=cloned_cloud_servers,
            unsupported_cloud_servers=unsupported_cloud_servers,
            usage_details=usage_details,
            appendices=appendices,
        )

        single_license_report.additional_properties = d
        return single_license_report

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
