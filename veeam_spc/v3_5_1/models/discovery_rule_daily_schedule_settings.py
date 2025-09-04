from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.discovery_rule_daily_schedule_settings_specific_days_item import (
    DiscoveryRuleDailyScheduleSettingsSpecificDaysItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DiscoveryRuleDailyScheduleSettings")


@_attrs_define
class DiscoveryRuleDailyScheduleSettings:
    """
    Attributes:
        time (Union[Unset, str]): Time of the day when discovery must run in the `hh:mm` format. Default: '0:30'.
        specific_days (Union[Unset, list[DiscoveryRuleDailyScheduleSettingsSpecificDaysItem]]): Week days on which
            discovery must be performed.
            > Required for the `SpecificDay` schedule type.
    """

    time: Union[Unset, str] = "0:30"
    specific_days: Union[Unset, list[DiscoveryRuleDailyScheduleSettingsSpecificDaysItem]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

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
        if specific_days is not UNSET:
            field_dict["specificDays"] = specific_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        specific_days = []
        _specific_days = d.pop("specificDays", UNSET)
        for specific_days_item_data in _specific_days or []:
            specific_days_item = DiscoveryRuleDailyScheduleSettingsSpecificDaysItem(specific_days_item_data)

            specific_days.append(specific_days_item)

        discovery_rule_daily_schedule_settings = cls(
            time=time,
            specific_days=specific_days,
        )

        discovery_rule_daily_schedule_settings.additional_properties = d
        return discovery_rule_daily_schedule_settings

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
