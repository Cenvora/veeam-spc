from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vb_365_backup_job_schedule_policy_daily_type import Vb365BackupJobSchedulePolicyDailyType
from ..models.vb_365_backup_job_schedule_policy_periodically_every import Vb365BackupJobSchedulePolicyPeriodicallyEvery
from ..models.vb_365_backup_job_schedule_policy_schedule_policy_type import (
    Vb365BackupJobSchedulePolicySchedulePolicyType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vb_365_backup_window_settings import Vb365BackupWindowSettings


T = TypeVar("T", bound="Vb365BackupJobSchedulePolicy")


@_attrs_define
class Vb365BackupJobSchedulePolicy:
    """
    Attributes:
        schedule_policy_type (Vb365BackupJobSchedulePolicySchedulePolicyType): Type of a job schedule policy.
        periodically_every (Vb365BackupJobSchedulePolicyPeriodicallyEvery | Unset): Type of a time interval for a
            periodically running job.
        daily_type (Vb365BackupJobSchedulePolicyDailyType | Unset): Days when the daily job runs.
        schedule_enabled (bool | Unset): Indicates whether a job schedule is enabled. Default: False.
        backup_window_enabled (bool | Unset): Indicates whether backup window is enabled. Default: False.
        backup_window_settings (Vb365BackupWindowSettings | Unset):
        periodically_window_settings (Vb365BackupWindowSettings | Unset):
        periodically_window_enabled (bool | Unset): Indicates whether backup window is enabled for periodically running
            jobs.
        periodically_offset_minutes (int | Unset): Number of minutes that must be skipped after specified job starting
            time. Default: 0.
        daily_time (str | Unset): Time of day when job must start in the `hh:mm` format.
        retry_enabled (bool | Unset): Indicates whether job retry is enabled. Default: False.
        retry_number (int | Unset): Number of allowed retries.
        retry_wait_interval (int | Unset): Time interval between job retries.
    """

    schedule_policy_type: Vb365BackupJobSchedulePolicySchedulePolicyType
    periodically_every: Vb365BackupJobSchedulePolicyPeriodicallyEvery | Unset = UNSET
    daily_type: Vb365BackupJobSchedulePolicyDailyType | Unset = UNSET
    schedule_enabled: bool | Unset = False
    backup_window_enabled: bool | Unset = False
    backup_window_settings: Vb365BackupWindowSettings | Unset = UNSET
    periodically_window_settings: Vb365BackupWindowSettings | Unset = UNSET
    periodically_window_enabled: bool | Unset = UNSET
    periodically_offset_minutes: int | Unset = 0
    daily_time: str | Unset = UNSET
    retry_enabled: bool | Unset = False
    retry_number: int | Unset = UNSET
    retry_wait_interval: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_policy_type = self.schedule_policy_type.value

        periodically_every: str | Unset = UNSET
        if not isinstance(self.periodically_every, Unset):
            periodically_every = self.periodically_every.value

        daily_type: str | Unset = UNSET
        if not isinstance(self.daily_type, Unset):
            daily_type = self.daily_type.value

        schedule_enabled = self.schedule_enabled

        backup_window_enabled = self.backup_window_enabled

        backup_window_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_window_settings, Unset):
            backup_window_settings = self.backup_window_settings.to_dict()

        periodically_window_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.periodically_window_settings, Unset):
            periodically_window_settings = self.periodically_window_settings.to_dict()

        periodically_window_enabled = self.periodically_window_enabled

        periodically_offset_minutes = self.periodically_offset_minutes

        daily_time = self.daily_time

        retry_enabled = self.retry_enabled

        retry_number = self.retry_number

        retry_wait_interval = self.retry_wait_interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedulePolicyType": schedule_policy_type,
            }
        )
        if periodically_every is not UNSET:
            field_dict["periodicallyEvery"] = periodically_every
        if daily_type is not UNSET:
            field_dict["dailyType"] = daily_type
        if schedule_enabled is not UNSET:
            field_dict["scheduleEnabled"] = schedule_enabled
        if backup_window_enabled is not UNSET:
            field_dict["backupWindowEnabled"] = backup_window_enabled
        if backup_window_settings is not UNSET:
            field_dict["backupWindowSettings"] = backup_window_settings
        if periodically_window_settings is not UNSET:
            field_dict["periodicallyWindowSettings"] = periodically_window_settings
        if periodically_window_enabled is not UNSET:
            field_dict["periodicallyWindowEnabled"] = periodically_window_enabled
        if periodically_offset_minutes is not UNSET:
            field_dict["periodicallyOffsetMinutes"] = periodically_offset_minutes
        if daily_time is not UNSET:
            field_dict["dailyTime"] = daily_time
        if retry_enabled is not UNSET:
            field_dict["retryEnabled"] = retry_enabled
        if retry_number is not UNSET:
            field_dict["retryNumber"] = retry_number
        if retry_wait_interval is not UNSET:
            field_dict["retryWaitInterval"] = retry_wait_interval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vb_365_backup_window_settings import Vb365BackupWindowSettings

        d = dict(src_dict)
        schedule_policy_type = Vb365BackupJobSchedulePolicySchedulePolicyType(d.pop("schedulePolicyType"))

        _periodically_every = d.pop("periodicallyEvery", UNSET)
        periodically_every: Vb365BackupJobSchedulePolicyPeriodicallyEvery | Unset
        if isinstance(_periodically_every, Unset):
            periodically_every = UNSET
        else:
            periodically_every = Vb365BackupJobSchedulePolicyPeriodicallyEvery(_periodically_every)

        _daily_type = d.pop("dailyType", UNSET)
        daily_type: Vb365BackupJobSchedulePolicyDailyType | Unset
        if isinstance(_daily_type, Unset):
            daily_type = UNSET
        else:
            daily_type = Vb365BackupJobSchedulePolicyDailyType(_daily_type)

        schedule_enabled = d.pop("scheduleEnabled", UNSET)

        backup_window_enabled = d.pop("backupWindowEnabled", UNSET)

        _backup_window_settings = d.pop("backupWindowSettings", UNSET)
        backup_window_settings: Vb365BackupWindowSettings | Unset
        if isinstance(_backup_window_settings, Unset):
            backup_window_settings = UNSET
        else:
            backup_window_settings = Vb365BackupWindowSettings.from_dict(_backup_window_settings)

        _periodically_window_settings = d.pop("periodicallyWindowSettings", UNSET)
        periodically_window_settings: Vb365BackupWindowSettings | Unset
        if isinstance(_periodically_window_settings, Unset):
            periodically_window_settings = UNSET
        else:
            periodically_window_settings = Vb365BackupWindowSettings.from_dict(_periodically_window_settings)

        periodically_window_enabled = d.pop("periodicallyWindowEnabled", UNSET)

        periodically_offset_minutes = d.pop("periodicallyOffsetMinutes", UNSET)

        daily_time = d.pop("dailyTime", UNSET)

        retry_enabled = d.pop("retryEnabled", UNSET)

        retry_number = d.pop("retryNumber", UNSET)

        retry_wait_interval = d.pop("retryWaitInterval", UNSET)

        vb_365_backup_job_schedule_policy = cls(
            schedule_policy_type=schedule_policy_type,
            periodically_every=periodically_every,
            daily_type=daily_type,
            schedule_enabled=schedule_enabled,
            backup_window_enabled=backup_window_enabled,
            backup_window_settings=backup_window_settings,
            periodically_window_settings=periodically_window_settings,
            periodically_window_enabled=periodically_window_enabled,
            periodically_offset_minutes=periodically_offset_minutes,
            daily_time=daily_time,
            retry_enabled=retry_enabled,
            retry_number=retry_number,
            retry_wait_interval=retry_wait_interval,
        )

        vb_365_backup_job_schedule_policy.additional_properties = d
        return vb_365_backup_job_schedule_policy

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
