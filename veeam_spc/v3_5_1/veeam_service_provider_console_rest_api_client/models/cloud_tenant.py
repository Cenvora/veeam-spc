import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
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
        name (Union[None, Unset, str]): Name of a tenant account.
        description (Union[None, Unset, str]): Description of a tenant account.
        hashed_password (Union[Unset, str]): Password of a tenant account.
        type_ (Union[Unset, CloudTenantType]): Type of a tenant account.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a Veeam Cloud Connect server.
        last_active (Union[None, Unset, datetime.datetime]): The last time when a tenant was active.
        gateway_selection_type (Union[Unset, CloudTenantGatewaySelectionType]): Type of gateway selection.
        is_enabled (Union[Unset, bool]): Indicates whether a tenant account is enabled.
        is_lease_expiration_enabled (Union[Unset, bool]): Indicates whether a tenant account must be disabled
            automatically.
        lease_expiration_date (Union[None, Unset, datetime.datetime]): Date and time when a company account must be
            disabled.
        is_backup_protection_enabled (Union[Unset, bool]): Indicates whether deleted backup file protection is enabled.
        backup_protection_period (Union[None, Unset, int]): Number of days during which deleted backup files must be
            kept in the recycle bin on the Veeam Cloud Connect server.
        is_gateway_failover_enabled (Union[Unset, bool]): Indicates whether a tenant is allowed to fail over to a cloud
            gateway that is not added to a selected cloud gateway pool.
        gateway_pools_uids (Union[None, Unset, list[UUID]]): Collection of UIDs assigned to gateway pools that are
            allocated to a company.
            > If the collection is empty, company will automatically use a standalone gateway.
        is_throttling_enabled (Union[Unset, bool]): Indicates whether incoming network traffic that will be accepted
            from a tenant is limited.
        throttling_value (Union[None, Unset, int]): Maximum incoming network traffic bandwidth that will be accepted
            from a tenant.
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
    name: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    hashed_password: Union[Unset, str] = UNSET
    type_: Union[Unset, CloudTenantType] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    last_active: Union[None, Unset, datetime.datetime] = UNSET
    gateway_selection_type: Union[Unset, CloudTenantGatewaySelectionType] = UNSET
    is_enabled: Union[Unset, bool] = UNSET
    is_lease_expiration_enabled: Union[Unset, bool] = UNSET
    lease_expiration_date: Union[None, Unset, datetime.datetime] = UNSET
    is_backup_protection_enabled: Union[Unset, bool] = UNSET
    backup_protection_period: Union[None, Unset, int] = UNSET
    is_gateway_failover_enabled: Union[Unset, bool] = UNSET
    gateway_pools_uids: Union[None, Unset, list[UUID]] = UNSET
    is_throttling_enabled: Union[Unset, bool] = UNSET
    throttling_value: Union[None, Unset, int] = UNSET
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

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        hashed_password = self.hashed_password

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        last_active: Union[None, Unset, str]
        if isinstance(self.last_active, Unset):
            last_active = UNSET
        elif isinstance(self.last_active, datetime.datetime):
            last_active = self.last_active.isoformat()
        else:
            last_active = self.last_active

        gateway_selection_type: Union[Unset, str] = UNSET
        if not isinstance(self.gateway_selection_type, Unset):
            gateway_selection_type = self.gateway_selection_type.value

        is_enabled = self.is_enabled

        is_lease_expiration_enabled = self.is_lease_expiration_enabled

        lease_expiration_date: Union[None, Unset, str]
        if isinstance(self.lease_expiration_date, Unset):
            lease_expiration_date = UNSET
        elif isinstance(self.lease_expiration_date, datetime.datetime):
            lease_expiration_date = self.lease_expiration_date.isoformat()
        else:
            lease_expiration_date = self.lease_expiration_date

        is_backup_protection_enabled = self.is_backup_protection_enabled

        backup_protection_period: Union[None, Unset, int]
        if isinstance(self.backup_protection_period, Unset):
            backup_protection_period = UNSET
        else:
            backup_protection_period = self.backup_protection_period

        is_gateway_failover_enabled = self.is_gateway_failover_enabled

        gateway_pools_uids: Union[None, Unset, list[str]]
        if isinstance(self.gateway_pools_uids, Unset):
            gateway_pools_uids = UNSET
        elif isinstance(self.gateway_pools_uids, list):
            gateway_pools_uids = []
            for gateway_pools_uids_type_0_item_data in self.gateway_pools_uids:
                gateway_pools_uids_type_0_item = str(gateway_pools_uids_type_0_item_data)
                gateway_pools_uids.append(gateway_pools_uids_type_0_item)

        else:
            gateway_pools_uids = self.gateway_pools_uids

        is_throttling_enabled = self.is_throttling_enabled

        throttling_value: Union[None, Unset, int]
        if isinstance(self.throttling_value, Unset):
            throttling_value = UNSET
        else:
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

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

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

        def _parse_last_active(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_active_type_0 = isoparse(data)

                return last_active_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_active = _parse_last_active(d.pop("lastActive", UNSET))

        _gateway_selection_type = d.pop("gatewaySelectionType", UNSET)
        gateway_selection_type: Union[Unset, CloudTenantGatewaySelectionType]
        if isinstance(_gateway_selection_type, Unset):
            gateway_selection_type = UNSET
        else:
            gateway_selection_type = CloudTenantGatewaySelectionType(_gateway_selection_type)

        is_enabled = d.pop("isEnabled", UNSET)

        is_lease_expiration_enabled = d.pop("isLeaseExpirationEnabled", UNSET)

        def _parse_lease_expiration_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lease_expiration_date_type_0 = isoparse(data)

                return lease_expiration_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        lease_expiration_date = _parse_lease_expiration_date(d.pop("leaseExpirationDate", UNSET))

        is_backup_protection_enabled = d.pop("isBackupProtectionEnabled", UNSET)

        def _parse_backup_protection_period(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        backup_protection_period = _parse_backup_protection_period(d.pop("backupProtectionPeriod", UNSET))

        is_gateway_failover_enabled = d.pop("isGatewayFailoverEnabled", UNSET)

        def _parse_gateway_pools_uids(data: object) -> Union[None, Unset, list[UUID]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                gateway_pools_uids_type_0 = []
                _gateway_pools_uids_type_0 = data
                for gateway_pools_uids_type_0_item_data in _gateway_pools_uids_type_0:
                    gateway_pools_uids_type_0_item = UUID(gateway_pools_uids_type_0_item_data)

                    gateway_pools_uids_type_0.append(gateway_pools_uids_type_0_item)

                return gateway_pools_uids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[UUID]], data)

        gateway_pools_uids = _parse_gateway_pools_uids(d.pop("gatewayPoolsUids", UNSET))

        is_throttling_enabled = d.pop("isThrottlingEnabled", UNSET)

        def _parse_throttling_value(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        throttling_value = _parse_throttling_value(d.pop("throttlingValue", UNSET))

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
