from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_schedule_after_this_job_type_0 import (
        BackupServerBackupJobScheduleAfterThisJobType0,
    )
    from ..models.backup_server_backup_job_schedule_backup_window_type_0 import (
        BackupServerBackupJobScheduleBackupWindowType0,
    )
    from ..models.backup_server_backup_job_schedule_daily_type_0 import BackupServerBackupJobScheduleDailyType0
    from ..models.backup_server_backup_job_schedule_monthly_type_0 import BackupServerBackupJobScheduleMonthlyType0
    from ..models.backup_server_backup_job_schedule_periodically_type_0 import (
        BackupServerBackupJobSchedulePeriodicallyType0,
    )
    from ..models.backup_server_backup_job_schedule_retry_type_0 import BackupServerBackupJobScheduleRetryType0


T = TypeVar("T", bound="BackupServerBackupJobSchedule")


@_attrs_define
class BackupServerBackupJobSchedule:
    """Job scheduling settings.

    Attributes:
        run_automatically (Union[Unset, bool]): Indicates whether job scheduling is enabled. Default: False.
        daily (Union['BackupServerBackupJobScheduleDailyType0', None, Unset]): Daily job scheduling settings.
        monthly (Union['BackupServerBackupJobScheduleMonthlyType0', None, Unset]): Monthly job scheduling settings.
        periodically (Union['BackupServerBackupJobSchedulePeriodicallyType0', None, Unset]): Periodic job scheduling
            options.
        continuously (Union['BackupServerBackupJobScheduleBackupWindowType0', None, Unset]): Backup window settings.
        after_this_job (Union['BackupServerBackupJobScheduleAfterThisJobType0', None, Unset]): Job chaining settings.
        retry (Union['BackupServerBackupJobScheduleRetryType0', None, Unset]): Job retry settings.
        backup_window (Union['BackupServerBackupJobScheduleBackupWindowType0', None, Unset]): Backup window settings.
    """

    run_automatically: Union[Unset, bool] = False
    daily: Union["BackupServerBackupJobScheduleDailyType0", None, Unset] = UNSET
    monthly: Union["BackupServerBackupJobScheduleMonthlyType0", None, Unset] = UNSET
    periodically: Union["BackupServerBackupJobSchedulePeriodicallyType0", None, Unset] = UNSET
    continuously: Union["BackupServerBackupJobScheduleBackupWindowType0", None, Unset] = UNSET
    after_this_job: Union["BackupServerBackupJobScheduleAfterThisJobType0", None, Unset] = UNSET
    retry: Union["BackupServerBackupJobScheduleRetryType0", None, Unset] = UNSET
    backup_window: Union["BackupServerBackupJobScheduleBackupWindowType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.backup_server_backup_job_schedule_after_this_job_type_0 import (
            BackupServerBackupJobScheduleAfterThisJobType0,
        )
        from ..models.backup_server_backup_job_schedule_backup_window_type_0 import (
            BackupServerBackupJobScheduleBackupWindowType0,
        )
        from ..models.backup_server_backup_job_schedule_daily_type_0 import BackupServerBackupJobScheduleDailyType0
        from ..models.backup_server_backup_job_schedule_monthly_type_0 import BackupServerBackupJobScheduleMonthlyType0
        from ..models.backup_server_backup_job_schedule_periodically_type_0 import (
            BackupServerBackupJobSchedulePeriodicallyType0,
        )
        from ..models.backup_server_backup_job_schedule_retry_type_0 import BackupServerBackupJobScheduleRetryType0

        run_automatically = self.run_automatically

        daily: Union[None, Unset, dict[str, Any]]
        if isinstance(self.daily, Unset):
            daily = UNSET
        elif isinstance(self.daily, BackupServerBackupJobScheduleDailyType0):
            daily = self.daily.to_dict()
        else:
            daily = self.daily

        monthly: Union[None, Unset, dict[str, Any]]
        if isinstance(self.monthly, Unset):
            monthly = UNSET
        elif isinstance(self.monthly, BackupServerBackupJobScheduleMonthlyType0):
            monthly = self.monthly.to_dict()
        else:
            monthly = self.monthly

        periodically: Union[None, Unset, dict[str, Any]]
        if isinstance(self.periodically, Unset):
            periodically = UNSET
        elif isinstance(self.periodically, BackupServerBackupJobSchedulePeriodicallyType0):
            periodically = self.periodically.to_dict()
        else:
            periodically = self.periodically

        continuously: Union[None, Unset, dict[str, Any]]
        if isinstance(self.continuously, Unset):
            continuously = UNSET
        elif isinstance(self.continuously, BackupServerBackupJobScheduleBackupWindowType0):
            continuously = self.continuously.to_dict()
        else:
            continuously = self.continuously

        after_this_job: Union[None, Unset, dict[str, Any]]
        if isinstance(self.after_this_job, Unset):
            after_this_job = UNSET
        elif isinstance(self.after_this_job, BackupServerBackupJobScheduleAfterThisJobType0):
            after_this_job = self.after_this_job.to_dict()
        else:
            after_this_job = self.after_this_job

        retry: Union[None, Unset, dict[str, Any]]
        if isinstance(self.retry, Unset):
            retry = UNSET
        elif isinstance(self.retry, BackupServerBackupJobScheduleRetryType0):
            retry = self.retry.to_dict()
        else:
            retry = self.retry

        backup_window: Union[None, Unset, dict[str, Any]]
        if isinstance(self.backup_window, Unset):
            backup_window = UNSET
        elif isinstance(self.backup_window, BackupServerBackupJobScheduleBackupWindowType0):
            backup_window = self.backup_window.to_dict()
        else:
            backup_window = self.backup_window

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
        from ..models.backup_server_backup_job_schedule_after_this_job_type_0 import (
            BackupServerBackupJobScheduleAfterThisJobType0,
        )
        from ..models.backup_server_backup_job_schedule_backup_window_type_0 import (
            BackupServerBackupJobScheduleBackupWindowType0,
        )
        from ..models.backup_server_backup_job_schedule_daily_type_0 import BackupServerBackupJobScheduleDailyType0
        from ..models.backup_server_backup_job_schedule_monthly_type_0 import BackupServerBackupJobScheduleMonthlyType0
        from ..models.backup_server_backup_job_schedule_periodically_type_0 import (
            BackupServerBackupJobSchedulePeriodicallyType0,
        )
        from ..models.backup_server_backup_job_schedule_retry_type_0 import BackupServerBackupJobScheduleRetryType0

        d = dict(src_dict)
        run_automatically = d.pop("runAutomatically", UNSET)

        def _parse_daily(data: object) -> Union["BackupServerBackupJobScheduleDailyType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_schedule_daily_type_0 = (
                    BackupServerBackupJobScheduleDailyType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_schedule_daily_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobScheduleDailyType0", None, Unset], data)

        daily = _parse_daily(d.pop("daily", UNSET))

        def _parse_monthly(data: object) -> Union["BackupServerBackupJobScheduleMonthlyType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_schedule_monthly_type_0 = (
                    BackupServerBackupJobScheduleMonthlyType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_schedule_monthly_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobScheduleMonthlyType0", None, Unset], data)

        monthly = _parse_monthly(d.pop("monthly", UNSET))

        def _parse_periodically(data: object) -> Union["BackupServerBackupJobSchedulePeriodicallyType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_schedule_periodically_type_0 = (
                    BackupServerBackupJobSchedulePeriodicallyType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_schedule_periodically_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobSchedulePeriodicallyType0", None, Unset], data)

        periodically = _parse_periodically(d.pop("periodically", UNSET))

        def _parse_continuously(data: object) -> Union["BackupServerBackupJobScheduleBackupWindowType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_schedule_backup_window_type_0 = (
                    BackupServerBackupJobScheduleBackupWindowType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_schedule_backup_window_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobScheduleBackupWindowType0", None, Unset], data)

        continuously = _parse_continuously(d.pop("continuously", UNSET))

        def _parse_after_this_job(data: object) -> Union["BackupServerBackupJobScheduleAfterThisJobType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_schedule_after_this_job_type_0 = (
                    BackupServerBackupJobScheduleAfterThisJobType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_schedule_after_this_job_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobScheduleAfterThisJobType0", None, Unset], data)

        after_this_job = _parse_after_this_job(d.pop("afterThisJob", UNSET))

        def _parse_retry(data: object) -> Union["BackupServerBackupJobScheduleRetryType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_schedule_retry_type_0 = (
                    BackupServerBackupJobScheduleRetryType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_schedule_retry_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobScheduleRetryType0", None, Unset], data)

        retry = _parse_retry(d.pop("retry", UNSET))

        def _parse_backup_window(data: object) -> Union["BackupServerBackupJobScheduleBackupWindowType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_schedule_backup_window_type_0 = (
                    BackupServerBackupJobScheduleBackupWindowType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_schedule_backup_window_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobScheduleBackupWindowType0", None, Unset], data)

        backup_window = _parse_backup_window(d.pop("backupWindow", UNSET))

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
