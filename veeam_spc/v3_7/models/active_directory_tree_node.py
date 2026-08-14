from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.active_directory_tree_node_type import ActiveDirectoryTreeNodeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActiveDirectoryTreeNode")


@_attrs_define
class ActiveDirectoryTreeNode:
    """
    Attributes:
        id (str | Unset): ID assigned to an organizational unit.
        name (str | Unset): Name of an organizational unit.
        children (list[ActiveDirectoryTreeNode] | Unset): Array of child organizational units.
        type_ (ActiveDirectoryTreeNodeType | Unset): Type of an organizational unit.
        leaf (bool | Unset): Indicates whether an organizational unit has child objects.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    children: list[ActiveDirectoryTreeNode] | Unset = UNSET
    type_: ActiveDirectoryTreeNodeType | Unset = UNSET
    leaf: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        leaf = self.leaf

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if children is not UNSET:
            field_dict["children"] = children
        if type_ is not UNSET:
            field_dict["type"] = type_
        if leaf is not UNSET:
            field_dict["leaf"] = leaf

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _children = d.pop("children", UNSET)
        children: list[ActiveDirectoryTreeNode] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = ActiveDirectoryTreeNode.from_dict(children_item_data)

                children.append(children_item)

        _type_ = d.pop("type", UNSET)
        type_: ActiveDirectoryTreeNodeType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ActiveDirectoryTreeNodeType(_type_)

        leaf = d.pop("leaf", UNSET)

        active_directory_tree_node = cls(
            id=id,
            name=name,
            children=children,
            type_=type_,
            leaf=leaf,
        )

        active_directory_tree_node.additional_properties = d
        return active_directory_tree_node

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
