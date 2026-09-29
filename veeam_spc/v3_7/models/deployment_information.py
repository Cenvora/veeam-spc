from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentInformation")


@_attrs_define
class DeploymentInformation:
    """
    Attributes:
        deploy_task_uid (UUID | Unset): UID assigned to a deployment task.
        deploy_task_id (int | None | Unset): ID assigned to a deployment task.
    """

    deploy_task_uid: UUID | Unset = UNSET
    deploy_task_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deploy_task_uid: str | Unset = UNSET
        if not isinstance(self.deploy_task_uid, Unset):
            deploy_task_uid = str(self.deploy_task_uid)

        deploy_task_id: int | None | Unset
        if isinstance(self.deploy_task_id, Unset):
            deploy_task_id = UNSET
        else:
            deploy_task_id = self.deploy_task_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deploy_task_uid is not UNSET:
            field_dict["deployTaskUid"] = deploy_task_uid
        if deploy_task_id is not UNSET:
            field_dict["deployTaskId"] = deploy_task_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _deploy_task_uid = d.pop("deployTaskUid", UNSET)
        deploy_task_uid: UUID | Unset
        if isinstance(_deploy_task_uid, Unset):
            deploy_task_uid = UNSET
        else:
            deploy_task_uid = UUID(_deploy_task_uid)

        def _parse_deploy_task_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        deploy_task_id = _parse_deploy_task_id(d.pop("deployTaskId", UNSET))

        deployment_information = cls(
            deploy_task_uid=deploy_task_uid,
            deploy_task_id=deploy_task_id,
        )

        deployment_information.additional_properties = d
        return deployment_information

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
