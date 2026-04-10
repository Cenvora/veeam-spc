import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

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
        title (Union[Unset, str]): Title of a message.
        description (Union[Unset, str]): Description of a process.
        severity (Union[Unset, BackupFailoverPlanSessionMessageSeverity]): Severity of a failover plan session message.
        start_time (Union[None, Unset, datetime.datetime]): Start date and time of a process.
        end_time (Union[None, Unset, datetime.datetime]): End date and time of a process.
    """

    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    severity: Union[Unset, BackupFailoverPlanSessionMessageSeverity] = UNSET
    start_time: Union[None, Unset, datetime.datetime] = UNSET
    end_time: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        description = self.description

        severity: Union[Unset, str] = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        start_time: Union[None, Unset, str]
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        elif isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        end_time: Union[None, Unset, str]
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

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
        severity: Union[Unset, BackupFailoverPlanSessionMessageSeverity]
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = BackupFailoverPlanSessionMessageSeverity(_severity)

        def _parse_start_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_type_0 = isoparse(data)

                return start_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        start_time = _parse_start_time(d.pop("startTime", UNSET))

        def _parse_end_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = isoparse(data)

                return end_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        end_time = _parse_end_time(d.pop("endTime", UNSET))

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
