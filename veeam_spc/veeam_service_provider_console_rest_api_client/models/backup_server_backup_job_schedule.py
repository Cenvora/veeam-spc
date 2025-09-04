from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_schedule_after_this_job import BackupServerBackupJobScheduleAfterThisJob
    from ..models.backup_server_backup_job_schedule_backup_window import BackupServerBackupJobScheduleBackupWindow
    from ..models.backup_server_backup_job_schedule_daily import BackupServerBackupJobScheduleDaily
    from ..models.backup_server_backup_job_schedule_monthly import BackupServerBackupJobScheduleMonthly
    from ..models.backup_server_backup_job_schedule_periodically import BackupServerBackupJobSchedulePeriodically
    from ..models.backup_server_backup_job_schedule_retry import BackupServerBackupJobScheduleRetry


T = TypeVar("T", bound="BackupServerBackupJobSchedule")


@_attrs_define
class BackupServerBackupJobSchedule:
    """Job scheduling settings.

    Attributes:
        run_automatically (Union[Unset, bool]): Indicates whether job scheduling is enabled. Default: False.
        daily (Union[Unset, BackupServerBackupJobScheduleDaily]): Daily job scheduling settings.
        monthly (Union[Unset, BackupServerBackupJobScheduleMonthly]): Monthly job scheduling settings.
        periodically (Union[Unset, BackupServerBackupJobSchedulePeriodically]): Periodic job scheduling options.
        continuously (Union[Unset, BackupServerBackupJobScheduleBackupWindow]): Backup window settings.
        after_this_job (Union[Unset, BackupServerBackupJobScheduleAfterThisJob]): Job chaining settings.
        retry (Union[Unset, BackupServerBackupJobScheduleRetry]): Job retry settings.
        backup_window (Union[Unset, BackupServerBackupJobScheduleBackupWindow]): Backup window settings.
    """

    run_automatically: Union[Unset, bool] = False
    daily: Union[Unset, "BackupServerBackupJobScheduleDaily"] = UNSET
    monthly: Union[Unset, "BackupServerBackupJobScheduleMonthly"] = UNSET
    periodically: Union[Unset, "BackupServerBackupJobSchedulePeriodically"] = UNSET
    continuously: Union[Unset, "BackupServerBackupJobScheduleBackupWindow"] = UNSET
    after_this_job: Union[Unset, "BackupServerBackupJobScheduleAfterThisJob"] = UNSET
    retry: Union[Unset, "BackupServerBackupJobScheduleRetry"] = UNSET
    backup_window: Union[Unset, "BackupServerBackupJobScheduleBackupWindow"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_automatically = self.run_automatically

        daily: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.daily, Unset):
            daily = self.daily.to_dict()

        monthly: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.monthly, Unset):
            monthly = self.monthly.to_dict()

        periodically: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.periodically, Unset):
            periodically = self.periodically.to_dict()

        continuously: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.continuously, Unset):
            continuously = self.continuously.to_dict()

        after_this_job: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.after_this_job, Unset):
            after_this_job = self.after_this_job.to_dict()

        retry: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.retry, Unset):
            retry = self.retry.to_dict()

        backup_window: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.backup_window, Unset):
            backup_window = self.backup_window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if run_automatically is not UNSET:
            field_dict["runAutomatically"] = run_automatically
        if daily is not UNSET:
            field_dict["daily"] = daily
        if monthly is not UNSET:
            field_dict["monthly"] = monthly
        if periodically is not UNSET:
            field_dict["periodically"] = periodically
        if continuously is not UNSET:
            field_dict["continuously"] = continuously
        if after_this_job is not UNSET:
            field_dict["afterThisJob"] = after_this_job
        if retry is not UNSET:
            field_dict["retry"] = retry
        if backup_window is not UNSET:
            field_dict["backupWindow"] = backup_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_backup_job_schedule_after_this_job import BackupServerBackupJobScheduleAfterThisJob
        from ..models.backup_server_backup_job_schedule_backup_window import BackupServerBackupJobScheduleBackupWindow
        from ..models.backup_server_backup_job_schedule_daily import BackupServerBackupJobScheduleDaily
        from ..models.backup_server_backup_job_schedule_monthly import BackupServerBackupJobScheduleMonthly
        from ..models.backup_server_backup_job_schedule_periodically import BackupServerBackupJobSchedulePeriodically
        from ..models.backup_server_backup_job_schedule_retry import BackupServerBackupJobScheduleRetry

        d = dict(src_dict)
        run_automatically = d.pop("runAutomatically", UNSET)

        _daily = d.pop("daily", UNSET)
        daily: Union[Unset, BackupServerBackupJobScheduleDaily]
        if isinstance(_daily, Unset):
            daily = UNSET
        else:
            daily = BackupServerBackupJobScheduleDaily.from_dict(_daily)

        _monthly = d.pop("monthly", UNSET)
        monthly: Union[Unset, BackupServerBackupJobScheduleMonthly]
        if isinstance(_monthly, Unset):
            monthly = UNSET
        else:
            monthly = BackupServerBackupJobScheduleMonthly.from_dict(_monthly)

        _periodically = d.pop("periodically", UNSET)
        periodically: Union[Unset, BackupServerBackupJobSchedulePeriodically]
        if isinstance(_periodically, Unset):
            periodically = UNSET
        else:
            periodically = BackupServerBackupJobSchedulePeriodically.from_dict(_periodically)

        _continuously = d.pop("continuously", UNSET)
        continuously: Union[Unset, BackupServerBackupJobScheduleBackupWindow]
        if isinstance(_continuously, Unset):
            continuously = UNSET
        else:
            continuously = BackupServerBackupJobScheduleBackupWindow.from_dict(_continuously)

        _after_this_job = d.pop("afterThisJob", UNSET)
        after_this_job: Union[Unset, BackupServerBackupJobScheduleAfterThisJob]
        if isinstance(_after_this_job, Unset):
            after_this_job = UNSET
        else:
            after_this_job = BackupServerBackupJobScheduleAfterThisJob.from_dict(_after_this_job)

        _retry = d.pop("retry", UNSET)
        retry: Union[Unset, BackupServerBackupJobScheduleRetry]
        if isinstance(_retry, Unset):
            retry = UNSET
        else:
            retry = BackupServerBackupJobScheduleRetry.from_dict(_retry)

        _backup_window = d.pop("backupWindow", UNSET)
        backup_window: Union[Unset, BackupServerBackupJobScheduleBackupWindow]
        if isinstance(_backup_window, Unset):
            backup_window = UNSET
        else:
            backup_window = BackupServerBackupJobScheduleBackupWindow.from_dict(_backup_window)

        backup_server_backup_job_schedule = cls(
            run_automatically=run_automatically,
            daily=daily,
            monthly=monthly,
            periodically=periodically,
            continuously=continuously,
            after_this_job=after_this_job,
            retry=retry,
            backup_window=backup_window,
        )

        backup_server_backup_job_schedule.additional_properties = d
        return backup_server_backup_job_schedule

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
