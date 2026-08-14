from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.backup_failover_plan_session_message_severity import BackupFailoverPlanSessionMessageSeverity
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupFailoverPlanSessionMessage")


@_attrs_define
class BackupFailoverPlanSessionMessage:
    """
    Attributes:
        title (str | Unset): Title of a message.
        description (str | Unset): Description of a process.
        severity (BackupFailoverPlanSessionMessageSeverity | Unset): Severity of a failover plan session message.
        start_time (datetime.datetime | Unset): Start date and time of a process.
        end_time (datetime.datetime | Unset): End date and time of a process.
    """

    title: str | Unset = UNSET
    description: str | Unset = UNSET
    severity: BackupFailoverPlanSessionMessageSeverity | Unset = UNSET
    start_time: datetime.datetime | Unset = UNSET
    end_time: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        description = self.description

        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        start_time: str | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        end_time: str | Unset = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if severity is not UNSET:
            field_dict["severity"] = severity
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        _severity = d.pop("severity", UNSET)
        severity: BackupFailoverPlanSessionMessageSeverity | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = BackupFailoverPlanSessionMessageSeverity(_severity)

        _start_time = d.pop("startTime", UNSET)
        start_time: datetime.datetime | Unset
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _end_time = d.pop("endTime", UNSET)
        end_time: datetime.datetime | Unset
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        backup_failover_plan_session_message = cls(
            title=title,
            description=description,
            severity=severity,
            start_time=start_time,
            end_time=end_time,
        )

        backup_failover_plan_session_message.additional_properties = d
        return backup_failover_plan_session_message

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
