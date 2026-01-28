import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.protected_object_storage_source import ProtectedObjectStorageSource


T = TypeVar("T", bound="ProtectedObjectStorageBackup")


@_attrs_define
class ProtectedObjectStorageBackup:
    """
    Attributes:
        object_storage_uid (Union[Unset, UUID]): UID assigned to an object storage.
        bucket_uid (Union[Unset, UUID]): UID assigned to an object storage bucket.
        job_uid (Union[None, UUID, Unset]): UID assigned to a backup job that protects an object storage.
        backup_uid (Union[None, UUID, Unset]): UID assigned to a backup.
        repository_uid (Union[Unset, UUID]): UID assigned to a backup repository.
        archive_repository_uid (Union[None, UUID, Unset]): UID assigned to an archive repository.
        archive_size (Union[Unset, int]): Size of archived file copies, in bytes.
        short_term_backup_size (Union[Unset, int]): Size of recent file copies, in bytes.
        archive_restore_points (Union[Unset, int]): Number of restore points for long-term retention.
        restore_points (Union[Unset, int]): Number of restore points.
        latest_restore_point_date (Union[Unset, datetime.datetime]): Date and time of the latest restore point creation.
        source_size (Union[None, Unset, int]): Size of the protected data, in bytes.
        sources (Union[Unset, list['ProtectedObjectStorageSource']]): Object storage backup scope.
    """

    object_storage_uid: Union[Unset, UUID] = UNSET
    bucket_uid: Union[Unset, UUID] = UNSET
    job_uid: Union[None, UUID, Unset] = UNSET
    backup_uid: Union[None, UUID, Unset] = UNSET
    repository_uid: Union[Unset, UUID] = UNSET
    archive_repository_uid: Union[None, UUID, Unset] = UNSET
    archive_size: Union[Unset, int] = UNSET
    short_term_backup_size: Union[Unset, int] = UNSET
    archive_restore_points: Union[Unset, int] = UNSET
    restore_points: Union[Unset, int] = UNSET
    latest_restore_point_date: Union[Unset, datetime.datetime] = UNSET
    source_size: Union[None, Unset, int] = UNSET
    sources: Union[Unset, list["ProtectedObjectStorageSource"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_storage_uid: Union[Unset, str] = UNSET
        if not isinstance(self.object_storage_uid, Unset):
            object_storage_uid = str(self.object_storage_uid)

        bucket_uid: Union[Unset, str] = UNSET
        if not isinstance(self.bucket_uid, Unset):
            bucket_uid = str(self.bucket_uid)

        job_uid: Union[None, Unset, str]
        if isinstance(self.job_uid, Unset):
            job_uid = UNSET
        elif isinstance(self.job_uid, UUID):
            job_uid = str(self.job_uid)
        else:
            job_uid = self.job_uid

        backup_uid: Union[None, Unset, str]
        if isinstance(self.backup_uid, Unset):
            backup_uid = UNSET
        elif isinstance(self.backup_uid, UUID):
            backup_uid = str(self.backup_uid)
        else:
            backup_uid = self.backup_uid

        repository_uid: Union[Unset, str] = UNSET
        if not isinstance(self.repository_uid, Unset):
            repository_uid = str(self.repository_uid)

        archive_repository_uid: Union[None, Unset, str]
        if isinstance(self.archive_repository_uid, Unset):
            archive_repository_uid = UNSET
        elif isinstance(self.archive_repository_uid, UUID):
            archive_repository_uid = str(self.archive_repository_uid)
        else:
            archive_repository_uid = self.archive_repository_uid

        archive_size = self.archive_size

        short_term_backup_size = self.short_term_backup_size

        archive_restore_points = self.archive_restore_points

        restore_points = self.restore_points

        latest_restore_point_date: Union[Unset, str] = UNSET
        if not isinstance(self.latest_restore_point_date, Unset):
            latest_restore_point_date = self.latest_restore_point_date.isoformat()

        source_size: Union[None, Unset, int]
        if isinstance(self.source_size, Unset):
            source_size = UNSET
        else:
            source_size = self.source_size

        sources: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_storage_uid is not UNSET:
            field_dict["objectStorageUid"] = object_storage_uid
        if bucket_uid is not UNSET:
            field_dict["bucketUid"] = bucket_uid
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if backup_uid is not UNSET:
            field_dict["backupUid"] = backup_uid
        if repository_uid is not UNSET:
            field_dict["repositoryUid"] = repository_uid
        if archive_repository_uid is not UNSET:
            field_dict["archiveRepositoryUid"] = archive_repository_uid
        if archive_size is not UNSET:
            field_dict["archiveSize"] = archive_size
        if short_term_backup_size is not UNSET:
            field_dict["shortTermBackupSize"] = short_term_backup_size
        if archive_restore_points is not UNSET:
            field_dict["archiveRestorePoints"] = archive_restore_points
        if restore_points is not UNSET:
            field_dict["restorePoints"] = restore_points
        if latest_restore_point_date is not UNSET:
            field_dict["latestRestorePointDate"] = latest_restore_point_date
        if source_size is not UNSET:
            field_dict["sourceSize"] = source_size
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.protected_object_storage_source import ProtectedObjectStorageSource

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

        _repository_uid = d.pop("repositoryUid", UNSET)
        repository_uid: Union[Unset, UUID]
        if isinstance(_repository_uid, Unset):
            repository_uid = UNSET
        else:
            repository_uid = UUID(_repository_uid)

        def _parse_archive_repository_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                archive_repository_uid_type_0 = UUID(data)

                return archive_repository_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        archive_repository_uid = _parse_archive_repository_uid(d.pop("archiveRepositoryUid", UNSET))

        archive_size = d.pop("archiveSize", UNSET)

        short_term_backup_size = d.pop("shortTermBackupSize", UNSET)

        archive_restore_points = d.pop("archiveRestorePoints", UNSET)

        restore_points = d.pop("restorePoints", UNSET)

        _latest_restore_point_date = d.pop("latestRestorePointDate", UNSET)
        latest_restore_point_date: Union[Unset, datetime.datetime]
        if isinstance(_latest_restore_point_date, Unset):
            latest_restore_point_date = UNSET
        else:
            latest_restore_point_date = isoparse(_latest_restore_point_date)

        def _parse_source_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        source_size = _parse_source_size(d.pop("sourceSize", UNSET))

        sources = []
        _sources = d.pop("sources", UNSET)
        for sources_item_data in _sources or []:
            sources_item = ProtectedObjectStorageSource.from_dict(sources_item_data)

            sources.append(sources_item)

        protected_object_storage_backup = cls(
            object_storage_uid=object_storage_uid,
            bucket_uid=bucket_uid,
            job_uid=job_uid,
            backup_uid=backup_uid,
            repository_uid=repository_uid,
            archive_repository_uid=archive_repository_uid,
            archive_size=archive_size,
            short_term_backup_size=short_term_backup_size,
            archive_restore_points=archive_restore_points,
            restore_points=restore_points,
            latest_restore_point_date=latest_restore_point_date,
            source_size=source_size,
            sources=sources,
        )

        protected_object_storage_backup.additional_properties = d
        return protected_object_storage_backup

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
