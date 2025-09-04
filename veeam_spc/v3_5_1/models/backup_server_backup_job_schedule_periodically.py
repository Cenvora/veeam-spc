from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_backup_job_periodically_kinds_nullable import BackupServerBackupJobPeriodicallyKindsNullable
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_window_setting import BackupServerBackupJobWindowSetting


T = TypeVar("T", bound="BackupServerBackupJobSchedulePeriodically")


@_attrs_define
class BackupServerBackupJobSchedulePeriodically:
    """Periodic job scheduling options.

    Attributes:
        is_enabled (bool): Indicates whether periodic job schedule is enabled. Default: False.
        periodically_kind (Union[Unset, BackupServerBackupJobPeriodicallyKindsNullable]): Time unit for periodic job
            scheduling.
        frequency (Union[Unset, int]): Number of time units that define schedule periods.
        backup_window (Union[Unset, BackupServerBackupJobWindowSetting]): Array of daily schemes that define backup
            window.
        start_time_within_an_hour (Union[Unset, int]): Start time within an hour, in minutes.
    """

    is_enabled: bool = False
    periodically_kind: Union[Unset, BackupServerBackupJobPeriodicallyKindsNullable] = UNSET
    frequency: Union[Unset, int] = UNSET
    backup_window: Union[Unset, "BackupServerBackupJobWindowSetting"] = UNSET
    start_time_within_an_hour: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        periodically_kind: Union[Unset, str] = UNSET
        if not isinstance(self.periodically_kind, Unset):
            periodically_kind = self.periodically_kind.value

        frequency = self.frequency

        backup_window: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.backup_window, Unset):
            backup_window = self.backup_window.to_dict()

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
        from ..models.backup_server_backup_job_window_setting import BackupServerBackupJobWindowSetting

        d = dict(src_dict)
        is_enabled = d.pop("isEnabled")

        _periodically_kind = d.pop("periodicallyKind", UNSET)
        periodically_kind: Union[Unset, BackupServerBackupJobPeriodicallyKindsNullable]
        if isinstance(_periodically_kind, Unset):
            periodically_kind = UNSET
        else:
            periodically_kind = BackupServerBackupJobPeriodicallyKindsNullable(_periodically_kind)

        frequency = d.pop("frequency", UNSET)

        _backup_window = d.pop("backupWindow", UNSET)
        backup_window: Union[Unset, BackupServerBackupJobWindowSetting]
        if isinstance(_backup_window, Unset):
            backup_window = UNSET
        else:
            backup_window = BackupServerBackupJobWindowSetting.from_dict(_backup_window)

        start_time_within_an_hour = d.pop("startTimeWithinAnHour", UNSET)

        backup_server_backup_job_schedule_periodically = cls(
            is_enabled=is_enabled,
            periodically_kind=periodically_kind,
            frequency=frequency,
            backup_window=backup_window,
            start_time_within_an_hour=start_time_within_an_hour,
        )

        backup_server_backup_job_schedule_periodically.additional_properties = d
        return backup_server_backup_job_schedule_periodically

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
