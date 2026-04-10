from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.local_user_rule_type import LocalUserRuleType
from ..models.win_context_type import WinContextType
from ..types import UNSET, Unset

T = TypeVar("T", bound="LocalUserRuleDiscoveryItem")


@_attrs_define
class LocalUserRuleDiscoveryItem:
    """
    Attributes:
        sid (Union[Unset, str]): SID assigned to a user or group.
        name (Union[Unset, str]): Name of a user or group.
        display_name (Union[Unset, str]): Display name of a user or group.
        description (Union[Unset, str]): Description of a user or group.
        type_ (Union[Unset, LocalUserRuleType]): Type of a user or group.
        context_type (Union[Unset, WinContextType]): Type of a location where an account is stored.
    """

    sid: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    type_: Union[Unset, LocalUserRuleType] = UNSET
    context_type: Union[Unset, WinContextType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sid = self.sid

        name = self.name

        display_name = self.display_name

        description = self.description

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        context_type: Union[Unset, str] = UNSET
        if not isinstance(self.context_type, Unset):
            context_type = self.context_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sid is not UNSET:
            field_dict["sid"] = sid
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if type_ is not UNSET:
            field_dict["type"] = type_
        if context_type is not UNSET:
            field_dict["contextType"] = context_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sid = d.pop("sid", UNSET)

        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        description = d.pop("description", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, LocalUserRuleType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = LocalUserRuleType(_type_)

        _context_type = d.pop("contextType", UNSET)
        context_type: Union[Unset, WinContextType]
        if isinstance(_context_type, Unset):
            context_type = UNSET
        else:
            context_type = WinContextType(_context_type)

        local_user_rule_discovery_item = cls(
            sid=sid,
            name=name,
            display_name=display_name,
            description=description,
            type_=type_,
            context_type=context_type,
        )

        local_user_rule_discovery_item.additional_properties = d
        return local_user_rule_discovery_item

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
