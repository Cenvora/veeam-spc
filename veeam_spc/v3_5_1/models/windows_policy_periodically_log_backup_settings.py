from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.windows_policy_periodically_log_backup_settings_backup_retention_mode import (
    WindowsPolicyPeriodicallyLogBackupSettingsBackupRetentionMode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="WindowsPolicyPeriodicallyLogBackupSettings")


@_attrs_define
class WindowsPolicyPeriodicallyLogBackupSettings:
    """
    Attributes:
        backup_logs_every_min (Union[Unset, int]): Frequency for archived logs backup, in minutes. Default: 15.
        backup_retention_mode (Union[Unset, WindowsPolicyPeriodicallyLogBackupSettingsBackupRetentionMode]): Type of a
            retention policy for archived logs. Default:
            WindowsPolicyPeriodicallyLogBackupSettingsBackupRetentionMode.UNTILBACKUPISDELETED.
        keep_backups_only_last_days (Union[Unset, int]): Number of days for which archived logs are kept. Default: 15.
    """

    backup_logs_every_min: Union[Unset, int] = 15
    backup_retention_mode: Union[Unset, WindowsPolicyPeriodicallyLogBackupSettingsBackupRetentionMode] = (
        WindowsPolicyPeriodicallyLogBackupSettingsBackupRetentionMode.UNTILBACKUPISDELETED
    )
    keep_backups_only_last_days: Union[Unset, int] = 15
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_logs_every_min = self.backup_logs_every_min

        backup_retention_mode: Union[Unset, str] = UNSET
        if not isinstance(self.backup_retention_mode, Unset):
            backup_retention_mode = self.backup_retention_mode.value

        keep_backups_only_last_days = self.keep_backups_only_last_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_logs_every_min is not UNSET:
            field_dict["backupLogsEveryMin"] = backup_logs_every_min
        if backup_retention_mode is not UNSET:
            field_dict["backupRetentionMode"] = backup_retention_mode
        if keep_backups_only_last_days is not UNSET:
            field_dict["keepBackupsOnlyLastDays"] = keep_backups_only_last_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backup_logs_every_min = d.pop("backupLogsEveryMin", UNSET)

        _backup_retention_mode = d.pop("backupRetentionMode", UNSET)
        backup_retention_mode: Union[Unset, WindowsPolicyPeriodicallyLogBackupSettingsBackupRetentionMode]
        if isinstance(_backup_retention_mode, Unset):
            backup_retention_mode = UNSET
        else:
            backup_retention_mode = WindowsPolicyPeriodicallyLogBackupSettingsBackupRetentionMode(
                _backup_retention_mode
            )

        keep_backups_only_last_days = d.pop("keepBackupsOnlyLastDays", UNSET)

        windows_policy_periodically_log_backup_settings = cls(
            backup_logs_every_min=backup_logs_every_min,
            backup_retention_mode=backup_retention_mode,
            keep_backups_only_last_days=keep_backups_only_last_days,
        )

        windows_policy_periodically_log_backup_settings.additional_properties = d
        return windows_policy_periodically_log_backup_settings

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
