from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.org_container_type import OrgContainerType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgContainer")


@_attrs_define
class OrgContainer:
    """
    Attributes:
        name (str): Name of an organization.
        instance_uid (UUID | Unset): UID assigned to an organization.
        type_ (OrgContainerType | Unset): Type of an organization container. Default: OrgContainerType.CUSTOM.
        children_organizations (list[UUID] | Unset): Array of UIDs assigned to organizations in a container.
        children_containers (list[UUID] | Unset): Array of UIDs assigned to child organization containers.
    """

    name: str
    instance_uid: UUID | Unset = UNSET
    type_: OrgContainerType | Unset = OrgContainerType.CUSTOM
    children_organizations: list[UUID] | Unset = UNSET
    children_containers: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        children_organizations: list[str] | Unset = UNSET
        if not isinstance(self.children_organizations, Unset):
            children_organizations = []
            for children_organizations_item_data in self.children_organizations:
                children_organizations_item = str(children_organizations_item_data)
                children_organizations.append(children_organizations_item)

        children_containers: list[str] | Unset = UNSET
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
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if type_ is not UNSET:
            field_dict["type"] = type_
        if children_organizations is not UNSET:
            field_dict["childrenOrganizations"] = children_organizations
        if children_containers is not UNSET:
            field_dict["childrenContainers"] = children_containers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _type_ = d.pop("type", UNSET)
        type_: OrgContainerType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = OrgContainerType(_type_)

        _children_organizations = d.pop("childrenOrganizations", UNSET)
        children_organizations: list[UUID] | Unset = UNSET
        if _children_organizations is not UNSET:
            children_organizations = []
            for children_organizations_item_data in _children_organizations:
                children_organizations_item = UUID(children_organizations_item_data)

                children_organizations.append(children_organizations_item)

        _children_containers = d.pop("childrenContainers", UNSET)
        children_containers: list[UUID] | Unset = UNSET
        if _children_containers is not UNSET:
            children_containers = []
            for children_containers_item_data in _children_containers:
                children_containers_item = UUID(children_containers_item_data)

                children_containers.append(children_containers_item)

        org_container = cls(
            name=name,
            instance_uid=instance_uid,
            type_=type_,
            children_organizations=children_organizations,
            children_containers=children_containers,
        )

        org_container.additional_properties = d
        return org_container

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
