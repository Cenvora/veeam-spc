import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.backup_server_job_object_last_session_backup_status import BackupServerJobObjectLastSessionBackupStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerJobObjectLastSession")


@_attrs_define
class BackupServerJobObjectLastSession:
    """
    Attributes:
        backup_status (Union[Unset, BackupServerJobObjectLastSessionBackupStatus]): Status of the latest job session.
        total_backed_size (Union[None, Unset, int]): Size of backup files, in bytes.
        source_size (Union[None, Unset, int]): Size of processed data, in bytes.
        start_time (Union[None, Unset, datetime.datetime]): Date and time when the latest job session started.
        end_time (Union[None, Unset, datetime.datetime]): Date and time when the latest job session finished.
        duration (Union[None, Unset, int]): Time taken to complete the latest job session, in seconds.
        messages (Union[Unset, list[str]]): Array of job session messages.
    """

    backup_status: Union[Unset, BackupServerJobObjectLastSessionBackupStatus] = UNSET
    total_backed_size: Union[None, Unset, int] = UNSET
    source_size: Union[None, Unset, int] = UNSET
    start_time: Union[None, Unset, datetime.datetime] = UNSET
    end_time: Union[None, Unset, datetime.datetime] = UNSET
    duration: Union[None, Unset, int] = UNSET
    messages: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_status: Union[Unset, str] = UNSET
        if not isinstance(self.backup_status, Unset):
            backup_status = self.backup_status.value

        total_backed_size: Union[None, Unset, int]
        if isinstance(self.total_backed_size, Unset):
            total_backed_size = UNSET
        else:
            total_backed_size = self.total_backed_size

        source_size: Union[None, Unset, int]
        if isinstance(self.source_size, Unset):
            source_size = UNSET
        else:
            source_size = self.source_size

        start_time: Union[None, Unset, str]
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        elif isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        end_time: Union[None, Unset, str]
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

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
        if total_backed_size is not UNSET:
            field_dict["totalBackedSize"] = total_backed_size
        if source_size is not UNSET:
            field_dict["sourceSize"] = source_size
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if duration is not UNSET:
            field_dict["duration"] = duration
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _backup_status = d.pop("backupStatus", UNSET)
        backup_status: Union[Unset, BackupServerJobObjectLastSessionBackupStatus]
        if isinstance(_backup_status, Unset):
            backup_status = UNSET
        else:
            backup_status = BackupServerJobObjectLastSessionBackupStatus(_backup_status)

        def _parse_total_backed_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_backed_size = _parse_total_backed_size(d.pop("totalBackedSize", UNSET))

        def _parse_source_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        source_size = _parse_source_size(d.pop("sourceSize", UNSET))

        def _parse_start_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_type_0 = isoparse(data)

                return start_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        start_time = _parse_start_time(d.pop("startTime", UNSET))

        def _parse_end_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = isoparse(data)

                return end_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        end_time = _parse_end_time(d.pop("endTime", UNSET))

        def _parse_duration(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        duration = _parse_duration(d.pop("duration", UNSET))

        messages = cast(list[str], d.pop("messages", UNSET))

        backup_server_job_object_last_session = cls(
            backup_status=backup_status,
            total_backed_size=total_backed_size,
            source_size=source_size,
            start_time=start_time,
            end_time=end_time,
            duration=duration,
            messages=messages,
        )

        backup_server_job_object_last_session.additional_properties = d
        return backup_server_job_object_last_session

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
