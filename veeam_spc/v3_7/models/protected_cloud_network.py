from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.backup_server_public_cloud_appliance_platform import BackupServerPublicCloudAppliancePlatform
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedCloudNetwork")


@_attrs_define
class ProtectedCloudNetwork:
    """
    Attributes:
        instance_id (str | Unset): ID assigned to a cloud network.
        account_uid (None | Unset | UUID): UID assigned to a public cloud account.
        account_name (str | Unset): Name of a public cloud account.
        subscription_uid (None | Unset | UUID): UID assigned to a cloud subscription.
        subscription_name (str | Unset): Name of a cloud subscription.
        region_tag (str | Unset): Tag of a cloud network region.
        region_name (str | Unset): Name of a cloud network region.
        policy_uid (UUID | Unset): UID assigned to a cloud network policy.
        policy_name (str | Unset): Name of a cloud network policy.
        appliance_uid (None | Unset | UUID): UID assigned to a Veeam Backup for Public Clouds appliance.
        backup_server_uid (UUID | Unset): UID assigned to a Veeam Backup & Replication server.
        backup_server_name (str | Unset): Name of a Veeam Backup & Replication server.
        restore_points_count (int | Unset): Number of restore points.
        platform_type (BackupServerPublicCloudAppliancePlatform | Unset): Platform of a Veeam Backup for Public Clouds
            appliance.
        last_backup (datetime.datetime | Unset): Date and time when the latest backup was created.
        location_uid (UUID | Unset): UID assigned to a cloud network location.
        organization_uid (UUID | Unset): UID assigned to a mapped organization.
    """

    instance_id: str | Unset = UNSET
    account_uid: None | Unset | UUID = UNSET
    account_name: str | Unset = UNSET
    subscription_uid: None | Unset | UUID = UNSET
    subscription_name: str | Unset = UNSET
    region_tag: str | Unset = UNSET
    region_name: str | Unset = UNSET
    policy_uid: UUID | Unset = UNSET
    policy_name: str | Unset = UNSET
    appliance_uid: None | Unset | UUID = UNSET
    backup_server_uid: UUID | Unset = UNSET
    backup_server_name: str | Unset = UNSET
    restore_points_count: int | Unset = UNSET
    platform_type: BackupServerPublicCloudAppliancePlatform | Unset = UNSET
    last_backup: datetime.datetime | Unset = UNSET
    location_uid: UUID | Unset = UNSET
    organization_uid: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_id = self.instance_id

        account_uid: None | str | Unset
        if isinstance(self.account_uid, Unset):
            account_uid = UNSET
        elif isinstance(self.account_uid, UUID):
            account_uid = str(self.account_uid)
        else:
            account_uid = self.account_uid

        account_name = self.account_name

        subscription_uid: None | str | Unset
        if isinstance(self.subscription_uid, Unset):
            subscription_uid = UNSET
        elif isinstance(self.subscription_uid, UUID):
            subscription_uid = str(self.subscription_uid)
        else:
            subscription_uid = self.subscription_uid

        subscription_name = self.subscription_name

        region_tag = self.region_tag

        region_name = self.region_name

        policy_uid: str | Unset = UNSET
        if not isinstance(self.policy_uid, Unset):
            policy_uid = str(self.policy_uid)

        policy_name = self.policy_name

        appliance_uid: None | str | Unset
        if isinstance(self.appliance_uid, Unset):
            appliance_uid = UNSET
        elif isinstance(self.appliance_uid, UUID):
            appliance_uid = str(self.appliance_uid)
        else:
            appliance_uid = self.appliance_uid

        backup_server_uid: str | Unset = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        backup_server_name = self.backup_server_name

        restore_points_count = self.restore_points_count

        platform_type: str | Unset = UNSET
        if not isinstance(self.platform_type, Unset):
            platform_type = self.platform_type.value

        last_backup: str | Unset = UNSET
        if not isinstance(self.last_backup, Unset):
            last_backup = self.last_backup.isoformat()

        location_uid: str | Unset = UNSET
        if not isinstance(self.location_uid, Unset):
            location_uid = str(self.location_uid)

        organization_uid: str | Unset = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_id is not UNSET:
            field_dict["instanceId"] = instance_id
        if account_uid is not UNSET:
            field_dict["accountUid"] = account_uid
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if subscription_uid is not UNSET:
            field_dict["subscriptionUid"] = subscription_uid
        if subscription_name is not UNSET:
            field_dict["subscriptionName"] = subscription_name
        if region_tag is not UNSET:
            field_dict["regionTag"] = region_tag
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if policy_uid is not UNSET:
            field_dict["policyUid"] = policy_uid
        if policy_name is not UNSET:
            field_dict["policyName"] = policy_name
        if appliance_uid is not UNSET:
            field_dict["applianceUid"] = appliance_uid
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if backup_server_name is not UNSET:
            field_dict["backupServerName"] = backup_server_name
        if restore_points_count is not UNSET:
            field_dict["restorePointsCount"] = restore_points_count
        if platform_type is not UNSET:
            field_dict["platformType"] = platform_type
        if last_backup is not UNSET:
            field_dict["lastBackup"] = last_backup
        if location_uid is not UNSET:
            field_dict["locationUid"] = location_uid
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        instance_id = d.pop("instanceId", UNSET)

        def _parse_account_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                account_uid_type_0 = UUID(data)

                return account_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        account_uid = _parse_account_uid(d.pop("accountUid", UNSET))

        account_name = d.pop("accountName", UNSET)

        def _parse_subscription_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subscription_uid_type_0 = UUID(data)

                return subscription_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        subscription_uid = _parse_subscription_uid(d.pop("subscriptionUid", UNSET))

        subscription_name = d.pop("subscriptionName", UNSET)

        region_tag = d.pop("regionTag", UNSET)

        region_name = d.pop("regionName", UNSET)

        _policy_uid = d.pop("policyUid", UNSET)
        policy_uid: UUID | Unset
        if isinstance(_policy_uid, Unset):
            policy_uid = UNSET
        else:
            policy_uid = UUID(_policy_uid)

        policy_name = d.pop("policyName", UNSET)

        def _parse_appliance_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                appliance_uid_type_0 = UUID(data)

                return appliance_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        appliance_uid = _parse_appliance_uid(d.pop("applianceUid", UNSET))

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: UUID | Unset
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        backup_server_name = d.pop("backupServerName", UNSET)

        restore_points_count = d.pop("restorePointsCount", UNSET)

        _platform_type = d.pop("platformType", UNSET)
        platform_type: BackupServerPublicCloudAppliancePlatform | Unset
        if isinstance(_platform_type, Unset):
            platform_type = UNSET
        else:
            platform_type = BackupServerPublicCloudAppliancePlatform(_platform_type)

        _last_backup = d.pop("lastBackup", UNSET)
        last_backup: datetime.datetime | Unset
        if isinstance(_last_backup, Unset):
            last_backup = UNSET
        else:
            last_backup = isoparse(_last_backup)

        _location_uid = d.pop("locationUid", UNSET)
        location_uid: UUID | Unset
        if isinstance(_location_uid, Unset):
            location_uid = UNSET
        else:
            location_uid = UUID(_location_uid)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: UUID | Unset
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        protected_cloud_network = cls(
            instance_id=instance_id,
            account_uid=account_uid,
            account_name=account_name,
            subscription_uid=subscription_uid,
            subscription_name=subscription_name,
            region_tag=region_tag,
            region_name=region_name,
            policy_uid=policy_uid,
            policy_name=policy_name,
            appliance_uid=appliance_uid,
            backup_server_uid=backup_server_uid,
            backup_server_name=backup_server_name,
            restore_points_count=restore_points_count,
            platform_type=platform_type,
            last_backup=last_backup,
            location_uid=location_uid,
            organization_uid=organization_uid,
        )

        protected_cloud_network.additional_properties = d
        return protected_cloud_network

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
