from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.label_scope import LabelScope
from ..types import UNSET, Unset

T = TypeVar("T", bound="LabelInput")


@_attrs_define
class LabelInput:
    """
    Example:
        {'key': 'Production', 'description': 'Repositories and agents serving production workloads.', 'scope':
            ['VbrRepositories', 'Agents']}

    Attributes:
        key (str): Label key. Must be unique across all labels.
        scope (list[LabelScope]): Array of categories to which a label may be assigned.
        description (str | Unset): Description of a label.
    """

    key: str
    scope: list[LabelScope]
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        scope = []
        for scope_item_data in self.scope:
            scope_item = scope_item_data.value
            scope.append(scope_item)

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "scope": scope,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

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

        description = d.pop("description", UNSET)

        label_input = cls(
            key=key,
            scope=scope,
            description=description,
        )

        label_input.additional_properties = d
        return label_input

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
