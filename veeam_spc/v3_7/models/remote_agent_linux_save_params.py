from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RemoteAgentLinuxSaveParams")


@_attrs_define
class RemoteAgentLinuxSaveParams:
    """
    Attributes:
        management_agent_uid (UUID): UID assigned to a management agent that is already installed on the primary node of
            the High Availability cluster. This management agent is used by Veeam Service Provider Console as a gateway to
            reach the target secondary node and deploy an agent on it.
        description (str): Description of a deployment.
        clustered_agent_uid (UUID | Unset): UID assigned to a clustered agent registration in case a management agent
            runs on a secondary node of a High Availability cluster. Has empty value in case of non-clustered and primary-
            only deployments.
    """

    management_agent_uid: UUID
    description: str
    clustered_agent_uid: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        management_agent_uid = str(self.management_agent_uid)

        description = self.description

        clustered_agent_uid: str | Unset = UNSET
        if not isinstance(self.clustered_agent_uid, Unset):
            clustered_agent_uid = str(self.clustered_agent_uid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "managementAgentUid": management_agent_uid,
                "description": description,
            }
        )
        if clustered_agent_uid is not UNSET:
            field_dict["clusteredAgentUid"] = clustered_agent_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        management_agent_uid = UUID(d.pop("managementAgentUid"))

        description = d.pop("description")

        _clustered_agent_uid = d.pop("clusteredAgentUid", UNSET)
        clustered_agent_uid: UUID | Unset
        if isinstance(_clustered_agent_uid, Unset):
            clustered_agent_uid = UNSET
        else:
            clustered_agent_uid = UUID(_clustered_agent_uid)

        remote_agent_linux_save_params = cls(
            management_agent_uid=management_agent_uid,
            description=description,
            clustered_agent_uid=clustered_agent_uid,
        )

        remote_agent_linux_save_params.additional_properties = d
        return remote_agent_linux_save_params

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
