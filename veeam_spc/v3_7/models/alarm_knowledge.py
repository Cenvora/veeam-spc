from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlarmKnowledge")


@_attrs_define
class AlarmKnowledge:
    """Knowledge base for an alarm template.

    Attributes:
        summary (str | Unset): General description of an alarm template.
        cause (str | Unset): Possible causes of an alarm trigger.
        resolution (str | Unset): Recommended solutions.
        custom (str | Unset): Custom knowledge base content provided by an administrator. Shown to operators
            in addition to the predefined summary, cause, and resolution. Update via
            PATCH /alarms/templates/{alarmUid}/knowledge.
    """

    summary: str | Unset = UNSET
    cause: str | Unset = UNSET
    resolution: str | Unset = UNSET
    custom: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summary = self.summary

        cause = self.cause

        resolution = self.resolution

        custom = self.custom

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if summary is not UNSET:
            field_dict["summary"] = summary
        if cause is not UNSET:
            field_dict["cause"] = cause
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if custom is not UNSET:
            field_dict["custom"] = custom

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        summary = d.pop("summary", UNSET)

        cause = d.pop("cause", UNSET)

        resolution = d.pop("resolution", UNSET)

        custom = d.pop("custom", UNSET)

        alarm_knowledge = cls(
            summary=summary,
            cause=cause,
            resolution=resolution,
            custom=custom,
        )

        alarm_knowledge.additional_properties = d
        return alarm_knowledge

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
