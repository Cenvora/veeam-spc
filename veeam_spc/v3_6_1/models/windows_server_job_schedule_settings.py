from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.windows_server_job_schedule_settings_schedule_type import WindowsServerJobScheduleSettingsScheduleType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_schedule_window_day import JobScheduleWindowDay
    from ..models.windows_continuous_schedule_settings import WindowsContinuousScheduleSettings
    from ..models.windows_daily_schedule_settings import WindowsDailyScheduleSettings
    from ..models.windows_monthly_schedule_settings import WindowsMonthlyScheduleSettings
    from ..models.windows_periodical_schedule_settings import WindowsPeriodicalScheduleSettings
    from ..models.windows_server_job_retry_settings import WindowsServerJobRetrySettings


T = TypeVar("T", bound="WindowsServerJobScheduleSettings")


@_attrs_define
class WindowsServerJobScheduleSettings:
    """
    Attributes:
        schedule_type (Union[Unset, WindowsServerJobScheduleSettingsScheduleType]): Type of periodicity. Default:
            WindowsServerJobScheduleSettingsScheduleType.DAILY.
        daily_schedule_settings (Union[Unset, WindowsDailyScheduleSettings]):
        monthly_schedule_settings (Union[Unset, WindowsMonthlyScheduleSettings]):
        periodical_schedule_settings (Union[Unset, WindowsPeriodicalScheduleSettings]):
        continuous_schedule_settings (Union[Unset, WindowsContinuousScheduleSettings]):
        retry_settings (Union[Unset, WindowsServerJobRetrySettings]):
        backup_window (Union[None, Unset, list['JobScheduleWindowDay']]): Time interval within which a job must
            complete.
            > The `null` value indicates that a job can be run at any time.
    """

    schedule_type: Union[Unset, WindowsServerJobScheduleSettingsScheduleType] = (
        WindowsServerJobScheduleSettingsScheduleType.DAILY
    )
    daily_schedule_settings: Union[Unset, "WindowsDailyScheduleSettings"] = UNSET
    monthly_schedule_settings: Union[Unset, "WindowsMonthlyScheduleSettings"] = UNSET
    periodical_schedule_settings: Union[Unset, "WindowsPeriodicalScheduleSettings"] = UNSET
    continuous_schedule_settings: Union[Unset, "WindowsContinuousScheduleSettings"] = UNSET
    retry_settings: Union[Unset, "WindowsServerJobRetrySettings"] = UNSET
    backup_window: Union[None, Unset, list["JobScheduleWindowDay"]] = UNSET
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

        periodical_schedule_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.periodical_schedule_settings, Unset):
            periodical_schedule_settings = self.periodical_schedule_settings.to_dict()

        continuous_schedule_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.continuous_schedule_settings, Unset):
            continuous_schedule_settings = self.continuous_schedule_settings.to_dict()

        retry_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.retry_settings, Unset):
            retry_settings = self.retry_settings.to_dict()

        backup_window: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.backup_window, Unset):
            backup_window = UNSET
        elif isinstance(self.backup_window, list):
            backup_window = []
            for backup_window_type_0_item_data in self.backup_window:
                backup_window_type_0_item = backup_window_type_0_item_data.to_dict()
                backup_window.append(backup_window_type_0_item)

        else:
            backup_window = self.backup_window

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schedule_type is not UNSET:
            field_dict["scheduleType"] = schedule_type
        if daily_schedule_settings is not UNSET:
            field_dict["dailyScheduleSettings"] = daily_schedule_settings
        if monthly_schedule_settings is not UNSET:
            field_dict["monthlyScheduleSettings"] = monthly_schedule_settings
        if periodical_schedule_settings is not UNSET:
            field_dict["periodicalScheduleSettings"] = periodical_schedule_settings
        if continuous_schedule_settings is not UNSET:
            field_dict["continuousScheduleSettings"] = continuous_schedule_settings
        if retry_settings is not UNSET:
            field_dict["retrySettings"] = retry_settings
        if backup_window is not UNSET:
            field_dict["backupWindow"] = backup_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_schedule_window_day import JobScheduleWindowDay
        from ..models.windows_continuous_schedule_settings import WindowsContinuousScheduleSettings
        from ..models.windows_daily_schedule_settings import WindowsDailyScheduleSettings
        from ..models.windows_monthly_schedule_settings import WindowsMonthlyScheduleSettings
        from ..models.windows_periodical_schedule_settings import WindowsPeriodicalScheduleSettings
        from ..models.windows_server_job_retry_settings import WindowsServerJobRetrySettings

        d = dict(src_dict)
        _schedule_type = d.pop("scheduleType", UNSET)
        schedule_type: Union[Unset, WindowsServerJobScheduleSettingsScheduleType]
        if isinstance(_schedule_type, Unset):
            schedule_type = UNSET
        else:
            schedule_type = WindowsServerJobScheduleSettingsScheduleType(_schedule_type)

        _daily_schedule_settings = d.pop("dailyScheduleSettings", UNSET)
        daily_schedule_settings: Union[Unset, WindowsDailyScheduleSettings]
        if isinstance(_daily_schedule_settings, Unset):
            daily_schedule_settings = UNSET
        else:
            daily_schedule_settings = WindowsDailyScheduleSettings.from_dict(_daily_schedule_settings)

        _monthly_schedule_settings = d.pop("monthlyScheduleSettings", UNSET)
        monthly_schedule_settings: Union[Unset, WindowsMonthlyScheduleSettings]
        if isinstance(_monthly_schedule_settings, Unset):
            monthly_schedule_settings = UNSET
        else:
            monthly_schedule_settings = WindowsMonthlyScheduleSettings.from_dict(_monthly_schedule_settings)

        _periodical_schedule_settings = d.pop("periodicalScheduleSettings", UNSET)
        periodical_schedule_settings: Union[Unset, WindowsPeriodicalScheduleSettings]
        if isinstance(_periodical_schedule_settings, Unset):
            periodical_schedule_settings = UNSET
        else:
            periodical_schedule_settings = WindowsPeriodicalScheduleSettings.from_dict(_periodical_schedule_settings)

        _continuous_schedule_settings = d.pop("continuousScheduleSettings", UNSET)
        continuous_schedule_settings: Union[Unset, WindowsContinuousScheduleSettings]
        if isinstance(_continuous_schedule_settings, Unset):
            continuous_schedule_settings = UNSET
        else:
            continuous_schedule_settings = WindowsContinuousScheduleSettings.from_dict(_continuous_schedule_settings)

        _retry_settings = d.pop("retrySettings", UNSET)
        retry_settings: Union[Unset, WindowsServerJobRetrySettings]
        if isinstance(_retry_settings, Unset):
            retry_settings = UNSET
        else:
            retry_settings = WindowsServerJobRetrySettings.from_dict(_retry_settings)

        def _parse_backup_window(data: object) -> Union[None, Unset, list["JobScheduleWindowDay"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                backup_window_type_0 = []
                _backup_window_type_0 = data
                for backup_window_type_0_item_data in _backup_window_type_0:
                    backup_window_type_0_item = JobScheduleWindowDay.from_dict(backup_window_type_0_item_data)

                    backup_window_type_0.append(backup_window_type_0_item)

                return backup_window_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["JobScheduleWindowDay"]], data)

        backup_window = _parse_backup_window(d.pop("backupWindow", UNSET))

        windows_server_job_schedule_settings = cls(
            schedule_type=schedule_type,
            daily_schedule_settings=daily_schedule_settings,
            monthly_schedule_settings=monthly_schedule_settings,
            periodical_schedule_settings=periodical_schedule_settings,
            continuous_schedule_settings=continuous_schedule_settings,
            retry_settings=retry_settings,
            backup_window=backup_window,
        )

        windows_server_job_schedule_settings.additional_properties = d
        return windows_server_job_schedule_settings

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
