from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LabelAssignmentTarget")


@_attrs_define
class LabelAssignmentTarget:
    """
    Attributes:
        target_type (str | Unset): Type of the assigned object.
        target_uid (UUID | Unset): Unique identifier of the assigned object.
        assigned_at (datetime.datetime | Unset): Date and time when the label was assigned.
    """

    target_type: str | Unset = UNSET
    target_uid: UUID | Unset = UNSET
    assigned_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_type = self.target_type

        target_uid: str | Unset = UNSET
        if not isinstance(self.target_uid, Unset):
            target_uid = str(self.target_uid)

        assigned_at: str | Unset = UNSET
        if not isinstance(self.assigned_at, Unset):
            assigned_at = self.assigned_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target_type is not UNSET:
            field_dict["targetType"] = target_type
        if target_uid is not UNSET:
            field_dict["targetUid"] = target_uid
        if assigned_at is not UNSET:
            field_dict["assignedAt"] = assigned_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_type = d.pop("targetType", UNSET)

        _target_uid = d.pop("targetUid", UNSET)
        target_uid: UUID | Unset
        if isinstance(_target_uid, Unset):
            target_uid = UNSET
        else:
            target_uid = UUID(_target_uid)

        _assigned_at = d.pop("assignedAt", UNSET)
        assigned_at: datetime.datetime | Unset
        if isinstance(_assigned_at, Unset):
            assigned_at = UNSET
        else:
            assigned_at = isoparse(_assigned_at)

        label_assignment_target = cls(
            target_type=target_type,
            target_uid=target_uid,
            assigned_at=assigned_at,
        )

        label_assignment_target.additional_properties = d
        return label_assignment_target

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
