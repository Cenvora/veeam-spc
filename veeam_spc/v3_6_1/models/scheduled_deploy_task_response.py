from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ScheduledDeployTaskResponse")


@_attrs_define
class ScheduledDeployTaskResponse:
    """
    Attributes:
        scheduled_task_uid (UUID): UID assigned to a scheduled task.
        task_uid (UUID): UID will be assigned to a deployment task when it has been be started.
    """

    scheduled_task_uid: UUID
    task_uid: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scheduled_task_uid = str(self.scheduled_task_uid)

        task_uid = str(self.task_uid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scheduledTaskUid": scheduled_task_uid,
                "taskUid": task_uid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scheduled_task_uid = UUID(d.pop("scheduledTaskUid"))

        task_uid = UUID(d.pop("taskUid"))

        scheduled_deploy_task_response = cls(
            scheduled_task_uid=scheduled_task_uid,
            task_uid=task_uid,
        )

        scheduled_deploy_task_response.additional_properties = d
        return scheduled_deploy_task_response

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
