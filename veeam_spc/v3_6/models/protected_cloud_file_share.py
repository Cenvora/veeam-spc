import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.protected_cloud_file_share_platform import ProtectedCloudFileSharePlatform
from ..models.public_cloud_file_share_type import PublicCloudFileShareType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedCloudFileShare")


@_attrs_define
class ProtectedCloudFileShare:
    """
    Attributes:
        file_share_uid (Union[Unset, UUID]): UID assigned to a file share.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a backup server.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization.
        name (Union[Unset, str]): Name of a file share.
        appliance_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup for Public Clouds appliance.
        resource_id (Union[Unset, str]): ID assigned to a file share in public cloud infrastructure.
        platform (Union[Unset, ProtectedCloudFileSharePlatform]): Public cloud platform.
        file_share_type (Union[Unset, PublicCloudFileShareType]): Public cloud fileshare type.
        snapshots_count (Union[Unset, int]): Number of snapshots.
        policy_count (Union[Unset, int]): Number of backup policies protecting a file share.
        replica_snapshots_count (Union[Unset, int]): Number of replica snapshots.
        latest_snapshot_date (Union[Unset, datetime.datetime]): Date and time when the latest snapshot was created.
        latest_replica_snapshot_date (Union[Unset, datetime.datetime]): Date and time when the latest replica snapshot
            was created.
    """

    file_share_uid: Union[Unset, UUID] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    appliance_uid: Union[Unset, UUID] = UNSET
    resource_id: Union[Unset, str] = UNSET
    platform: Union[Unset, ProtectedCloudFileSharePlatform] = UNSET
    file_share_type: Union[Unset, PublicCloudFileShareType] = UNSET
    snapshots_count: Union[Unset, int] = UNSET
    policy_count: Union[Unset, int] = UNSET
    replica_snapshots_count: Union[Unset, int] = UNSET
    latest_snapshot_date: Union[Unset, datetime.datetime] = UNSET
    latest_replica_snapshot_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_share_uid: Union[Unset, str] = UNSET
        if not isinstance(self.file_share_uid, Unset):
            file_share_uid = str(self.file_share_uid)

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        name = self.name

        appliance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.appliance_uid, Unset):
            appliance_uid = str(self.appliance_uid)

        resource_id = self.resource_id

        platform: Union[Unset, str] = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        file_share_type: Union[Unset, str] = UNSET
        if not isinstance(self.file_share_type, Unset):
            file_share_type = self.file_share_type.value

        snapshots_count = self.snapshots_count

        policy_count = self.policy_count

        replica_snapshots_count = self.replica_snapshots_count

        latest_snapshot_date: Union[Unset, str] = UNSET
        if not isinstance(self.latest_snapshot_date, Unset):
            latest_snapshot_date = self.latest_snapshot_date.isoformat()

        latest_replica_snapshot_date: Union[Unset, str] = UNSET
        if not isinstance(self.latest_replica_snapshot_date, Unset):
            latest_replica_snapshot_date = self.latest_replica_snapshot_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_share_uid is not UNSET:
            field_dict["fileShareUid"] = file_share_uid
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if name is not UNSET:
            field_dict["name"] = name
        if appliance_uid is not UNSET:
            field_dict["applianceUid"] = appliance_uid
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if platform is not UNSET:
            field_dict["platform"] = platform
        if file_share_type is not UNSET:
            field_dict["fileShareType"] = file_share_type
        if snapshots_count is not UNSET:
            field_dict["snapshotsCount"] = snapshots_count
        if policy_count is not UNSET:
            field_dict["policyCount"] = policy_count
        if replica_snapshots_count is not UNSET:
            field_dict["replicaSnapshotsCount"] = replica_snapshots_count
        if latest_snapshot_date is not UNSET:
            field_dict["latestSnapshotDate"] = latest_snapshot_date
        if latest_replica_snapshot_date is not UNSET:
            field_dict["latestReplicaSnapshotDate"] = latest_replica_snapshot_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _file_share_uid = d.pop("fileShareUid", UNSET)
        file_share_uid: Union[Unset, UUID]
        if isinstance(_file_share_uid, Unset):
            file_share_uid = UNSET
        else:
            file_share_uid = UUID(_file_share_uid)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: Union[Unset, UUID]
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        name = d.pop("name", UNSET)

        _appliance_uid = d.pop("applianceUid", UNSET)
        appliance_uid: Union[Unset, UUID]
        if isinstance(_appliance_uid, Unset):
            appliance_uid = UNSET
        else:
            appliance_uid = UUID(_appliance_uid)

        resource_id = d.pop("resourceId", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: Union[Unset, ProtectedCloudFileSharePlatform]
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = ProtectedCloudFileSharePlatform(_platform)

        _file_share_type = d.pop("fileShareType", UNSET)
        file_share_type: Union[Unset, PublicCloudFileShareType]
        if isinstance(_file_share_type, Unset):
            file_share_type = UNSET
        else:
            file_share_type = PublicCloudFileShareType(_file_share_type)

        snapshots_count = d.pop("snapshotsCount", UNSET)

        policy_count = d.pop("policyCount", UNSET)

        replica_snapshots_count = d.pop("replicaSnapshotsCount", UNSET)

        _latest_snapshot_date = d.pop("latestSnapshotDate", UNSET)
        latest_snapshot_date: Union[Unset, datetime.datetime]
        if isinstance(_latest_snapshot_date, Unset):
            latest_snapshot_date = UNSET
        else:
            latest_snapshot_date = isoparse(_latest_snapshot_date)

        _latest_replica_snapshot_date = d.pop("latestReplicaSnapshotDate", UNSET)
        latest_replica_snapshot_date: Union[Unset, datetime.datetime]
        if isinstance(_latest_replica_snapshot_date, Unset):
            latest_replica_snapshot_date = UNSET
        else:
            latest_replica_snapshot_date = isoparse(_latest_replica_snapshot_date)

        protected_cloud_file_share = cls(
            file_share_uid=file_share_uid,
            backup_server_uid=backup_server_uid,
            organization_uid=organization_uid,
            name=name,
            appliance_uid=appliance_uid,
            resource_id=resource_id,
            platform=platform,
            file_share_type=file_share_type,
            snapshots_count=snapshots_count,
            policy_count=policy_count,
            replica_snapshots_count=replica_snapshots_count,
            latest_snapshot_date=latest_snapshot_date,
            latest_replica_snapshot_date=latest_replica_snapshot_date,
        )

        protected_cloud_file_share.additional_properties = d
        return protected_cloud_file_share

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
