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
        object_uid (Union[None, UUID, Unset]): UID assigned to an object included in a job.
        object_name (Union[None, Unset, str]): Name of an object included in a job.
        total_objects (Union[None, Unset, int]): Number of objects included in a job.
        processed_objects (Union[None, Unset, int]): Number of objects processed by a job session.
        read_data_size (Union[None, Unset, int]): Size of object data that a job processes.
        transferred_data_size (Union[None, Unset, int]): Size of processed object data.
        start_time (Union[None, Unset, datetime.datetime]): Start date and time of a job session task.
        end_time (Union[None, Unset, datetime.datetime]): End date and time of a job session task.
        duration (Union[None, Unset, int]): Duration of a job session task, in seconds.
        failure_messages (Union[None, Unset, list[str]]): Messages containing information on job session task errors.
        status (Union[Unset, BackupServerJobSessionTaskStatus]): Status of a job session task.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    object_uid: Union[None, UUID, Unset] = UNSET
    object_name: Union[None, Unset, str] = UNSET
    total_objects: Union[None, Unset, int] = UNSET
    processed_objects: Union[None, Unset, int] = UNSET
    read_data_size: Union[None, Unset, int] = UNSET
    transferred_data_size: Union[None, Unset, int] = UNSET
    start_time: Union[None, Unset, datetime.datetime] = UNSET
    end_time: Union[None, Unset, datetime.datetime] = UNSET
    duration: Union[None, Unset, int] = UNSET
    failure_messages: Union[None, Unset, list[str]] = UNSET
    status: Union[Unset, BackupServerJobSessionTaskStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        object_uid: Union[None, Unset, str]
        if isinstance(self.object_uid, Unset):
            object_uid = UNSET
        elif isinstance(self.object_uid, UUID):
            object_uid = str(self.object_uid)
        else:
            object_uid = self.object_uid

        object_name: Union[None, Unset, str]
        if isinstance(self.object_name, Unset):
            object_name = UNSET
        else:
            object_name = self.object_name

        total_objects: Union[None, Unset, int]
        if isinstance(self.total_objects, Unset):
            total_objects = UNSET
        else:
            total_objects = self.total_objects

        processed_objects: Union[None, Unset, int]
        if isinstance(self.processed_objects, Unset):
            processed_objects = UNSET
        else:
            processed_objects = self.processed_objects

        read_data_size: Union[None, Unset, int]
        if isinstance(self.read_data_size, Unset):
            read_data_size = UNSET
        else:
            read_data_size = self.read_data_size

        transferred_data_size: Union[None, Unset, int]
        if isinstance(self.transferred_data_size, Unset):
            transferred_data_size = UNSET
        else:
            transferred_data_size = self.transferred_data_size

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

        failure_messages: Union[None, Unset, list[str]]
        if isinstance(self.failure_messages, Unset):
            failure_messages = UNSET
        elif isinstance(self.failure_messages, list):
            failure_messages = self.failure_messages

        else:
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

        def _parse_object_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                object_uid_type_0 = UUID(data)

                return object_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        object_uid = _parse_object_uid(d.pop("objectUid", UNSET))

        def _parse_object_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        object_name = _parse_object_name(d.pop("objectName", UNSET))

        def _parse_total_objects(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_objects = _parse_total_objects(d.pop("totalObjects", UNSET))

        def _parse_processed_objects(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        processed_objects = _parse_processed_objects(d.pop("processedObjects", UNSET))

        def _parse_read_data_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        read_data_size = _parse_read_data_size(d.pop("readDataSize", UNSET))

        def _parse_transferred_data_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        transferred_data_size = _parse_transferred_data_size(d.pop("transferredDataSize", UNSET))

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

        def _parse_failure_messages(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                failure_messages_type_0 = cast(list[str], data)

                return failure_messages_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        failure_messages = _parse_failure_messages(d.pop("failureMessages", UNSET))

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
