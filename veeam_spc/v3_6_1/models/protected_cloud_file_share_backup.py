import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.public_cloud_file_share_type import PublicCloudFileShareType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedCloudFileShareBackup")


@_attrs_define
class ProtectedCloudFileShareBackup:
    """
    Attributes:
        file_share_uid (Union[Unset, UUID]): UID assigned to a file share.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a backup server.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization.
        policy_uid (Union[None, UUID, Unset]): UID assigned to a backup policy.
        policy_name (Union[None, Unset, str]): Name of a backup policy.
        region (Union[Unset, str]): Region where a file share is located.
        replica_region (Union[Unset, str]): Region where a file share replica is located.
        file_share_type (Union[Unset, PublicCloudFileShareType]): Public cloud fileshare type.
        name (Union[Unset, str]): Name of a file share.
        snapshots_count (Union[Unset, int]): Number of file share snaphots.
        replica_snapshots_count (Union[Unset, int]): Number of file share replica snapshots.
        latest_snapshot_date (Union[None, Unset, datetime.datetime]): Date and time when the latest file share snapshot
            was created.
        latest_replica_snapshot_date (Union[None, Unset, datetime.datetime]): Date and time when the latest file share
            replica snapshot was created.
        total_size (Union[None, Unset, int]): Total size of file share and file share replica snapshots, in bytes.
    """

    file_share_uid: Union[Unset, UUID] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    policy_uid: Union[None, UUID, Unset] = UNSET
    policy_name: Union[None, Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    replica_region: Union[Unset, str] = UNSET
    file_share_type: Union[Unset, PublicCloudFileShareType] = UNSET
    name: Union[Unset, str] = UNSET
    snapshots_count: Union[Unset, int] = UNSET
    replica_snapshots_count: Union[Unset, int] = UNSET
    latest_snapshot_date: Union[None, Unset, datetime.datetime] = UNSET
    latest_replica_snapshot_date: Union[None, Unset, datetime.datetime] = UNSET
    total_size: Union[None, Unset, int] = UNSET
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

        policy_uid: Union[None, Unset, str]
        if isinstance(self.policy_uid, Unset):
            policy_uid = UNSET
        elif isinstance(self.policy_uid, UUID):
            policy_uid = str(self.policy_uid)
        else:
            policy_uid = self.policy_uid

        policy_name: Union[None, Unset, str]
        if isinstance(self.policy_name, Unset):
            policy_name = UNSET
        else:
            policy_name = self.policy_name

        region = self.region

        replica_region = self.replica_region

        file_share_type: Union[Unset, str] = UNSET
        if not isinstance(self.file_share_type, Unset):
            file_share_type = self.file_share_type.value

        name = self.name

        snapshots_count = self.snapshots_count

        replica_snapshots_count = self.replica_snapshots_count

        latest_snapshot_date: Union[None, Unset, str]
        if isinstance(self.latest_snapshot_date, Unset):
            latest_snapshot_date = UNSET
        elif isinstance(self.latest_snapshot_date, datetime.datetime):
            latest_snapshot_date = self.latest_snapshot_date.isoformat()
        else:
            latest_snapshot_date = self.latest_snapshot_date

        latest_replica_snapshot_date: Union[None, Unset, str]
        if isinstance(self.latest_replica_snapshot_date, Unset):
            latest_replica_snapshot_date = UNSET
        elif isinstance(self.latest_replica_snapshot_date, datetime.datetime):
            latest_replica_snapshot_date = self.latest_replica_snapshot_date.isoformat()
        else:
            latest_replica_snapshot_date = self.latest_replica_snapshot_date

        total_size: Union[None, Unset, int]
        if isinstance(self.total_size, Unset):
            total_size = UNSET
        else:
            total_size = self.total_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_share_uid is not UNSET:
            field_dict["fileShareUid"] = file_share_uid
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if policy_uid is not UNSET:
            field_dict["policyUid"] = policy_uid
        if policy_name is not UNSET:
            field_dict["policyName"] = policy_name
        if region is not UNSET:
            field_dict["region"] = region
        if replica_region is not UNSET:
            field_dict["replicaRegion"] = replica_region
        if file_share_type is not UNSET:
            field_dict["fileShareType"] = file_share_type
        if name is not UNSET:
            field_dict["name"] = name
        if snapshots_count is not UNSET:
            field_dict["snapshotsCount"] = snapshots_count
        if replica_snapshots_count is not UNSET:
            field_dict["replicaSnapshotsCount"] = replica_snapshots_count
        if latest_snapshot_date is not UNSET:
            field_dict["latestSnapshotDate"] = latest_snapshot_date
        if latest_replica_snapshot_date is not UNSET:
            field_dict["latestReplicaSnapshotDate"] = latest_replica_snapshot_date
        if total_size is not UNSET:
            field_dict["totalSize"] = total_size

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

        def _parse_policy_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                policy_uid_type_0 = UUID(data)

                return policy_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        policy_uid = _parse_policy_uid(d.pop("policyUid", UNSET))

        def _parse_policy_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        policy_name = _parse_policy_name(d.pop("policyName", UNSET))

        region = d.pop("region", UNSET)

        replica_region = d.pop("replicaRegion", UNSET)

        _file_share_type = d.pop("fileShareType", UNSET)
        file_share_type: Union[Unset, PublicCloudFileShareType]
        if isinstance(_file_share_type, Unset):
            file_share_type = UNSET
        else:
            file_share_type = PublicCloudFileShareType(_file_share_type)

        name = d.pop("name", UNSET)

        snapshots_count = d.pop("snapshotsCount", UNSET)

        replica_snapshots_count = d.pop("replicaSnapshotsCount", UNSET)

        def _parse_latest_snapshot_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                latest_snapshot_date_type_0 = isoparse(data)

                return latest_snapshot_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        latest_snapshot_date = _parse_latest_snapshot_date(d.pop("latestSnapshotDate", UNSET))

        def _parse_latest_replica_snapshot_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                latest_replica_snapshot_date_type_0 = isoparse(data)

                return latest_replica_snapshot_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        latest_replica_snapshot_date = _parse_latest_replica_snapshot_date(d.pop("latestReplicaSnapshotDate", UNSET))

        def _parse_total_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_size = _parse_total_size(d.pop("totalSize", UNSET))

        protected_cloud_file_share_backup = cls(
            file_share_uid=file_share_uid,
            backup_server_uid=backup_server_uid,
            organization_uid=organization_uid,
            policy_uid=policy_uid,
            policy_name=policy_name,
            region=region,
            replica_region=replica_region,
            file_share_type=file_share_type,
            name=name,
            snapshots_count=snapshots_count,
            replica_snapshots_count=replica_snapshots_count,
            latest_snapshot_date=latest_snapshot_date,
            latest_replica_snapshot_date=latest_replica_snapshot_date,
            total_size=total_size,
        )

        protected_cloud_file_share_backup.additional_properties = d
        return protected_cloud_file_share_backup

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
