from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.label_scope import LabelScope
from ..types import UNSET, Unset

T = TypeVar("T", bound="Label")


@_attrs_define
class Label:
    """Assigned label.

    Attributes:
        key (str): Label key used for identification.
        scope (list[LabelScope]): Array of categories to which a label may be assigned.
        instance_uid (UUID | Unset): UID assigned to a label.
        description (str | Unset): Description of a label.
        object_count (int | Unset): Number of objects to which a label is assigned.
    """

    key: str
    scope: list[LabelScope]
    instance_uid: UUID | Unset = UNSET
    description: str | Unset = UNSET
    object_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        scope = []
        for scope_item_data in self.scope:
            scope_item = scope_item_data.value
            scope.append(scope_item)

        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        description = self.description

        object_count = self.object_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "scope": scope,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if description is not UNSET:
            field_dict["description"] = description
        if object_count is not UNSET:
            field_dict["objectCount"] = object_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        scope = []
        _scope = d.pop("scope")
        for scope_item_data in _scope:
            scope_item = LabelScope(scope_item_data)

            scope.append(scope_item)

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        description = d.pop("description", UNSET)

        object_count = d.pop("objectCount", UNSET)

        label = cls(
            key=key,
            scope=scope,
            instance_uid=instance_uid,
            description=description,
            object_count=object_count,
        )

        label.additional_properties = d
        return label

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
