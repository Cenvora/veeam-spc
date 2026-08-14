from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlarmKnowledgePatch")


@_attrs_define
class AlarmKnowledgePatch:
    """Knowledge base customization for an alarm template. Send via
    PATCH /alarms/templates/{alarmUid}/knowledge to override the predefined
    knowledge base content for a single alarm template.

        Example:
            {'custom': 'Internal runbook: check VBR job session logs on vbr01.tech.local before escalating. If the job has
                been disabled intentionally for maintenance, suppress this alarm via the suppression schedule instead of re-
                enabling the job.'}

        Attributes:
            custom (str | Unset): Custom knowledge base content provided by an administrator. Send an empty
                string or null to clear a previously customized value.
    """

    custom: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom = self.custom

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom is not UNSET:
            field_dict["custom"] = custom

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        custom = d.pop("custom", UNSET)

        alarm_knowledge_patch = cls(
            custom=custom,
        )

        alarm_knowledge_patch.additional_properties = d
        return alarm_knowledge_patch

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
