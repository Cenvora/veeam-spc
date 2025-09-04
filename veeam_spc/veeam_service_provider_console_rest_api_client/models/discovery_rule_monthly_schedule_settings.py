from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.discovery_rule_monthly_schedule_calendar_with_day_settings import (
        DiscoveryRuleMonthlyScheduleCalendarWithDaySettings,
    )


T = TypeVar("T", bound="DiscoveryRuleMonthlyScheduleSettings")


@_attrs_define
class DiscoveryRuleMonthlyScheduleSettings:
    """
    Attributes:
        time (str): Time of the day when discovery must run in the `hh:mm` format.
        calendar_settings (DiscoveryRuleMonthlyScheduleCalendarWithDaySettings):
    """

    time: str
    calendar_settings: "DiscoveryRuleMonthlyScheduleCalendarWithDaySettings"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        calendar_settings = self.calendar_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time": time,
                "calendarSettings": calendar_settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.discovery_rule_monthly_schedule_calendar_with_day_settings import (
            DiscoveryRuleMonthlyScheduleCalendarWithDaySettings,
        )

        d = dict(src_dict)
        time = d.pop("time")

        calendar_settings = DiscoveryRuleMonthlyScheduleCalendarWithDaySettings.from_dict(d.pop("calendarSettings"))

        discovery_rule_monthly_schedule_settings = cls(
            time=time,
            calendar_settings=calendar_settings,
        )

        discovery_rule_monthly_schedule_settings.additional_properties = d
        return discovery_rule_monthly_schedule_settings

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
