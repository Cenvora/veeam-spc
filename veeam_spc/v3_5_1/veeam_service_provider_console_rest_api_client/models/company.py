from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.company_permissions_item import CompanyPermissionsItem
from ..models.company_status import CompanyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_services import CompanyServices
    from ..models.embedded_for_organization_children_type_0 import EmbeddedForOrganizationChildrenType0


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
        reseller_uid (Union[None, UUID, Unset]): UID assigned to a reseller that manages the company.
        subscription_plan_uid (Union[None, UUID, Unset]): UID assigned to a company subscription plan.
        permissions (Union[Unset, list[CompanyPermissionsItem]]): Array of the Veeam Service Provider Console components
            that a company can access.
        is_alarm_detect_enabled (Union[Unset, bool]): Indicates whether a company must receive notifications about
            alarms that were triggered for this company. Default: False.
        login_url (Union[None, Unset, str]): Company portal URL.
            > Can be configured by performing the `ReplaceCompanyLoginUrl` operation.'
        field_embedded (Union['EmbeddedForOrganizationChildrenType0', None, Unset]): Resource representation of the
            related organization entity.
    """

    company_services: "CompanyServices"
    instance_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    status: Union[Unset, CompanyStatus] = CompanyStatus.ACTIVE
    reseller_uid: Union[None, UUID, Unset] = UNSET
    subscription_plan_uid: Union[None, UUID, Unset] = UNSET
    permissions: Union[Unset, list[CompanyPermissionsItem]] = UNSET
    is_alarm_detect_enabled: Union[Unset, bool] = False
    login_url: Union[None, Unset, str] = UNSET
    field_embedded: Union["EmbeddedForOrganizationChildrenType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.embedded_for_organization_children_type_0 import EmbeddedForOrganizationChildrenType0

        company_services = self.company_services.to_dict()

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

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

        permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.value
                permissions.append(permissions_item)

        is_alarm_detect_enabled = self.is_alarm_detect_enabled

        login_url: Union[None, Unset, str]
        if isinstance(self.login_url, Unset):
            login_url = UNSET
        else:
            login_url = self.login_url

        field_embedded: Union[None, Unset, dict[str, Any]]
        if isinstance(self.field_embedded, Unset):
            field_embedded = UNSET
        elif isinstance(self.field_embedded, EmbeddedForOrganizationChildrenType0):
            field_embedded = self.field_embedded.to_dict()
        else:
            field_embedded = self.field_embedded

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
        from ..models.embedded_for_organization_children_type_0 import EmbeddedForOrganizationChildrenType0

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

        permissions = []
        _permissions = d.pop("permissions", UNSET)
        for permissions_item_data in _permissions or []:
            permissions_item = CompanyPermissionsItem(permissions_item_data)

            permissions.append(permissions_item)

        is_alarm_detect_enabled = d.pop("isAlarmDetectEnabled", UNSET)

        def _parse_login_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        login_url = _parse_login_url(d.pop("loginUrl", UNSET))

        def _parse_field_embedded(data: object) -> Union["EmbeddedForOrganizationChildrenType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_embedded_for_organization_children_type_0 = (
                    EmbeddedForOrganizationChildrenType0.from_dict(data)
                )

                return componentsschemas_embedded_for_organization_children_type_0
            except:  # noqa: E722
                pass
            return cast(Union["EmbeddedForOrganizationChildrenType0", None, Unset], data)

        field_embedded = _parse_field_embedded(d.pop("_embedded", UNSET))

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
