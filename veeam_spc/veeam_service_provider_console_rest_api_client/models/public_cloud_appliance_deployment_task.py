from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudApplianceDeploymentTask")


@_attrs_define
class PublicCloudApplianceDeploymentTask:
    """
    Attributes:
        task_uid (Union[Unset, UUID]): UID assigned to a deployment task.
        management_agent_uid (Union[Unset, UUID]): UID assigned to management agent installed on server where Veeam
            Backup for Public Clouds appliance will be deployed.
    """

    task_uid: Union[Unset, UUID] = UNSET
    management_agent_uid: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_uid: Union[Unset, str] = UNSET
        if not isinstance(self.task_uid, Unset):
            task_uid = str(self.task_uid)

        management_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.management_agent_uid, Unset):
            management_agent_uid = str(self.management_agent_uid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_uid is not UNSET:
            field_dict["taskUid"] = task_uid
        if management_agent_uid is not UNSET:
            field_dict["managementAgentUid"] = management_agent_uid

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

        _management_agent_uid = d.pop("managementAgentUid", UNSET)
        management_agent_uid: Union[Unset, UUID]
        if isinstance(_management_agent_uid, Unset):
            management_agent_uid = UNSET
        else:
            management_agent_uid = UUID(_management_agent_uid)

        public_cloud_appliance_deployment_task = cls(
            task_uid=task_uid,
            management_agent_uid=management_agent_uid,
        )

        public_cloud_appliance_deployment_task.additional_properties = d
        return public_cloud_appliance_deployment_task

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
