from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.windows_monthly_schedule_calendar_with_day_settings import (
        WindowsMonthlyScheduleCalendarWithDaySettings,
    )


T = TypeVar("T", bound="WindowsMonthlyScheduleSettings")


@_attrs_define
class WindowsMonthlyScheduleSettings:
    """
    Attributes:
        calendar_settings (WindowsMonthlyScheduleCalendarWithDaySettings):
        time (Union[Unset, str]): Timestamp of a job start. Default: '10:00'.
    """

    calendar_settings: "WindowsMonthlyScheduleCalendarWithDaySettings"
    time: Union[Unset, str] = "10:00"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        calendar_settings = self.calendar_settings.to_dict()

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "calendarSettings": calendar_settings,
            }
        )
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.windows_monthly_schedule_calendar_with_day_settings import (
            WindowsMonthlyScheduleCalendarWithDaySettings,
        )

        d = dict(src_dict)
        calendar_settings = WindowsMonthlyScheduleCalendarWithDaySettings.from_dict(d.pop("calendarSettings"))

        time = d.pop("time", UNSET)

        windows_monthly_schedule_settings = cls(
            calendar_settings=calendar_settings,
            time=time,
        )

        windows_monthly_schedule_settings.additional_properties = d
        return windows_monthly_schedule_settings

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
