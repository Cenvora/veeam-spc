from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
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
        instance_uid (Union[Unset, UUID]): UID assigned to an organization.
        type_ (Union[Unset, OrgContainerType]): Type of an organization container. Default: OrgContainerType.CUSTOM.
        children_organizations (Union[None, Unset, list[UUID]]): Array of UIDs assigned to organizations in a container.
        children_containers (Union[None, Unset, list[UUID]]): Array of UIDs assigned to child organization containers.
    """

    name: str
    instance_uid: Union[Unset, UUID] = UNSET
    type_: Union[Unset, OrgContainerType] = OrgContainerType.CUSTOM
    children_organizations: Union[None, Unset, list[UUID]] = UNSET
    children_containers: Union[None, Unset, list[UUID]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        children_organizations: Union[None, Unset, list[str]]
        if isinstance(self.children_organizations, Unset):
            children_organizations = UNSET
        elif isinstance(self.children_organizations, list):
            children_organizations = []
            for children_organizations_type_0_item_data in self.children_organizations:
                children_organizations_type_0_item = str(children_organizations_type_0_item_data)
                children_organizations.append(children_organizations_type_0_item)

        else:
            children_organizations = self.children_organizations

        children_containers: Union[None, Unset, list[str]]
        if isinstance(self.children_containers, Unset):
            children_containers = UNSET
        elif isinstance(self.children_containers, list):
            children_containers = []
            for children_containers_type_0_item_data in self.children_containers:
                children_containers_type_0_item = str(children_containers_type_0_item_data)
                children_containers.append(children_containers_type_0_item)

        else:
            children_containers = self.children_containers

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
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, OrgContainerType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = OrgContainerType(_type_)

        def _parse_children_organizations(data: object) -> Union[None, Unset, list[UUID]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                children_organizations_type_0 = []
                _children_organizations_type_0 = data
                for children_organizations_type_0_item_data in _children_organizations_type_0:
                    children_organizations_type_0_item = UUID(children_organizations_type_0_item_data)

                    children_organizations_type_0.append(children_organizations_type_0_item)

                return children_organizations_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[UUID]], data)

        children_organizations = _parse_children_organizations(d.pop("childrenOrganizations", UNSET))

        def _parse_children_containers(data: object) -> Union[None, Unset, list[UUID]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                children_containers_type_0 = []
                _children_containers_type_0 = data
                for children_containers_type_0_item_data in _children_containers_type_0:
                    children_containers_type_0_item = UUID(children_containers_type_0_item_data)

                    children_containers_type_0.append(children_containers_type_0_item)

                return children_containers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[UUID]], data)

        children_containers = _parse_children_containers(d.pop("childrenContainers", UNSET))

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
