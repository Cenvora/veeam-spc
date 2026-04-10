from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.discovery_rule_notification_settings_schedule_type import DiscoveryRuleNotificationSettingsScheduleType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.discovery_rule_notification_settings_week_settings_type_0 import (
        DiscoveryRuleNotificationSettingsWeekSettingsType0,
    )


T = TypeVar("T", bound="DiscoveryRuleNotificationSettings")


@_attrs_define
class DiscoveryRuleNotificationSettings:
    """
    Example:
        {'isEnabled': True, 'scheduleType': 'Days', 'scheduleTime': '12:30', 'scheduleDay': 'Sunday', 'to':
            'administrator@vac.com', 'subject': 'VSPC Discovery Results', 'notifyOnTheFirstRun': False}

    Attributes:
        schedule_type (DiscoveryRuleNotificationSettingsScheduleType): Notification frequency.
        is_enabled (Union[Unset, bool]): Indicates whether notifications about discovery results are enabled. Default:
            True.
        schedule_time (Union[Unset, str]): Time at which notifications must are sent in the `hh:mm` format. Default:
            '10:00'.
        week_settings (Union['DiscoveryRuleNotificationSettingsWeekSettingsType0', None, Unset]):
        to (Union[None, Unset, str]): Email address at which notifications must be sent.
        subject (Union[None, Unset, str]): Subject of a notification message.
        notify_on_the_first_run (Union[Unset, bool]): Indicates whether a notification must be sent on the first
            Default: False.
    """

    schedule_type: DiscoveryRuleNotificationSettingsScheduleType
    is_enabled: Union[Unset, bool] = True
    schedule_time: Union[Unset, str] = "10:00"
    week_settings: Union["DiscoveryRuleNotificationSettingsWeekSettingsType0", None, Unset] = UNSET
    to: Union[None, Unset, str] = UNSET
    subject: Union[None, Unset, str] = UNSET
    notify_on_the_first_run: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.discovery_rule_notification_settings_week_settings_type_0 import (
            DiscoveryRuleNotificationSettingsWeekSettingsType0,
        )

        schedule_type = self.schedule_type.value

        is_enabled = self.is_enabled

        schedule_time = self.schedule_time

        week_settings: Union[None, Unset, dict[str, Any]]
        if isinstance(self.week_settings, Unset):
            week_settings = UNSET
        elif isinstance(self.week_settings, DiscoveryRuleNotificationSettingsWeekSettingsType0):
            week_settings = self.week_settings.to_dict()
        else:
            week_settings = self.week_settings

        to: Union[None, Unset, str]
        if isinstance(self.to, Unset):
            to = UNSET
        else:
            to = self.to

        subject: Union[None, Unset, str]
        if isinstance(self.subject, Unset):
            subject = UNSET
        else:
            subject = self.subject

        notify_on_the_first_run = self.notify_on_the_first_run

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scheduleType": schedule_type,
            }
        )
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if schedule_time is not UNSET:
            field_dict["scheduleTime"] = schedule_time
        if week_settings is not UNSET:
            field_dict["weekSettings"] = week_settings
        if to is not UNSET:
            field_dict["to"] = to
        if subject is not UNSET:
            field_dict["subject"] = subject
        if notify_on_the_first_run is not UNSET:
            field_dict["notifyOnTheFirstRun"] = notify_on_the_first_run

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.discovery_rule_notification_settings_week_settings_type_0 import (
            DiscoveryRuleNotificationSettingsWeekSettingsType0,
        )

        d = dict(src_dict)
        schedule_type = DiscoveryRuleNotificationSettingsScheduleType(d.pop("scheduleType"))

        is_enabled = d.pop("isEnabled", UNSET)

        schedule_time = d.pop("scheduleTime", UNSET)

        def _parse_week_settings(
            data: object,
        ) -> Union["DiscoveryRuleNotificationSettingsWeekSettingsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                week_settings_type_0 = DiscoveryRuleNotificationSettingsWeekSettingsType0.from_dict(data)

                return week_settings_type_0
            except:  # noqa: E722
                pass
            return cast(Union["DiscoveryRuleNotificationSettingsWeekSettingsType0", None, Unset], data)

        week_settings = _parse_week_settings(d.pop("weekSettings", UNSET))

        def _parse_to(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        to = _parse_to(d.pop("to", UNSET))

        def _parse_subject(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        subject = _parse_subject(d.pop("subject", UNSET))

        notify_on_the_first_run = d.pop("notifyOnTheFirstRun", UNSET)

        discovery_rule_notification_settings = cls(
            schedule_type=schedule_type,
            is_enabled=is_enabled,
            schedule_time=schedule_time,
            week_settings=week_settings,
            to=to,
            subject=subject,
            notify_on_the_first_run=notify_on_the_first_run,
        )

        discovery_rule_notification_settings.additional_properties = d
        return discovery_rule_notification_settings

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
