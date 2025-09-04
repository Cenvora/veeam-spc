import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.company_site_resource_cloud_tenant_type import CompanySiteResourceCloudTenantType
from ..models.company_site_resource_gateway_selection_type import CompanySiteResourceGatewaySelectionType
from ..models.company_site_resource_throttling_unit import CompanySiteResourceThrottlingUnit
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.owner_credentials import OwnerCredentials


T = TypeVar("T", bound="CompanySiteResource")


@_attrs_define
class CompanySiteResource:
    """
    Attributes:
        site_uid (UUID): UID assigned to a Veeam Cloud Connect site.
        owner_credentials (OwnerCredentials):
        cloud_tenant_type (Union[Unset, CompanySiteResourceCloudTenantType]): Tenant type in Veeam Cloud Connect.
            Default: CompanySiteResourceCloudTenantType.GENERAL.
        company_uid (Union[Unset, UUID]): UID assigned to a company.
        cloud_tenant_uid (Union[Unset, UUID]): UID assigned to a company tenant.
        v_cloud_organization_uid (Union[Unset, UUID]): UID assigned to a VMware Cloud Director organization.
        last_active (Union[Unset, datetime.datetime]): The last time when a tenant was active.
        lease_expiration_enabled (Union[Unset, bool]): Indicates whether a company account must be disabled
            automatically. Default: False.
        lease_expiration_date (Union[Unset, datetime.datetime]): Date and time when a company account must be disabled.
        description (Union[Unset, str]): Company description.
        throttling_enabled (Union[Unset, bool]): Indicates whether incoming network traffic that will be accepted from a
            company is limited. Default: False.
        throttling_value (Union[Unset, int]): Maximum incoming network traffic bandwidth that will be accepted from a
            company. Default: 1.
        throttling_unit (Union[Unset, CompanySiteResourceThrottlingUnit]): Measurement units of incoming network traffic
            accepted from a company. Default: CompanySiteResourceThrottlingUnit.MBYTEPERSEC.
        max_concurrent_task (Union[Unset, int]): Maximum number of concurrent tasks available to a company. Default: 1.
        backup_protection_enabled (Union[Unset, bool]): Indicates whether deleted backup file protection is enabled.
            Default: False.
        backup_protection_period_days (Union[Unset, int]): Number of days during which deleted backup files must be kept
            in the recycle bin on the Veeam Cloud Connect server. Default: 7.
        gateway_selection_type (Union[Unset, CompanySiteResourceGatewaySelectionType]): Type of cloud gateway selection.
            Default: CompanySiteResourceGatewaySelectionType.STANDALONEGATEWAYS.
        gateway_pools_uids (Union[Unset, list[UUID]]): Collection of UIDs assigned to gateway pools that are allocated
            to a company. If the collection is empty, company will automatically use a standalone gateway.
        is_gateway_failover_enabled (Union[Unset, bool]): Indicates whether a company is allowed to fail over to a cloud
            gateway that is not added to a selected cloud gateway pool. Default: False.
    """

    site_uid: UUID
    owner_credentials: "OwnerCredentials"
    cloud_tenant_type: Union[Unset, CompanySiteResourceCloudTenantType] = CompanySiteResourceCloudTenantType.GENERAL
    company_uid: Union[Unset, UUID] = UNSET
    cloud_tenant_uid: Union[Unset, UUID] = UNSET
    v_cloud_organization_uid: Union[Unset, UUID] = UNSET
    last_active: Union[Unset, datetime.datetime] = UNSET
    lease_expiration_enabled: Union[Unset, bool] = False
    lease_expiration_date: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    throttling_enabled: Union[Unset, bool] = False
    throttling_value: Union[Unset, int] = 1
    throttling_unit: Union[Unset, CompanySiteResourceThrottlingUnit] = CompanySiteResourceThrottlingUnit.MBYTEPERSEC
    max_concurrent_task: Union[Unset, int] = 1
    backup_protection_enabled: Union[Unset, bool] = False
    backup_protection_period_days: Union[Unset, int] = 7
    gateway_selection_type: Union[Unset, CompanySiteResourceGatewaySelectionType] = (
        CompanySiteResourceGatewaySelectionType.STANDALONEGATEWAYS
    )
    gateway_pools_uids: Union[Unset, list[UUID]] = UNSET
    is_gateway_failover_enabled: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_uid = str(self.site_uid)

        owner_credentials = self.owner_credentials.to_dict()

        cloud_tenant_type: Union[Unset, str] = UNSET
        if not isinstance(self.cloud_tenant_type, Unset):
            cloud_tenant_type = self.cloud_tenant_type.value

        company_uid: Union[Unset, str] = UNSET
        if not isinstance(self.company_uid, Unset):
            company_uid = str(self.company_uid)

        cloud_tenant_uid: Union[Unset, str] = UNSET
        if not isinstance(self.cloud_tenant_uid, Unset):
            cloud_tenant_uid = str(self.cloud_tenant_uid)

        v_cloud_organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.v_cloud_organization_uid, Unset):
            v_cloud_organization_uid = str(self.v_cloud_organization_uid)

        last_active: Union[Unset, str] = UNSET
        if not isinstance(self.last_active, Unset):
            last_active = self.last_active.isoformat()

        lease_expiration_enabled = self.lease_expiration_enabled

        lease_expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.lease_expiration_date, Unset):
            lease_expiration_date = self.lease_expiration_date.isoformat()

        description = self.description

        throttling_enabled = self.throttling_enabled

        throttling_value = self.throttling_value

        throttling_unit: Union[Unset, str] = UNSET
        if not isinstance(self.throttling_unit, Unset):
            throttling_unit = self.throttling_unit.value

        max_concurrent_task = self.max_concurrent_task

        backup_protection_enabled = self.backup_protection_enabled

        backup_protection_period_days = self.backup_protection_period_days

        gateway_selection_type: Union[Unset, str] = UNSET
        if not isinstance(self.gateway_selection_type, Unset):
            gateway_selection_type = self.gateway_selection_type.value

        gateway_pools_uids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.gateway_pools_uids, Unset):
            gateway_pools_uids = []
            for gateway_pools_uids_item_data in self.gateway_pools_uids:
                gateway_pools_uids_item = str(gateway_pools_uids_item_data)
                gateway_pools_uids.append(gateway_pools_uids_item)

        is_gateway_failover_enabled = self.is_gateway_failover_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "siteUid": site_uid,
                "ownerCredentials": owner_credentials,
            }
        )
        if cloud_tenant_type is not UNSET:
            field_dict["cloudTenantType"] = cloud_tenant_type
        if company_uid is not UNSET:
            field_dict["companyUid"] = company_uid
        if cloud_tenant_uid is not UNSET:
            field_dict["cloudTenantUid"] = cloud_tenant_uid
        if v_cloud_organization_uid is not UNSET:
            field_dict["vCloudOrganizationUid"] = v_cloud_organization_uid
        if last_active is not UNSET:
            field_dict["lastActive"] = last_active
        if lease_expiration_enabled is not UNSET:
            field_dict["leaseExpirationEnabled"] = lease_expiration_enabled
        if lease_expiration_date is not UNSET:
            field_dict["leaseExpirationDate"] = lease_expiration_date
        if description is not UNSET:
            field_dict["description"] = description
        if throttling_enabled is not UNSET:
            field_dict["throttlingEnabled"] = throttling_enabled
        if throttling_value is not UNSET:
            field_dict["throttlingValue"] = throttling_value
        if throttling_unit is not UNSET:
            field_dict["throttlingUnit"] = throttling_unit
        if max_concurrent_task is not UNSET:
            field_dict["maxConcurrentTask"] = max_concurrent_task
        if backup_protection_enabled is not UNSET:
            field_dict["backupProtectionEnabled"] = backup_protection_enabled
        if backup_protection_period_days is not UNSET:
            field_dict["backupProtectionPeriodDays"] = backup_protection_period_days
        if gateway_selection_type is not UNSET:
            field_dict["gatewaySelectionType"] = gateway_selection_type
        if gateway_pools_uids is not UNSET:
            field_dict["gatewayPoolsUids"] = gateway_pools_uids
        if is_gateway_failover_enabled is not UNSET:
            field_dict["isGatewayFailoverEnabled"] = is_gateway_failover_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.owner_credentials import OwnerCredentials

        d = dict(src_dict)
        site_uid = UUID(d.pop("siteUid"))

        owner_credentials = OwnerCredentials.from_dict(d.pop("ownerCredentials"))

        _cloud_tenant_type = d.pop("cloudTenantType", UNSET)
        cloud_tenant_type: Union[Unset, CompanySiteResourceCloudTenantType]
        if isinstance(_cloud_tenant_type, Unset):
            cloud_tenant_type = UNSET
        else:
            cloud_tenant_type = CompanySiteResourceCloudTenantType(_cloud_tenant_type)

        _company_uid = d.pop("companyUid", UNSET)
        company_uid: Union[Unset, UUID]
        if isinstance(_company_uid, Unset):
            company_uid = UNSET
        else:
            company_uid = UUID(_company_uid)

        _cloud_tenant_uid = d.pop("cloudTenantUid", UNSET)
        cloud_tenant_uid: Union[Unset, UUID]
        if isinstance(_cloud_tenant_uid, Unset):
            cloud_tenant_uid = UNSET
        else:
            cloud_tenant_uid = UUID(_cloud_tenant_uid)

        _v_cloud_organization_uid = d.pop("vCloudOrganizationUid", UNSET)
        v_cloud_organization_uid: Union[Unset, UUID]
        if isinstance(_v_cloud_organization_uid, Unset):
            v_cloud_organization_uid = UNSET
        else:
            v_cloud_organization_uid = UUID(_v_cloud_organization_uid)

        _last_active = d.pop("lastActive", UNSET)
        last_active: Union[Unset, datetime.datetime]
        if isinstance(_last_active, Unset):
            last_active = UNSET
        else:
            last_active = isoparse(_last_active)

        lease_expiration_enabled = d.pop("leaseExpirationEnabled", UNSET)

        _lease_expiration_date = d.pop("leaseExpirationDate", UNSET)
        lease_expiration_date: Union[Unset, datetime.datetime]
        if isinstance(_lease_expiration_date, Unset):
            lease_expiration_date = UNSET
        else:
            lease_expiration_date = isoparse(_lease_expiration_date)

        description = d.pop("description", UNSET)

        throttling_enabled = d.pop("throttlingEnabled", UNSET)

        throttling_value = d.pop("throttlingValue", UNSET)

        _throttling_unit = d.pop("throttlingUnit", UNSET)
        throttling_unit: Union[Unset, CompanySiteResourceThrottlingUnit]
        if isinstance(_throttling_unit, Unset):
            throttling_unit = UNSET
        else:
            throttling_unit = CompanySiteResourceThrottlingUnit(_throttling_unit)

        max_concurrent_task = d.pop("maxConcurrentTask", UNSET)

        backup_protection_enabled = d.pop("backupProtectionEnabled", UNSET)

        backup_protection_period_days = d.pop("backupProtectionPeriodDays", UNSET)

        _gateway_selection_type = d.pop("gatewaySelectionType", UNSET)
        gateway_selection_type: Union[Unset, CompanySiteResourceGatewaySelectionType]
        if isinstance(_gateway_selection_type, Unset):
            gateway_selection_type = UNSET
        else:
            gateway_selection_type = CompanySiteResourceGatewaySelectionType(_gateway_selection_type)

        gateway_pools_uids = []
        _gateway_pools_uids = d.pop("gatewayPoolsUids", UNSET)
        for gateway_pools_uids_item_data in _gateway_pools_uids or []:
            gateway_pools_uids_item = UUID(gateway_pools_uids_item_data)

            gateway_pools_uids.append(gateway_pools_uids_item)

        is_gateway_failover_enabled = d.pop("isGatewayFailoverEnabled", UNSET)

        company_site_resource = cls(
            site_uid=site_uid,
            owner_credentials=owner_credentials,
            cloud_tenant_type=cloud_tenant_type,
            company_uid=company_uid,
            cloud_tenant_uid=cloud_tenant_uid,
            v_cloud_organization_uid=v_cloud_organization_uid,
            last_active=last_active,
            lease_expiration_enabled=lease_expiration_enabled,
            lease_expiration_date=lease_expiration_date,
            description=description,
            throttling_enabled=throttling_enabled,
            throttling_value=throttling_value,
            throttling_unit=throttling_unit,
            max_concurrent_task=max_concurrent_task,
            backup_protection_enabled=backup_protection_enabled,
            backup_protection_period_days=backup_protection_period_days,
            gateway_selection_type=gateway_selection_type,
            gateway_pools_uids=gateway_pools_uids,
            is_gateway_failover_enabled=is_gateway_failover_enabled,
        )

        company_site_resource.additional_properties = d
        return company_site_resource

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
