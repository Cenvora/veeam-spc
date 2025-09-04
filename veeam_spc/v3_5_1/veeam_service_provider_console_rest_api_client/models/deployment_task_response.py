from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentTaskResponse")


@_attrs_define
class DeploymentTaskResponse:
    """
    Attributes:
        deployment_task_uid (Union[None, UUID, Unset]): UID assigned to a deployment task.
    """

    deployment_task_uid: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deployment_task_uid: Union[None, Unset, str]
        if isinstance(self.deployment_task_uid, Unset):
            deployment_task_uid = UNSET
        elif isinstance(self.deployment_task_uid, UUID):
            deployment_task_uid = str(self.deployment_task_uid)
        else:
            deployment_task_uid = self.deployment_task_uid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deployment_task_uid is not UNSET:
            field_dict["deploymentTaskUid"] = deployment_task_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_deployment_task_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deployment_task_uid_type_0 = UUID(data)

                return deployment_task_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        deployment_task_uid = _parse_deployment_task_uid(d.pop("deploymentTaskUid", UNSET))

        deployment_task_response = cls(
            deployment_task_uid=deployment_task_uid,
        )

        deployment_task_response.additional_properties = d
        return deployment_task_response

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
