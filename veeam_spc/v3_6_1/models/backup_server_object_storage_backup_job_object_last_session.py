from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_object_storage_backup_job_object_last_session_backup_status import (
    BackupServerObjectStorageBackupJobObjectLastSessionBackupStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerObjectStorageBackupJobObjectLastSession")


@_attrs_define
class BackupServerObjectStorageBackupJobObjectLastSession:
    """
    Attributes:
        backup_status (Union[Unset, BackupServerObjectStorageBackupJobObjectLastSessionBackupStatus]): Status of a job.
        source_files_count (Union[None, Unset, int]): Number of source files.
        changed_files_count (Union[None, Unset, int]): Number of changed files.
        skipped_files_count (Union[None, Unset, int]): Number of skipped files.
        backed_up_files_count (Union[None, Unset, int]): Number of backed up files.
        transferred_size (Union[None, Unset, int]): Total size of processed object storage backup data, in bytes.
        source_size (Union[None, Unset, int]): Total size of all source files, in bytes.
        duration (Union[None, Unset, int]): Duration of the latest job session, in seconds.
        messages (Union[Unset, list[str]]): Message that is displayed after a job session finishes.
    """

    backup_status: Union[Unset, BackupServerObjectStorageBackupJobObjectLastSessionBackupStatus] = UNSET
    source_files_count: Union[None, Unset, int] = UNSET
    changed_files_count: Union[None, Unset, int] = UNSET
    skipped_files_count: Union[None, Unset, int] = UNSET
    backed_up_files_count: Union[None, Unset, int] = UNSET
    transferred_size: Union[None, Unset, int] = UNSET
    source_size: Union[None, Unset, int] = UNSET
    duration: Union[None, Unset, int] = UNSET
    messages: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_status: Union[Unset, str] = UNSET
        if not isinstance(self.backup_status, Unset):
            backup_status = self.backup_status.value

        source_files_count: Union[None, Unset, int]
        if isinstance(self.source_files_count, Unset):
            source_files_count = UNSET
        else:
            source_files_count = self.source_files_count

        changed_files_count: Union[None, Unset, int]
        if isinstance(self.changed_files_count, Unset):
            changed_files_count = UNSET
        else:
            changed_files_count = self.changed_files_count

        skipped_files_count: Union[None, Unset, int]
        if isinstance(self.skipped_files_count, Unset):
            skipped_files_count = UNSET
        else:
            skipped_files_count = self.skipped_files_count

        backed_up_files_count: Union[None, Unset, int]
        if isinstance(self.backed_up_files_count, Unset):
            backed_up_files_count = UNSET
        else:
            backed_up_files_count = self.backed_up_files_count

        transferred_size: Union[None, Unset, int]
        if isinstance(self.transferred_size, Unset):
            transferred_size = UNSET
        else:
            transferred_size = self.transferred_size

        source_size: Union[None, Unset, int]
        if isinstance(self.source_size, Unset):
            source_size = UNSET
        else:
            source_size = self.source_size

        duration: Union[None, Unset, int]
        if isinstance(self.duration, Unset):
            duration = UNSET
        else:
            duration = self.duration

        messages: Union[Unset, list[str]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = self.messages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_status is not UNSET:
            field_dict["backupStatus"] = backup_status
        if source_files_count is not UNSET:
            field_dict["sourceFilesCount"] = source_files_count
        if changed_files_count is not UNSET:
            field_dict["changedFilesCount"] = changed_files_count
        if skipped_files_count is not UNSET:
            field_dict["skippedFilesCount"] = skipped_files_count
        if backed_up_files_count is not UNSET:
            field_dict["backedUpFilesCount"] = backed_up_files_count
        if transferred_size is not UNSET:
            field_dict["transferredSize"] = transferred_size
        if source_size is not UNSET:
            field_dict["sourceSize"] = source_size
        if duration is not UNSET:
            field_dict["duration"] = duration
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _backup_status = d.pop("backupStatus", UNSET)
        backup_status: Union[Unset, BackupServerObjectStorageBackupJobObjectLastSessionBackupStatus]
        if isinstance(_backup_status, Unset):
            backup_status = UNSET
        else:
            backup_status = BackupServerObjectStorageBackupJobObjectLastSessionBackupStatus(_backup_status)

        def _parse_source_files_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        source_files_count = _parse_source_files_count(d.pop("sourceFilesCount", UNSET))

        def _parse_changed_files_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        changed_files_count = _parse_changed_files_count(d.pop("changedFilesCount", UNSET))

        def _parse_skipped_files_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        skipped_files_count = _parse_skipped_files_count(d.pop("skippedFilesCount", UNSET))

        def _parse_backed_up_files_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        backed_up_files_count = _parse_backed_up_files_count(d.pop("backedUpFilesCount", UNSET))

        def _parse_transferred_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        transferred_size = _parse_transferred_size(d.pop("transferredSize", UNSET))

        def _parse_source_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        source_size = _parse_source_size(d.pop("sourceSize", UNSET))

        def _parse_duration(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        duration = _parse_duration(d.pop("duration", UNSET))

        messages = cast(list[str], d.pop("messages", UNSET))

        backup_server_object_storage_backup_job_object_last_session = cls(
            backup_status=backup_status,
            source_files_count=source_files_count,
            changed_files_count=changed_files_count,
            skipped_files_count=skipped_files_count,
            backed_up_files_count=backed_up_files_count,
            transferred_size=transferred_size,
            source_size=source_size,
            duration=duration,
            messages=messages,
        )

        backup_server_object_storage_backup_job_object_last_session.additional_properties = d
        return backup_server_object_storage_backup_job_object_last_session

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
