import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.scheduled_deployment_task_type import ScheduledDeploymentTaskType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduledComputerDeploymentTask")


@_attrs_define
class ScheduledComputerDeploymentTask:
    """
    Attributes:
        date_time (datetime.datetime): Date and time when the scheduled deployment must start.
        task_uid (Union[Unset, UUID]): UID assigned to a scheduled deployment task.
        task_type (Union[Unset, ScheduledDeploymentTaskType]): Type of a scheduled deployment task.
    """

    date_time: datetime.datetime
    task_uid: Union[Unset, UUID] = UNSET
    task_type: Union[Unset, ScheduledDeploymentTaskType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_time = self.date_time.isoformat()

        task_uid: Union[Unset, str] = UNSET
        if not isinstance(self.task_uid, Unset):
            task_uid = str(self.task_uid)

        task_type: Union[Unset, str] = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dateTime": date_time,
            }
        )
        if task_uid is not UNSET:
            field_dict["taskUid"] = task_uid
        if task_type is not UNSET:
            field_dict["taskType"] = task_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date_time = isoparse(d.pop("dateTime"))

        _task_uid = d.pop("taskUid", UNSET)
        task_uid: Union[Unset, UUID]
        if isinstance(_task_uid, Unset):
            task_uid = UNSET
        else:
            task_uid = UUID(_task_uid)

        _task_type = d.pop("taskType", UNSET)
        task_type: Union[Unset, ScheduledDeploymentTaskType]
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = ScheduledDeploymentTaskType(_task_type)

        scheduled_computer_deployment_task = cls(
            date_time=date_time,
            task_uid=task_uid,
            task_type=task_type,
        )

        scheduled_computer_deployment_task.additional_properties = d
        return scheduled_computer_deployment_task

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
