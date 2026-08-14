from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alarm_action_condition import AlarmActionCondition
from ..models.alarm_action_type import AlarmActionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlarmActionInput")


@_attrs_define
class AlarmActionInput:
    """
    Example:
        {'type': 'SendCustomEmail', 'condition': 'ErrorsAndWarnings', 'isEnabled': True, 'value':
            'noc@techcompany.local', 'comment': 'Notify the NOC team about job failures and warnings.'}

    Attributes:
        type_ (AlarmActionType):
        condition (AlarmActionCondition):
        is_enabled (bool | Unset): Whether the alarm action is enabled. Default: True.
        value (str | Unset): Action value: email address for SendCustomEmail, script path for Execute* types, webhook
            UID for SendWebhook.
        comment (str | Unset): Comment for the alarm action.
    """

    type_: AlarmActionType
    condition: AlarmActionCondition
    is_enabled: bool | Unset = True
    value: str | Unset = UNSET
    comment: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        condition = self.condition.value

        is_enabled = self.is_enabled

        value = self.value

        comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "condition": condition,
            }
        )
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if value is not UNSET:
            field_dict["value"] = value
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = AlarmActionType(d.pop("type"))

        condition = AlarmActionCondition(d.pop("condition"))

        is_enabled = d.pop("isEnabled", UNSET)

        value = d.pop("value", UNSET)

        comment = d.pop("comment", UNSET)

        alarm_action_input = cls(
            type_=type_,
            condition=condition,
            is_enabled=is_enabled,
            value=value,
            comment=comment,
        )

        alarm_action_input.additional_properties = d
        return alarm_action_input

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
