from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_services import CompanyServices
    from ..models.organization_input import OrganizationInput
    from ..models.owner_credentials import OwnerCredentials


T = TypeVar("T", bound="CompanyInput")


@_attrs_define
class CompanyInput:
    """
    Example:
        {'resellerUid': 'ae61e533-82c7-4cb6-a030-78ae589cf49d', 'organizationInput': {'name': 'Alpha', 'alias': 'alpha',
            'taxId': '643-70-9745', 'legalName': 'Alpha Holdings, Inc.', 'email': 's.smith@alpha.com', 'phone':
            '906-284-7082', 'country': 1, 'state': 22, 'countryName': 'USA', 'regionName': 'Midwest', 'city': 'Marquette',
            'street': '4493 Railroad Street', 'locationAdmin0Code': None, 'locationAdmin1Code': None, 'locationAdmin2Code':
            None, 'notes': None, 'zipCode': '49855', 'domain': 'alpha.com', 'website': 'www.alpha.com', 'veeamTenantId':
            None, 'companyId': None}, 'subscriptionPlanUid': None, 'isRestAccessEnabled': True, 'isAlarmDetectEnabled':
            False, 'companyServices': {'hostedServices': {'isVbPublicCloudManagementEnabled': False}, 'remoteServices':
            {'isBackupResourcesEnabled': True, 'backupAgentsManagement': None, 'backupServersManagement': None,
            'vb365ServersManagement': None, 'isVbPublicCloudManagementEnabled': False}}, 'ownerCredentials': {'userName':
            'alphaowner', 'password': 'Password1'}}

    Attributes:
        organization_input (OrganizationInput):
        owner_credentials (OwnerCredentials):
        reseller_uid (UUID | Unset): UID assigned to a reseller that manages the company.
        subscription_plan_uid (UUID | Unset): UID assigned to a company subscription plan.
        is_rest_access_enabled (bool | Unset): Defines whether access to REST API is enabled for a reseller. Default:
            False.
        is_alarm_detect_enabled (bool | Unset): Indicates whether alarms must be triggered for a company. Default:
            False.
        company_services (CompanyServices | Unset):
    """

    organization_input: OrganizationInput
    owner_credentials: OwnerCredentials
    reseller_uid: UUID | Unset = UNSET
    subscription_plan_uid: UUID | Unset = UNSET
    is_rest_access_enabled: bool | Unset = False
    is_alarm_detect_enabled: bool | Unset = False
    company_services: CompanyServices | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_input = self.organization_input.to_dict()

        owner_credentials = self.owner_credentials.to_dict()

        reseller_uid: str | Unset = UNSET
        if not isinstance(self.reseller_uid, Unset):
            reseller_uid = str(self.reseller_uid)

        subscription_plan_uid: str | Unset = UNSET
        if not isinstance(self.subscription_plan_uid, Unset):
            subscription_plan_uid = str(self.subscription_plan_uid)

        is_rest_access_enabled = self.is_rest_access_enabled

        is_alarm_detect_enabled = self.is_alarm_detect_enabled

        company_services: dict[str, Any] | Unset = UNSET
        if not isinstance(self.company_services, Unset):
            company_services = self.company_services.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organizationInput": organization_input,
                "ownerCredentials": owner_credentials,
            }
        )
        if reseller_uid is not UNSET:
            field_dict["resellerUid"] = reseller_uid
        if subscription_plan_uid is not UNSET:
            field_dict["subscriptionPlanUid"] = subscription_plan_uid
        if is_rest_access_enabled is not UNSET:
            field_dict["isRestAccessEnabled"] = is_rest_access_enabled
        if is_alarm_detect_enabled is not UNSET:
            field_dict["isAlarmDetectEnabled"] = is_alarm_detect_enabled
        if company_services is not UNSET:
            field_dict["companyServices"] = company_services

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_services import CompanyServices
        from ..models.organization_input import OrganizationInput
        from ..models.owner_credentials import OwnerCredentials

        d = dict(src_dict)
        organization_input = OrganizationInput.from_dict(d.pop("organizationInput"))

        owner_credentials = OwnerCredentials.from_dict(d.pop("ownerCredentials"))

        _reseller_uid = d.pop("resellerUid", UNSET)
        reseller_uid: UUID | Unset
        if isinstance(_reseller_uid, Unset):
            reseller_uid = UNSET
        else:
            reseller_uid = UUID(_reseller_uid)

        _subscription_plan_uid = d.pop("subscriptionPlanUid", UNSET)
        subscription_plan_uid: UUID | Unset
        if isinstance(_subscription_plan_uid, Unset):
            subscription_plan_uid = UNSET
        else:
            subscription_plan_uid = UUID(_subscription_plan_uid)

        is_rest_access_enabled = d.pop("isRestAccessEnabled", UNSET)

        is_alarm_detect_enabled = d.pop("isAlarmDetectEnabled", UNSET)

        _company_services = d.pop("companyServices", UNSET)
        company_services: CompanyServices | Unset
        if isinstance(_company_services, Unset):
            company_services = UNSET
        else:
            company_services = CompanyServices.from_dict(_company_services)

        company_input = cls(
            organization_input=organization_input,
            owner_credentials=owner_credentials,
            reseller_uid=reseller_uid,
            subscription_plan_uid=subscription_plan_uid,
            is_rest_access_enabled=is_rest_access_enabled,
            is_alarm_detect_enabled=is_alarm_detect_enabled,
            company_services=company_services,
        )

        company_input.additional_properties = d
        return company_input

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
