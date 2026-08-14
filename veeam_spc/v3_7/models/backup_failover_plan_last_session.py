from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.backup_failover_plan_session_status import BackupFailoverPlanSessionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_failover_plan_session_message import BackupFailoverPlanSessionMessage


T = TypeVar("T", bound="BackupFailoverPlanLastSession")


@_attrs_define
class BackupFailoverPlanLastSession:
    """Information on the latest failover plan session.

    Attributes:
        instance_uid (UUID): UID assigned to the latest failover plan session.
        end_time (datetime.datetime | Unset): Date and time when the latest failover plan session ended.
        status (BackupFailoverPlanSessionStatus | Unset): Status of a failover plan session.
        message (str | Unset): Message that is displayed in case of failover plan failure or warnings.
        detailed_messages (list[BackupFailoverPlanSessionMessage] | Unset): Array of detailed log messages. Available
            only in Veeam Backup & Replication v13 or later.
    """

    instance_uid: UUID
    end_time: datetime.datetime | Unset = UNSET
    status: BackupFailoverPlanSessionStatus | Unset = UNSET
    message: str | Unset = UNSET
    detailed_messages: list[BackupFailoverPlanSessionMessage] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid = str(self.instance_uid)

        end_time: str | Unset = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        message = self.message

        detailed_messages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.detailed_messages, Unset):
            detailed_messages = []
            for detailed_messages_item_data in self.detailed_messages:
                detailed_messages_item = detailed_messages_item_data.to_dict()
                detailed_messages.append(detailed_messages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instanceUid": instance_uid,
            }
        )
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message
        if detailed_messages is not UNSET:
            field_dict["detailedMessages"] = detailed_messages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_failover_plan_session_message import BackupFailoverPlanSessionMessage

        d = dict(src_dict)
        instance_uid = UUID(d.pop("instanceUid"))

        _end_time = d.pop("endTime", UNSET)
        end_time: datetime.datetime | Unset
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        _status = d.pop("status", UNSET)
        status: BackupFailoverPlanSessionStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BackupFailoverPlanSessionStatus(_status)

        message = d.pop("message", UNSET)

        _detailed_messages = d.pop("detailedMessages", UNSET)
        detailed_messages: list[BackupFailoverPlanSessionMessage] | Unset = UNSET
        if _detailed_messages is not UNSET:
            detailed_messages = []
            for detailed_messages_item_data in _detailed_messages:
                detailed_messages_item = BackupFailoverPlanSessionMessage.from_dict(detailed_messages_item_data)

                detailed_messages.append(detailed_messages_item)

        backup_failover_plan_last_session = cls(
            instance_uid=instance_uid,
            end_time=end_time,
            status=status,
            message=message,
            detailed_messages=detailed_messages,
        )

        backup_failover_plan_last_session.additional_properties = d
        return backup_failover_plan_last_session

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
