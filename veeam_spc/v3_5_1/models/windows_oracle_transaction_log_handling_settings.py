from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.windows_oracle_transaction_log_handling_settings_archived_logs_retention_mode import (
    WindowsOracleTransactionLogHandlingSettingsArchivedLogsRetentionMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.windows_oracle_account_settings import WindowsOracleAccountSettings
    from ..models.windows_policy_periodically_log_backup_settings import WindowsPolicyPeriodicallyLogBackupSettings


T = TypeVar("T", bound="WindowsOracleTransactionLogHandlingSettings")


@_attrs_define
class WindowsOracleTransactionLogHandlingSettings:
    """
    Attributes:
        credentials (Union[Unset, WindowsOracleAccountSettings]):
        archived_logs_retention_mode (Union[Unset,
            WindowsOracleTransactionLogHandlingSettingsArchivedLogsRetentionMode]): Archived log processing mode. Default:
            WindowsOracleTransactionLogHandlingSettingsArchivedLogsRetentionMode.DONOTDELETEARCHIVEDLOGS.
        backup_life_time_hours (Union[Unset, int]): Amount of time after which archived logs must be deleted, in hours.
            > Required for the `DeleteLogsOlderThanHours` archived log processing mode.
             Default: 24.
        backup_size_threshold_gb (Union[Unset, int]): Maximum threshold for archived log file size, in GB.
            > If an archived log file exceeds the limitation, it is deleted. <br>
            > Required for the `DeleteLogsOverGb` archived log processing mode.
             Default: 10.
        backup_logs_periodically (Union[Unset, bool]): Indicates whether Veeam Agent for Microsoft Windows must back up
            archive logs. Default: False.
        periodically_backup_setting (Union[Unset, WindowsPolicyPeriodicallyLogBackupSettings]):
    """

    credentials: Union[Unset, "WindowsOracleAccountSettings"] = UNSET
    archived_logs_retention_mode: Union[Unset, WindowsOracleTransactionLogHandlingSettingsArchivedLogsRetentionMode] = (
        WindowsOracleTransactionLogHandlingSettingsArchivedLogsRetentionMode.DONOTDELETEARCHIVEDLOGS
    )
    backup_life_time_hours: Union[Unset, int] = 24
    backup_size_threshold_gb: Union[Unset, int] = 10
    backup_logs_periodically: Union[Unset, bool] = False
    periodically_backup_setting: Union[Unset, "WindowsPolicyPeriodicallyLogBackupSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credentials: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        archived_logs_retention_mode: Union[Unset, str] = UNSET
        if not isinstance(self.archived_logs_retention_mode, Unset):
            archived_logs_retention_mode = self.archived_logs_retention_mode.value

        backup_life_time_hours = self.backup_life_time_hours

        backup_size_threshold_gb = self.backup_size_threshold_gb

        backup_logs_periodically = self.backup_logs_periodically

        periodically_backup_setting: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.periodically_backup_setting, Unset):
            periodically_backup_setting = self.periodically_backup_setting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if archived_logs_retention_mode is not UNSET:
            field_dict["archivedLogsRetentionMode"] = archived_logs_retention_mode
        if backup_life_time_hours is not UNSET:
            field_dict["backupLifeTimeHours"] = backup_life_time_hours
        if backup_size_threshold_gb is not UNSET:
            field_dict["backupSizeThresholdGb"] = backup_size_threshold_gb
        if backup_logs_periodically is not UNSET:
            field_dict["backupLogsPeriodically"] = backup_logs_periodically
        if periodically_backup_setting is not UNSET:
            field_dict["periodicallyBackupSetting"] = periodically_backup_setting

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.windows_oracle_account_settings import WindowsOracleAccountSettings
        from ..models.windows_policy_periodically_log_backup_settings import WindowsPolicyPeriodicallyLogBackupSettings

        d = dict(src_dict)
        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, WindowsOracleAccountSettings]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = WindowsOracleAccountSettings.from_dict(_credentials)

        _archived_logs_retention_mode = d.pop("archivedLogsRetentionMode", UNSET)
        archived_logs_retention_mode: Union[Unset, WindowsOracleTransactionLogHandlingSettingsArchivedLogsRetentionMode]
        if isinstance(_archived_logs_retention_mode, Unset):
            archived_logs_retention_mode = UNSET
        else:
            archived_logs_retention_mode = WindowsOracleTransactionLogHandlingSettingsArchivedLogsRetentionMode(
                _archived_logs_retention_mode
            )

        backup_life_time_hours = d.pop("backupLifeTimeHours", UNSET)

        backup_size_threshold_gb = d.pop("backupSizeThresholdGb", UNSET)

        backup_logs_periodically = d.pop("backupLogsPeriodically", UNSET)

        _periodically_backup_setting = d.pop("periodicallyBackupSetting", UNSET)
        periodically_backup_setting: Union[Unset, WindowsPolicyPeriodicallyLogBackupSettings]
        if isinstance(_periodically_backup_setting, Unset):
            periodically_backup_setting = UNSET
        else:
            periodically_backup_setting = WindowsPolicyPeriodicallyLogBackupSettings.from_dict(
                _periodically_backup_setting
            )

        windows_oracle_transaction_log_handling_settings = cls(
            credentials=credentials,
            archived_logs_retention_mode=archived_logs_retention_mode,
            backup_life_time_hours=backup_life_time_hours,
            backup_size_threshold_gb=backup_size_threshold_gb,
            backup_logs_periodically=backup_logs_periodically,
            periodically_backup_setting=periodically_backup_setting,
        )

        windows_oracle_transaction_log_handling_settings.additional_properties = d
        return windows_oracle_transaction_log_handling_settings

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
