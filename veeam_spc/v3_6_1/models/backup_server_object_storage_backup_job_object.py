from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_file_job_object_source import BackupServerFileJobObjectSource
    from ..models.backup_server_object_storage_backup_job_object_last_session import (
        BackupServerObjectStorageBackupJobObjectLastSession,
    )


T = TypeVar("T", bound="BackupServerObjectStorageBackupJobObject")


@_attrs_define
class BackupServerObjectStorageBackupJobObject:
    """
    Attributes:
        job_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Backup & Replication.
        unique_job_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Service Provider Console.
        object_storage_uid (Union[Unset, UUID]): UID assigned to an object storage.
        name (Union[Unset, str]): Name of an object storage.
        sources (Union[Unset, list['BackupServerFileJobObjectSource']]): Processed files and folders.
        last_session (Union[Unset, BackupServerObjectStorageBackupJobObjectLastSession]):
    """

    job_uid: Union[Unset, UUID] = UNSET
    unique_job_uid: Union[Unset, UUID] = UNSET
    object_storage_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    sources: Union[Unset, list["BackupServerFileJobObjectSource"]] = UNSET
    last_session: Union[Unset, "BackupServerObjectStorageBackupJobObjectLastSession"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_uid: Union[Unset, str] = UNSET
        if not isinstance(self.job_uid, Unset):
            job_uid = str(self.job_uid)

        unique_job_uid: Union[Unset, str] = UNSET
        if not isinstance(self.unique_job_uid, Unset):
            unique_job_uid = str(self.unique_job_uid)

        object_storage_uid: Union[Unset, str] = UNSET
        if not isinstance(self.object_storage_uid, Unset):
            object_storage_uid = str(self.object_storage_uid)

        name = self.name

        sources: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)

        last_session: Union[Unset, dict[str, Any]] = UNSET
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
        if name is not UNSET:
            field_dict["name"] = name
        if sources is not UNSET:
            field_dict["sources"] = sources
        if last_session is not UNSET:
            field_dict["lastSession"] = last_session

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_file_job_object_source import BackupServerFileJobObjectSource
        from ..models.backup_server_object_storage_backup_job_object_last_session import (
            BackupServerObjectStorageBackupJobObjectLastSession,
        )

        d = dict(src_dict)
        _job_uid = d.pop("jobUid", UNSET)
        job_uid: Union[Unset, UUID]
        if isinstance(_job_uid, Unset):
            job_uid = UNSET
        else:
            job_uid = UUID(_job_uid)

        _unique_job_uid = d.pop("uniqueJobUid", UNSET)
        unique_job_uid: Union[Unset, UUID]
        if isinstance(_unique_job_uid, Unset):
            unique_job_uid = UNSET
        else:
            unique_job_uid = UUID(_unique_job_uid)

        _object_storage_uid = d.pop("objectStorageUid", UNSET)
        object_storage_uid: Union[Unset, UUID]
        if isinstance(_object_storage_uid, Unset):
            object_storage_uid = UNSET
        else:
            object_storage_uid = UUID(_object_storage_uid)

        name = d.pop("name", UNSET)

        sources = []
        _sources = d.pop("sources", UNSET)
        for sources_item_data in _sources or []:
            sources_item = BackupServerFileJobObjectSource.from_dict(sources_item_data)

            sources.append(sources_item)

        _last_session = d.pop("lastSession", UNSET)
        last_session: Union[Unset, BackupServerObjectStorageBackupJobObjectLastSession]
        if isinstance(_last_session, Unset):
            last_session = UNSET
        else:
            last_session = BackupServerObjectStorageBackupJobObjectLastSession.from_dict(_last_session)

        backup_server_object_storage_backup_job_object = cls(
            job_uid=job_uid,
            unique_job_uid=unique_job_uid,
            object_storage_uid=object_storage_uid,
            name=name,
            sources=sources,
            last_session=last_session,
        )

        backup_server_object_storage_backup_job_object.additional_properties = d
        return backup_server_object_storage_backup_job_object

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
