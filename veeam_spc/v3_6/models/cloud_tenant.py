import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.cloud_tenant_gateway_selection_type import CloudTenantGatewaySelectionType
from ..models.cloud_tenant_throttling_unit import CloudTenantThrottlingUnit
from ..models.cloud_tenant_type import CloudTenantType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.owner_credentials import OwnerCredentials


T = TypeVar("T", bound="CloudTenant")


@_attrs_define
class CloudTenant:
    """
    Attributes:
        credentials (OwnerCredentials):
        instance_uid (Union[Unset, UUID]): UID assigned to a tenant.
        site_uid (Union[Unset, UUID]): UID assigned to a Veeam Cloud Connect site.
        site_name (Union[Unset, str]): Name assigned to a Veeam Cloud Connect site.
        type_ (Union[Unset, CloudTenantType]): Type of a tenant account. Default: CloudTenantType.GENERAL.
        v_cloud_organization_uid (Union[Unset, UUID]): UID assigned to a VMware Cloud Director organization.
        last_active (Union[Unset, datetime.datetime]): The last time when a tenant was active.
        is_lease_expiration_enabled (Union[Unset, bool]): Indicates whether a tenant account must be disabled
            automatically. Default: False.
        lease_expiration_date (Union[Unset, datetime.datetime]): Date and time when a company account must be disabled.
        description (Union[Unset, str]): Description of a tenant account.
        is_throttling_enabled (Union[Unset, bool]): Indicates whether incoming network traffic that will be accepted
            from a tenant is limited. Default: False.
        throttling_value (Union[Unset, int]): Maximum incoming network traffic bandwidth that will be accepted from a
            tenant.
            > If throttling is disabled, the property value is `null`.
             Default: 1.
        throttling_unit (Union[Unset, CloudTenantThrottlingUnit]): Measurement units of incoming network traffic
            accepted from a company.
            > If throttling is disabled, the property value is `null`.
             Default: CloudTenantThrottlingUnit.MBYTEPERSEC.
        max_concurrent_task (Union[Unset, int]): Maximum number of concurrent tasks available to a tenant. Default: 1.
        is_backup_protection_enabled (Union[Unset, bool]): Indicates whether deleted backup file protection is enabled.
            Default: False.
        backup_protection_period (Union[Unset, int]): Number of days during which deleted backup files must be kept in
            the recycle bin on the Veeam Cloud Connect server. Default: 7.
        gateway_selection_type (Union[Unset, CloudTenantGatewaySelectionType]): Type of gateway selection. Default:
            CloudTenantGatewaySelectionType.STANDALONEGATEWAYS.
        gateway_pools_uids (Union[Unset, list[UUID]]): Collection of UIDs assigned to gateway pools that are allocated
            to a company.
            > If the collection is empty, company will automatically use a standalone gateway.
        is_gateway_failover_enabled (Union[Unset, bool]): Indicates whether a tenant is allowed to fail over to a cloud
            gateway that is not added to a selected cloud gateway pool. Default: False.
        name (Union[Unset, str]): Name of a tenant account.
        hashed_password (Union[Unset, str]): Hash of a tenant account password.
        is_enabled (Union[Unset, bool]): Indicates whether a tenant account is enabled.
        is_backup_resources_enabled (Union[Unset, bool]): Indicates whether cloud backup resources are allocated to a
            tenant.
        is_native_replication_resources_enabled (Union[Unset, bool]): Indicates whether cloud replication resources are
            allocated to a tenant. Default: False.
        is_vcd_replication_resources_enabled (Union[Unset, bool]): Indicates whether organization VDCs are allocated to
            a tenant as cloud hosts. Default: False.
        assigned_for_company (Union[Unset, UUID]): UID of a company to which a tenant is assigned.
            > For reseller users, the property value is required.
    """

    credentials: "OwnerCredentials"
    instance_uid: Union[Unset, UUID] = UNSET
    site_uid: Union[Unset, UUID] = UNSET
    site_name: Union[Unset, str] = UNSET
    type_: Union[Unset, CloudTenantType] = CloudTenantType.GENERAL
    v_cloud_organization_uid: Union[Unset, UUID] = UNSET
    last_active: Union[Unset, datetime.datetime] = UNSET
    is_lease_expiration_enabled: Union[Unset, bool] = False
    lease_expiration_date: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    is_throttling_enabled: Union[Unset, bool] = False
    throttling_value: Union[Unset, int] = 1
    throttling_unit: Union[Unset, CloudTenantThrottlingUnit] = CloudTenantThrottlingUnit.MBYTEPERSEC
    max_concurrent_task: Union[Unset, int] = 1
    is_backup_protection_enabled: Union[Unset, bool] = False
    backup_protection_period: Union[Unset, int] = 7
    gateway_selection_type: Union[Unset, CloudTenantGatewaySelectionType] = (
        CloudTenantGatewaySelectionType.STANDALONEGATEWAYS
    )
    gateway_pools_uids: Union[Unset, list[UUID]] = UNSET
    is_gateway_failover_enabled: Union[Unset, bool] = False
    name: Union[Unset, str] = UNSET
    hashed_password: Union[Unset, str] = UNSET
    is_enabled: Union[Unset, bool] = UNSET
    is_backup_resources_enabled: Union[Unset, bool] = UNSET
    is_native_replication_resources_enabled: Union[Unset, bool] = False
    is_vcd_replication_resources_enabled: Union[Unset, bool] = False
    assigned_for_company: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credentials = self.credentials.to_dict()

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        site_uid: Union[Unset, str] = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        site_name = self.site_name

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        v_cloud_organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.v_cloud_organization_uid, Unset):
            v_cloud_organization_uid = str(self.v_cloud_organization_uid)

        last_active: Union[Unset, str] = UNSET
        if not isinstance(self.last_active, Unset):
            last_active = self.last_active.isoformat()

        is_lease_expiration_enabled = self.is_lease_expiration_enabled

        lease_expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.lease_expiration_date, Unset):
            lease_expiration_date = self.lease_expiration_date.isoformat()

        description = self.description

        is_throttling_enabled = self.is_throttling_enabled

        throttling_value = self.throttling_value

        throttling_unit: Union[Unset, str] = UNSET
        if not isinstance(self.throttling_unit, Unset):
            throttling_unit = self.throttling_unit.value

        max_concurrent_task = self.max_concurrent_task

        is_backup_protection_enabled = self.is_backup_protection_enabled

        backup_protection_period = self.backup_protection_period

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

        name = self.name

        hashed_password = self.hashed_password

        is_enabled = self.is_enabled

        is_backup_resources_enabled = self.is_backup_resources_enabled

        is_native_replication_resources_enabled = self.is_native_replication_resources_enabled

        is_vcd_replication_resources_enabled = self.is_vcd_replication_resources_enabled

        assigned_for_company: Union[Unset, str] = UNSET
        if not isinstance(self.assigned_for_company, Unset):
            assigned_for_company = str(self.assigned_for_company)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentials": credentials,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid
        if site_name is not UNSET:
            field_dict["siteName"] = site_name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if v_cloud_organization_uid is not UNSET:
            field_dict["vCloudOrganizationUid"] = v_cloud_organization_uid
        if last_active is not UNSET:
            field_dict["lastActive"] = last_active
        if is_lease_expiration_enabled is not UNSET:
            field_dict["isLeaseExpirationEnabled"] = is_lease_expiration_enabled
        if lease_expiration_date is not UNSET:
            field_dict["leaseExpirationDate"] = lease_expiration_date
        if description is not UNSET:
            field_dict["description"] = description
        if is_throttling_enabled is not UNSET:
            field_dict["isThrottlingEnabled"] = is_throttling_enabled
        if throttling_value is not UNSET:
            field_dict["throttlingValue"] = throttling_value
        if throttling_unit is not UNSET:
            field_dict["throttlingUnit"] = throttling_unit
        if max_concurrent_task is not UNSET:
            field_dict["maxConcurrentTask"] = max_concurrent_task
        if is_backup_protection_enabled is not UNSET:
            field_dict["isBackupProtectionEnabled"] = is_backup_protection_enabled
        if backup_protection_period is not UNSET:
            field_dict["backupProtectionPeriod"] = backup_protection_period
        if gateway_selection_type is not UNSET:
            field_dict["gatewaySelectionType"] = gateway_selection_type
        if gateway_pools_uids is not UNSET:
            field_dict["gatewayPoolsUids"] = gateway_pools_uids
        if is_gateway_failover_enabled is not UNSET:
            field_dict["isGatewayFailoverEnabled"] = is_gateway_failover_enabled
        if name is not UNSET:
            field_dict["name"] = name
        if hashed_password is not UNSET:
            field_dict["hashedPassword"] = hashed_password
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if is_backup_resources_enabled is not UNSET:
            field_dict["isBackupResourcesEnabled"] = is_backup_resources_enabled
        if is_native_replication_resources_enabled is not UNSET:
            field_dict["isNativeReplicationResourcesEnabled"] = is_native_replication_resources_enabled
        if is_vcd_replication_resources_enabled is not UNSET:
            field_dict["isVcdReplicationResourcesEnabled"] = is_vcd_replication_resources_enabled
        if assigned_for_company is not UNSET:
            field_dict["assignedForCompany"] = assigned_for_company

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.owner_credentials import OwnerCredentials

        d = dict(src_dict)
        credentials = OwnerCredentials.from_dict(d.pop("credentials"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _site_uid = d.pop("siteUid", UNSET)
        site_uid: Union[Unset, UUID]
        if isinstance(_site_uid, Unset):
            site_uid = UNSET
        else:
            site_uid = UUID(_site_uid)

        site_name = d.pop("siteName", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, CloudTenantType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CloudTenantType(_type_)

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

        is_lease_expiration_enabled = d.pop("isLeaseExpirationEnabled", UNSET)

        _lease_expiration_date = d.pop("leaseExpirationDate", UNSET)
        lease_expiration_date: Union[Unset, datetime.datetime]
        if isinstance(_lease_expiration_date, Unset):
            lease_expiration_date = UNSET
        else:
            lease_expiration_date = isoparse(_lease_expiration_date)

        description = d.pop("description", UNSET)

        is_throttling_enabled = d.pop("isThrottlingEnabled", UNSET)

        throttling_value = d.pop("throttlingValue", UNSET)

        _throttling_unit = d.pop("throttlingUnit", UNSET)
        throttling_unit: Union[Unset, CloudTenantThrottlingUnit]
        if isinstance(_throttling_unit, Unset):
            throttling_unit = UNSET
        else:
            throttling_unit = CloudTenantThrottlingUnit(_throttling_unit)

        max_concurrent_task = d.pop("maxConcurrentTask", UNSET)

        is_backup_protection_enabled = d.pop("isBackupProtectionEnabled", UNSET)

        backup_protection_period = d.pop("backupProtectionPeriod", UNSET)

        _gateway_selection_type = d.pop("gatewaySelectionType", UNSET)
        gateway_selection_type: Union[Unset, CloudTenantGatewaySelectionType]
        if isinstance(_gateway_selection_type, Unset):
            gateway_selection_type = UNSET
        else:
            gateway_selection_type = CloudTenantGatewaySelectionType(_gateway_selection_type)

        gateway_pools_uids = []
        _gateway_pools_uids = d.pop("gatewayPoolsUids", UNSET)
        for gateway_pools_uids_item_data in _gateway_pools_uids or []:
            gateway_pools_uids_item = UUID(gateway_pools_uids_item_data)

            gateway_pools_uids.append(gateway_pools_uids_item)

        is_gateway_failover_enabled = d.pop("isGatewayFailoverEnabled", UNSET)

        name = d.pop("name", UNSET)

        hashed_password = d.pop("hashedPassword", UNSET)

        is_enabled = d.pop("isEnabled", UNSET)

        is_backup_resources_enabled = d.pop("isBackupResourcesEnabled", UNSET)

        is_native_replication_resources_enabled = d.pop("isNativeReplicationResourcesEnabled", UNSET)

        is_vcd_replication_resources_enabled = d.pop("isVcdReplicationResourcesEnabled", UNSET)

        _assigned_for_company = d.pop("assignedForCompany", UNSET)
        assigned_for_company: Union[Unset, UUID]
        if isinstance(_assigned_for_company, Unset):
            assigned_for_company = UNSET
        else:
            assigned_for_company = UUID(_assigned_for_company)

        cloud_tenant = cls(
            credentials=credentials,
            instance_uid=instance_uid,
            site_uid=site_uid,
            site_name=site_name,
            type_=type_,
            v_cloud_organization_uid=v_cloud_organization_uid,
            last_active=last_active,
            is_lease_expiration_enabled=is_lease_expiration_enabled,
            lease_expiration_date=lease_expiration_date,
            description=description,
            is_throttling_enabled=is_throttling_enabled,
            throttling_value=throttling_value,
            throttling_unit=throttling_unit,
            max_concurrent_task=max_concurrent_task,
            is_backup_protection_enabled=is_backup_protection_enabled,
            backup_protection_period=backup_protection_period,
            gateway_selection_type=gateway_selection_type,
            gateway_pools_uids=gateway_pools_uids,
            is_gateway_failover_enabled=is_gateway_failover_enabled,
            name=name,
            hashed_password=hashed_password,
            is_enabled=is_enabled,
            is_backup_resources_enabled=is_backup_resources_enabled,
            is_native_replication_resources_enabled=is_native_replication_resources_enabled,
            is_vcd_replication_resources_enabled=is_vcd_replication_resources_enabled,
            assigned_for_company=assigned_for_company,
        )

        cloud_tenant.additional_properties = d
        return cloud_tenant

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
