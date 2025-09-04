import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedObjectStorage")


@_attrs_define
class ProtectedObjectStorage:
    """
    Attributes:
        object_storage_uid (Union[Unset, UUID]): UID assigned to an object storage.
        bucket_uid (Union[Unset, UUID]): UID assigned to an object storage bucket.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a backup server.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization.
        object_storage_name (Union[Unset, str]): Name of an object storage.
        bucket_name (Union[Unset, str]): Name of an object storage bucket.
        latest_restore_point_date (Union[None, Unset, datetime.datetime]): Date and time of the latest restore point
            creation.
        total_archive_size (Union[Unset, int]): Size of archived file copies, in bytes.
        total_short_term_backup_size (Union[Unset, int]): Size of recent file copies, in bytes.
        archive_restore_points (Union[Unset, int]): Number of restore points for long-term retention.
        restore_points (Union[Unset, int]): Number of restore points.
    """

    object_storage_uid: Union[Unset, UUID] = UNSET
    bucket_uid: Union[Unset, UUID] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    object_storage_name: Union[Unset, str] = UNSET
    bucket_name: Union[Unset, str] = UNSET
    latest_restore_point_date: Union[None, Unset, datetime.datetime] = UNSET
    total_archive_size: Union[Unset, int] = UNSET
    total_short_term_backup_size: Union[Unset, int] = UNSET
    archive_restore_points: Union[Unset, int] = UNSET
    restore_points: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_storage_uid: Union[Unset, str] = UNSET
        if not isinstance(self.object_storage_uid, Unset):
            object_storage_uid = str(self.object_storage_uid)

        bucket_uid: Union[Unset, str] = UNSET
        if not isinstance(self.bucket_uid, Unset):
            bucket_uid = str(self.bucket_uid)

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        object_storage_name = self.object_storage_name

        bucket_name = self.bucket_name

        latest_restore_point_date: Union[None, Unset, str]
        if isinstance(self.latest_restore_point_date, Unset):
            latest_restore_point_date = UNSET
        elif isinstance(self.latest_restore_point_date, datetime.datetime):
            latest_restore_point_date = self.latest_restore_point_date.isoformat()
        else:
            latest_restore_point_date = self.latest_restore_point_date

        total_archive_size = self.total_archive_size

        total_short_term_backup_size = self.total_short_term_backup_size

        archive_restore_points = self.archive_restore_points

        restore_points = self.restore_points

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_storage_uid is not UNSET:
            field_dict["objectStorageUid"] = object_storage_uid
        if bucket_uid is not UNSET:
            field_dict["bucketUid"] = bucket_uid
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if object_storage_name is not UNSET:
            field_dict["objectStorageName"] = object_storage_name
        if bucket_name is not UNSET:
            field_dict["bucketName"] = bucket_name
        if latest_restore_point_date is not UNSET:
            field_dict["latestRestorePointDate"] = latest_restore_point_date
        if total_archive_size is not UNSET:
            field_dict["totalArchiveSize"] = total_archive_size
        if total_short_term_backup_size is not UNSET:
            field_dict["totalShortTermBackupSize"] = total_short_term_backup_size
        if archive_restore_points is not UNSET:
            field_dict["archiveRestorePoints"] = archive_restore_points
        if restore_points is not UNSET:
            field_dict["restorePoints"] = restore_points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _object_storage_uid = d.pop("objectStorageUid", UNSET)
        object_storage_uid: Union[Unset, UUID]
        if isinstance(_object_storage_uid, Unset):
            object_storage_uid = UNSET
        else:
            object_storage_uid = UUID(_object_storage_uid)

        _bucket_uid = d.pop("bucketUid", UNSET)
        bucket_uid: Union[Unset, UUID]
        if isinstance(_bucket_uid, Unset):
            bucket_uid = UNSET
        else:
            bucket_uid = UUID(_bucket_uid)

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

        object_storage_name = d.pop("objectStorageName", UNSET)

        bucket_name = d.pop("bucketName", UNSET)

        def _parse_latest_restore_point_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                latest_restore_point_date_type_0 = isoparse(data)

                return latest_restore_point_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        latest_restore_point_date = _parse_latest_restore_point_date(d.pop("latestRestorePointDate", UNSET))

        total_archive_size = d.pop("totalArchiveSize", UNSET)

        total_short_term_backup_size = d.pop("totalShortTermBackupSize", UNSET)

        archive_restore_points = d.pop("archiveRestorePoints", UNSET)

        restore_points = d.pop("restorePoints", UNSET)

        protected_object_storage = cls(
            object_storage_uid=object_storage_uid,
            bucket_uid=bucket_uid,
            backup_server_uid=backup_server_uid,
            organization_uid=organization_uid,
            object_storage_name=object_storage_name,
            bucket_name=bucket_name,
            latest_restore_point_date=latest_restore_point_date,
            total_archive_size=total_archive_size,
            total_short_term_backup_size=total_short_term_backup_size,
            archive_restore_points=archive_restore_points,
            restore_points=restore_points,
        )

        protected_object_storage.additional_properties = d
        return protected_object_storage

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
