import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedObjectStorageRestorePoint")


@_attrs_define
class ProtectedObjectStorageRestorePoint:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a restore point.
        object_storage_uid (Union[Unset, UUID]): UID assigned to an object storage.
        bucket_uid (Union[Unset, UUID]): UID assigned to an object storage bucket.
        backup_uid (Union[None, UUID, Unset]): UID assigned to a backup.
        job_uid (Union[None, UUID, Unset]): UID assigned to a job.
        restore_point_date (Union[Unset, datetime.datetime]): Date and time of the restore point creation.
        size (Union[None, Unset, int]): Size of a restore point.
        is_archive (Union[Unset, bool]): Indicates whether an restore point is stored in an archive repository. Default:
            True.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    object_storage_uid: Union[Unset, UUID] = UNSET
    bucket_uid: Union[Unset, UUID] = UNSET
    backup_uid: Union[None, UUID, Unset] = UNSET
    job_uid: Union[None, UUID, Unset] = UNSET
    restore_point_date: Union[Unset, datetime.datetime] = UNSET
    size: Union[None, Unset, int] = UNSET
    is_archive: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        object_storage_uid: Union[Unset, str] = UNSET
        if not isinstance(self.object_storage_uid, Unset):
            object_storage_uid = str(self.object_storage_uid)

        bucket_uid: Union[Unset, str] = UNSET
        if not isinstance(self.bucket_uid, Unset):
            bucket_uid = str(self.bucket_uid)

        backup_uid: Union[None, Unset, str]
        if isinstance(self.backup_uid, Unset):
            backup_uid = UNSET
        elif isinstance(self.backup_uid, UUID):
            backup_uid = str(self.backup_uid)
        else:
            backup_uid = self.backup_uid

        job_uid: Union[None, Unset, str]
        if isinstance(self.job_uid, Unset):
            job_uid = UNSET
        elif isinstance(self.job_uid, UUID):
            job_uid = str(self.job_uid)
        else:
            job_uid = self.job_uid

        restore_point_date: Union[Unset, str] = UNSET
        if not isinstance(self.restore_point_date, Unset):
            restore_point_date = self.restore_point_date.isoformat()

        size: Union[None, Unset, int]
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        is_archive = self.is_archive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if object_storage_uid is not UNSET:
            field_dict["objectStorageUid"] = object_storage_uid
        if bucket_uid is not UNSET:
            field_dict["bucketUid"] = bucket_uid
        if backup_uid is not UNSET:
            field_dict["backupUid"] = backup_uid
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if restore_point_date is not UNSET:
            field_dict["restorePointDate"] = restore_point_date
        if size is not UNSET:
            field_dict["size"] = size
        if is_archive is not UNSET:
            field_dict["isArchive"] = is_archive

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

        def _parse_backup_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_uid_type_0 = UUID(data)

                return backup_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        backup_uid = _parse_backup_uid(d.pop("backupUid", UNSET))

        def _parse_job_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_uid_type_0 = UUID(data)

                return job_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        job_uid = _parse_job_uid(d.pop("jobUid", UNSET))

        _restore_point_date = d.pop("restorePointDate", UNSET)
        restore_point_date: Union[Unset, datetime.datetime]
        if isinstance(_restore_point_date, Unset):
            restore_point_date = UNSET
        else:
            restore_point_date = isoparse(_restore_point_date)

        def _parse_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        size = _parse_size(d.pop("size", UNSET))

        is_archive = d.pop("isArchive", UNSET)

        protected_object_storage_restore_point = cls(
            instance_uid=instance_uid,
            object_storage_uid=object_storage_uid,
            bucket_uid=bucket_uid,
            backup_uid=backup_uid,
            job_uid=job_uid,
            restore_point_date=restore_point_date,
            size=size,
            is_archive=is_archive,
        )

        protected_object_storage_restore_point.additional_properties = d
        return protected_object_storage_restore_point

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
