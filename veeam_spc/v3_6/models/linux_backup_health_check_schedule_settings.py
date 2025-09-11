from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.linux_backup_health_check_schedule_settings_weekly_on_days_item import (
    LinuxBackupHealthCheckScheduleSettingsWeeklyOnDaysItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linux_backup_health_check_monthly_schedule import LinuxBackupHealthCheckMonthlySchedule


T = TypeVar("T", bound="LinuxBackupHealthCheckScheduleSettings")


@_attrs_define
class LinuxBackupHealthCheckScheduleSettings:
    """
    Attributes:
        monthly_settings (Union[Unset, LinuxBackupHealthCheckMonthlySchedule]):
        weekly_on_days (Union[Unset, list[LinuxBackupHealthCheckScheduleSettingsWeeklyOnDaysItem]]): Scheduling settings
            for weekly full backup creation.
            > If the `monthlySettings` property is also provided, it is ignored.
    """

    monthly_settings: Union[Unset, "LinuxBackupHealthCheckMonthlySchedule"] = UNSET
    weekly_on_days: Union[Unset, list[LinuxBackupHealthCheckScheduleSettingsWeeklyOnDaysItem]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monthly_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.monthly_settings, Unset):
            monthly_settings = self.monthly_settings.to_dict()

        weekly_on_days: Union[Unset, list[str]] = UNSET
        if not isinstance(self.weekly_on_days, Unset):
            weekly_on_days = []
            for weekly_on_days_item_data in self.weekly_on_days:
                weekly_on_days_item = weekly_on_days_item_data.value
                weekly_on_days.append(weekly_on_days_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if monthly_settings is not UNSET:
            field_dict["monthlySettings"] = monthly_settings
        if weekly_on_days is not UNSET:
            field_dict["weeklyOnDays"] = weekly_on_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linux_backup_health_check_monthly_schedule import LinuxBackupHealthCheckMonthlySchedule

        d = dict(src_dict)
        _monthly_settings = d.pop("monthlySettings", UNSET)
        monthly_settings: Union[Unset, LinuxBackupHealthCheckMonthlySchedule]
        if isinstance(_monthly_settings, Unset):
            monthly_settings = UNSET
        else:
            monthly_settings = LinuxBackupHealthCheckMonthlySchedule.from_dict(_monthly_settings)

        weekly_on_days = []
        _weekly_on_days = d.pop("weeklyOnDays", UNSET)
        for weekly_on_days_item_data in _weekly_on_days or []:
            weekly_on_days_item = LinuxBackupHealthCheckScheduleSettingsWeeklyOnDaysItem(weekly_on_days_item_data)

            weekly_on_days.append(weekly_on_days_item)

        linux_backup_health_check_schedule_settings = cls(
            monthly_settings=monthly_settings,
            weekly_on_days=weekly_on_days,
        )

        linux_backup_health_check_schedule_settings.additional_properties = d
        return linux_backup_health_check_schedule_settings

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
