from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.windows_advanced_schedule_settings_synthetic_full_on_days_type_0_item import (
    WindowsAdvancedScheduleSettingsSyntheticFullOnDaysType0Item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monthly_or_weekly_schedule_with_day_settings import MonthlyOrWeeklyScheduleWithDaySettings


T = TypeVar("T", bound="WindowsAdvancedScheduleSettings")


@_attrs_define
class WindowsAdvancedScheduleSettings:
    """
    Attributes:
        synthetic_full_on_days (Union[None, Unset, list[WindowsAdvancedScheduleSettingsSyntheticFullOnDaysType0Item]]):
            Week days on which creation of synthetic full backups is scheduled
            > The `null` value indicates that periodic creation of synthetic full backups is disabled.
        active_full_settings (Union[Unset, MonthlyOrWeeklyScheduleWithDaySettings]):
    """

    synthetic_full_on_days: Union[None, Unset, list[WindowsAdvancedScheduleSettingsSyntheticFullOnDaysType0Item]] = (
        UNSET
    )
    active_full_settings: Union[Unset, "MonthlyOrWeeklyScheduleWithDaySettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        synthetic_full_on_days: Union[None, Unset, list[str]]
        if isinstance(self.synthetic_full_on_days, Unset):
            synthetic_full_on_days = UNSET
        elif isinstance(self.synthetic_full_on_days, list):
            synthetic_full_on_days = []
            for synthetic_full_on_days_type_0_item_data in self.synthetic_full_on_days:
                synthetic_full_on_days_type_0_item = synthetic_full_on_days_type_0_item_data.value
                synthetic_full_on_days.append(synthetic_full_on_days_type_0_item)

        else:
            synthetic_full_on_days = self.synthetic_full_on_days

        active_full_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.active_full_settings, Unset):
            active_full_settings = self.active_full_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if synthetic_full_on_days is not UNSET:
            field_dict["syntheticFullOnDays"] = synthetic_full_on_days
        if active_full_settings is not UNSET:
            field_dict["activeFullSettings"] = active_full_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monthly_or_weekly_schedule_with_day_settings import MonthlyOrWeeklyScheduleWithDaySettings

        d = dict(src_dict)

        def _parse_synthetic_full_on_days(
            data: object,
        ) -> Union[None, Unset, list[WindowsAdvancedScheduleSettingsSyntheticFullOnDaysType0Item]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                synthetic_full_on_days_type_0 = []
                _synthetic_full_on_days_type_0 = data
                for synthetic_full_on_days_type_0_item_data in _synthetic_full_on_days_type_0:
                    synthetic_full_on_days_type_0_item = WindowsAdvancedScheduleSettingsSyntheticFullOnDaysType0Item(
                        synthetic_full_on_days_type_0_item_data
                    )

                    synthetic_full_on_days_type_0.append(synthetic_full_on_days_type_0_item)

                return synthetic_full_on_days_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[WindowsAdvancedScheduleSettingsSyntheticFullOnDaysType0Item]], data)

        synthetic_full_on_days = _parse_synthetic_full_on_days(d.pop("syntheticFullOnDays", UNSET))

        _active_full_settings = d.pop("activeFullSettings", UNSET)
        active_full_settings: Union[Unset, MonthlyOrWeeklyScheduleWithDaySettings]
        if isinstance(_active_full_settings, Unset):
            active_full_settings = UNSET
        else:
            active_full_settings = MonthlyOrWeeklyScheduleWithDaySettings.from_dict(_active_full_settings)

        windows_advanced_schedule_settings = cls(
            synthetic_full_on_days=synthetic_full_on_days,
            active_full_settings=active_full_settings,
        )

        windows_advanced_schedule_settings.additional_properties = d
        return windows_advanced_schedule_settings

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
