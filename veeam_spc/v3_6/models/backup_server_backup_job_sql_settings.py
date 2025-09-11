from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_backup_job_retain_log_backups_type import BackupServerBackupJobRetainLogBackupsType
from ..models.backup_server_sql_logs_processing import BackupServerSQLLogsProcessing
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_log_shipping_servers import BackupServerBackupJobLogShippingServers


T = TypeVar("T", bound="BackupServerBackupJobSQLSettings")


@_attrs_define
class BackupServerBackupJobSQLSettings:
    """Microsoft SQL Server transaction log settings.

    Attributes:
        logs_processing (BackupServerSQLLogsProcessing): Type of transaction log processing.
        backup_minutes_count (Union[Unset, int]): Frequency of transaction log backup, in minutes. Default: 15.
        retain_log_backups (Union[Unset, BackupServerBackupJobRetainLogBackupsType]): Type of log retention policy.
        keep_days_count (Union[Unset, int]): Number of days to keep transaction logs. Default: 15.
        log_shipping_servers (Union[Unset, BackupServerBackupJobLogShippingServers]): Log shipping servers used to
            transport transaction logs.
    """

    logs_processing: BackupServerSQLLogsProcessing
    backup_minutes_count: Union[Unset, int] = 15
    retain_log_backups: Union[Unset, BackupServerBackupJobRetainLogBackupsType] = UNSET
    keep_days_count: Union[Unset, int] = 15
    log_shipping_servers: Union[Unset, "BackupServerBackupJobLogShippingServers"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logs_processing = self.logs_processing.value

        backup_minutes_count = self.backup_minutes_count

        retain_log_backups: Union[Unset, str] = UNSET
        if not isinstance(self.retain_log_backups, Unset):
            retain_log_backups = self.retain_log_backups.value

        keep_days_count = self.keep_days_count

        log_shipping_servers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.log_shipping_servers, Unset):
            log_shipping_servers = self.log_shipping_servers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "logsProcessing": logs_processing,
            }
        )
        if backup_minutes_count is not UNSET:
            field_dict["backupMinutesCount"] = backup_minutes_count
        if retain_log_backups is not UNSET:
            field_dict["retainLogBackups"] = retain_log_backups
        if keep_days_count is not UNSET:
            field_dict["keepDaysCount"] = keep_days_count
        if log_shipping_servers is not UNSET:
            field_dict["logShippingServers"] = log_shipping_servers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_backup_job_log_shipping_servers import BackupServerBackupJobLogShippingServers

        d = dict(src_dict)
        logs_processing = BackupServerSQLLogsProcessing(d.pop("logsProcessing"))

        backup_minutes_count = d.pop("backupMinutesCount", UNSET)

        _retain_log_backups = d.pop("retainLogBackups", UNSET)
        retain_log_backups: Union[Unset, BackupServerBackupJobRetainLogBackupsType]
        if isinstance(_retain_log_backups, Unset):
            retain_log_backups = UNSET
        else:
            retain_log_backups = BackupServerBackupJobRetainLogBackupsType(_retain_log_backups)

        keep_days_count = d.pop("keepDaysCount", UNSET)

        _log_shipping_servers = d.pop("logShippingServers", UNSET)
        log_shipping_servers: Union[Unset, BackupServerBackupJobLogShippingServers]
        if isinstance(_log_shipping_servers, Unset):
            log_shipping_servers = UNSET
        else:
            log_shipping_servers = BackupServerBackupJobLogShippingServers.from_dict(_log_shipping_servers)

        backup_server_backup_job_sql_settings = cls(
            logs_processing=logs_processing,
            backup_minutes_count=backup_minutes_count,
            retain_log_backups=retain_log_backups,
            keep_days_count=keep_days_count,
            log_shipping_servers=log_shipping_servers,
        )

        backup_server_backup_job_sql_settings.additional_properties = d
        return backup_server_backup_job_sql_settings

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
