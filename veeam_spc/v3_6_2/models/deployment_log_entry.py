from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentLogEntry")


@_attrs_define
class DeploymentLogEntry:
    """
    Attributes:
        task_uid (UUID | Unset): UID assigned to a deployment task.
        event (int | Unset): Event represented by the log entry.
        management_agent_uid (UUID | Unset): UID assigned to a deployed management agent.
        bios_uuid (UUID | Unset): UUID in Win32_ComputerSystem WMI class.
        host_name (str | Unset): Hostname of a target computer.
        task_name (str | Unset): Name of a deployment task.
        message (None | str | Unset): Message.
        time (datetime.datetime | None | Unset): Date and time of an event.
    """

    task_uid: UUID | Unset = UNSET
    event: int | Unset = UNSET
    management_agent_uid: UUID | Unset = UNSET
    bios_uuid: UUID | Unset = UNSET
    host_name: str | Unset = UNSET
    task_name: str | Unset = UNSET
    message: None | str | Unset = UNSET
    time: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_uid: str | Unset = UNSET
        if not isinstance(self.task_uid, Unset):
            task_uid = str(self.task_uid)

        event = self.event

        management_agent_uid: str | Unset = UNSET
        if not isinstance(self.management_agent_uid, Unset):
            management_agent_uid = str(self.management_agent_uid)

        bios_uuid: str | Unset = UNSET
        if not isinstance(self.bios_uuid, Unset):
            bios_uuid = str(self.bios_uuid)

        host_name = self.host_name

        task_name = self.task_name

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        time: None | str | Unset
        if isinstance(self.time, Unset):
            time = UNSET
        elif isinstance(self.time, datetime.datetime):
            time = self.time.isoformat()
        else:
            time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_uid is not UNSET:
            field_dict["taskUid"] = task_uid
        if event is not UNSET:
            field_dict["event"] = event
        if management_agent_uid is not UNSET:
            field_dict["managementAgentUid"] = management_agent_uid
        if bios_uuid is not UNSET:
            field_dict["biosUuid"] = bios_uuid
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if task_name is not UNSET:
            field_dict["taskName"] = task_name
        if message is not UNSET:
            field_dict["message"] = message
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _task_uid = d.pop("taskUid", UNSET)
        task_uid: UUID | Unset
        if isinstance(_task_uid, Unset):
            task_uid = UNSET
        else:
            task_uid = UUID(_task_uid)

        event = d.pop("event", UNSET)

        _management_agent_uid = d.pop("managementAgentUid", UNSET)
        management_agent_uid: UUID | Unset
        if isinstance(_management_agent_uid, Unset):
            management_agent_uid = UNSET
        else:
            management_agent_uid = UUID(_management_agent_uid)

        _bios_uuid = d.pop("biosUuid", UNSET)
        bios_uuid: UUID | Unset
        if isinstance(_bios_uuid, Unset):
            bios_uuid = UNSET
        else:
            bios_uuid = UUID(_bios_uuid)

        host_name = d.pop("hostName", UNSET)

        task_name = d.pop("taskName", UNSET)

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_type_0 = isoparse(data)

                return time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time = _parse_time(d.pop("time", UNSET))

        deployment_log_entry = cls(
            task_uid=task_uid,
            event=event,
            management_agent_uid=management_agent_uid,
            bios_uuid=bios_uuid,
            host_name=host_name,
            task_name=task_name,
            message=message,
            time=time,
        )

        deployment_log_entry.additional_properties = d
        return deployment_log_entry

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
