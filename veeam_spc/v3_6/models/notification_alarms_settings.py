from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_alarms_settings_daily_sorting import NotificationAlarmsSettingsDailySorting
from ..models.notification_alarms_settings_daily_status_filter_item import (
    NotificationAlarmsSettingsDailyStatusFilterItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationAlarmsSettings")


@_attrs_define
class NotificationAlarmsSettings:
    r"""
    Attributes:
        sender_name (Union[Unset, str]): Name of a sender.
        from_ (Union[Unset, str]): Email address from which notifications must be sent.
        to (Union[Unset, str]): Email address at which notifications must be sent.
        daily_subject (Union[Unset, str]): Subject of notification message. Default: 'Company: \\"%company%\\",
            Location: \\"%location%\\", Alarm: \\"%alarmName%\\", Status: \\"%alarmStatus%\\" '.
        is_daily_notification_enabled (Union[Unset, bool]): Indicates whether summary daily notifications is enabled.
        daily_time (Union[Unset, str]): Time of the day when summary daily notifications are sent. Default: '9:00'.
        daily_status_filter (Union[Unset, list[NotificationAlarmsSettingsDailyStatusFilterItem]]): Array of statuses
            that alarms must have to be included into daily notifications.
        daily_sorting (Union[Unset, NotificationAlarmsSettingsDailySorting]): Type of sorting applied to the list of
            alarms included into daily notifications. Default: NotificationAlarmsSettingsDailySorting.BYTIME.
    """

    sender_name: Union[Unset, str] = UNSET
    from_: Union[Unset, str] = UNSET
    to: Union[Unset, str] = UNSET
    daily_subject: Union[Unset, str] = (
        'Company: \\"%company%\\", Location: \\"%location%\\", Alarm: \\"%alarmName%\\", Status: \\"%alarmStatus%\\" '
    )
    is_daily_notification_enabled: Union[Unset, bool] = UNSET
    daily_time: Union[Unset, str] = "9:00"
    daily_status_filter: Union[Unset, list[NotificationAlarmsSettingsDailyStatusFilterItem]] = UNSET
    daily_sorting: Union[Unset, NotificationAlarmsSettingsDailySorting] = NotificationAlarmsSettingsDailySorting.BYTIME
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sender_name = self.sender_name

        from_ = self.from_

        to = self.to

        daily_subject = self.daily_subject

        is_daily_notification_enabled = self.is_daily_notification_enabled

        daily_time = self.daily_time

        daily_status_filter: Union[Unset, list[str]] = UNSET
        if not isinstance(self.daily_status_filter, Unset):
            daily_status_filter = []
            for daily_status_filter_item_data in self.daily_status_filter:
                daily_status_filter_item = daily_status_filter_item_data.value
                daily_status_filter.append(daily_status_filter_item)

        daily_sorting: Union[Unset, str] = UNSET
        if not isinstance(self.daily_sorting, Unset):
            daily_sorting = self.daily_sorting.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sender_name is not UNSET:
            field_dict["senderName"] = sender_name
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if daily_subject is not UNSET:
            field_dict["dailySubject"] = daily_subject
        if is_daily_notification_enabled is not UNSET:
            field_dict["isDailyNotificationEnabled"] = is_daily_notification_enabled
        if daily_time is not UNSET:
            field_dict["dailyTime"] = daily_time
        if daily_status_filter is not UNSET:
            field_dict["dailyStatusFilter"] = daily_status_filter
        if daily_sorting is not UNSET:
            field_dict["dailySorting"] = daily_sorting

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sender_name = d.pop("senderName", UNSET)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        daily_subject = d.pop("dailySubject", UNSET)

        is_daily_notification_enabled = d.pop("isDailyNotificationEnabled", UNSET)

        daily_time = d.pop("dailyTime", UNSET)

        daily_status_filter = []
        _daily_status_filter = d.pop("dailyStatusFilter", UNSET)
        for daily_status_filter_item_data in _daily_status_filter or []:
            daily_status_filter_item = NotificationAlarmsSettingsDailyStatusFilterItem(daily_status_filter_item_data)

            daily_status_filter.append(daily_status_filter_item)

        _daily_sorting = d.pop("dailySorting", UNSET)
        daily_sorting: Union[Unset, NotificationAlarmsSettingsDailySorting]
        if isinstance(_daily_sorting, Unset):
            daily_sorting = UNSET
        else:
            daily_sorting = NotificationAlarmsSettingsDailySorting(_daily_sorting)

        notification_alarms_settings = cls(
            sender_name=sender_name,
            from_=from_,
            to=to,
            daily_subject=daily_subject,
            is_daily_notification_enabled=is_daily_notification_enabled,
            daily_time=daily_time,
            daily_status_filter=daily_status_filter,
            daily_sorting=daily_sorting,
        )

        notification_alarms_settings.additional_properties = d
        return notification_alarms_settings

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
