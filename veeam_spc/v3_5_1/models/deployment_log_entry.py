import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
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
        task_uid (Union[Unset, UUID]): UID assigned to a deployment task.
        event (Union[Unset, int]): Event represented by the log entry.
        management_agent_uid (Union[Unset, UUID]): UID assigned to a deployed management agent.
        bios_uuid (Union[Unset, UUID]): UUID in Win32_ComputerSystem WMI class.
        host_name (Union[Unset, str]): Hostname of a target computer.
        task_name (Union[Unset, str]): Name of a deployment task.
        message (Union[Unset, str]): Message.
        time (Union[Unset, datetime.datetime]): Date and time of an event.
    """

    task_uid: Union[Unset, UUID] = UNSET
    event: Union[Unset, int] = UNSET
    management_agent_uid: Union[Unset, UUID] = UNSET
    bios_uuid: Union[Unset, UUID] = UNSET
    host_name: Union[Unset, str] = UNSET
    task_name: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_uid: Union[Unset, str] = UNSET
        if not isinstance(self.task_uid, Unset):
            task_uid = str(self.task_uid)

        event = self.event

        management_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.management_agent_uid, Unset):
            management_agent_uid = str(self.management_agent_uid)

        bios_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.bios_uuid, Unset):
            bios_uuid = str(self.bios_uuid)

        host_name = self.host_name

        task_name = self.task_name

        message = self.message

        time: Union[Unset, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

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
        task_uid: Union[Unset, UUID]
        if isinstance(_task_uid, Unset):
            task_uid = UNSET
        else:
            task_uid = UUID(_task_uid)

        event = d.pop("event", UNSET)

        _management_agent_uid = d.pop("managementAgentUid", UNSET)
        management_agent_uid: Union[Unset, UUID]
        if isinstance(_management_agent_uid, Unset):
            management_agent_uid = UNSET
        else:
            management_agent_uid = UUID(_management_agent_uid)

        _bios_uuid = d.pop("biosUuid", UNSET)
        bios_uuid: Union[Unset, UUID]
        if isinstance(_bios_uuid, Unset):
            bios_uuid = UNSET
        else:
            bios_uuid = UUID(_bios_uuid)

        host_name = d.pop("hostName", UNSET)

        task_name = d.pop("taskName", UNSET)

        message = d.pop("message", UNSET)

        _time = d.pop("time", UNSET)
        time: Union[Unset, datetime.datetime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

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
