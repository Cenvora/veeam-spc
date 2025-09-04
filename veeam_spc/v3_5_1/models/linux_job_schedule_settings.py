from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.linux_job_schedule_settings_schedule_type import LinuxJobScheduleSettingsScheduleType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linux_active_full_settings import LinuxActiveFullSettings
    from ..models.linux_daily_schedule_settings import LinuxDailyScheduleSettings
    from ..models.linux_monthly_schedule_settings import LinuxMonthlyScheduleSettings
    from ..models.linux_periodically_schedule_settings import LinuxPeriodicallyScheduleSettings
    from ..models.linux_schedule_retry_settings import LinuxScheduleRetrySettings


T = TypeVar("T", bound="LinuxJobScheduleSettings")


@_attrs_define
class LinuxJobScheduleSettings:
    """
    Attributes:
        schedule_type (Union[Unset, LinuxJobScheduleSettingsScheduleType]): Type of periodicity. Default:
            LinuxJobScheduleSettingsScheduleType.DAILY.
        daily_schedule_settings (Union[Unset, LinuxDailyScheduleSettings]):
        monthly_schedule_settings (Union[Unset, LinuxMonthlyScheduleSettings]):
        periodically_schedule_settings (Union[Unset, LinuxPeriodicallyScheduleSettings]):
        active_full_settings (Union[Unset, LinuxActiveFullSettings]):
        retry_settings (Union[Unset, LinuxScheduleRetrySettings]):
    """

    schedule_type: Union[Unset, LinuxJobScheduleSettingsScheduleType] = LinuxJobScheduleSettingsScheduleType.DAILY
    daily_schedule_settings: Union[Unset, "LinuxDailyScheduleSettings"] = UNSET
    monthly_schedule_settings: Union[Unset, "LinuxMonthlyScheduleSettings"] = UNSET
    periodically_schedule_settings: Union[Unset, "LinuxPeriodicallyScheduleSettings"] = UNSET
    active_full_settings: Union[Unset, "LinuxActiveFullSettings"] = UNSET
    retry_settings: Union[Unset, "LinuxScheduleRetrySettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_type: Union[Unset, str] = UNSET
        if not isinstance(self.schedule_type, Unset):
            schedule_type = self.schedule_type.value

        daily_schedule_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.daily_schedule_settings, Unset):
            daily_schedule_settings = self.daily_schedule_settings.to_dict()

        monthly_schedule_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.monthly_schedule_settings, Unset):
            monthly_schedule_settings = self.monthly_schedule_settings.to_dict()

        periodically_schedule_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.periodically_schedule_settings, Unset):
            periodically_schedule_settings = self.periodically_schedule_settings.to_dict()

        active_full_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.active_full_settings, Unset):
            active_full_settings = self.active_full_settings.to_dict()

        retry_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.retry_settings, Unset):
            retry_settings = self.retry_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schedule_type is not UNSET:
            field_dict["scheduleType"] = schedule_type
        if daily_schedule_settings is not UNSET:
            field_dict["dailyScheduleSettings"] = daily_schedule_settings
        if monthly_schedule_settings is not UNSET:
            field_dict["monthlyScheduleSettings"] = monthly_schedule_settings
        if periodically_schedule_settings is not UNSET:
            field_dict["periodicallyScheduleSettings"] = periodically_schedule_settings
        if active_full_settings is not UNSET:
            field_dict["activeFullSettings"] = active_full_settings
        if retry_settings is not UNSET:
            field_dict["retrySettings"] = retry_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linux_active_full_settings import LinuxActiveFullSettings
        from ..models.linux_daily_schedule_settings import LinuxDailyScheduleSettings
        from ..models.linux_monthly_schedule_settings import LinuxMonthlyScheduleSettings
        from ..models.linux_periodically_schedule_settings import LinuxPeriodicallyScheduleSettings
        from ..models.linux_schedule_retry_settings import LinuxScheduleRetrySettings

        d = dict(src_dict)
        _schedule_type = d.pop("scheduleType", UNSET)
        schedule_type: Union[Unset, LinuxJobScheduleSettingsScheduleType]
        if isinstance(_schedule_type, Unset):
            schedule_type = UNSET
        else:
            schedule_type = LinuxJobScheduleSettingsScheduleType(_schedule_type)

        _daily_schedule_settings = d.pop("dailyScheduleSettings", UNSET)
        daily_schedule_settings: Union[Unset, LinuxDailyScheduleSettings]
        if isinstance(_daily_schedule_settings, Unset):
            daily_schedule_settings = UNSET
        else:
            daily_schedule_settings = LinuxDailyScheduleSettings.from_dict(_daily_schedule_settings)

        _monthly_schedule_settings = d.pop("monthlyScheduleSettings", UNSET)
        monthly_schedule_settings: Union[Unset, LinuxMonthlyScheduleSettings]
        if isinstance(_monthly_schedule_settings, Unset):
            monthly_schedule_settings = UNSET
        else:
            monthly_schedule_settings = LinuxMonthlyScheduleSettings.from_dict(_monthly_schedule_settings)

        _periodically_schedule_settings = d.pop("periodicallyScheduleSettings", UNSET)
        periodically_schedule_settings: Union[Unset, LinuxPeriodicallyScheduleSettings]
        if isinstance(_periodically_schedule_settings, Unset):
            periodically_schedule_settings = UNSET
        else:
            periodically_schedule_settings = LinuxPeriodicallyScheduleSettings.from_dict(
                _periodically_schedule_settings
            )

        _active_full_settings = d.pop("activeFullSettings", UNSET)
        active_full_settings: Union[Unset, LinuxActiveFullSettings]
        if isinstance(_active_full_settings, Unset):
            active_full_settings = UNSET
        else:
            active_full_settings = LinuxActiveFullSettings.from_dict(_active_full_settings)

        _retry_settings = d.pop("retrySettings", UNSET)
        retry_settings: Union[Unset, LinuxScheduleRetrySettings]
        if isinstance(_retry_settings, Unset):
            retry_settings = UNSET
        else:
            retry_settings = LinuxScheduleRetrySettings.from_dict(_retry_settings)

        linux_job_schedule_settings = cls(
            schedule_type=schedule_type,
            daily_schedule_settings=daily_schedule_settings,
            monthly_schedule_settings=monthly_schedule_settings,
            periodically_schedule_settings=periodically_schedule_settings,
            active_full_settings=active_full_settings,
            retry_settings=retry_settings,
        )

        linux_job_schedule_settings.additional_properties = d
        return linux_job_schedule_settings

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
