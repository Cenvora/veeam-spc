from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_alarms_settings_daily_sorting import NotificationAlarmsSettingsDailySorting
from ..models.notification_alarms_settings_daily_status_filter_type_0_item import (
    NotificationAlarmsSettingsDailyStatusFilterType0Item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationAlarmsSettings")


@_attrs_define
class NotificationAlarmsSettings:
    r"""
    Attributes:
        from_ (Union[None, Unset, str]): Email address from which notifications must be sent.
        to (Union[None, Unset, str]): Email address at which notifications must be sent.
        daily_subject (Union[Unset, str]): Subject of notification message. Default: 'Company: \\"%company%\\",
            Location: \\"%location%\\", Alarm: \\"%alarmName%\\", Status: \\"%alarmStatus%\\" '.
        is_daily_notification_enabled (Union[Unset, bool]): Indicates whether summary daily notifications is enabled.
        daily_time (Union[Unset, str]): Time of the day when summary daily notifications are sent. Default: '9:00'.
        daily_status_filter (Union[None, Unset, list[NotificationAlarmsSettingsDailyStatusFilterType0Item]]): Array of
            statuses that alarms must have to be included into daily notifications.
        daily_sorting (Union[Unset, NotificationAlarmsSettingsDailySorting]): Type of sorting applied to the list of
            alarms included into daily notifications. Default: NotificationAlarmsSettingsDailySorting.BYTIME.
    """

    from_: Union[None, Unset, str] = UNSET
    to: Union[None, Unset, str] = UNSET
    daily_subject: Union[Unset, str] = (
        'Company: \\"%company%\\", Location: \\"%location%\\", Alarm: \\"%alarmName%\\", Status: \\"%alarmStatus%\\" '
    )
    is_daily_notification_enabled: Union[Unset, bool] = UNSET
    daily_time: Union[Unset, str] = "9:00"
    daily_status_filter: Union[None, Unset, list[NotificationAlarmsSettingsDailyStatusFilterType0Item]] = UNSET
    daily_sorting: Union[Unset, NotificationAlarmsSettingsDailySorting] = NotificationAlarmsSettingsDailySorting.BYTIME
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

        daily_subject = self.daily_subject

        is_daily_notification_enabled = self.is_daily_notification_enabled

        daily_time = self.daily_time

        daily_status_filter: Union[None, Unset, list[str]]
        if isinstance(self.daily_status_filter, Unset):
            daily_status_filter = UNSET
        elif isinstance(self.daily_status_filter, list):
            daily_status_filter = []
            for daily_status_filter_type_0_item_data in self.daily_status_filter:
                daily_status_filter_type_0_item = daily_status_filter_type_0_item_data.value
                daily_status_filter.append(daily_status_filter_type_0_item)

        else:
            daily_status_filter = self.daily_status_filter

        daily_sorting: Union[Unset, str] = UNSET
        if not isinstance(self.daily_sorting, Unset):
            daily_sorting = self.daily_sorting.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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

        daily_subject = d.pop("dailySubject", UNSET)

        is_daily_notification_enabled = d.pop("isDailyNotificationEnabled", UNSET)

        daily_time = d.pop("dailyTime", UNSET)

        def _parse_daily_status_filter(
            data: object,
        ) -> Union[None, Unset, list[NotificationAlarmsSettingsDailyStatusFilterType0Item]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                daily_status_filter_type_0 = []
                _daily_status_filter_type_0 = data
                for daily_status_filter_type_0_item_data in _daily_status_filter_type_0:
                    daily_status_filter_type_0_item = NotificationAlarmsSettingsDailyStatusFilterType0Item(
                        daily_status_filter_type_0_item_data
                    )

                    daily_status_filter_type_0.append(daily_status_filter_type_0_item)

                return daily_status_filter_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[NotificationAlarmsSettingsDailyStatusFilterType0Item]], data)

        daily_status_filter = _parse_daily_status_filter(d.pop("dailyStatusFilter", UNSET))

        _daily_sorting = d.pop("dailySorting", UNSET)
        daily_sorting: Union[Unset, NotificationAlarmsSettingsDailySorting]
        if isinstance(_daily_sorting, Unset):
            daily_sorting = UNSET
        else:
            daily_sorting = NotificationAlarmsSettingsDailySorting(_daily_sorting)

        notification_alarms_settings = cls(
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
