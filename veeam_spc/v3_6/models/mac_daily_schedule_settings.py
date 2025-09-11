from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mac_daily_schedule_settings_daily_mode import MacDailyScheduleSettingsDailyMode
from ..models.mac_daily_schedule_settings_specific_days_item import MacDailyScheduleSettingsSpecificDaysItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="MacDailyScheduleSettings")


@_attrs_define
class MacDailyScheduleSettings:
    """
    Attributes:
        time (Union[Unset, str]): Time when a job must start, in the `hh:mm` format. Default: '0:30'.
        daily_mode (Union[Unset, MacDailyScheduleSettingsDailyMode]): Type of the daily schedule. Default:
            MacDailyScheduleSettingsDailyMode.EVERYDAY.
        specific_days (Union[Unset, list[MacDailyScheduleSettingsSpecificDaysItem]]): Array of the week days on which a
            job must start.
            > Required for the `SpecificDays` type of the daily schedule.
    """

    time: Union[Unset, str] = "0:30"
    daily_mode: Union[Unset, MacDailyScheduleSettingsDailyMode] = MacDailyScheduleSettingsDailyMode.EVERYDAY
    specific_days: Union[Unset, list[MacDailyScheduleSettingsSpecificDaysItem]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        daily_mode: Union[Unset, str] = UNSET
        if not isinstance(self.daily_mode, Unset):
            daily_mode = self.daily_mode.value

        specific_days: Union[Unset, list[str]] = UNSET
        if not isinstance(self.specific_days, Unset):
            specific_days = []
            for specific_days_item_data in self.specific_days:
                specific_days_item = specific_days_item_data.value
                specific_days.append(specific_days_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if daily_mode is not UNSET:
            field_dict["dailyMode"] = daily_mode
        if specific_days is not UNSET:
            field_dict["specificDays"] = specific_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        _daily_mode = d.pop("dailyMode", UNSET)
        daily_mode: Union[Unset, MacDailyScheduleSettingsDailyMode]
        if isinstance(_daily_mode, Unset):
            daily_mode = UNSET
        else:
            daily_mode = MacDailyScheduleSettingsDailyMode(_daily_mode)

        specific_days = []
        _specific_days = d.pop("specificDays", UNSET)
        for specific_days_item_data in _specific_days or []:
            specific_days_item = MacDailyScheduleSettingsSpecificDaysItem(specific_days_item_data)

            specific_days.append(specific_days_item)

        mac_daily_schedule_settings = cls(
            time=time,
            daily_mode=daily_mode,
            specific_days=specific_days,
        )

        mac_daily_schedule_settings.additional_properties = d
        return mac_daily_schedule_settings

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
