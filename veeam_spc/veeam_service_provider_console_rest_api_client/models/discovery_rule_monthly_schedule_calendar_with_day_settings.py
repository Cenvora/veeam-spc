from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.discovery_rule_monthly_schedule_calendar_with_day_settings_day_of_week import (
    DiscoveryRuleMonthlyScheduleCalendarWithDaySettingsDayOfWeek,
)
from ..models.discovery_rule_monthly_schedule_calendar_with_day_settings_monthly_mode import (
    DiscoveryRuleMonthlyScheduleCalendarWithDaySettingsMonthlyMode,
)
from ..models.discovery_rule_monthly_schedule_calendar_with_day_settings_months_item import (
    DiscoveryRuleMonthlyScheduleCalendarWithDaySettingsMonthsItem,
)
from ..models.discovery_rule_monthly_schedule_calendar_with_day_settings_week_day_number import (
    DiscoveryRuleMonthlyScheduleCalendarWithDaySettingsWeekDayNumber,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DiscoveryRuleMonthlyScheduleCalendarWithDaySettings")


@_attrs_define
class DiscoveryRuleMonthlyScheduleCalendarWithDaySettings:
    """
    Attributes:
        monthly_mode (DiscoveryRuleMonthlyScheduleCalendarWithDaySettingsMonthlyMode): Type of schedule for monthly
            discovery. Default: DiscoveryRuleMonthlyScheduleCalendarWithDaySettingsMonthlyMode.DAY.
        months (list[DiscoveryRuleMonthlyScheduleCalendarWithDaySettingsMonthsItem]): Month.
        week_day_number (Union[Unset, DiscoveryRuleMonthlyScheduleCalendarWithDaySettingsWeekDayNumber]): Counting
            number of the week day.
            > Required for the `DayOfWeek` schedule type.
        day_of_week (Union[Unset, DiscoveryRuleMonthlyScheduleCalendarWithDaySettingsDayOfWeek]): Week day.
            > Required for the `DayOfWeek` schedule type.
        day (Union[Unset, int]): Day of the month.
            > Required for the `Day` schedule type.
    """

    months: list[DiscoveryRuleMonthlyScheduleCalendarWithDaySettingsMonthsItem]
    monthly_mode: DiscoveryRuleMonthlyScheduleCalendarWithDaySettingsMonthlyMode = (
        DiscoveryRuleMonthlyScheduleCalendarWithDaySettingsMonthlyMode.DAY
    )
    week_day_number: Union[Unset, DiscoveryRuleMonthlyScheduleCalendarWithDaySettingsWeekDayNumber] = UNSET
    day_of_week: Union[Unset, DiscoveryRuleMonthlyScheduleCalendarWithDaySettingsDayOfWeek] = UNSET
    day: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monthly_mode = self.monthly_mode.value

        months = []
        for months_item_data in self.months:
            months_item = months_item_data.value
            months.append(months_item)

        week_day_number: Union[Unset, str] = UNSET
        if not isinstance(self.week_day_number, Unset):
            week_day_number = self.week_day_number.value

        day_of_week: Union[Unset, str] = UNSET
        if not isinstance(self.day_of_week, Unset):
            day_of_week = self.day_of_week.value

        day = self.day

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "monthlyMode": monthly_mode,
                "months": months,
            }
        )
        if week_day_number is not UNSET:
            field_dict["weekDayNumber"] = week_day_number
        if day_of_week is not UNSET:
            field_dict["dayOfWeek"] = day_of_week
        if day is not UNSET:
            field_dict["day"] = day

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        monthly_mode = DiscoveryRuleMonthlyScheduleCalendarWithDaySettingsMonthlyMode(d.pop("monthlyMode"))

        months = []
        _months = d.pop("months")
        for months_item_data in _months:
            months_item = DiscoveryRuleMonthlyScheduleCalendarWithDaySettingsMonthsItem(months_item_data)

            months.append(months_item)

        _week_day_number = d.pop("weekDayNumber", UNSET)
        week_day_number: Union[Unset, DiscoveryRuleMonthlyScheduleCalendarWithDaySettingsWeekDayNumber]
        if isinstance(_week_day_number, Unset):
            week_day_number = UNSET
        else:
            week_day_number = DiscoveryRuleMonthlyScheduleCalendarWithDaySettingsWeekDayNumber(_week_day_number)

        _day_of_week = d.pop("dayOfWeek", UNSET)
        day_of_week: Union[Unset, DiscoveryRuleMonthlyScheduleCalendarWithDaySettingsDayOfWeek]
        if isinstance(_day_of_week, Unset):
            day_of_week = UNSET
        else:
            day_of_week = DiscoveryRuleMonthlyScheduleCalendarWithDaySettingsDayOfWeek(_day_of_week)

        day = d.pop("day", UNSET)

        discovery_rule_monthly_schedule_calendar_with_day_settings = cls(
            monthly_mode=monthly_mode,
            months=months,
            week_day_number=week_day_number,
            day_of_week=day_of_week,
            day=day,
        )

        discovery_rule_monthly_schedule_calendar_with_day_settings.additional_properties = d
        return discovery_rule_monthly_schedule_calendar_with_day_settings

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
