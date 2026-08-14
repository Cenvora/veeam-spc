from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_file_share_job_object_last_session_backup_status import (
    BackupServerFileShareJobObjectLastSessionBackupStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerFileShareJobObjectLastSession")


@_attrs_define
class BackupServerFileShareJobObjectLastSession:
    """
    Attributes:
        backup_status (BackupServerFileShareJobObjectLastSessionBackupStatus | Unset): Status of a job.
        source_files_count (int | Unset): Total number of files in all sources.
        changed_files_count (int | Unset): Number of processed files.
        skipped_files_count (int | Unset): Number of skipped files.
        backed_up_files_count (int | Unset): Number of backed up files.
        transferred_size (int | Unset): Total size of backed up file share data, in bytes.
        source_size (int | Unset): Total size of all source files, in bytes.
        duration (int | Unset): Time taken to complete the latest job session, in seconds.
        messages (list[str] | Unset): Message that is displayed after a job session finishes.
    """

    backup_status: BackupServerFileShareJobObjectLastSessionBackupStatus | Unset = UNSET
    source_files_count: int | Unset = UNSET
    changed_files_count: int | Unset = UNSET
    skipped_files_count: int | Unset = UNSET
    backed_up_files_count: int | Unset = UNSET
    transferred_size: int | Unset = UNSET
    source_size: int | Unset = UNSET
    duration: int | Unset = UNSET
    messages: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_status: str | Unset = UNSET
        if not isinstance(self.backup_status, Unset):
            backup_status = self.backup_status.value

        source_files_count = self.source_files_count

        changed_files_count = self.changed_files_count

        skipped_files_count = self.skipped_files_count

        backed_up_files_count = self.backed_up_files_count

        transferred_size = self.transferred_size

        source_size = self.source_size

        duration = self.duration

        messages: list[str] | Unset = UNSET
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
        backup_status: BackupServerFileShareJobObjectLastSessionBackupStatus | Unset
        if isinstance(_backup_status, Unset):
            backup_status = UNSET
        else:
            backup_status = BackupServerFileShareJobObjectLastSessionBackupStatus(_backup_status)

        source_files_count = d.pop("sourceFilesCount", UNSET)

        changed_files_count = d.pop("changedFilesCount", UNSET)

        skipped_files_count = d.pop("skippedFilesCount", UNSET)

        backed_up_files_count = d.pop("backedUpFilesCount", UNSET)

        transferred_size = d.pop("transferredSize", UNSET)

        source_size = d.pop("sourceSize", UNSET)

        duration = d.pop("duration", UNSET)

        messages = cast(list[str], d.pop("messages", UNSET))

        backup_server_file_share_job_object_last_session = cls(
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

        backup_server_file_share_job_object_last_session.additional_properties = d
        return backup_server_file_share_job_object_last_session

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
