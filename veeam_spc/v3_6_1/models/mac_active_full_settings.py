from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mac_active_full_settings_schedule_type import MacActiveFullSettingsScheduleType
from ..models.mac_active_full_settings_weekly_on_days_type_0_item import MacActiveFullSettingsWeeklyOnDaysType0Item
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mac_monthly_schedule_settings import MacMonthlyScheduleSettings


T = TypeVar("T", bound="MacActiveFullSettings")


@_attrs_define
class MacActiveFullSettings:
    """
    Attributes:
        schedule_type (Union[Unset, MacActiveFullSettingsScheduleType]): Type of periodicity. Default:
            MacActiveFullSettingsScheduleType.NOTSCHEDULED.
        monthly (Union[Unset, MacMonthlyScheduleSettings]):
        weekly_on_days (Union[None, Unset, list[MacActiveFullSettingsWeeklyOnDaysType0Item]]): Array of the week days on
            which active full backups must be created.
    """

    schedule_type: Union[Unset, MacActiveFullSettingsScheduleType] = MacActiveFullSettingsScheduleType.NOTSCHEDULED
    monthly: Union[Unset, "MacMonthlyScheduleSettings"] = UNSET
    weekly_on_days: Union[None, Unset, list[MacActiveFullSettingsWeeklyOnDaysType0Item]] = UNSET
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
        from ..models.mac_monthly_schedule_settings import MacMonthlyScheduleSettings

        d = dict(src_dict)
        _schedule_type = d.pop("scheduleType", UNSET)
        schedule_type: Union[Unset, MacActiveFullSettingsScheduleType]
        if isinstance(_schedule_type, Unset):
            schedule_type = UNSET
        else:
            schedule_type = MacActiveFullSettingsScheduleType(_schedule_type)

        _monthly = d.pop("monthly", UNSET)
        monthly: Union[Unset, MacMonthlyScheduleSettings]
        if isinstance(_monthly, Unset):
            monthly = UNSET
        else:
            monthly = MacMonthlyScheduleSettings.from_dict(_monthly)

        def _parse_weekly_on_days(data: object) -> Union[None, Unset, list[MacActiveFullSettingsWeeklyOnDaysType0Item]]:
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
                    weekly_on_days_type_0_item = MacActiveFullSettingsWeeklyOnDaysType0Item(
                        weekly_on_days_type_0_item_data
                    )

                    weekly_on_days_type_0.append(weekly_on_days_type_0_item)

                return weekly_on_days_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[MacActiveFullSettingsWeeklyOnDaysType0Item]], data)

        weekly_on_days = _parse_weekly_on_days(d.pop("weeklyOnDays", UNSET))

        mac_active_full_settings = cls(
            schedule_type=schedule_type,
            monthly=monthly,
            weekly_on_days=weekly_on_days,
        )

        mac_active_full_settings.additional_properties = d
        return mac_active_full_settings

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
