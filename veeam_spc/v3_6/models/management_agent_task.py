import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.management_agent_task_status import ManagementAgentTaskStatus
from ..models.management_agent_task_type import ManagementAgentTaskType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManagementAgentTask")


@_attrs_define
class ManagementAgentTask:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a management agent task.
        task_type (Union[Unset, ManagementAgentTaskType]): Type of a management agent task.
        status (Union[Unset, ManagementAgentTaskStatus]): Status of a management agent task.
        description (Union[Unset, str]): Description of a management agent task.
        management_agent_uid (Union[Unset, UUID]): UID assigned to a management agent.
        start_time (Union[Unset, datetime.datetime]): Start date and time of a management agent task.
        end_time (Union[Unset, datetime.datetime]): End date and time of a management agent task.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    task_type: Union[Unset, ManagementAgentTaskType] = UNSET
    status: Union[Unset, ManagementAgentTaskStatus] = UNSET
    description: Union[Unset, str] = UNSET
    management_agent_uid: Union[Unset, UUID] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    end_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        task_type: Union[Unset, str] = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        description = self.description

        management_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.management_agent_uid, Unset):
            management_agent_uid = str(self.management_agent_uid)

        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        end_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if task_type is not UNSET:
            field_dict["taskType"] = task_type
        if status is not UNSET:
            field_dict["status"] = status
        if description is not UNSET:
            field_dict["description"] = description
        if management_agent_uid is not UNSET:
            field_dict["managementAgentUid"] = management_agent_uid
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time

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

        _task_type = d.pop("taskType", UNSET)
        task_type: Union[Unset, ManagementAgentTaskType]
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = ManagementAgentTaskType(_task_type)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ManagementAgentTaskStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ManagementAgentTaskStatus(_status)

        description = d.pop("description", UNSET)

        _management_agent_uid = d.pop("managementAgentUid", UNSET)
        management_agent_uid: Union[Unset, UUID]
        if isinstance(_management_agent_uid, Unset):
            management_agent_uid = UNSET
        else:
            management_agent_uid = UUID(_management_agent_uid)

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

        management_agent_task = cls(
            instance_uid=instance_uid,
            task_type=task_type,
            status=status,
            description=description,
            management_agent_uid=management_agent_uid,
            start_time=start_time,
            end_time=end_time,
        )

        management_agent_task.additional_properties = d
        return management_agent_task

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
