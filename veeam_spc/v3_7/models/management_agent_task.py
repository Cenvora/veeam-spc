from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
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
        instance_uid (UUID | Unset): UID assigned to a management agent task.
        task_type (ManagementAgentTaskType | Unset): Type of a management agent task.
        status (ManagementAgentTaskStatus | Unset): Status of a management agent task.
        description (str | Unset): Description of a management agent task.
        management_agent_uid (UUID | Unset): UID assigned to a management agent.
        start_time (datetime.datetime | None | Unset): Start date and time of a management agent task.
        end_time (datetime.datetime | None | Unset): End date and time of a management agent task.
    """

    instance_uid: UUID | Unset = UNSET
    task_type: ManagementAgentTaskType | Unset = UNSET
    status: ManagementAgentTaskStatus | Unset = UNSET
    description: str | Unset = UNSET
    management_agent_uid: UUID | Unset = UNSET
    start_time: datetime.datetime | None | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        description = self.description

        management_agent_uid: str | Unset = UNSET
        if not isinstance(self.management_agent_uid, Unset):
            management_agent_uid = str(self.management_agent_uid)

        start_time: None | str | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        elif isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

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
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _task_type = d.pop("taskType", UNSET)
        task_type: ManagementAgentTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = ManagementAgentTaskType(_task_type)

        _status = d.pop("status", UNSET)
        status: ManagementAgentTaskStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ManagementAgentTaskStatus(_status)

        description = d.pop("description", UNSET)

        _management_agent_uid = d.pop("managementAgentUid", UNSET)
        management_agent_uid: UUID | Unset
        if isinstance(_management_agent_uid, Unset):
            management_agent_uid = UNSET
        else:
            management_agent_uid = UUID(_management_agent_uid)

        def _parse_start_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_type_0 = isoparse(data)

                return start_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_time = _parse_start_time(d.pop("startTime", UNSET))

        def _parse_end_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = isoparse(data)

                return end_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_time = _parse_end_time(d.pop("endTime", UNSET))

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
