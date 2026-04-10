from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.active_directory_tree_node_type import ActiveDirectoryTreeNodeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActiveDirectoryTreeNode")


@_attrs_define
class ActiveDirectoryTreeNode:
    """
    Attributes:
        id (Union[Unset, str]): ID assigned to an organizational unit.
        name (Union[Unset, str]): Name of an organizational unit.
        children (Union[None, Unset, list['ActiveDirectoryTreeNode']]): Array of child organizational units.
        type_ (Union[Unset, ActiveDirectoryTreeNodeType]): Type of an organizational unit.
        leaf (Union[Unset, bool]): Indicates whether an organizational unit has child objects.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    children: Union[None, Unset, list["ActiveDirectoryTreeNode"]] = UNSET
    type_: Union[Unset, ActiveDirectoryTreeNodeType] = UNSET
    leaf: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        children: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.children, Unset):
            children = UNSET
        elif isinstance(self.children, list):
            children = []
            for children_type_0_item_data in self.children:
                children_type_0_item = children_type_0_item_data.to_dict()
                children.append(children_type_0_item)

        else:
            children = self.children

        type_: Union[Unset, str] = UNSET
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

        def _parse_children(data: object) -> Union[None, Unset, list["ActiveDirectoryTreeNode"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                children_type_0 = []
                _children_type_0 = data
                for children_type_0_item_data in _children_type_0:
                    children_type_0_item = ActiveDirectoryTreeNode.from_dict(children_type_0_item_data)

                    children_type_0.append(children_type_0_item)

                return children_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["ActiveDirectoryTreeNode"]], data)

        children = _parse_children(d.pop("children", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ActiveDirectoryTreeNodeType]
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
