import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.pulse_configuration_status import PulseConfigurationStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PulseConfiguration")


@_attrs_define
class PulseConfiguration:
    """
    Attributes:
        is_company_mapping_enabled (bool): Indicates whether company management in VCSP Pulse is enabled.
        is_license_management_enabled (bool): Indicates whether license management in VCSP Pulse is enabled.
        is_pushing_new_companies_to_pulse_enabled (bool): Indicates whether a VCSP Pulse tenant must be created for each
            new company.
        token (Union[Unset, str]): VCSP Pulse authentication token.
        status (Union[Unset, PulseConfigurationStatus]): Status of VCSP Pulse configuration.
        status_message (Union[Unset, str]): Status message.
        last_update_date (Union[Unset, datetime.datetime]): Date of the last VCSP Pulse integration update.
        token_expiration_date (Union[Unset, datetime.datetime]): Date when the VCSP Pulse Portal connection token
            expires.
    """

    is_company_mapping_enabled: bool
    is_license_management_enabled: bool
    is_pushing_new_companies_to_pulse_enabled: bool
    token: Union[Unset, str] = UNSET
    status: Union[Unset, PulseConfigurationStatus] = UNSET
    status_message: Union[Unset, str] = UNSET
    last_update_date: Union[Unset, datetime.datetime] = UNSET
    token_expiration_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_company_mapping_enabled = self.is_company_mapping_enabled

        is_license_management_enabled = self.is_license_management_enabled

        is_pushing_new_companies_to_pulse_enabled = self.is_pushing_new_companies_to_pulse_enabled

        token = self.token

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_message = self.status_message

        last_update_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_update_date, Unset):
            last_update_date = self.last_update_date.isoformat()

        token_expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.token_expiration_date, Unset):
            token_expiration_date = self.token_expiration_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isCompanyMappingEnabled": is_company_mapping_enabled,
                "isLicenseManagementEnabled": is_license_management_enabled,
                "isPushingNewCompaniesToPulseEnabled": is_pushing_new_companies_to_pulse_enabled,
            }
        )
        if token is not UNSET:
            field_dict["token"] = token
        if status is not UNSET:
            field_dict["status"] = status
        if status_message is not UNSET:
            field_dict["statusMessage"] = status_message
        if last_update_date is not UNSET:
            field_dict["lastUpdateDate"] = last_update_date
        if token_expiration_date is not UNSET:
            field_dict["tokenExpirationDate"] = token_expiration_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_company_mapping_enabled = d.pop("isCompanyMappingEnabled")

        is_license_management_enabled = d.pop("isLicenseManagementEnabled")

        is_pushing_new_companies_to_pulse_enabled = d.pop("isPushingNewCompaniesToPulseEnabled")

        token = d.pop("token", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, PulseConfigurationStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PulseConfigurationStatus(_status)

        status_message = d.pop("statusMessage", UNSET)

        _last_update_date = d.pop("lastUpdateDate", UNSET)
        last_update_date: Union[Unset, datetime.datetime]
        if isinstance(_last_update_date, Unset):
            last_update_date = UNSET
        else:
            last_update_date = isoparse(_last_update_date)

        _token_expiration_date = d.pop("tokenExpirationDate", UNSET)
        token_expiration_date: Union[Unset, datetime.datetime]
        if isinstance(_token_expiration_date, Unset):
            token_expiration_date = UNSET
        else:
            token_expiration_date = isoparse(_token_expiration_date)

        pulse_configuration = cls(
            is_company_mapping_enabled=is_company_mapping_enabled,
            is_license_management_enabled=is_license_management_enabled,
            is_pushing_new_companies_to_pulse_enabled=is_pushing_new_companies_to_pulse_enabled,
            token=token,
            status=status,
            status_message=status_message,
            last_update_date=last_update_date,
            token_expiration_date=token_expiration_date,
        )

        pulse_configuration.additional_properties = d
        return pulse_configuration

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
