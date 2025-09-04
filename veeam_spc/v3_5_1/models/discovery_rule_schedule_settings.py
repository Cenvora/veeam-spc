from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.discovery_rule_schedule_settings_schedule_type import DiscoveryRuleScheduleSettingsScheduleType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.discovery_rule_daily_schedule_settings import DiscoveryRuleDailyScheduleSettings
    from ..models.discovery_rule_monthly_schedule_settings import DiscoveryRuleMonthlyScheduleSettings
    from ..models.discovery_rule_periodical_schedule_settings import DiscoveryRulePeriodicalScheduleSettings
    from ..models.time_zone import TimeZone


T = TypeVar("T", bound="DiscoveryRuleScheduleSettings")


@_attrs_define
class DiscoveryRuleScheduleSettings:
    """
    Attributes:
        schedule_type (DiscoveryRuleScheduleSettingsScheduleType): Schedule type Default:
            DiscoveryRuleScheduleSettingsScheduleType.NOTSCHEDULED.
        time_zone (Union[Unset, TimeZone]):
        daily_schedule_settings (Union[Unset, DiscoveryRuleDailyScheduleSettings]):
        monthly_schedule_settings (Union[Unset, DiscoveryRuleMonthlyScheduleSettings]):
        periodical_schedule_settings (Union[Unset, DiscoveryRulePeriodicalScheduleSettings]):
    """

    schedule_type: DiscoveryRuleScheduleSettingsScheduleType = DiscoveryRuleScheduleSettingsScheduleType.NOTSCHEDULED
    time_zone: Union[Unset, "TimeZone"] = UNSET
    daily_schedule_settings: Union[Unset, "DiscoveryRuleDailyScheduleSettings"] = UNSET
    monthly_schedule_settings: Union[Unset, "DiscoveryRuleMonthlyScheduleSettings"] = UNSET
    periodical_schedule_settings: Union[Unset, "DiscoveryRulePeriodicalScheduleSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_type = self.schedule_type.value

        time_zone: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_zone, Unset):
            time_zone = self.time_zone.to_dict()

        daily_schedule_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.daily_schedule_settings, Unset):
            daily_schedule_settings = self.daily_schedule_settings.to_dict()

        monthly_schedule_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.monthly_schedule_settings, Unset):
            monthly_schedule_settings = self.monthly_schedule_settings.to_dict()

        periodical_schedule_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.periodical_schedule_settings, Unset):
            periodical_schedule_settings = self.periodical_schedule_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scheduleType": schedule_type,
            }
        )
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if daily_schedule_settings is not UNSET:
            field_dict["dailyScheduleSettings"] = daily_schedule_settings
        if monthly_schedule_settings is not UNSET:
            field_dict["monthlyScheduleSettings"] = monthly_schedule_settings
        if periodical_schedule_settings is not UNSET:
            field_dict["periodicalScheduleSettings"] = periodical_schedule_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.discovery_rule_daily_schedule_settings import DiscoveryRuleDailyScheduleSettings
        from ..models.discovery_rule_monthly_schedule_settings import DiscoveryRuleMonthlyScheduleSettings
        from ..models.discovery_rule_periodical_schedule_settings import DiscoveryRulePeriodicalScheduleSettings
        from ..models.time_zone import TimeZone

        d = dict(src_dict)
        schedule_type = DiscoveryRuleScheduleSettingsScheduleType(d.pop("scheduleType"))

        _time_zone = d.pop("timeZone", UNSET)
        time_zone: Union[Unset, TimeZone]
        if isinstance(_time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = TimeZone.from_dict(_time_zone)

        _daily_schedule_settings = d.pop("dailyScheduleSettings", UNSET)
        daily_schedule_settings: Union[Unset, DiscoveryRuleDailyScheduleSettings]
        if isinstance(_daily_schedule_settings, Unset):
            daily_schedule_settings = UNSET
        else:
            daily_schedule_settings = DiscoveryRuleDailyScheduleSettings.from_dict(_daily_schedule_settings)

        _monthly_schedule_settings = d.pop("monthlyScheduleSettings", UNSET)
        monthly_schedule_settings: Union[Unset, DiscoveryRuleMonthlyScheduleSettings]
        if isinstance(_monthly_schedule_settings, Unset):
            monthly_schedule_settings = UNSET
        else:
            monthly_schedule_settings = DiscoveryRuleMonthlyScheduleSettings.from_dict(_monthly_schedule_settings)

        _periodical_schedule_settings = d.pop("periodicalScheduleSettings", UNSET)
        periodical_schedule_settings: Union[Unset, DiscoveryRulePeriodicalScheduleSettings]
        if isinstance(_periodical_schedule_settings, Unset):
            periodical_schedule_settings = UNSET
        else:
            periodical_schedule_settings = DiscoveryRulePeriodicalScheduleSettings.from_dict(
                _periodical_schedule_settings
            )

        discovery_rule_schedule_settings = cls(
            schedule_type=schedule_type,
            time_zone=time_zone,
            daily_schedule_settings=daily_schedule_settings,
            monthly_schedule_settings=monthly_schedule_settings,
            periodical_schedule_settings=periodical_schedule_settings,
        )

        discovery_rule_schedule_settings.additional_properties = d
        return discovery_rule_schedule_settings

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
