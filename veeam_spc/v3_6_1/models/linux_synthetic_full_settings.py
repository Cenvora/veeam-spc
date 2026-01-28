from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.linux_synthetic_full_settings_schedule_type import LinuxSyntheticFullSettingsScheduleType
from ..models.linux_synthetic_full_settings_weekly_on_days_type_0_item import (
    LinuxSyntheticFullSettingsWeeklyOnDaysType0Item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linux_monthly_schedule_settings import LinuxMonthlyScheduleSettings


T = TypeVar("T", bound="LinuxSyntheticFullSettings")


@_attrs_define
class LinuxSyntheticFullSettings:
    """
    Attributes:
        schedule_type (Union[Unset, LinuxSyntheticFullSettingsScheduleType]): Type of periodicity. Default:
            LinuxSyntheticFullSettingsScheduleType.NOTSCHEDULED.
        monthly (Union[Unset, LinuxMonthlyScheduleSettings]):
        weekly_on_days (Union[None, Unset, list[LinuxSyntheticFullSettingsWeeklyOnDaysType0Item]]): Name of the week
            day.
    """

    schedule_type: Union[Unset, LinuxSyntheticFullSettingsScheduleType] = (
        LinuxSyntheticFullSettingsScheduleType.NOTSCHEDULED
    )
    monthly: Union[Unset, "LinuxMonthlyScheduleSettings"] = UNSET
    weekly_on_days: Union[None, Unset, list[LinuxSyntheticFullSettingsWeeklyOnDaysType0Item]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_type: Union[Unset, str] = UNSET
        if not isinstance(self.schedule_type, Unset):
            schedule_type = self.schedule_type.value

        monthly: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.monthly, Unset):
            monthly = self.monthly.to_dict()

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
        schedule_type: Union[Unset, LinuxSyntheticFullSettingsScheduleType]
        if isinstance(_schedule_type, Unset):
            schedule_type = UNSET
        else:
            schedule_type = LinuxSyntheticFullSettingsScheduleType(_schedule_type)

        _monthly = d.pop("monthly", UNSET)
        monthly: Union[Unset, LinuxMonthlyScheduleSettings]
        if isinstance(_monthly, Unset):
            monthly = UNSET
        else:
            monthly = LinuxMonthlyScheduleSettings.from_dict(_monthly)

        def _parse_weekly_on_days(
            data: object,
        ) -> Union[None, Unset, list[LinuxSyntheticFullSettingsWeeklyOnDaysType0Item]]:
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
                    weekly_on_days_type_0_item = LinuxSyntheticFullSettingsWeeklyOnDaysType0Item(
                        weekly_on_days_type_0_item_data
                    )

                    weekly_on_days_type_0.append(weekly_on_days_type_0_item)

                return weekly_on_days_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[LinuxSyntheticFullSettingsWeeklyOnDaysType0Item]], data)

        weekly_on_days = _parse_weekly_on_days(d.pop("weeklyOnDays", UNSET))

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
