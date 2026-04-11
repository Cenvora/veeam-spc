from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.activity_log_kind import ActivityLogKind
from ..models.activity_log_type import ActivityLogType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityLog")


@_attrs_define
class ActivityLog:
    """
    Attributes:
        message (str | Unset): Description of an activity.
        activity_log_type (ActivityLogType | Unset): Activity variation.
        activity_kind (ActivityLogKind | Unset): Type of an activity.
        date (datetime.datetime | Unset): Date and time when an activity was performed.
        user_uid (None | Unset | UUID): UID assigned to a user that initiated an activity.
        organization_uid (None | Unset | UUID): UID assigned to an organization.
    """

    message: str | Unset = UNSET
    activity_log_type: ActivityLogType | Unset = UNSET
    activity_kind: ActivityLogKind | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    user_uid: None | Unset | UUID = UNSET
    organization_uid: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        activity_log_type: str | Unset = UNSET
        if not isinstance(self.activity_log_type, Unset):
            activity_log_type = self.activity_log_type.value

        activity_kind: str | Unset = UNSET
        if not isinstance(self.activity_kind, Unset):
            activity_kind = self.activity_kind.value

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        user_uid: None | str | Unset
        if isinstance(self.user_uid, Unset):
            user_uid = UNSET
        elif isinstance(self.user_uid, UUID):
            user_uid = str(self.user_uid)
        else:
            user_uid = self.user_uid

        organization_uid: None | str | Unset
        if isinstance(self.organization_uid, Unset):
            organization_uid = UNSET
        elif isinstance(self.organization_uid, UUID):
            organization_uid = str(self.organization_uid)
        else:
            organization_uid = self.organization_uid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if activity_log_type is not UNSET:
            field_dict["activityLogType"] = activity_log_type
        if activity_kind is not UNSET:
            field_dict["activityKind"] = activity_kind
        if date is not UNSET:
            field_dict["date"] = date
        if user_uid is not UNSET:
            field_dict["userUid"] = user_uid
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        _activity_log_type = d.pop("activityLogType", UNSET)
        activity_log_type: ActivityLogType | Unset
        if isinstance(_activity_log_type, Unset):
            activity_log_type = UNSET
        else:
            activity_log_type = ActivityLogType(_activity_log_type)

        _activity_kind = d.pop("activityKind", UNSET)
        activity_kind: ActivityLogKind | Unset
        if isinstance(_activity_kind, Unset):
            activity_kind = UNSET
        else:
            activity_kind = ActivityLogKind(_activity_kind)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        def _parse_user_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_uid_type_0 = UUID(data)

                return user_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_uid = _parse_user_uid(d.pop("userUid", UNSET))

        def _parse_organization_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_uid_type_0 = UUID(data)

                return organization_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        organization_uid = _parse_organization_uid(d.pop("organizationUid", UNSET))

        activity_log = cls(
            message=message,
            activity_log_type=activity_log_type,
            activity_kind=activity_kind,
            date=date,
            user_uid=user_uid,
            organization_uid=organization_uid,
        )

        activity_log.additional_properties = d
        return activity_log

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
