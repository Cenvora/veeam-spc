from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.company_permissions_item import CompanyPermissionsItem
from ..models.company_status import CompanyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_services import CompanyServices
    from ..models.embedded_for_organization_children import EmbeddedForOrganizationChildren


T = TypeVar("T", bound="Company")


@_attrs_define
class Company:
    """
    Attributes:
        company_services (CompanyServices):
        instance_uid (Union[Unset, UUID]): UID assigned to a company.
        name (Union[Unset, str]): Name of a company.
            > Can be changed using the `PatchOrganization` operation.
        status (Union[Unset, CompanyStatus]): Status of a service provider. You can set the `Active` or `Disabled` value
            using the PATCH method. Default: CompanyStatus.ACTIVE.
        reseller_uid (Union[Unset, UUID]): UID assigned to a reseller that manages the company.
        subscription_plan_uid (Union[Unset, UUID]): UID assigned to a company subscription plan.
        permissions (Union[Unset, list[CompanyPermissionsItem]]): Array of the Veeam Service Provider Console components
            that a company can access.
        is_alarm_detect_enabled (Union[Unset, bool]): Indicates whether a company must receive notifications about
            alarms that were triggered for this company. Default: False.
        login_url (Union[Unset, str]): Company portal URL.
            > Can be configured by performing the `ReplaceCompanyLoginUrl` operation.'
        field_embedded (Union[Unset, EmbeddedForOrganizationChildren]): Resource representation of the related
            organization entity.
    """

    company_services: "CompanyServices"
    instance_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    status: Union[Unset, CompanyStatus] = CompanyStatus.ACTIVE
    reseller_uid: Union[Unset, UUID] = UNSET
    subscription_plan_uid: Union[Unset, UUID] = UNSET
    permissions: Union[Unset, list[CompanyPermissionsItem]] = UNSET
    is_alarm_detect_enabled: Union[Unset, bool] = False
    login_url: Union[Unset, str] = UNSET
    field_embedded: Union[Unset, "EmbeddedForOrganizationChildren"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_services = self.company_services.to_dict()

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        reseller_uid: Union[Unset, str] = UNSET
        if not isinstance(self.reseller_uid, Unset):
            reseller_uid = str(self.reseller_uid)

        subscription_plan_uid: Union[Unset, str] = UNSET
        if not isinstance(self.subscription_plan_uid, Unset):
            subscription_plan_uid = str(self.subscription_plan_uid)

        permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.value
                permissions.append(permissions_item)

        is_alarm_detect_enabled = self.is_alarm_detect_enabled

        login_url = self.login_url

        field_embedded: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_embedded, Unset):
            field_embedded = self.field_embedded.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyServices": company_services,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if reseller_uid is not UNSET:
            field_dict["resellerUid"] = reseller_uid
        if subscription_plan_uid is not UNSET:
            field_dict["subscriptionPlanUid"] = subscription_plan_uid
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if is_alarm_detect_enabled is not UNSET:
            field_dict["isAlarmDetectEnabled"] = is_alarm_detect_enabled
        if login_url is not UNSET:
            field_dict["loginUrl"] = login_url
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_services import CompanyServices
        from ..models.embedded_for_organization_children import EmbeddedForOrganizationChildren

        d = dict(src_dict)
        company_services = CompanyServices.from_dict(d.pop("companyServices"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CompanyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CompanyStatus(_status)

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
        for permissions_item_data in _permissions or []:
            permissions_item = CompanyPermissionsItem(permissions_item_data)

            permissions.append(permissions_item)

        is_alarm_detect_enabled = d.pop("isAlarmDetectEnabled", UNSET)

        login_url = d.pop("loginUrl", UNSET)

        _field_embedded = d.pop("_embedded", UNSET)
        field_embedded: Union[Unset, EmbeddedForOrganizationChildren]
        if isinstance(_field_embedded, Unset):
            field_embedded = UNSET
        else:
            field_embedded = EmbeddedForOrganizationChildren.from_dict(_field_embedded)

        company = cls(
            company_services=company_services,
            instance_uid=instance_uid,
            name=name,
            status=status,
            reseller_uid=reseller_uid,
            subscription_plan_uid=subscription_plan_uid,
            permissions=permissions,
            is_alarm_detect_enabled=is_alarm_detect_enabled,
            login_url=login_url,
            field_embedded=field_embedded,
        )

        company.additional_properties = d
        return company

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
