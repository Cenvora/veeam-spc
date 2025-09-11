from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mac_job_schedule_settings_schedule_type import MacJobScheduleSettingsScheduleType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mac_active_full_settings import MacActiveFullSettings
    from ..models.mac_backup_health_check_schedule_settings import MacBackupHealthCheckScheduleSettings
    from ..models.mac_daily_schedule_settings import MacDailyScheduleSettings
    from ..models.mac_monthly_schedule_settings import MacMonthlyScheduleSettings
    from ..models.mac_periodically_schedule_settings import MacPeriodicallyScheduleSettings
    from ..models.mac_schedule_retry_settings import MacScheduleRetrySettings


T = TypeVar("T", bound="MacJobScheduleSettings")


@_attrs_define
class MacJobScheduleSettings:
    """
    Attributes:
        schedule_type (Union[Unset, MacJobScheduleSettingsScheduleType]): Type of job periodicity. Default:
            MacJobScheduleSettingsScheduleType.NOTSCHEDULED.
        daily_schedule_settings (Union[Unset, MacDailyScheduleSettings]):
        monthly_schedule_settings (Union[Unset, MacMonthlyScheduleSettings]):
        periodically_schedule_settings (Union[Unset, MacPeriodicallyScheduleSettings]):
        active_full_settings (Union[Unset, MacActiveFullSettings]):
        retry_settings (Union[Unset, MacScheduleRetrySettings]):
        backup_health_check_schedule_settings (Union[Unset, MacBackupHealthCheckScheduleSettings]):
    """

    schedule_type: Union[Unset, MacJobScheduleSettingsScheduleType] = MacJobScheduleSettingsScheduleType.NOTSCHEDULED
    daily_schedule_settings: Union[Unset, "MacDailyScheduleSettings"] = UNSET
    monthly_schedule_settings: Union[Unset, "MacMonthlyScheduleSettings"] = UNSET
    periodically_schedule_settings: Union[Unset, "MacPeriodicallyScheduleSettings"] = UNSET
    active_full_settings: Union[Unset, "MacActiveFullSettings"] = UNSET
    retry_settings: Union[Unset, "MacScheduleRetrySettings"] = UNSET
    backup_health_check_schedule_settings: Union[Unset, "MacBackupHealthCheckScheduleSettings"] = UNSET
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

        backup_health_check_schedule_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.backup_health_check_schedule_settings, Unset):
            backup_health_check_schedule_settings = self.backup_health_check_schedule_settings.to_dict()

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
        if backup_health_check_schedule_settings is not UNSET:
            field_dict["backupHealthCheckScheduleSettings"] = backup_health_check_schedule_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mac_active_full_settings import MacActiveFullSettings
        from ..models.mac_backup_health_check_schedule_settings import MacBackupHealthCheckScheduleSettings
        from ..models.mac_daily_schedule_settings import MacDailyScheduleSettings
        from ..models.mac_monthly_schedule_settings import MacMonthlyScheduleSettings
        from ..models.mac_periodically_schedule_settings import MacPeriodicallyScheduleSettings
        from ..models.mac_schedule_retry_settings import MacScheduleRetrySettings

        d = dict(src_dict)
        _schedule_type = d.pop("scheduleType", UNSET)
        schedule_type: Union[Unset, MacJobScheduleSettingsScheduleType]
        if isinstance(_schedule_type, Unset):
            schedule_type = UNSET
        else:
            schedule_type = MacJobScheduleSettingsScheduleType(_schedule_type)

        _daily_schedule_settings = d.pop("dailyScheduleSettings", UNSET)
        daily_schedule_settings: Union[Unset, MacDailyScheduleSettings]
        if isinstance(_daily_schedule_settings, Unset):
            daily_schedule_settings = UNSET
        else:
            daily_schedule_settings = MacDailyScheduleSettings.from_dict(_daily_schedule_settings)

        _monthly_schedule_settings = d.pop("monthlyScheduleSettings", UNSET)
        monthly_schedule_settings: Union[Unset, MacMonthlyScheduleSettings]
        if isinstance(_monthly_schedule_settings, Unset):
            monthly_schedule_settings = UNSET
        else:
            monthly_schedule_settings = MacMonthlyScheduleSettings.from_dict(_monthly_schedule_settings)

        _periodically_schedule_settings = d.pop("periodicallyScheduleSettings", UNSET)
        periodically_schedule_settings: Union[Unset, MacPeriodicallyScheduleSettings]
        if isinstance(_periodically_schedule_settings, Unset):
            periodically_schedule_settings = UNSET
        else:
            periodically_schedule_settings = MacPeriodicallyScheduleSettings.from_dict(_periodically_schedule_settings)

        _active_full_settings = d.pop("activeFullSettings", UNSET)
        active_full_settings: Union[Unset, MacActiveFullSettings]
        if isinstance(_active_full_settings, Unset):
            active_full_settings = UNSET
        else:
            active_full_settings = MacActiveFullSettings.from_dict(_active_full_settings)

        _retry_settings = d.pop("retrySettings", UNSET)
        retry_settings: Union[Unset, MacScheduleRetrySettings]
        if isinstance(_retry_settings, Unset):
            retry_settings = UNSET
        else:
            retry_settings = MacScheduleRetrySettings.from_dict(_retry_settings)

        _backup_health_check_schedule_settings = d.pop("backupHealthCheckScheduleSettings", UNSET)
        backup_health_check_schedule_settings: Union[Unset, MacBackupHealthCheckScheduleSettings]
        if isinstance(_backup_health_check_schedule_settings, Unset):
            backup_health_check_schedule_settings = UNSET
        else:
            backup_health_check_schedule_settings = MacBackupHealthCheckScheduleSettings.from_dict(
                _backup_health_check_schedule_settings
            )

        mac_job_schedule_settings = cls(
            schedule_type=schedule_type,
            daily_schedule_settings=daily_schedule_settings,
            monthly_schedule_settings=monthly_schedule_settings,
            periodically_schedule_settings=periodically_schedule_settings,
            active_full_settings=active_full_settings,
            retry_settings=retry_settings,
            backup_health_check_schedule_settings=backup_health_check_schedule_settings,
        )

        mac_job_schedule_settings.additional_properties = d
        return mac_job_schedule_settings

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
