import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.deployment_task_status import DeploymentTaskStatus
from ..models.deployment_task_type import DeploymentTaskType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentTask")


@_attrs_define
class DeploymentTask:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a deployment task.
        management_agent_uid (Union[Unset, UUID]): UID assigned to a master agent or a management agent installed on a
            target server.
        type_ (Union[Unset, DeploymentTaskType]): Type of a deployment task.
        status (Union[Unset, DeploymentTaskStatus]): Status of a deployment task.
        start_date (Union[Unset, datetime.datetime]): Date and time when a task started.
        end_date (Union[Unset, datetime.datetime]): Date and time when a task ended.
        error_message (Union[Unset, str]): Error message for failed deployment task.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    management_agent_uid: Union[Unset, UUID] = UNSET
    type_: Union[Unset, DeploymentTaskType] = UNSET
    status: Union[Unset, DeploymentTaskStatus] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    error_message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        management_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.management_agent_uid, Unset):
            management_agent_uid = str(self.management_agent_uid)

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if management_agent_uid is not UNSET:
            field_dict["managementAgentUid"] = management_agent_uid
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message

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

        _management_agent_uid = d.pop("managementAgentUid", UNSET)
        management_agent_uid: Union[Unset, UUID]
        if isinstance(_management_agent_uid, Unset):
            management_agent_uid = UNSET
        else:
            management_agent_uid = UUID(_management_agent_uid)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, DeploymentTaskType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DeploymentTaskType(_type_)

        _status = d.pop("status", UNSET)
        status: Union[Unset, DeploymentTaskStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DeploymentTaskStatus(_status)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        error_message = d.pop("errorMessage", UNSET)

        deployment_task = cls(
            instance_uid=instance_uid,
            management_agent_uid=management_agent_uid,
            type_=type_,
            status=status,
            start_date=start_date,
            end_date=end_date,
            error_message=error_message,
        )

        deployment_task.additional_properties = d
        return deployment_task

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
