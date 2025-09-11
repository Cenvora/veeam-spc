from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.company_permissions_nullable_item import CompanyPermissionsNullableItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_services import CompanyServices
    from ..models.organization_input import OrganizationInput


T = TypeVar("T", bound="CompanyInput")


@_attrs_define
class CompanyInput:
    """
    Attributes:
        organization_input (OrganizationInput):
        reseller_uid (Union[Unset, UUID]): UID assigned to a reseller that manages the company.
        subscription_plan_uid (Union[Unset, UUID]): UID assigned to a company subscription plan.
        permissions (Union[Unset, list[CompanyPermissionsNullableItem]]): Array of the Veeam Service Provider Console
            components that a company can access.
        is_alarm_detect_enabled (Union[Unset, bool]): Defines whether a company must receive notifications about alarms
            that were triggered for this company. Default: False.
        company_services (Union[Unset, CompanyServices]):
    """

    organization_input: "OrganizationInput"
    reseller_uid: Union[Unset, UUID] = UNSET
    subscription_plan_uid: Union[Unset, UUID] = UNSET
    permissions: Union[Unset, list[CompanyPermissionsNullableItem]] = UNSET
    is_alarm_detect_enabled: Union[Unset, bool] = False
    company_services: Union[Unset, "CompanyServices"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_input = self.organization_input.to_dict()

        reseller_uid: Union[Unset, str] = UNSET
        if not isinstance(self.reseller_uid, Unset):
            reseller_uid = str(self.reseller_uid)

        subscription_plan_uid: Union[Unset, str] = UNSET
        if not isinstance(self.subscription_plan_uid, Unset):
            subscription_plan_uid = str(self.subscription_plan_uid)

        permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for componentsschemas_company_permissions_nullable_item_data in self.permissions:
                componentsschemas_company_permissions_nullable_item = (
                    componentsschemas_company_permissions_nullable_item_data.value
                )
                permissions.append(componentsschemas_company_permissions_nullable_item)

        is_alarm_detect_enabled = self.is_alarm_detect_enabled

        company_services: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.company_services, Unset):
            company_services = self.company_services.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organizationInput": organization_input,
            }
        )
        if reseller_uid is not UNSET:
            field_dict["resellerUid"] = reseller_uid
        if subscription_plan_uid is not UNSET:
            field_dict["subscriptionPlanUid"] = subscription_plan_uid
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if is_alarm_detect_enabled is not UNSET:
            field_dict["isAlarmDetectEnabled"] = is_alarm_detect_enabled
        if company_services is not UNSET:
            field_dict["companyServices"] = company_services

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_services import CompanyServices
        from ..models.organization_input import OrganizationInput

        d = dict(src_dict)
        organization_input = OrganizationInput.from_dict(d.pop("organizationInput"))

        _reseller_uid = d.pop("resellerUid", UNSET)
        reseller_uid: Union[Unset, UUID]
        if isinstance(_reseller_uid, Unset):
            reseller_uid = UNSET
        else:
            reseller_uid = UUID(_reseller_uid)

        _subscription_plan_uid = d.pop("subscriptionPlanUid", UNSET)
        subscription_plan_uid: Union[Unset, UUID]
        if isinstance(_subscription_plan_uid, Unset):
            subscription_plan_uid = UNSET
        else:
            subscription_plan_uid = UUID(_subscription_plan_uid)

        permissions = []
        _permissions = d.pop("permissions", UNSET)
        for componentsschemas_company_permissions_nullable_item_data in _permissions or []:
            componentsschemas_company_permissions_nullable_item = CompanyPermissionsNullableItem(
                componentsschemas_company_permissions_nullable_item_data
            )

            permissions.append(componentsschemas_company_permissions_nullable_item)

        is_alarm_detect_enabled = d.pop("isAlarmDetectEnabled", UNSET)

        _company_services = d.pop("companyServices", UNSET)
        company_services: Union[Unset, CompanyServices]
        if isinstance(_company_services, Unset):
            company_services = UNSET
        else:
            company_services = CompanyServices.from_dict(_company_services)

        company_input = cls(
            organization_input=organization_input,
            reseller_uid=reseller_uid,
            subscription_plan_uid=subscription_plan_uid,
            permissions=permissions,
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
