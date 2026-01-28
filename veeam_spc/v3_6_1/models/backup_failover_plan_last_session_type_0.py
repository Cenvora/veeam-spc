import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.backup_failover_plan_session_status import BackupFailoverPlanSessionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_failover_plan_session_message import BackupFailoverPlanSessionMessage


T = TypeVar("T", bound="BackupFailoverPlanLastSessionType0")


@_attrs_define
class BackupFailoverPlanLastSessionType0:
    """Information on the latest failover plan session.

    Attributes:
        instance_uid (UUID): UID assigned to the latest failover plan session.
        end_time (Union[None, Unset, datetime.datetime]): Date and time when the latest failover plan session ended.
        status (Union[Unset, BackupFailoverPlanSessionStatus]): Status of a failover plan session.
        message (Union[None, Unset, str]): Message that is displayed in case of failover plan failure or warnings.
        detailed_messages (Union[None, Unset, list['BackupFailoverPlanSessionMessage']]): Array of detailed log
            messages. Available only in Veeam Backup & Replication v13 or later.
    """

    instance_uid: UUID
    end_time: Union[None, Unset, datetime.datetime] = UNSET
    status: Union[Unset, BackupFailoverPlanSessionStatus] = UNSET
    message: Union[None, Unset, str] = UNSET
    detailed_messages: Union[None, Unset, list["BackupFailoverPlanSessionMessage"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid = str(self.instance_uid)

        end_time: Union[None, Unset, str]
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        message: Union[None, Unset, str]
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        detailed_messages: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.detailed_messages, Unset):
            detailed_messages = UNSET
        elif isinstance(self.detailed_messages, list):
            detailed_messages = []
            for detailed_messages_type_0_item_data in self.detailed_messages:
                detailed_messages_type_0_item = detailed_messages_type_0_item_data.to_dict()
                detailed_messages.append(detailed_messages_type_0_item)

        else:
            detailed_messages = self.detailed_messages

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

        _status = d.pop("status", UNSET)
        status: Union[Unset, BackupFailoverPlanSessionStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BackupFailoverPlanSessionStatus(_status)

        def _parse_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_detailed_messages(data: object) -> Union[None, Unset, list["BackupFailoverPlanSessionMessage"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                detailed_messages_type_0 = []
                _detailed_messages_type_0 = data
                for detailed_messages_type_0_item_data in _detailed_messages_type_0:
                    detailed_messages_type_0_item = BackupFailoverPlanSessionMessage.from_dict(
                        detailed_messages_type_0_item_data
                    )

                    detailed_messages_type_0.append(detailed_messages_type_0_item)

                return detailed_messages_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["BackupFailoverPlanSessionMessage"]], data)

        detailed_messages = _parse_detailed_messages(d.pop("detailedMessages", UNSET))

        backup_failover_plan_last_session_type_0 = cls(
            instance_uid=instance_uid,
            end_time=end_time,
            status=status,
            message=message,
            detailed_messages=detailed_messages,
        )

        backup_failover_plan_last_session_type_0.additional_properties = d
        return backup_failover_plan_last_session_type_0

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
