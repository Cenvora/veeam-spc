from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.discovery_rule_notification_settings_week_settings_schedule_day import (
    DiscoveryRuleNotificationSettingsWeekSettingsScheduleDay,
)

T = TypeVar("T", bound="DiscoveryRuleNotificationSettingsWeekSettings")


@_attrs_define
class DiscoveryRuleNotificationSettingsWeekSettings:
    """
    Attributes:
        schedule_day (DiscoveryRuleNotificationSettingsWeekSettingsScheduleDay): Day at which notifications must are
            sent.
    """

    schedule_day: DiscoveryRuleNotificationSettingsWeekSettingsScheduleDay
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_day = self.schedule_day.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scheduleDay": schedule_day,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        schedule_day = DiscoveryRuleNotificationSettingsWeekSettingsScheduleDay(d.pop("scheduleDay"))

        discovery_rule_notification_settings_week_settings = cls(
            schedule_day=schedule_day,
        )

        discovery_rule_notification_settings_week_settings.additional_properties = d
        return discovery_rule_notification_settings_week_settings

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
