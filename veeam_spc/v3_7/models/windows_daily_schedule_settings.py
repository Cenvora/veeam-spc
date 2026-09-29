from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.windows_daily_schedule_settings_daily_mode import WindowsDailyScheduleSettingsDailyMode
from ..models.windows_daily_schedule_settings_specific_days_type_0_item import (
    WindowsDailyScheduleSettingsSpecificDaysType0Item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="WindowsDailyScheduleSettings")


@_attrs_define
class WindowsDailyScheduleSettings:
    """
    Attributes:
        time (str | Unset): Time when a job must start, in the `hh:mm` format. Default: '0:30'.
        daily_mode (WindowsDailyScheduleSettingsDailyMode | Unset): Type of daily schedule. Default:
            WindowsDailyScheduleSettingsDailyMode.EVERYDAY.
        specific_days (list[WindowsDailyScheduleSettingsSpecificDaysType0Item] | None | Unset): Array of the week days
            on which a job must start.
            > Required for the `SpecificDays` type of daily schedule.
    """

    time: str | Unset = "0:30"
    daily_mode: WindowsDailyScheduleSettingsDailyMode | Unset = WindowsDailyScheduleSettingsDailyMode.EVERYDAY
    specific_days: list[WindowsDailyScheduleSettingsSpecificDaysType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        daily_mode: str | Unset = UNSET
        if not isinstance(self.daily_mode, Unset):
            daily_mode = self.daily_mode.value

        specific_days: list[str] | None | Unset
        if isinstance(self.specific_days, Unset):
            specific_days = UNSET
        elif isinstance(self.specific_days, list):
            specific_days = []
            for specific_days_type_0_item_data in self.specific_days:
                specific_days_type_0_item = specific_days_type_0_item_data.value
                specific_days.append(specific_days_type_0_item)

        else:
            specific_days = self.specific_days

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
        daily_mode: WindowsDailyScheduleSettingsDailyMode | Unset
        if isinstance(_daily_mode, Unset):
            daily_mode = UNSET
        else:
            daily_mode = WindowsDailyScheduleSettingsDailyMode(_daily_mode)

        def _parse_specific_days(
            data: object,
        ) -> list[WindowsDailyScheduleSettingsSpecificDaysType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                specific_days_type_0 = []
                _specific_days_type_0 = data
                for specific_days_type_0_item_data in _specific_days_type_0:
                    specific_days_type_0_item = WindowsDailyScheduleSettingsSpecificDaysType0Item(
                        specific_days_type_0_item_data
                    )

                    specific_days_type_0.append(specific_days_type_0_item)

                return specific_days_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[WindowsDailyScheduleSettingsSpecificDaysType0Item] | None | Unset, data)

        specific_days = _parse_specific_days(d.pop("specificDays", UNSET))

        windows_daily_schedule_settings = cls(
            time=time,
            daily_mode=daily_mode,
            specific_days=specific_days,
        )

        windows_daily_schedule_settings.additional_properties = d
        return windows_daily_schedule_settings

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
