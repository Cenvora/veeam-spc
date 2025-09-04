import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
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
        instance_id (Union[Unset, str]): ID assigned to a cloud network.
        account_uid (Union[Unset, UUID]): UID assigned to a public cloud account.
        account_name (Union[Unset, str]): Name of a public cloud account.
        subscription_uid (Union[Unset, UUID]): UID assigned to a cloud subscription.
        subscription_name (Union[Unset, str]): Name of a cloud subscription.
        region_tag (Union[Unset, str]): Tag of a cloud network region.
        region_name (Union[Unset, str]): Name of a cloud network region.
        policy_uid (Union[Unset, UUID]): UID assigned to a cloud network policy.
        policy_name (Union[Unset, str]): Name of a cloud network policy.
        appliance_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup for Public Clouds appliance.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup & Replication server.
        backup_server_name (Union[Unset, str]): Name of a Veeam Backup & Replication server.
        restore_points_count (Union[Unset, int]): Number of restore points.
        platform_type (Union[Unset, BackupServerPublicCloudAppliancePlatform]): Platform of a Veeam Backup for Public
            Clouds appliance.
        last_backup (Union[Unset, datetime.datetime]): Date and time when the latest backup was created.
        location_uid (Union[Unset, UUID]): UID assigned to a cloud network location.
        organization_uid (Union[Unset, UUID]): UID assigned to a mapped organization.
    """

    instance_id: Union[Unset, str] = UNSET
    account_uid: Union[Unset, UUID] = UNSET
    account_name: Union[Unset, str] = UNSET
    subscription_uid: Union[Unset, UUID] = UNSET
    subscription_name: Union[Unset, str] = UNSET
    region_tag: Union[Unset, str] = UNSET
    region_name: Union[Unset, str] = UNSET
    policy_uid: Union[Unset, UUID] = UNSET
    policy_name: Union[Unset, str] = UNSET
    appliance_uid: Union[Unset, UUID] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    backup_server_name: Union[Unset, str] = UNSET
    restore_points_count: Union[Unset, int] = UNSET
    platform_type: Union[Unset, BackupServerPublicCloudAppliancePlatform] = UNSET
    last_backup: Union[Unset, datetime.datetime] = UNSET
    location_uid: Union[Unset, UUID] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_id = self.instance_id

        account_uid: Union[Unset, str] = UNSET
        if not isinstance(self.account_uid, Unset):
            account_uid = str(self.account_uid)

        account_name = self.account_name

        subscription_uid: Union[Unset, str] = UNSET
        if not isinstance(self.subscription_uid, Unset):
            subscription_uid = str(self.subscription_uid)

        subscription_name = self.subscription_name

        region_tag = self.region_tag

        region_name = self.region_name

        policy_uid: Union[Unset, str] = UNSET
        if not isinstance(self.policy_uid, Unset):
            policy_uid = str(self.policy_uid)

        policy_name = self.policy_name

        appliance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.appliance_uid, Unset):
            appliance_uid = str(self.appliance_uid)

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        backup_server_name = self.backup_server_name

        restore_points_count = self.restore_points_count

        platform_type: Union[Unset, str] = UNSET
        if not isinstance(self.platform_type, Unset):
            platform_type = self.platform_type.value

        last_backup: Union[Unset, str] = UNSET
        if not isinstance(self.last_backup, Unset):
            last_backup = self.last_backup.isoformat()

        location_uid: Union[Unset, str] = UNSET
        if not isinstance(self.location_uid, Unset):
            location_uid = str(self.location_uid)

        organization_uid: Union[Unset, str] = UNSET
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

        _account_uid = d.pop("accountUid", UNSET)
        account_uid: Union[Unset, UUID]
        if isinstance(_account_uid, Unset):
            account_uid = UNSET
        else:
            account_uid = UUID(_account_uid)

        account_name = d.pop("accountName", UNSET)

        _subscription_uid = d.pop("subscriptionUid", UNSET)
        subscription_uid: Union[Unset, UUID]
        if isinstance(_subscription_uid, Unset):
            subscription_uid = UNSET
        else:
            subscription_uid = UUID(_subscription_uid)

        subscription_name = d.pop("subscriptionName", UNSET)

        region_tag = d.pop("regionTag", UNSET)

        region_name = d.pop("regionName", UNSET)

        _policy_uid = d.pop("policyUid", UNSET)
        policy_uid: Union[Unset, UUID]
        if isinstance(_policy_uid, Unset):
            policy_uid = UNSET
        else:
            policy_uid = UUID(_policy_uid)

        policy_name = d.pop("policyName", UNSET)

        _appliance_uid = d.pop("applianceUid", UNSET)
        appliance_uid: Union[Unset, UUID]
        if isinstance(_appliance_uid, Unset):
            appliance_uid = UNSET
        else:
            appliance_uid = UUID(_appliance_uid)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: Union[Unset, UUID]
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        backup_server_name = d.pop("backupServerName", UNSET)

        restore_points_count = d.pop("restorePointsCount", UNSET)

        _platform_type = d.pop("platformType", UNSET)
        platform_type: Union[Unset, BackupServerPublicCloudAppliancePlatform]
        if isinstance(_platform_type, Unset):
            platform_type = UNSET
        else:
            platform_type = BackupServerPublicCloudAppliancePlatform(_platform_type)

        _last_backup = d.pop("lastBackup", UNSET)
        last_backup: Union[Unset, datetime.datetime]
        if isinstance(_last_backup, Unset):
            last_backup = UNSET
        else:
            last_backup = isoparse(_last_backup)

        _location_uid = d.pop("locationUid", UNSET)
        location_uid: Union[Unset, UUID]
        if isinstance(_location_uid, Unset):
            location_uid = UNSET
        else:
            location_uid = UUID(_location_uid)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
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
