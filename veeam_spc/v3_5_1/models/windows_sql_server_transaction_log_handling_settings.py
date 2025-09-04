from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.windows_sql_server_transaction_log_handling_settings_logs_processing_mode import (
    WindowsSqlServerTransactionLogHandlingSettingsLogsProcessingMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.windows_ms_sql_account_settings import WindowsMsSqlAccountSettings
    from ..models.windows_policy_periodically_log_backup_settings import WindowsPolicyPeriodicallyLogBackupSettings


T = TypeVar("T", bound="WindowsSqlServerTransactionLogHandlingSettings")


@_attrs_define
class WindowsSqlServerTransactionLogHandlingSettings:
    """
    Attributes:
        credentials (Union[Unset, WindowsMsSqlAccountSettings]):
        logs_processing_mode (Union[Unset, WindowsSqlServerTransactionLogHandlingSettingsLogsProcessingMode]):
            Transaction log processing mode. Default:
            WindowsSqlServerTransactionLogHandlingSettingsLogsProcessingMode.TRUNCATELOGS.
        periodically_backup_setting (Union[Unset, WindowsPolicyPeriodicallyLogBackupSettings]):
    """

    credentials: Union[Unset, "WindowsMsSqlAccountSettings"] = UNSET
    logs_processing_mode: Union[Unset, WindowsSqlServerTransactionLogHandlingSettingsLogsProcessingMode] = (
        WindowsSqlServerTransactionLogHandlingSettingsLogsProcessingMode.TRUNCATELOGS
    )
    periodically_backup_setting: Union[Unset, "WindowsPolicyPeriodicallyLogBackupSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credentials: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        logs_processing_mode: Union[Unset, str] = UNSET
        if not isinstance(self.logs_processing_mode, Unset):
            logs_processing_mode = self.logs_processing_mode.value

        periodically_backup_setting: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.periodically_backup_setting, Unset):
            periodically_backup_setting = self.periodically_backup_setting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if logs_processing_mode is not UNSET:
            field_dict["logsProcessingMode"] = logs_processing_mode
        if periodically_backup_setting is not UNSET:
            field_dict["periodicallyBackupSetting"] = periodically_backup_setting

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.windows_ms_sql_account_settings import WindowsMsSqlAccountSettings
        from ..models.windows_policy_periodically_log_backup_settings import WindowsPolicyPeriodicallyLogBackupSettings

        d = dict(src_dict)
        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, WindowsMsSqlAccountSettings]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = WindowsMsSqlAccountSettings.from_dict(_credentials)

        _logs_processing_mode = d.pop("logsProcessingMode", UNSET)
        logs_processing_mode: Union[Unset, WindowsSqlServerTransactionLogHandlingSettingsLogsProcessingMode]
        if isinstance(_logs_processing_mode, Unset):
            logs_processing_mode = UNSET
        else:
            logs_processing_mode = WindowsSqlServerTransactionLogHandlingSettingsLogsProcessingMode(
                _logs_processing_mode
            )

        _periodically_backup_setting = d.pop("periodicallyBackupSetting", UNSET)
        periodically_backup_setting: Union[Unset, WindowsPolicyPeriodicallyLogBackupSettings]
        if isinstance(_periodically_backup_setting, Unset):
            periodically_backup_setting = UNSET
        else:
            periodically_backup_setting = WindowsPolicyPeriodicallyLogBackupSettings.from_dict(
                _periodically_backup_setting
            )

        windows_sql_server_transaction_log_handling_settings = cls(
            credentials=credentials,
            logs_processing_mode=logs_processing_mode,
            periodically_backup_setting=periodically_backup_setting,
        )

        windows_sql_server_transaction_log_handling_settings.additional_properties = d
        return windows_sql_server_transaction_log_handling_settings

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
