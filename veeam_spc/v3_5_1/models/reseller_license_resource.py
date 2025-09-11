from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reseller_license_resource_pulse_configuration_status import (
    ResellerLicenseResourcePulseConfigurationStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResellerLicenseResource")


@_attrs_define
class ResellerLicenseResource:
    """
    Attributes:
        reseller_uid (Union[Unset, UUID]): UID assigned to a reseller.
        pulse_configuration_status (Union[Unset, ResellerLicenseResourcePulseConfigurationStatus]): Status of VCSP Pulse
            configuration.
        pulse_configuration_status_message (Union[Unset, str]): Status message.
        pulse_auto_connect_with_provider_token (Union[Unset, bool]): Indicates whether reseller is forced to connect to
            VCSP Pulse using a provider token. Default: False.
        is_license_management_enabled (Union[Unset, bool]): Indicates whether license management is enabled for a
            reseller. Default: False.
        license_contract_id (Union[Unset, str]): ID assigned to a license rental agreement contract.
        license_points_quota (Union[Unset, int]): Number of license points available to a reseller.
        is_license_points_quota_unlimited (Union[Unset, bool]): Indicates whether a reseller can use an unlimited number
            of license points. Default: True.
        license_points_usage (Union[Unset, float]): Number of license points used by a reseller.
        is_creating_new_companies_to_pulse_enabled (Union[Unset, bool]): Indicates whether a reseller can add new
            companies to VCSP Pulse.
    """

    reseller_uid: Union[Unset, UUID] = UNSET
    pulse_configuration_status: Union[Unset, ResellerLicenseResourcePulseConfigurationStatus] = UNSET
    pulse_configuration_status_message: Union[Unset, str] = UNSET
    pulse_auto_connect_with_provider_token: Union[Unset, bool] = False
    is_license_management_enabled: Union[Unset, bool] = False
    license_contract_id: Union[Unset, str] = UNSET
    license_points_quota: Union[Unset, int] = UNSET
    is_license_points_quota_unlimited: Union[Unset, bool] = True
    license_points_usage: Union[Unset, float] = UNSET
    is_creating_new_companies_to_pulse_enabled: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reseller_uid: Union[Unset, str] = UNSET
        if not isinstance(self.reseller_uid, Unset):
            reseller_uid = str(self.reseller_uid)

        pulse_configuration_status: Union[Unset, str] = UNSET
        if not isinstance(self.pulse_configuration_status, Unset):
            pulse_configuration_status = self.pulse_configuration_status.value

        pulse_configuration_status_message = self.pulse_configuration_status_message

        pulse_auto_connect_with_provider_token = self.pulse_auto_connect_with_provider_token

        is_license_management_enabled = self.is_license_management_enabled

        license_contract_id = self.license_contract_id

        license_points_quota = self.license_points_quota

        is_license_points_quota_unlimited = self.is_license_points_quota_unlimited

        license_points_usage = self.license_points_usage

        is_creating_new_companies_to_pulse_enabled = self.is_creating_new_companies_to_pulse_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reseller_uid is not UNSET:
            field_dict["resellerUid"] = reseller_uid
        if pulse_configuration_status is not UNSET:
            field_dict["pulseConfigurationStatus"] = pulse_configuration_status
        if pulse_configuration_status_message is not UNSET:
            field_dict["pulseConfigurationStatusMessage"] = pulse_configuration_status_message
        if pulse_auto_connect_with_provider_token is not UNSET:
            field_dict["pulseAutoConnectWithProviderToken"] = pulse_auto_connect_with_provider_token
        if is_license_management_enabled is not UNSET:
            field_dict["isLicenseManagementEnabled"] = is_license_management_enabled
        if license_contract_id is not UNSET:
            field_dict["licenseContractId"] = license_contract_id
        if license_points_quota is not UNSET:
            field_dict["licensePointsQuota"] = license_points_quota
        if is_license_points_quota_unlimited is not UNSET:
            field_dict["isLicensePointsQuotaUnlimited"] = is_license_points_quota_unlimited
        if license_points_usage is not UNSET:
            field_dict["licensePointsUsage"] = license_points_usage
        if is_creating_new_companies_to_pulse_enabled is not UNSET:
            field_dict["isCreatingNewCompaniesToPulseEnabled"] = is_creating_new_companies_to_pulse_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _reseller_uid = d.pop("resellerUid", UNSET)
        reseller_uid: Union[Unset, UUID]
        if isinstance(_reseller_uid, Unset):
            reseller_uid = UNSET
        else:
            reseller_uid = UUID(_reseller_uid)

        _pulse_configuration_status = d.pop("pulseConfigurationStatus", UNSET)
        pulse_configuration_status: Union[Unset, ResellerLicenseResourcePulseConfigurationStatus]
        if isinstance(_pulse_configuration_status, Unset):
            pulse_configuration_status = UNSET
        else:
            pulse_configuration_status = ResellerLicenseResourcePulseConfigurationStatus(_pulse_configuration_status)

        pulse_configuration_status_message = d.pop("pulseConfigurationStatusMessage", UNSET)

        pulse_auto_connect_with_provider_token = d.pop("pulseAutoConnectWithProviderToken", UNSET)

        is_license_management_enabled = d.pop("isLicenseManagementEnabled", UNSET)

        license_contract_id = d.pop("licenseContractId", UNSET)

        license_points_quota = d.pop("licensePointsQuota", UNSET)

        is_license_points_quota_unlimited = d.pop("isLicensePointsQuotaUnlimited", UNSET)

        license_points_usage = d.pop("licensePointsUsage", UNSET)

        is_creating_new_companies_to_pulse_enabled = d.pop("isCreatingNewCompaniesToPulseEnabled", UNSET)

        reseller_license_resource = cls(
            reseller_uid=reseller_uid,
            pulse_configuration_status=pulse_configuration_status,
            pulse_configuration_status_message=pulse_configuration_status_message,
            pulse_auto_connect_with_provider_token=pulse_auto_connect_with_provider_token,
            is_license_management_enabled=is_license_management_enabled,
            license_contract_id=license_contract_id,
            license_points_quota=license_points_quota,
            is_license_points_quota_unlimited=is_license_points_quota_unlimited,
            license_points_usage=license_points_usage,
            is_creating_new_companies_to_pulse_enabled=is_creating_new_companies_to_pulse_enabled,
        )

        reseller_license_resource.additional_properties = d
        return reseller_license_resource

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
