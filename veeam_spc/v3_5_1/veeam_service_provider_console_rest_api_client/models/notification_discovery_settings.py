from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationDiscoverySettings")


@_attrs_define
class NotificationDiscoverySettings:
    r"""
    Attributes:
        from_ (Union[None, Unset, str]): Email address from which notifications are sent.
        to (Union[None, Unset, str]): Email address at which notifications are sent.
        subject (Union[Unset, str]): Text that is displayed as a subject of notification. Default: 'Company:
            \\"%company%\\", Location: \\"%location%\\", Rule: \\"%ruleName%\\", Status: \\"%ruleStatus%\\" '.
        is_daily_notification_enabled (Union[Unset, bool]): Indicates whether daily notifications are enabled.
        daily_time (Union[None, Unset, str]): Time at which daily notifications are sent.
    """

    from_: Union[None, Unset, str] = UNSET
    to: Union[None, Unset, str] = UNSET
    subject: Union[Unset, str] = (
        'Company: \\"%company%\\", Location: \\"%location%\\", Rule: \\"%ruleName%\\", Status: \\"%ruleStatus%\\" '
    )
    is_daily_notification_enabled: Union[Unset, bool] = UNSET
    daily_time: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_: Union[None, Unset, str]
        if isinstance(self.from_, Unset):
            from_ = UNSET
        else:
            from_ = self.from_

        to: Union[None, Unset, str]
        if isinstance(self.to, Unset):
            to = UNSET
        else:
            to = self.to

        subject = self.subject

        is_daily_notification_enabled = self.is_daily_notification_enabled

        daily_time: Union[None, Unset, str]
        if isinstance(self.daily_time, Unset):
            daily_time = UNSET
        else:
            daily_time = self.daily_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if subject is not UNSET:
            field_dict["subject"] = subject
        if is_daily_notification_enabled is not UNSET:
            field_dict["isDailyNotificationEnabled"] = is_daily_notification_enabled
        if daily_time is not UNSET:
            field_dict["dailyTime"] = daily_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_from_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        from_ = _parse_from_(d.pop("from", UNSET))

        def _parse_to(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        to = _parse_to(d.pop("to", UNSET))

        subject = d.pop("subject", UNSET)

        is_daily_notification_enabled = d.pop("isDailyNotificationEnabled", UNSET)

        def _parse_daily_time(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        daily_time = _parse_daily_time(d.pop("dailyTime", UNSET))

        notification_discovery_settings = cls(
            from_=from_,
            to=to,
            subject=subject,
            is_daily_notification_enabled=is_daily_notification_enabled,
            daily_time=daily_time,
        )

        notification_discovery_settings.additional_properties = d
        return notification_discovery_settings

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
