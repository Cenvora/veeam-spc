from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HostedAgentLinuxSaveParams")


@_attrs_define
class HostedAgentLinuxSaveParams:
    """
    Attributes:
        management_agent_uid (Union[None, UUID, Unset]): UID assigned to a hosted management agent.
    """

    management_agent_uid: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        management_agent_uid: Union[None, Unset, str]
        if isinstance(self.management_agent_uid, Unset):
            management_agent_uid = UNSET
        elif isinstance(self.management_agent_uid, UUID):
            management_agent_uid = str(self.management_agent_uid)
        else:
            management_agent_uid = self.management_agent_uid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if management_agent_uid is not UNSET:
            field_dict["managementAgentUid"] = management_agent_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_management_agent_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                management_agent_uid_type_0 = UUID(data)

                return management_agent_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        management_agent_uid = _parse_management_agent_uid(d.pop("managementAgentUid", UNSET))

        hosted_agent_linux_save_params = cls(
            management_agent_uid=management_agent_uid,
        )

        hosted_agent_linux_save_params.additional_properties = d
        return hosted_agent_linux_save_params

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
