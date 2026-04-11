from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_backup_job_periodically_kinds_nullable import BackupServerBackupJobPeriodicallyKindsNullable
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_window_setting_type_0 import BackupServerBackupJobWindowSettingType0


T = TypeVar("T", bound="BackupServerBackupJobSchedulePeriodicallyType0")


@_attrs_define
class BackupServerBackupJobSchedulePeriodicallyType0:
    """Periodic job scheduling options.

    Attributes:
        is_enabled (bool): Indicates whether periodic job schedule is enabled. Default: False.
        periodically_kind (BackupServerBackupJobPeriodicallyKindsNullable | Unset): Time unit for periodic job
            scheduling.
        frequency (int | None | Unset): Number of time units that define schedule periods.
        backup_window (BackupServerBackupJobWindowSettingType0 | None | Unset): Array of daily schemes that define
            backup window.
        start_time_within_an_hour (int | None | Unset): Start time within an hour, in minutes.
    """

    is_enabled: bool = False
    periodically_kind: BackupServerBackupJobPeriodicallyKindsNullable | Unset = UNSET
    frequency: int | None | Unset = UNSET
    backup_window: BackupServerBackupJobWindowSettingType0 | None | Unset = UNSET
    start_time_within_an_hour: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.backup_server_backup_job_window_setting_type_0 import BackupServerBackupJobWindowSettingType0

        is_enabled = self.is_enabled

        periodically_kind: str | Unset = UNSET
        if not isinstance(self.periodically_kind, Unset):
            periodically_kind = self.periodically_kind.value

        frequency: int | None | Unset
        if isinstance(self.frequency, Unset):
            frequency = UNSET
        else:
            frequency = self.frequency

        backup_window: dict[str, Any] | None | Unset
        if isinstance(self.backup_window, Unset):
            backup_window = UNSET
        elif isinstance(self.backup_window, BackupServerBackupJobWindowSettingType0):
            backup_window = self.backup_window.to_dict()
        else:
            backup_window = self.backup_window

        start_time_within_an_hour: int | None | Unset
        if isinstance(self.start_time_within_an_hour, Unset):
            start_time_within_an_hour = UNSET
        else:
            start_time_within_an_hour = self.start_time_within_an_hour

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isEnabled": is_enabled,
            }
        )
        if periodically_kind is not UNSET:
            field_dict["periodicallyKind"] = periodically_kind
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if backup_window is not UNSET:
            field_dict["backupWindow"] = backup_window
        if start_time_within_an_hour is not UNSET:
            field_dict["startTimeWithinAnHour"] = start_time_within_an_hour

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_backup_job_window_setting_type_0 import BackupServerBackupJobWindowSettingType0

        d = dict(src_dict)
        is_enabled = d.pop("isEnabled")

        _periodically_kind = d.pop("periodicallyKind", UNSET)
        periodically_kind: BackupServerBackupJobPeriodicallyKindsNullable | Unset
        if isinstance(_periodically_kind, Unset):
            periodically_kind = UNSET
        else:
            periodically_kind = BackupServerBackupJobPeriodicallyKindsNullable(_periodically_kind)

        def _parse_frequency(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        frequency = _parse_frequency(d.pop("frequency", UNSET))

        def _parse_backup_window(data: object) -> BackupServerBackupJobWindowSettingType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_window_setting_type_0 = (
                    BackupServerBackupJobWindowSettingType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_window_setting_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BackupServerBackupJobWindowSettingType0 | None | Unset, data)

        backup_window = _parse_backup_window(d.pop("backupWindow", UNSET))

        def _parse_start_time_within_an_hour(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        start_time_within_an_hour = _parse_start_time_within_an_hour(d.pop("startTimeWithinAnHour", UNSET))

        backup_server_backup_job_schedule_periodically_type_0 = cls(
            is_enabled=is_enabled,
            periodically_kind=periodically_kind,
            frequency=frequency,
            backup_window=backup_window,
            start_time_within_an_hour=start_time_within_an_hour,
        )

        backup_server_backup_job_schedule_periodically_type_0.additional_properties = d
        return backup_server_backup_job_schedule_periodically_type_0

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
