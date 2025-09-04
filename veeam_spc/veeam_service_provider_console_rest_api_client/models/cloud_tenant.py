import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.cloud_tenant_gateway_selection_type import CloudTenantGatewaySelectionType
from ..models.cloud_tenant_throttling_unit import CloudTenantThrottlingUnit
from ..models.cloud_tenant_type import CloudTenantType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudTenant")


@_attrs_define
class CloudTenant:
    """
    Example:
        {'instanceUid': '0000568E-F90F-4702-8151-CBE3CE2A8C10', 'name': 'Tenant01', 'description': 'Created by Veeam
            Service Provider Console at 01.01.2019', 'hashedPassword':
            '5E884898DA28047151D0E56F8DC6292773603D0D6AABBDD62A11EF721D1542D8', 'type': 'General', 'backupServerUid':
            'DF997BD3-4AE9-4841-8152-8FF5CC703EAB', 'gatewaySelectionType': 'StandaloneGateways', 'isEnabled': True,
            'isLeaseExpirationEnabled': True, 'leaseExpirationDate': datetime.datetime(1985, 4, 13, 1, 20, 50, 520000,
            tzinfo=datetime.timezone(datetime.timedelta(seconds=7200), '+02:00')), 'isBackupProtectionEnabled': True,
            'backupProtectionPeriod': 14, 'isGatewayFailoverEnabled': True, 'isThrottlingEnabled': True, 'throttlingValue':
            4, 'throttlingUnit': 'MbytePerSec', 'maxConcurrentTask': 7, 'isBackupResourcesEnabled': True,
            'isNativeReplicationResourcesEnabled': True, 'isVcdReplicationResourcesEnabled': True}

    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a Veeam Cloud Connect tenant.
        name (Union[Unset, str]): Name of a tenant account.
        description (Union[Unset, str]): Description of a tenant account.
        hashed_password (Union[Unset, str]): Password of a tenant account.
        type_ (Union[Unset, CloudTenantType]): Type of a tenant account.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a Veeam Cloud Connect server.
        last_active (Union[Unset, datetime.datetime]): The last time when a tenant was active.
        gateway_selection_type (Union[Unset, CloudTenantGatewaySelectionType]): Type of gateway selection.
        is_enabled (Union[Unset, bool]): Indicates whether a tenant account is enabled.
        is_lease_expiration_enabled (Union[Unset, bool]): Indicates whether a tenant account must be disabled
            automatically.
        lease_expiration_date (Union[Unset, datetime.datetime]): Date and time when a company account must be disabled.
        is_backup_protection_enabled (Union[Unset, bool]): Indicates whether deleted backup file protection is enabled.
        backup_protection_period (Union[Unset, int]): Number of days during which deleted backup files must be kept in
            the recycle bin on the Veeam Cloud Connect server.
        is_gateway_failover_enabled (Union[Unset, bool]): Indicates whether a tenant is allowed to fail over to a cloud
            gateway that is not added to a selected cloud gateway pool.
        gateway_pools_uids (Union[Unset, list[UUID]]): Collection of UIDs assigned to gateway pools that are allocated
            to a company.
            > If the collection is empty, company will automatically use a standalone gateway.
        is_throttling_enabled (Union[Unset, bool]): Indicates whether incoming network traffic that will be accepted
            from a tenant is limited.
        throttling_value (Union[Unset, int]): Maximum incoming network traffic bandwidth that will be accepted from a
            tenant.
            > If throttling is disabled, the property value is `null`.
        throttling_unit (Union[Unset, CloudTenantThrottlingUnit]): Measurement units of incoming network traffic
            accepted from a company.
            > If throttling is disabled, the property value is `null`.
        max_concurrent_task (Union[Unset, int]): Maximum number of concurrent tasks available to a tenant.
        is_backup_resources_enabled (Union[Unset, bool]): Indicates whether cloud backup resources are allocated to a
            tenant.
        is_native_replication_resources_enabled (Union[Unset, bool]): Indicates whether cloud replication resources are
            allocated to a tenant.
        is_vcd_replication_resources_enabled (Union[Unset, bool]): Indicates whether organization VDCs are allocated to
            a tenant as cloud hosts.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    hashed_password: Union[Unset, str] = UNSET
    type_: Union[Unset, CloudTenantType] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    last_active: Union[Unset, datetime.datetime] = UNSET
    gateway_selection_type: Union[Unset, CloudTenantGatewaySelectionType] = UNSET
    is_enabled: Union[Unset, bool] = UNSET
    is_lease_expiration_enabled: Union[Unset, bool] = UNSET
    lease_expiration_date: Union[Unset, datetime.datetime] = UNSET
    is_backup_protection_enabled: Union[Unset, bool] = UNSET
    backup_protection_period: Union[Unset, int] = UNSET
    is_gateway_failover_enabled: Union[Unset, bool] = UNSET
    gateway_pools_uids: Union[Unset, list[UUID]] = UNSET
    is_throttling_enabled: Union[Unset, bool] = UNSET
    throttling_value: Union[Unset, int] = UNSET
    throttling_unit: Union[Unset, CloudTenantThrottlingUnit] = UNSET
    max_concurrent_task: Union[Unset, int] = UNSET
    is_backup_resources_enabled: Union[Unset, bool] = UNSET
    is_native_replication_resources_enabled: Union[Unset, bool] = UNSET
    is_vcd_replication_resources_enabled: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        description = self.description

        hashed_password = self.hashed_password

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        last_active: Union[Unset, str] = UNSET
        if not isinstance(self.last_active, Unset):
            last_active = self.last_active.isoformat()

        gateway_selection_type: Union[Unset, str] = UNSET
        if not isinstance(self.gateway_selection_type, Unset):
            gateway_selection_type = self.gateway_selection_type.value

        is_enabled = self.is_enabled

        is_lease_expiration_enabled = self.is_lease_expiration_enabled

        lease_expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.lease_expiration_date, Unset):
            lease_expiration_date = self.lease_expiration_date.isoformat()

        is_backup_protection_enabled = self.is_backup_protection_enabled

        backup_protection_period = self.backup_protection_period

        is_gateway_failover_enabled = self.is_gateway_failover_enabled

        gateway_pools_uids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.gateway_pools_uids, Unset):
            gateway_pools_uids = []
            for gateway_pools_uids_item_data in self.gateway_pools_uids:
                gateway_pools_uids_item = str(gateway_pools_uids_item_data)
                gateway_pools_uids.append(gateway_pools_uids_item)

        is_throttling_enabled = self.is_throttling_enabled

        throttling_value = self.throttling_value

        throttling_unit: Union[Unset, str] = UNSET
        if not isinstance(self.throttling_unit, Unset):
            throttling_unit = self.throttling_unit.value

        max_concurrent_task = self.max_concurrent_task

        is_backup_resources_enabled = self.is_backup_resources_enabled

        is_native_replication_resources_enabled = self.is_native_replication_resources_enabled

        is_vcd_replication_resources_enabled = self.is_vcd_replication_resources_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if hashed_password is not UNSET:
            field_dict["hashedPassword"] = hashed_password
        if type_ is not UNSET:
            field_dict["type"] = type_
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if last_active is not UNSET:
            field_dict["lastActive"] = last_active
        if gateway_selection_type is not UNSET:
            field_dict["gatewaySelectionType"] = gateway_selection_type
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if is_lease_expiration_enabled is not UNSET:
            field_dict["isLeaseExpirationEnabled"] = is_lease_expiration_enabled
        if lease_expiration_date is not UNSET:
            field_dict["leaseExpirationDate"] = lease_expiration_date
        if is_backup_protection_enabled is not UNSET:
            field_dict["isBackupProtectionEnabled"] = is_backup_protection_enabled
        if backup_protection_period is not UNSET:
            field_dict["backupProtectionPeriod"] = backup_protection_period
        if is_gateway_failover_enabled is not UNSET:
            field_dict["isGatewayFailoverEnabled"] = is_gateway_failover_enabled
        if gateway_pools_uids is not UNSET:
            field_dict["gatewayPoolsUids"] = gateway_pools_uids
        if is_throttling_enabled is not UNSET:
            field_dict["isThrottlingEnabled"] = is_throttling_enabled
        if throttling_value is not UNSET:
            field_dict["throttlingValue"] = throttling_value
        if throttling_unit is not UNSET:
            field_dict["throttlingUnit"] = throttling_unit
        if max_concurrent_task is not UNSET:
            field_dict["maxConcurrentTask"] = max_concurrent_task
        if is_backup_resources_enabled is not UNSET:
            field_dict["isBackupResourcesEnabled"] = is_backup_resources_enabled
        if is_native_replication_resources_enabled is not UNSET:
            field_dict["isNativeReplicationResourcesEnabled"] = is_native_replication_resources_enabled
        if is_vcd_replication_resources_enabled is not UNSET:
            field_dict["isVcdReplicationResourcesEnabled"] = is_vcd_replication_resources_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        hashed_password = d.pop("hashedPassword", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, CloudTenantType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CloudTenantType(_type_)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: Union[Unset, UUID]
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        _last_active = d.pop("lastActive", UNSET)
        last_active: Union[Unset, datetime.datetime]
        if isinstance(_last_active, Unset):
            last_active = UNSET
        else:
            last_active = isoparse(_last_active)

        _gateway_selection_type = d.pop("gatewaySelectionType", UNSET)
        gateway_selection_type: Union[Unset, CloudTenantGatewaySelectionType]
        if isinstance(_gateway_selection_type, Unset):
            gateway_selection_type = UNSET
        else:
            gateway_selection_type = CloudTenantGatewaySelectionType(_gateway_selection_type)

        is_enabled = d.pop("isEnabled", UNSET)

        is_lease_expiration_enabled = d.pop("isLeaseExpirationEnabled", UNSET)

        _lease_expiration_date = d.pop("leaseExpirationDate", UNSET)
        lease_expiration_date: Union[Unset, datetime.datetime]
        if isinstance(_lease_expiration_date, Unset):
            lease_expiration_date = UNSET
        else:
            lease_expiration_date = isoparse(_lease_expiration_date)

        is_backup_protection_enabled = d.pop("isBackupProtectionEnabled", UNSET)

        backup_protection_period = d.pop("backupProtectionPeriod", UNSET)

        is_gateway_failover_enabled = d.pop("isGatewayFailoverEnabled", UNSET)

        gateway_pools_uids = []
        _gateway_pools_uids = d.pop("gatewayPoolsUids", UNSET)
        for gateway_pools_uids_item_data in _gateway_pools_uids or []:
            gateway_pools_uids_item = UUID(gateway_pools_uids_item_data)

            gateway_pools_uids.append(gateway_pools_uids_item)

        is_throttling_enabled = d.pop("isThrottlingEnabled", UNSET)

        throttling_value = d.pop("throttlingValue", UNSET)

        _throttling_unit = d.pop("throttlingUnit", UNSET)
        throttling_unit: Union[Unset, CloudTenantThrottlingUnit]
        if isinstance(_throttling_unit, Unset):
            throttling_unit = UNSET
        else:
            throttling_unit = CloudTenantThrottlingUnit(_throttling_unit)

        max_concurrent_task = d.pop("maxConcurrentTask", UNSET)

        is_backup_resources_enabled = d.pop("isBackupResourcesEnabled", UNSET)

        is_native_replication_resources_enabled = d.pop("isNativeReplicationResourcesEnabled", UNSET)

        is_vcd_replication_resources_enabled = d.pop("isVcdReplicationResourcesEnabled", UNSET)

        cloud_tenant = cls(
            instance_uid=instance_uid,
            name=name,
            description=description,
            hashed_password=hashed_password,
            type_=type_,
            backup_server_uid=backup_server_uid,
            last_active=last_active,
            gateway_selection_type=gateway_selection_type,
            is_enabled=is_enabled,
            is_lease_expiration_enabled=is_lease_expiration_enabled,
            lease_expiration_date=lease_expiration_date,
            is_backup_protection_enabled=is_backup_protection_enabled,
            backup_protection_period=backup_protection_period,
            is_gateway_failover_enabled=is_gateway_failover_enabled,
            gateway_pools_uids=gateway_pools_uids,
            is_throttling_enabled=is_throttling_enabled,
            throttling_value=throttling_value,
            throttling_unit=throttling_unit,
            max_concurrent_task=max_concurrent_task,
            is_backup_resources_enabled=is_backup_resources_enabled,
            is_native_replication_resources_enabled=is_native_replication_resources_enabled,
            is_vcd_replication_resources_enabled=is_vcd_replication_resources_enabled,
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
