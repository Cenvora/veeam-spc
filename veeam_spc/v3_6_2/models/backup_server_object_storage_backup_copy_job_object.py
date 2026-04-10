from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_file_job_object_source import BackupServerFileJobObjectSource
    from ..models.backup_server_job_object_last_session import BackupServerJobObjectLastSession


T = TypeVar("T", bound="BackupServerObjectStorageBackupCopyJobObject")


@_attrs_define
class BackupServerObjectStorageBackupCopyJobObject:
    """
    Attributes:
        job_uid (UUID | Unset): UID assigned to a job in Veeam Backup & Replication.
        unique_job_uid (UUID | Unset): UID assigned to a job in Veeam Service Provider Console.
        object_storage_uid (UUID | Unset): UID assigned to an object storage.
        path (str | Unset): Path to a location of protected data.
        sources (list[BackupServerFileJobObjectSource] | Unset): Processed files and folders.
        last_session (BackupServerJobObjectLastSession | Unset):
    """

    job_uid: UUID | Unset = UNSET
    unique_job_uid: UUID | Unset = UNSET
    object_storage_uid: UUID | Unset = UNSET
    path: str | Unset = UNSET
    sources: list[BackupServerFileJobObjectSource] | Unset = UNSET
    last_session: BackupServerJobObjectLastSession | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_uid: str | Unset = UNSET
        if not isinstance(self.job_uid, Unset):
            job_uid = str(self.job_uid)

        unique_job_uid: str | Unset = UNSET
        if not isinstance(self.unique_job_uid, Unset):
            unique_job_uid = str(self.unique_job_uid)

        object_storage_uid: str | Unset = UNSET
        if not isinstance(self.object_storage_uid, Unset):
            object_storage_uid = str(self.object_storage_uid)

        path = self.path

        sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)

        last_session: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_session, Unset):
            last_session = self.last_session.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if unique_job_uid is not UNSET:
            field_dict["uniqueJobUid"] = unique_job_uid
        if object_storage_uid is not UNSET:
            field_dict["objectStorageUid"] = object_storage_uid
        if path is not UNSET:
            field_dict["path"] = path
        if sources is not UNSET:
            field_dict["sources"] = sources
        if last_session is not UNSET:
            field_dict["lastSession"] = last_session

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_file_job_object_source import BackupServerFileJobObjectSource
        from ..models.backup_server_job_object_last_session import BackupServerJobObjectLastSession

        d = dict(src_dict)
        _job_uid = d.pop("jobUid", UNSET)
        job_uid: UUID | Unset
        if isinstance(_job_uid, Unset):
            job_uid = UNSET
        else:
            job_uid = UUID(_job_uid)

        _unique_job_uid = d.pop("uniqueJobUid", UNSET)
        unique_job_uid: UUID | Unset
        if isinstance(_unique_job_uid, Unset):
            unique_job_uid = UNSET
        else:
            unique_job_uid = UUID(_unique_job_uid)

        _object_storage_uid = d.pop("objectStorageUid", UNSET)
        object_storage_uid: UUID | Unset
        if isinstance(_object_storage_uid, Unset):
            object_storage_uid = UNSET
        else:
            object_storage_uid = UUID(_object_storage_uid)

        path = d.pop("path", UNSET)

        _sources = d.pop("sources", UNSET)
        sources: list[BackupServerFileJobObjectSource] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = BackupServerFileJobObjectSource.from_dict(sources_item_data)

                sources.append(sources_item)

        _last_session = d.pop("lastSession", UNSET)
        last_session: BackupServerJobObjectLastSession | Unset
        if isinstance(_last_session, Unset):
            last_session = UNSET
        else:
            last_session = BackupServerJobObjectLastSession.from_dict(_last_session)

        backup_server_object_storage_backup_copy_job_object = cls(
            job_uid=job_uid,
            unique_job_uid=unique_job_uid,
            object_storage_uid=object_storage_uid,
            path=path,
            sources=sources,
            last_session=last_session,
        )

        backup_server_object_storage_backup_copy_job_object.additional_properties = d
        return backup_server_object_storage_backup_copy_job_object

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
