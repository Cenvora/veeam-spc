from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_backup_job_daily_kinds import BackupServerBackupJobDailyKinds
from ..models.days_of_week_nullable import DaysOfWeekNullable
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerBackupJobScheduleDaily")


@_attrs_define
class BackupServerBackupJobScheduleDaily:
    """Daily job scheduling settings.

    Attributes:
        is_enabled (bool): Indicates whether daily schedule is enabled. Default: False.
        local_time (str | Unset): Local time when a job must start.
        daily_kind (BackupServerBackupJobDailyKinds | Unset): Type of daily job scheduling.
        days (list[DaysOfWeekNullable] | Unset): Days of the week when the job must start.
    """

    is_enabled: bool = False
    local_time: str | Unset = UNSET
    daily_kind: BackupServerBackupJobDailyKinds | Unset = UNSET
    days: list[DaysOfWeekNullable] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        local_time = self.local_time

        daily_kind: str | Unset = UNSET
        if not isinstance(self.daily_kind, Unset):
            daily_kind = self.daily_kind.value

        days: list[str] | Unset = UNSET
        if not isinstance(self.days, Unset):
            days = []
            for days_item_data in self.days:
                days_item = days_item_data.value
                days.append(days_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isEnabled": is_enabled,
            }
        )
        if local_time is not UNSET:
            field_dict["localTime"] = local_time
        if daily_kind is not UNSET:
            field_dict["dailyKind"] = daily_kind
        if days is not UNSET:
            field_dict["days"] = days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_enabled = d.pop("isEnabled")

        local_time = d.pop("localTime", UNSET)

        _daily_kind = d.pop("dailyKind", UNSET)
        daily_kind: BackupServerBackupJobDailyKinds | Unset
        if isinstance(_daily_kind, Unset):
            daily_kind = UNSET
        else:
            daily_kind = BackupServerBackupJobDailyKinds(_daily_kind)

        _days = d.pop("days", UNSET)
        days: list[DaysOfWeekNullable] | Unset = UNSET
        if _days is not UNSET:
            days = []
            for days_item_data in _days:
                days_item = DaysOfWeekNullable(days_item_data)

                days.append(days_item)

        backup_server_backup_job_schedule_daily = cls(
            is_enabled=is_enabled,
            local_time=local_time,
            daily_kind=daily_kind,
            days=days,
        )

        backup_server_backup_job_schedule_daily.additional_properties = d
        return backup_server_backup_job_schedule_daily

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
