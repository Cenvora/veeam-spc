from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_job_schedule_options_backup_window import BackupServerJobScheduleOptionsBackupWindow
    from ..models.backup_server_job_schedule_options_chaining import BackupServerJobScheduleOptionsChaining
    from ..models.backup_server_job_schedule_options_daily import BackupServerJobScheduleOptionsDaily
    from ..models.backup_server_job_schedule_options_monthly import BackupServerJobScheduleOptionsMonthly
    from ..models.backup_server_job_schedule_options_periodically import BackupServerJobScheduleOptionsPeriodically


T = TypeVar("T", bound="BackupServerJobSchedule")


@_attrs_define
class BackupServerJobSchedule:
    """
    Attributes:
        start_date_time (datetime.datetime | Unset): Start date and time of the next scheduled job session.
        start_date_time_utc (datetime.datetime | Unset): Start date and time of the next scheduled job session in UTC.
        daily_schedule_options (BackupServerJobScheduleOptionsDaily | Unset):
        monthly_schedule_options (BackupServerJobScheduleOptionsMonthly | Unset):
        periodically_schedule_options (BackupServerJobScheduleOptionsPeriodically | Unset):
        backup_window_options (BackupServerJobScheduleOptionsBackupWindow | Unset):
        continuous_schedule_enabled (bool | Unset): Indicates whether continuous schedule is enabled.
        chaining_options (BackupServerJobScheduleOptionsChaining | Unset):
    """

    start_date_time: datetime.datetime | Unset = UNSET
    start_date_time_utc: datetime.datetime | Unset = UNSET
    daily_schedule_options: BackupServerJobScheduleOptionsDaily | Unset = UNSET
    monthly_schedule_options: BackupServerJobScheduleOptionsMonthly | Unset = UNSET
    periodically_schedule_options: BackupServerJobScheduleOptionsPeriodically | Unset = UNSET
    backup_window_options: BackupServerJobScheduleOptionsBackupWindow | Unset = UNSET
    continuous_schedule_enabled: bool | Unset = UNSET
    chaining_options: BackupServerJobScheduleOptionsChaining | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_date_time: str | Unset = UNSET
        if not isinstance(self.start_date_time, Unset):
            start_date_time = self.start_date_time.isoformat()

        start_date_time_utc: str | Unset = UNSET
        if not isinstance(self.start_date_time_utc, Unset):
            start_date_time_utc = self.start_date_time_utc.isoformat()

        daily_schedule_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.daily_schedule_options, Unset):
            daily_schedule_options = self.daily_schedule_options.to_dict()

        monthly_schedule_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monthly_schedule_options, Unset):
            monthly_schedule_options = self.monthly_schedule_options.to_dict()

        periodically_schedule_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.periodically_schedule_options, Unset):
            periodically_schedule_options = self.periodically_schedule_options.to_dict()

        backup_window_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_window_options, Unset):
            backup_window_options = self.backup_window_options.to_dict()

        continuous_schedule_enabled = self.continuous_schedule_enabled

        chaining_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.chaining_options, Unset):
            chaining_options = self.chaining_options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_date_time is not UNSET:
            field_dict["startDateTime"] = start_date_time
        if start_date_time_utc is not UNSET:
            field_dict["startDateTimeUtc"] = start_date_time_utc
        if daily_schedule_options is not UNSET:
            field_dict["dailyScheduleOptions"] = daily_schedule_options
        if monthly_schedule_options is not UNSET:
            field_dict["monthlyScheduleOptions"] = monthly_schedule_options
        if periodically_schedule_options is not UNSET:
            field_dict["periodicallyScheduleOptions"] = periodically_schedule_options
        if backup_window_options is not UNSET:
            field_dict["backupWindowOptions"] = backup_window_options
        if continuous_schedule_enabled is not UNSET:
            field_dict["continuousScheduleEnabled"] = continuous_schedule_enabled
        if chaining_options is not UNSET:
            field_dict["chainingOptions"] = chaining_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_job_schedule_options_backup_window import BackupServerJobScheduleOptionsBackupWindow
        from ..models.backup_server_job_schedule_options_chaining import BackupServerJobScheduleOptionsChaining
        from ..models.backup_server_job_schedule_options_daily import BackupServerJobScheduleOptionsDaily
        from ..models.backup_server_job_schedule_options_monthly import BackupServerJobScheduleOptionsMonthly
        from ..models.backup_server_job_schedule_options_periodically import BackupServerJobScheduleOptionsPeriodically

        d = dict(src_dict)
        _start_date_time = d.pop("startDateTime", UNSET)
        start_date_time: datetime.datetime | Unset
        if isinstance(_start_date_time, Unset):
            start_date_time = UNSET
        else:
            start_date_time = isoparse(_start_date_time)

        _start_date_time_utc = d.pop("startDateTimeUtc", UNSET)
        start_date_time_utc: datetime.datetime | Unset
        if isinstance(_start_date_time_utc, Unset):
            start_date_time_utc = UNSET
        else:
            start_date_time_utc = isoparse(_start_date_time_utc)

        _daily_schedule_options = d.pop("dailyScheduleOptions", UNSET)
        daily_schedule_options: BackupServerJobScheduleOptionsDaily | Unset
        if isinstance(_daily_schedule_options, Unset):
            daily_schedule_options = UNSET
        else:
            daily_schedule_options = BackupServerJobScheduleOptionsDaily.from_dict(_daily_schedule_options)

        _monthly_schedule_options = d.pop("monthlyScheduleOptions", UNSET)
        monthly_schedule_options: BackupServerJobScheduleOptionsMonthly | Unset
        if isinstance(_monthly_schedule_options, Unset):
            monthly_schedule_options = UNSET
        else:
            monthly_schedule_options = BackupServerJobScheduleOptionsMonthly.from_dict(_monthly_schedule_options)

        _periodically_schedule_options = d.pop("periodicallyScheduleOptions", UNSET)
        periodically_schedule_options: BackupServerJobScheduleOptionsPeriodically | Unset
        if isinstance(_periodically_schedule_options, Unset):
            periodically_schedule_options = UNSET
        else:
            periodically_schedule_options = BackupServerJobScheduleOptionsPeriodically.from_dict(
                _periodically_schedule_options
            )

        _backup_window_options = d.pop("backupWindowOptions", UNSET)
        backup_window_options: BackupServerJobScheduleOptionsBackupWindow | Unset
        if isinstance(_backup_window_options, Unset):
            backup_window_options = UNSET
        else:
            backup_window_options = BackupServerJobScheduleOptionsBackupWindow.from_dict(_backup_window_options)

        continuous_schedule_enabled = d.pop("continuousScheduleEnabled", UNSET)

        _chaining_options = d.pop("chainingOptions", UNSET)
        chaining_options: BackupServerJobScheduleOptionsChaining | Unset
        if isinstance(_chaining_options, Unset):
            chaining_options = UNSET
        else:
            chaining_options = BackupServerJobScheduleOptionsChaining.from_dict(_chaining_options)

        backup_server_job_schedule = cls(
            start_date_time=start_date_time,
            start_date_time_utc=start_date_time_utc,
            daily_schedule_options=daily_schedule_options,
            monthly_schedule_options=monthly_schedule_options,
            periodically_schedule_options=periodically_schedule_options,
            backup_window_options=backup_window_options,
            continuous_schedule_enabled=continuous_schedule_enabled,
            chaining_options=chaining_options,
        )

        backup_server_job_schedule.additional_properties = d
        return backup_server_job_schedule

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
