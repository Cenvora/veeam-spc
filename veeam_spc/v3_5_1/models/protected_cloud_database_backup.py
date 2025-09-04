import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.protected_cloud_database_backup_backup_type import ProtectedCloudDatabaseBackupBackupType
from ..models.protected_cloud_database_engine_type import ProtectedCloudDatabaseEngineType
from ..models.public_cloud_database_type import PublicCloudDatabaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedCloudDatabaseBackup")


@_attrs_define
class ProtectedCloudDatabaseBackup:
    """
    Attributes:
        database_uid (Union[Unset, UUID]): UID assigned to a database.
        policy_uid (Union[Unset, UUID]): UID assigned to a backup policy.
        policy_name (Union[Unset, str]): Name of a backup policy.
        backup_type (Union[Unset, ProtectedCloudDatabaseBackupBackupType]): Backup policy type.
        size (Union[Unset, int]): Total size of a backup chain, in bytes.
            > For the `Snapshot` and `ReplicaSnapshot` policy types, size of a database server, in bytes.
        destinations (Union[Unset, list[str]]): Array of target backup vaults.
        restore_points (Union[Unset, int]): Number of restore points.
        latest_restore_point_date (Union[Unset, datetime.datetime]): Date and time of the latest restore point creation.
        database_type (Union[Unset, PublicCloudDatabaseType]): Type of a cloud database included in a policy.
        engine_type (Union[Unset, ProtectedCloudDatabaseEngineType]): Database platform.
    """

    database_uid: Union[Unset, UUID] = UNSET
    policy_uid: Union[Unset, UUID] = UNSET
    policy_name: Union[Unset, str] = UNSET
    backup_type: Union[Unset, ProtectedCloudDatabaseBackupBackupType] = UNSET
    size: Union[Unset, int] = UNSET
    destinations: Union[Unset, list[str]] = UNSET
    restore_points: Union[Unset, int] = UNSET
    latest_restore_point_date: Union[Unset, datetime.datetime] = UNSET
    database_type: Union[Unset, PublicCloudDatabaseType] = UNSET
    engine_type: Union[Unset, ProtectedCloudDatabaseEngineType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        database_uid: Union[Unset, str] = UNSET
        if not isinstance(self.database_uid, Unset):
            database_uid = str(self.database_uid)

        policy_uid: Union[Unset, str] = UNSET
        if not isinstance(self.policy_uid, Unset):
            policy_uid = str(self.policy_uid)

        policy_name = self.policy_name

        backup_type: Union[Unset, str] = UNSET
        if not isinstance(self.backup_type, Unset):
            backup_type = self.backup_type.value

        size = self.size

        destinations: Union[Unset, list[str]] = UNSET
        if not isinstance(self.destinations, Unset):
            destinations = self.destinations

        restore_points = self.restore_points

        latest_restore_point_date: Union[Unset, str] = UNSET
        if not isinstance(self.latest_restore_point_date, Unset):
            latest_restore_point_date = self.latest_restore_point_date.isoformat()

        database_type: Union[Unset, str] = UNSET
        if not isinstance(self.database_type, Unset):
            database_type = self.database_type.value

        engine_type: Union[Unset, str] = UNSET
        if not isinstance(self.engine_type, Unset):
            engine_type = self.engine_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if database_uid is not UNSET:
            field_dict["databaseUid"] = database_uid
        if policy_uid is not UNSET:
            field_dict["policyUid"] = policy_uid
        if policy_name is not UNSET:
            field_dict["policyName"] = policy_name
        if backup_type is not UNSET:
            field_dict["backupType"] = backup_type
        if size is not UNSET:
            field_dict["size"] = size
        if destinations is not UNSET:
            field_dict["destinations"] = destinations
        if restore_points is not UNSET:
            field_dict["restorePoints"] = restore_points
        if latest_restore_point_date is not UNSET:
            field_dict["latestRestorePointDate"] = latest_restore_point_date
        if database_type is not UNSET:
            field_dict["databaseType"] = database_type
        if engine_type is not UNSET:
            field_dict["engineType"] = engine_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _database_uid = d.pop("databaseUid", UNSET)
        database_uid: Union[Unset, UUID]
        if isinstance(_database_uid, Unset):
            database_uid = UNSET
        else:
            database_uid = UUID(_database_uid)

        _policy_uid = d.pop("policyUid", UNSET)
        policy_uid: Union[Unset, UUID]
        if isinstance(_policy_uid, Unset):
            policy_uid = UNSET
        else:
            policy_uid = UUID(_policy_uid)

        policy_name = d.pop("policyName", UNSET)

        _backup_type = d.pop("backupType", UNSET)
        backup_type: Union[Unset, ProtectedCloudDatabaseBackupBackupType]
        if isinstance(_backup_type, Unset):
            backup_type = UNSET
        else:
            backup_type = ProtectedCloudDatabaseBackupBackupType(_backup_type)

        size = d.pop("size", UNSET)

        destinations = cast(list[str], d.pop("destinations", UNSET))

        restore_points = d.pop("restorePoints", UNSET)

        _latest_restore_point_date = d.pop("latestRestorePointDate", UNSET)
        latest_restore_point_date: Union[Unset, datetime.datetime]
        if isinstance(_latest_restore_point_date, Unset):
            latest_restore_point_date = UNSET
        else:
            latest_restore_point_date = isoparse(_latest_restore_point_date)

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

        protected_cloud_database_backup = cls(
            database_uid=database_uid,
            policy_uid=policy_uid,
            policy_name=policy_name,
            backup_type=backup_type,
            size=size,
            destinations=destinations,
            restore_points=restore_points,
            latest_restore_point_date=latest_restore_point_date,
            database_type=database_type,
            engine_type=engine_type,
        )

        protected_cloud_database_backup.additional_properties = d
        return protected_cloud_database_backup

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
