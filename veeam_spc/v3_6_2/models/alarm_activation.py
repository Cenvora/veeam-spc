from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.alarm_activation_status import AlarmActivationStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlarmActivation")


@_attrs_define
class AlarmActivation:
    r"""
    Attributes:
        instance_uid (UUID | Unset): UID assigned to an alarm trigger.
        time (datetime.datetime | Unset): Date and time of an alarm trigger.
        status (AlarmActivationStatus | Unset): Alarm status.
        message (None | str | Unset): Cause of an alarm trigger.
            > Every line break is represented by the `\r\n` control characters.
        remark (None | str | Unset): Comment to the resolved alarm.
            > Every line break is represented by the `\r\n` control characters.
    """

    instance_uid: UUID | Unset = UNSET
    time: datetime.datetime | Unset = UNSET
    status: AlarmActivationStatus | Unset = UNSET
    message: None | str | Unset = UNSET
    remark: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        time: str | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        remark: None | str | Unset
        if isinstance(self.remark, Unset):
            remark = UNSET
        else:
            remark = self.remark

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if time is not UNSET:
            field_dict["time"] = time
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message
        if remark is not UNSET:
            field_dict["remark"] = remark

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _time = d.pop("time", UNSET)
        time: datetime.datetime | Unset
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        _status = d.pop("status", UNSET)
        status: AlarmActivationStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AlarmActivationStatus(_status)

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_remark(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remark = _parse_remark(d.pop("remark", UNSET))

        alarm_activation = cls(
            instance_uid=instance_uid,
            time=time,
            status=status,
            message=message,
            remark=remark,
        )

        alarm_activation.additional_properties = d
        return alarm_activation

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
