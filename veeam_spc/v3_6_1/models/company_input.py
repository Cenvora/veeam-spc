from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
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
    Attributes:
        organization_input (OrganizationInput):
        owner_credentials (OwnerCredentials):
        reseller_uid (Union[None, UUID, Unset]): UID assigned to a reseller that manages the company.
        subscription_plan_uid (Union[None, UUID, Unset]): UID assigned to a company subscription plan.
        is_rest_access_enabled (Union[Unset, bool]): Defines whether access to REST API is enabled for a reseller.
            Default: False.
        is_alarm_detect_enabled (Union[Unset, bool]): Defines whether a company must receive notifications about alarms
            that were triggered for this company. Default: False.
        company_services (Union[Unset, CompanyServices]):
    """

    organization_input: "OrganizationInput"
    owner_credentials: "OwnerCredentials"
    reseller_uid: Union[None, UUID, Unset] = UNSET
    subscription_plan_uid: Union[None, UUID, Unset] = UNSET
    is_rest_access_enabled: Union[Unset, bool] = False
    is_alarm_detect_enabled: Union[Unset, bool] = False
    company_services: Union[Unset, "CompanyServices"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_input = self.organization_input.to_dict()

        owner_credentials = self.owner_credentials.to_dict()

        reseller_uid: Union[None, Unset, str]
        if isinstance(self.reseller_uid, Unset):
            reseller_uid = UNSET
        elif isinstance(self.reseller_uid, UUID):
            reseller_uid = str(self.reseller_uid)
        else:
            reseller_uid = self.reseller_uid

        subscription_plan_uid: Union[None, Unset, str]
        if isinstance(self.subscription_plan_uid, Unset):
            subscription_plan_uid = UNSET
        elif isinstance(self.subscription_plan_uid, UUID):
            subscription_plan_uid = str(self.subscription_plan_uid)
        else:
            subscription_plan_uid = self.subscription_plan_uid

        is_rest_access_enabled = self.is_rest_access_enabled

        is_alarm_detect_enabled = self.is_alarm_detect_enabled

        company_services: Union[Unset, dict[str, Any]] = UNSET
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

        def _parse_reseller_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reseller_uid_type_0 = UUID(data)

                return reseller_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        reseller_uid = _parse_reseller_uid(d.pop("resellerUid", UNSET))

        def _parse_subscription_plan_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subscription_plan_uid_type_0 = UUID(data)

                return subscription_plan_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        subscription_plan_uid = _parse_subscription_plan_uid(d.pop("subscriptionPlanUid", UNSET))

        is_rest_access_enabled = d.pop("isRestAccessEnabled", UNSET)

        is_alarm_detect_enabled = d.pop("isAlarmDetectEnabled", UNSET)

        _company_services = d.pop("companyServices", UNSET)
        company_services: Union[Unset, CompanyServices]
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
