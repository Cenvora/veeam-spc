import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.protected_cloud_database_engine_type import ProtectedCloudDatabaseEngineType
from ..models.protected_cloud_database_platform import ProtectedCloudDatabasePlatform
from ..models.public_cloud_database_type import PublicCloudDatabaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedCloudDatabase")


@_attrs_define
class ProtectedCloudDatabase:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a protected public cloud database.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a backup server.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization.
        name (Union[Unset, str]): Name of a protected public cloud database.
        appliance_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup for Public Clouds appliance.
        region (Union[Unset, str]): Region where protected public cloud database is located.
        resource_id (Union[Unset, str]): Resource ID assigned to a database server in public cloud.
        hierarchy_root_name (Union[Unset, str]): Name of a Veeam Backup for Microsoft 365 appliance.
        latest_backup_date (Union[Unset, datetime.datetime]): Date and time of the latest successful backup job run
            protecting a public cloud database.
        latest_archive_date (Union[Unset, datetime.datetime]): Date and time of the latest successful archiving job run
            protecting public cloud database backups.
        latest_snapshot_date (Union[Unset, datetime.datetime]): Data and time when the latest public cloud database
            snapshot was created.
        latest_replica_snapshot_date (Union[Unset, datetime.datetime]): Date and time when the latest replica snapshot
            of a public cloud database was created.
        backup_count (Union[Unset, int]): Number of backup files.
        archive_count (Union[Unset, int]): Number of archived backup files.
        snapshot_count (Union[Unset, int]): Number of snapshots.
        replica_snapshot_count (Union[Unset, int]): Number of replica snapshots.
        instance_size (Union[Unset, int]): Size of a public cloud database.
        total_size (Union[Unset, int]): Size of all backups and snapshots of a public cloud database.
        platform (Union[Unset, ProtectedCloudDatabasePlatform]): Public cloud platform.
        database_type (Union[Unset, PublicCloudDatabaseType]): Type of a cloud database included in a policy.
        engine_type (Union[Unset, ProtectedCloudDatabaseEngineType]): Database platform.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    appliance_uid: Union[Unset, UUID] = UNSET
    region: Union[Unset, str] = UNSET
    resource_id: Union[Unset, str] = UNSET
    hierarchy_root_name: Union[Unset, str] = UNSET
    latest_backup_date: Union[Unset, datetime.datetime] = UNSET
    latest_archive_date: Union[Unset, datetime.datetime] = UNSET
    latest_snapshot_date: Union[Unset, datetime.datetime] = UNSET
    latest_replica_snapshot_date: Union[Unset, datetime.datetime] = UNSET
    backup_count: Union[Unset, int] = UNSET
    archive_count: Union[Unset, int] = UNSET
    snapshot_count: Union[Unset, int] = UNSET
    replica_snapshot_count: Union[Unset, int] = UNSET
    instance_size: Union[Unset, int] = UNSET
    total_size: Union[Unset, int] = UNSET
    platform: Union[Unset, ProtectedCloudDatabasePlatform] = UNSET
    database_type: Union[Unset, PublicCloudDatabaseType] = UNSET
    engine_type: Union[Unset, ProtectedCloudDatabaseEngineType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

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

        region = self.region

        resource_id = self.resource_id

        hierarchy_root_name = self.hierarchy_root_name

        latest_backup_date: Union[Unset, str] = UNSET
        if not isinstance(self.latest_backup_date, Unset):
            latest_backup_date = self.latest_backup_date.isoformat()

        latest_archive_date: Union[Unset, str] = UNSET
        if not isinstance(self.latest_archive_date, Unset):
            latest_archive_date = self.latest_archive_date.isoformat()

        latest_snapshot_date: Union[Unset, str] = UNSET
        if not isinstance(self.latest_snapshot_date, Unset):
            latest_snapshot_date = self.latest_snapshot_date.isoformat()

        latest_replica_snapshot_date: Union[Unset, str] = UNSET
        if not isinstance(self.latest_replica_snapshot_date, Unset):
            latest_replica_snapshot_date = self.latest_replica_snapshot_date.isoformat()

        backup_count = self.backup_count

        archive_count = self.archive_count

        snapshot_count = self.snapshot_count

        replica_snapshot_count = self.replica_snapshot_count

        instance_size = self.instance_size

        total_size = self.total_size

        platform: Union[Unset, str] = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        database_type: Union[Unset, str] = UNSET
        if not isinstance(self.database_type, Unset):
            database_type = self.database_type.value

        engine_type: Union[Unset, str] = UNSET
        if not isinstance(self.engine_type, Unset):
            engine_type = self.engine_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if name is not UNSET:
            field_dict["name"] = name
        if appliance_uid is not UNSET:
            field_dict["applianceUid"] = appliance_uid
        if region is not UNSET:
            field_dict["region"] = region
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if hierarchy_root_name is not UNSET:
            field_dict["hierarchyRootName"] = hierarchy_root_name
        if latest_backup_date is not UNSET:
            field_dict["latestBackupDate"] = latest_backup_date
        if latest_archive_date is not UNSET:
            field_dict["latestArchiveDate"] = latest_archive_date
        if latest_snapshot_date is not UNSET:
            field_dict["latestSnapshotDate"] = latest_snapshot_date
        if latest_replica_snapshot_date is not UNSET:
            field_dict["latestReplicaSnapshotDate"] = latest_replica_snapshot_date
        if backup_count is not UNSET:
            field_dict["backupCount"] = backup_count
        if archive_count is not UNSET:
            field_dict["archiveCount"] = archive_count
        if snapshot_count is not UNSET:
            field_dict["snapshotCount"] = snapshot_count
        if replica_snapshot_count is not UNSET:
            field_dict["replicaSnapshotCount"] = replica_snapshot_count
        if instance_size is not UNSET:
            field_dict["instanceSize"] = instance_size
        if total_size is not UNSET:
            field_dict["totalSize"] = total_size
        if platform is not UNSET:
            field_dict["platform"] = platform
        if database_type is not UNSET:
            field_dict["databaseType"] = database_type
        if engine_type is not UNSET:
            field_dict["engineType"] = engine_type

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

        region = d.pop("region", UNSET)

        resource_id = d.pop("resourceId", UNSET)

        hierarchy_root_name = d.pop("hierarchyRootName", UNSET)

        _latest_backup_date = d.pop("latestBackupDate", UNSET)
        latest_backup_date: Union[Unset, datetime.datetime]
        if isinstance(_latest_backup_date, Unset):
            latest_backup_date = UNSET
        else:
            latest_backup_date = isoparse(_latest_backup_date)

        _latest_archive_date = d.pop("latestArchiveDate", UNSET)
        latest_archive_date: Union[Unset, datetime.datetime]
        if isinstance(_latest_archive_date, Unset):
            latest_archive_date = UNSET
        else:
            latest_archive_date = isoparse(_latest_archive_date)

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

        backup_count = d.pop("backupCount", UNSET)

        archive_count = d.pop("archiveCount", UNSET)

        snapshot_count = d.pop("snapshotCount", UNSET)

        replica_snapshot_count = d.pop("replicaSnapshotCount", UNSET)

        instance_size = d.pop("instanceSize", UNSET)

        total_size = d.pop("totalSize", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: Union[Unset, ProtectedCloudDatabasePlatform]
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = ProtectedCloudDatabasePlatform(_platform)

        _database_type = d.pop("databaseType", UNSET)
        database_type: Union[Unset, PublicCloudDatabaseType]
        if isinstance(_database_type, Unset):
            database_type = UNSET
        else:
            database_type = PublicCloudDatabaseType(_database_type)

        _engine_type = d.pop("engineType", UNSET)
        engine_type: Union[Unset, ProtectedCloudDatabaseEngineType]
        if isinstance(_engine_type, Unset):
            engine_type = UNSET
        else:
            engine_type = ProtectedCloudDatabaseEngineType(_engine_type)

        protected_cloud_database = cls(
            instance_uid=instance_uid,
            backup_server_uid=backup_server_uid,
            organization_uid=organization_uid,
            name=name,
            appliance_uid=appliance_uid,
            region=region,
            resource_id=resource_id,
            hierarchy_root_name=hierarchy_root_name,
            latest_backup_date=latest_backup_date,
            latest_archive_date=latest_archive_date,
            latest_snapshot_date=latest_snapshot_date,
            latest_replica_snapshot_date=latest_replica_snapshot_date,
            backup_count=backup_count,
            archive_count=archive_count,
            snapshot_count=snapshot_count,
            replica_snapshot_count=replica_snapshot_count,
            instance_size=instance_size,
            total_size=total_size,
            platform=platform,
            database_type=database_type,
            engine_type=engine_type,
        )

        protected_cloud_database.additional_properties = d
        return protected_cloud_database

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
