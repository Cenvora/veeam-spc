from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_backup_job_daily_kinds import BackupServerBackupJobDailyKinds
from ..models.days_of_week_nullable import DaysOfWeekNullable
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerBackupJobScheduleDailyType0")


@_attrs_define
class BackupServerBackupJobScheduleDailyType0:
    """Daily job scheduling settings.

    Attributes:
        is_enabled (bool): Indicates whether daily schedule is enabled. Default: False.
        local_time (Union[None, Unset, str]): Local time when a job must start.
        daily_kind (Union[Unset, BackupServerBackupJobDailyKinds]): Type of daily job scheduling.
        days (Union[None, Unset, list[DaysOfWeekNullable]]): Days of the week when the job must start.
    """

    is_enabled: bool = False
    local_time: Union[None, Unset, str] = UNSET
    daily_kind: Union[Unset, BackupServerBackupJobDailyKinds] = UNSET
    days: Union[None, Unset, list[DaysOfWeekNullable]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        local_time: Union[None, Unset, str]
        if isinstance(self.local_time, Unset):
            local_time = UNSET
        else:
            local_time = self.local_time

        daily_kind: Union[Unset, str] = UNSET
        if not isinstance(self.daily_kind, Unset):
            daily_kind = self.daily_kind.value

        days: Union[None, Unset, list[str]]
        if isinstance(self.days, Unset):
            days = UNSET
        elif isinstance(self.days, list):
            days = []
            for days_type_0_item_data in self.days:
                days_type_0_item = days_type_0_item_data.value
                days.append(days_type_0_item)

        else:
            days = self.days

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

        def _parse_local_time(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        local_time = _parse_local_time(d.pop("localTime", UNSET))

        _daily_kind = d.pop("dailyKind", UNSET)
        daily_kind: Union[Unset, BackupServerBackupJobDailyKinds]
        if isinstance(_daily_kind, Unset):
            daily_kind = UNSET
        else:
            daily_kind = BackupServerBackupJobDailyKinds(_daily_kind)

        def _parse_days(data: object) -> Union[None, Unset, list[DaysOfWeekNullable]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                days_type_0 = []
                _days_type_0 = data
                for days_type_0_item_data in _days_type_0:
                    days_type_0_item = DaysOfWeekNullable(days_type_0_item_data)

                    days_type_0.append(days_type_0_item)

                return days_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[DaysOfWeekNullable]], data)

        days = _parse_days(d.pop("days", UNSET))

        backup_server_backup_job_schedule_daily_type_0 = cls(
            is_enabled=is_enabled,
            local_time=local_time,
            daily_kind=daily_kind,
            days=days,
        )

        backup_server_backup_job_schedule_daily_type_0.additional_properties = d
        return backup_server_backup_job_schedule_daily_type_0

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
