from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatePluginAgentRulesRequest")


@_attrs_define
class UpdatePluginAgentRulesRequest:
    """
    Attributes:
        allow_agemt_ids (Union[None, Unset, list[str]]): Array of IDs assigned to management agents that are permitted
            to access plugin.
        deny_agent_ids (Union[None, Unset, list[str]]): Array of IDs assigned to management agents that are not
            permitted to access plugin.
        allow_agents_by_default (Union[None, Unset, bool]): Defines whether all other management agents are permitted to
            access plugin by default.
            > Provide the `null` value to keep the current settings.
    """

    allow_agemt_ids: Union[None, Unset, list[str]] = UNSET
    deny_agent_ids: Union[None, Unset, list[str]] = UNSET
    allow_agents_by_default: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_agemt_ids: Union[None, Unset, list[str]]
        if isinstance(self.allow_agemt_ids, Unset):
            allow_agemt_ids = UNSET
        elif isinstance(self.allow_agemt_ids, list):
            allow_agemt_ids = self.allow_agemt_ids

        else:
            allow_agemt_ids = self.allow_agemt_ids

        deny_agent_ids: Union[None, Unset, list[str]]
        if isinstance(self.deny_agent_ids, Unset):
            deny_agent_ids = UNSET
        elif isinstance(self.deny_agent_ids, list):
            deny_agent_ids = self.deny_agent_ids

        else:
            deny_agent_ids = self.deny_agent_ids

        allow_agents_by_default: Union[None, Unset, bool]
        if isinstance(self.allow_agents_by_default, Unset):
            allow_agents_by_default = UNSET
        else:
            allow_agents_by_default = self.allow_agents_by_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_agemt_ids is not UNSET:
            field_dict["allowAgemtIds"] = allow_agemt_ids
        if deny_agent_ids is not UNSET:
            field_dict["denyAgentIds"] = deny_agent_ids
        if allow_agents_by_default is not UNSET:
            field_dict["allowAgentsByDefault"] = allow_agents_by_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_allow_agemt_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allow_agemt_ids_type_0 = cast(list[str], data)

                return allow_agemt_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        allow_agemt_ids = _parse_allow_agemt_ids(d.pop("allowAgemtIds", UNSET))

        def _parse_deny_agent_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                deny_agent_ids_type_0 = cast(list[str], data)

                return deny_agent_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        deny_agent_ids = _parse_deny_agent_ids(d.pop("denyAgentIds", UNSET))

        def _parse_allow_agents_by_default(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        allow_agents_by_default = _parse_allow_agents_by_default(d.pop("allowAgentsByDefault", UNSET))

        update_plugin_agent_rules_request = cls(
            allow_agemt_ids=allow_agemt_ids,
            deny_agent_ids=deny_agent_ids,
            allow_agents_by_default=allow_agents_by_default,
        )

        update_plugin_agent_rules_request.additional_properties = d
        return update_plugin_agent_rules_request

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
