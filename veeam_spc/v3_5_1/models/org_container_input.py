from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgContainerInput")


@_attrs_define
class OrgContainerInput:
    """
    Attributes:
        name (str): Name of a container.
        children_organizations (Union[Unset, list[UUID]]): Array of UIDs assigned to organizations that must be included
            in a container.
        children_containers (Union[Unset, list[UUID]]): Array of UIDs assigned to child organization containers.
    """

    name: str
    children_organizations: Union[Unset, list[UUID]] = UNSET
    children_containers: Union[Unset, list[UUID]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        children_organizations: Union[Unset, list[str]] = UNSET
        if not isinstance(self.children_organizations, Unset):
            children_organizations = []
            for children_organizations_item_data in self.children_organizations:
                children_organizations_item = str(children_organizations_item_data)
                children_organizations.append(children_organizations_item)

        children_containers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.children_containers, Unset):
            children_containers = []
            for children_containers_item_data in self.children_containers:
                children_containers_item = str(children_containers_item_data)
                children_containers.append(children_containers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if children_organizations is not UNSET:
            field_dict["childrenOrganizations"] = children_organizations
        if children_containers is not UNSET:
            field_dict["childrenContainers"] = children_containers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        children_organizations = []
        _children_organizations = d.pop("childrenOrganizations", UNSET)
        for children_organizations_item_data in _children_organizations or []:
            children_organizations_item = UUID(children_organizations_item_data)

            children_organizations.append(children_organizations_item)

        children_containers = []
        _children_containers = d.pop("childrenContainers", UNSET)
        for children_containers_item_data in _children_containers or []:
            children_containers_item = UUID(children_containers_item_data)

            children_containers.append(children_containers_item)

        org_container_input = cls(
            name=name,
            children_organizations=children_organizations,
            children_containers=children_containers,
        )

        org_container_input.additional_properties = d
        return org_container_input

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
