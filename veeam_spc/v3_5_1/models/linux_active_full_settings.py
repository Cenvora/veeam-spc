from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.linux_active_full_settings_schedule_type import LinuxActiveFullSettingsScheduleType
from ..models.linux_active_full_settings_weekly_on_days_item import LinuxActiveFullSettingsWeeklyOnDaysItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="LinuxActiveFullSettings")


@_attrs_define
class LinuxActiveFullSettings:
    """
    Attributes:
        schedule_type (Union[Unset, LinuxActiveFullSettingsScheduleType]): Type of periodicity. Default:
            LinuxActiveFullSettingsScheduleType.NOTSCHEDULED.
        day_of_month (Union[Unset, int]): Day of the month. Default: 1.
        weekly_on_days (Union[Unset, list[LinuxActiveFullSettingsWeeklyOnDaysItem]]): Name of the week day.
    """

    schedule_type: Union[Unset, LinuxActiveFullSettingsScheduleType] = LinuxActiveFullSettingsScheduleType.NOTSCHEDULED
    day_of_month: Union[Unset, int] = 1
    weekly_on_days: Union[Unset, list[LinuxActiveFullSettingsWeeklyOnDaysItem]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_type: Union[Unset, str] = UNSET
        if not isinstance(self.schedule_type, Unset):
            schedule_type = self.schedule_type.value

        day_of_month = self.day_of_month

        weekly_on_days: Union[Unset, list[str]] = UNSET
        if not isinstance(self.weekly_on_days, Unset):
            weekly_on_days = []
            for weekly_on_days_item_data in self.weekly_on_days:
                weekly_on_days_item = weekly_on_days_item_data.value
                weekly_on_days.append(weekly_on_days_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schedule_type is not UNSET:
            field_dict["scheduleType"] = schedule_type
        if day_of_month is not UNSET:
            field_dict["dayOfMonth"] = day_of_month
        if weekly_on_days is not UNSET:
            field_dict["weeklyOnDays"] = weekly_on_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _schedule_type = d.pop("scheduleType", UNSET)
        schedule_type: Union[Unset, LinuxActiveFullSettingsScheduleType]
        if isinstance(_schedule_type, Unset):
            schedule_type = UNSET
        else:
            schedule_type = LinuxActiveFullSettingsScheduleType(_schedule_type)

        day_of_month = d.pop("dayOfMonth", UNSET)

        weekly_on_days = []
        _weekly_on_days = d.pop("weeklyOnDays", UNSET)
        for weekly_on_days_item_data in _weekly_on_days or []:
            weekly_on_days_item = LinuxActiveFullSettingsWeeklyOnDaysItem(weekly_on_days_item_data)

            weekly_on_days.append(weekly_on_days_item)

        linux_active_full_settings = cls(
            schedule_type=schedule_type,
            day_of_month=day_of_month,
            weekly_on_days=weekly_on_days,
        )

        linux_active_full_settings.additional_properties = d
        return linux_active_full_settings

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
