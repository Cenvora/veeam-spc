import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.backup_server_job_session_task_status import BackupServerJobSessionTaskStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerJobSessionTask")


@_attrs_define
class BackupServerJobSessionTask:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a job session task.
        object_uid (Union[Unset, UUID]): UID assigned to an object included in a job.
        object_name (Union[Unset, str]): Name of an object included in a job.
        total_objects (Union[Unset, int]): Number of objects included in a job.
        processed_objects (Union[Unset, int]): Number of objects processed by a job session.
        read_data_size (Union[Unset, int]): Size of object data that a job processes.
        transferred_data_size (Union[Unset, int]): Size of processed object data.
        start_time (Union[Unset, datetime.datetime]): Start date and time of a job session task.
        end_time (Union[Unset, datetime.datetime]): End date and time of a job session task.
        duration (Union[Unset, int]): Duration of a job session task, in seconds.
        failure_messages (Union[Unset, list[str]]): Messages containing information on job session task errors.
        status (Union[Unset, BackupServerJobSessionTaskStatus]): Status of a job session task.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    object_uid: Union[Unset, UUID] = UNSET
    object_name: Union[Unset, str] = UNSET
    total_objects: Union[Unset, int] = UNSET
    processed_objects: Union[Unset, int] = UNSET
    read_data_size: Union[Unset, int] = UNSET
    transferred_data_size: Union[Unset, int] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    end_time: Union[Unset, datetime.datetime] = UNSET
    duration: Union[Unset, int] = UNSET
    failure_messages: Union[Unset, list[str]] = UNSET
    status: Union[Unset, BackupServerJobSessionTaskStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        object_uid: Union[Unset, str] = UNSET
        if not isinstance(self.object_uid, Unset):
            object_uid = str(self.object_uid)

        object_name = self.object_name

        total_objects = self.total_objects

        processed_objects = self.processed_objects

        read_data_size = self.read_data_size

        transferred_data_size = self.transferred_data_size

        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        end_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        duration = self.duration

        failure_messages: Union[Unset, list[str]] = UNSET
        if not isinstance(self.failure_messages, Unset):
            failure_messages = self.failure_messages

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if object_uid is not UNSET:
            field_dict["objectUid"] = object_uid
        if object_name is not UNSET:
            field_dict["objectName"] = object_name
        if total_objects is not UNSET:
            field_dict["totalObjects"] = total_objects
        if processed_objects is not UNSET:
            field_dict["processedObjects"] = processed_objects
        if read_data_size is not UNSET:
            field_dict["readDataSize"] = read_data_size
        if transferred_data_size is not UNSET:
            field_dict["transferredDataSize"] = transferred_data_size
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if duration is not UNSET:
            field_dict["duration"] = duration
        if failure_messages is not UNSET:
            field_dict["failureMessages"] = failure_messages
        if status is not UNSET:
            field_dict["status"] = status

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

        _object_uid = d.pop("objectUid", UNSET)
        object_uid: Union[Unset, UUID]
        if isinstance(_object_uid, Unset):
            object_uid = UNSET
        else:
            object_uid = UUID(_object_uid)

        object_name = d.pop("objectName", UNSET)

        total_objects = d.pop("totalObjects", UNSET)

        processed_objects = d.pop("processedObjects", UNSET)

        read_data_size = d.pop("readDataSize", UNSET)

        transferred_data_size = d.pop("transferredDataSize", UNSET)

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _end_time = d.pop("endTime", UNSET)
        end_time: Union[Unset, datetime.datetime]
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        duration = d.pop("duration", UNSET)

        failure_messages = cast(list[str], d.pop("failureMessages", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, BackupServerJobSessionTaskStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BackupServerJobSessionTaskStatus(_status)

        backup_server_job_session_task = cls(
            instance_uid=instance_uid,
            object_uid=object_uid,
            object_name=object_name,
            total_objects=total_objects,
            processed_objects=processed_objects,
            read_data_size=read_data_size,
            transferred_data_size=transferred_data_size,
            start_time=start_time,
            end_time=end_time,
            duration=duration,
            failure_messages=failure_messages,
            status=status,
        )

        backup_server_job_session_task.additional_properties = d
        return backup_server_job_session_task

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
