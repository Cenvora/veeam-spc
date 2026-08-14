from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.linux_synthetic_full_settings_schedule_type import LinuxSyntheticFullSettingsScheduleType
from ..models.linux_synthetic_full_settings_weekly_on_days_item import LinuxSyntheticFullSettingsWeeklyOnDaysItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linux_monthly_schedule_settings import LinuxMonthlyScheduleSettings


T = TypeVar("T", bound="LinuxSyntheticFullSettings")


@_attrs_define
class LinuxSyntheticFullSettings:
    """
    Attributes:
        schedule_type (LinuxSyntheticFullSettingsScheduleType | Unset): Type of periodicity. Default:
            LinuxSyntheticFullSettingsScheduleType.NOTSCHEDULED.
        monthly (LinuxMonthlyScheduleSettings | Unset):
        weekly_on_days (list[LinuxSyntheticFullSettingsWeeklyOnDaysItem] | Unset): Name of the week day.
    """

    schedule_type: LinuxSyntheticFullSettingsScheduleType | Unset = LinuxSyntheticFullSettingsScheduleType.NOTSCHEDULED
    monthly: LinuxMonthlyScheduleSettings | Unset = UNSET
    weekly_on_days: list[LinuxSyntheticFullSettingsWeeklyOnDaysItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_type: str | Unset = UNSET
        if not isinstance(self.schedule_type, Unset):
            schedule_type = self.schedule_type.value

        monthly: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monthly, Unset):
            monthly = self.monthly.to_dict()

        weekly_on_days: list[str] | Unset = UNSET
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
        if monthly is not UNSET:
            field_dict["monthly"] = monthly
        if weekly_on_days is not UNSET:
            field_dict["weeklyOnDays"] = weekly_on_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linux_monthly_schedule_settings import LinuxMonthlyScheduleSettings

        d = dict(src_dict)
        _schedule_type = d.pop("scheduleType", UNSET)
        schedule_type: LinuxSyntheticFullSettingsScheduleType | Unset
        if isinstance(_schedule_type, Unset):
            schedule_type = UNSET
        else:
            schedule_type = LinuxSyntheticFullSettingsScheduleType(_schedule_type)

        _monthly = d.pop("monthly", UNSET)
        monthly: LinuxMonthlyScheduleSettings | Unset
        if isinstance(_monthly, Unset):
            monthly = UNSET
        else:
            monthly = LinuxMonthlyScheduleSettings.from_dict(_monthly)

        _weekly_on_days = d.pop("weeklyOnDays", UNSET)
        weekly_on_days: list[LinuxSyntheticFullSettingsWeeklyOnDaysItem] | Unset = UNSET
        if _weekly_on_days is not UNSET:
            weekly_on_days = []
            for weekly_on_days_item_data in _weekly_on_days:
                weekly_on_days_item = LinuxSyntheticFullSettingsWeeklyOnDaysItem(weekly_on_days_item_data)

                weekly_on_days.append(weekly_on_days_item)

        linux_synthetic_full_settings = cls(
            schedule_type=schedule_type,
            monthly=monthly,
            weekly_on_days=weekly_on_days,
        )

        linux_synthetic_full_settings.additional_properties = d
        return linux_synthetic_full_settings

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
