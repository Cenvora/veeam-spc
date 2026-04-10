from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.windows_application_aware_processing_settings_transaction_log_processing_mode import (
    WindowsApplicationAwareProcessingSettingsTransactionLogProcessingMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.share_point_account_settings import SharePointAccountSettings
    from ..models.windows_job_script_settings import WindowsJobScriptSettings
    from ..models.windows_oracle_transaction_log_handling_settings import WindowsOracleTransactionLogHandlingSettings
    from ..models.windows_sql_server_transaction_log_handling_settings import (
        WindowsSqlServerTransactionLogHandlingSettings,
    )


T = TypeVar("T", bound="WindowsApplicationAwareProcessingSettings")


@_attrs_define
class WindowsApplicationAwareProcessingSettings:
    """
    Attributes:
        enabled (Union[Unset, bool]): Indicates whether the application-aware processing is enabled. Default: False.
        transaction_log_processing_mode (Union[Unset,
            WindowsApplicationAwareProcessingSettingsTransactionLogProcessingMode]): Application-aware processing type.
            Default: WindowsApplicationAwareProcessingSettingsTransactionLogProcessingMode.PROCESSTRANSACTIONLOGSWITHJOB.
        sql_server_transaction_log_handling_settings (Union[Unset, WindowsSqlServerTransactionLogHandlingSettings]):
        oracle_transaction_log_handling_settings (Union[Unset, WindowsOracleTransactionLogHandlingSettings]):
        share_point_account_settings (Union[Unset, SharePointAccountSettings]):
        script_settings (Union[Unset, WindowsJobScriptSettings]):
    """

    enabled: Union[Unset, bool] = False
    transaction_log_processing_mode: Union[
        Unset, WindowsApplicationAwareProcessingSettingsTransactionLogProcessingMode
    ] = WindowsApplicationAwareProcessingSettingsTransactionLogProcessingMode.PROCESSTRANSACTIONLOGSWITHJOB
    sql_server_transaction_log_handling_settings: Union[Unset, "WindowsSqlServerTransactionLogHandlingSettings"] = UNSET
    oracle_transaction_log_handling_settings: Union[Unset, "WindowsOracleTransactionLogHandlingSettings"] = UNSET
    share_point_account_settings: Union[Unset, "SharePointAccountSettings"] = UNSET
    script_settings: Union[Unset, "WindowsJobScriptSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        transaction_log_processing_mode: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_log_processing_mode, Unset):
            transaction_log_processing_mode = self.transaction_log_processing_mode.value

        sql_server_transaction_log_handling_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sql_server_transaction_log_handling_settings, Unset):
            sql_server_transaction_log_handling_settings = self.sql_server_transaction_log_handling_settings.to_dict()

        oracle_transaction_log_handling_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.oracle_transaction_log_handling_settings, Unset):
            oracle_transaction_log_handling_settings = self.oracle_transaction_log_handling_settings.to_dict()

        share_point_account_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.share_point_account_settings, Unset):
            share_point_account_settings = self.share_point_account_settings.to_dict()

        script_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.script_settings, Unset):
            script_settings = self.script_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if transaction_log_processing_mode is not UNSET:
            field_dict["transactionLogProcessingMode"] = transaction_log_processing_mode
        if sql_server_transaction_log_handling_settings is not UNSET:
            field_dict["sqlServerTransactionLogHandlingSettings"] = sql_server_transaction_log_handling_settings
        if oracle_transaction_log_handling_settings is not UNSET:
            field_dict["oracleTransactionLogHandlingSettings"] = oracle_transaction_log_handling_settings
        if share_point_account_settings is not UNSET:
            field_dict["sharePointAccountSettings"] = share_point_account_settings
        if script_settings is not UNSET:
            field_dict["scriptSettings"] = script_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.share_point_account_settings import SharePointAccountSettings
        from ..models.windows_job_script_settings import WindowsJobScriptSettings
        from ..models.windows_oracle_transaction_log_handling_settings import (
            WindowsOracleTransactionLogHandlingSettings,
        )
        from ..models.windows_sql_server_transaction_log_handling_settings import (
            WindowsSqlServerTransactionLogHandlingSettings,
        )

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        _transaction_log_processing_mode = d.pop("transactionLogProcessingMode", UNSET)
        transaction_log_processing_mode: Union[
            Unset, WindowsApplicationAwareProcessingSettingsTransactionLogProcessingMode
        ]
        if isinstance(_transaction_log_processing_mode, Unset):
            transaction_log_processing_mode = UNSET
        else:
            transaction_log_processing_mode = WindowsApplicationAwareProcessingSettingsTransactionLogProcessingMode(
                _transaction_log_processing_mode
            )

        _sql_server_transaction_log_handling_settings = d.pop("sqlServerTransactionLogHandlingSettings", UNSET)
        sql_server_transaction_log_handling_settings: Union[Unset, WindowsSqlServerTransactionLogHandlingSettings]
        if isinstance(_sql_server_transaction_log_handling_settings, Unset):
            sql_server_transaction_log_handling_settings = UNSET
        else:
            sql_server_transaction_log_handling_settings = WindowsSqlServerTransactionLogHandlingSettings.from_dict(
                _sql_server_transaction_log_handling_settings
            )

        _oracle_transaction_log_handling_settings = d.pop("oracleTransactionLogHandlingSettings", UNSET)
        oracle_transaction_log_handling_settings: Union[Unset, WindowsOracleTransactionLogHandlingSettings]
        if isinstance(_oracle_transaction_log_handling_settings, Unset):
            oracle_transaction_log_handling_settings = UNSET
        else:
            oracle_transaction_log_handling_settings = WindowsOracleTransactionLogHandlingSettings.from_dict(
                _oracle_transaction_log_handling_settings
            )

        _share_point_account_settings = d.pop("sharePointAccountSettings", UNSET)
        share_point_account_settings: Union[Unset, SharePointAccountSettings]
        if isinstance(_share_point_account_settings, Unset):
            share_point_account_settings = UNSET
        else:
            share_point_account_settings = SharePointAccountSettings.from_dict(_share_point_account_settings)

        _script_settings = d.pop("scriptSettings", UNSET)
        script_settings: Union[Unset, WindowsJobScriptSettings]
        if isinstance(_script_settings, Unset):
            script_settings = UNSET
        else:
            script_settings = WindowsJobScriptSettings.from_dict(_script_settings)

        windows_application_aware_processing_settings = cls(
            enabled=enabled,
            transaction_log_processing_mode=transaction_log_processing_mode,
            sql_server_transaction_log_handling_settings=sql_server_transaction_log_handling_settings,
            oracle_transaction_log_handling_settings=oracle_transaction_log_handling_settings,
            share_point_account_settings=share_point_account_settings,
            script_settings=script_settings,
        )

        windows_application_aware_processing_settings.additional_properties = d
        return windows_application_aware_processing_settings

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
