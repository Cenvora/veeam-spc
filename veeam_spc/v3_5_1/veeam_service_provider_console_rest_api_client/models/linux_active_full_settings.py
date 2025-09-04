from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.linux_active_full_settings_schedule_type import LinuxActiveFullSettingsScheduleType
from ..models.linux_active_full_settings_weekly_on_days_type_0_item import LinuxActiveFullSettingsWeeklyOnDaysType0Item
from ..types import UNSET, Unset

T = TypeVar("T", bound="LinuxActiveFullSettings")


@_attrs_define
class LinuxActiveFullSettings:
    """
    Attributes:
        schedule_type (Union[Unset, LinuxActiveFullSettingsScheduleType]): Type of periodicity. Default:
            LinuxActiveFullSettingsScheduleType.NOTSCHEDULED.
        day_of_month (Union[None, Unset, int]): Day of the month. Default: 1.
        weekly_on_days (Union[None, Unset, list[LinuxActiveFullSettingsWeeklyOnDaysType0Item]]): Name of the week day.
    """

    schedule_type: Union[Unset, LinuxActiveFullSettingsScheduleType] = LinuxActiveFullSettingsScheduleType.NOTSCHEDULED
    day_of_month: Union[None, Unset, int] = 1
    weekly_on_days: Union[None, Unset, list[LinuxActiveFullSettingsWeeklyOnDaysType0Item]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_type: Union[Unset, str] = UNSET
        if not isinstance(self.schedule_type, Unset):
            schedule_type = self.schedule_type.value

        day_of_month: Union[None, Unset, int]
        if isinstance(self.day_of_month, Unset):
            day_of_month = UNSET
        else:
            day_of_month = self.day_of_month

        weekly_on_days: Union[None, Unset, list[str]]
        if isinstance(self.weekly_on_days, Unset):
            weekly_on_days = UNSET
        elif isinstance(self.weekly_on_days, list):
            weekly_on_days = []
            for weekly_on_days_type_0_item_data in self.weekly_on_days:
                weekly_on_days_type_0_item = weekly_on_days_type_0_item_data.value
                weekly_on_days.append(weekly_on_days_type_0_item)

        else:
            weekly_on_days = self.weekly_on_days

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

        def _parse_day_of_month(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        day_of_month = _parse_day_of_month(d.pop("dayOfMonth", UNSET))

        def _parse_weekly_on_days(
            data: object,
        ) -> Union[None, Unset, list[LinuxActiveFullSettingsWeeklyOnDaysType0Item]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                weekly_on_days_type_0 = []
                _weekly_on_days_type_0 = data
                for weekly_on_days_type_0_item_data in _weekly_on_days_type_0:
                    weekly_on_days_type_0_item = LinuxActiveFullSettingsWeeklyOnDaysType0Item(
                        weekly_on_days_type_0_item_data
                    )

                    weekly_on_days_type_0.append(weekly_on_days_type_0_item)

                return weekly_on_days_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[LinuxActiveFullSettingsWeeklyOnDaysType0Item]], data)

        weekly_on_days = _parse_weekly_on_days(d.pop("weeklyOnDays", UNSET))

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
