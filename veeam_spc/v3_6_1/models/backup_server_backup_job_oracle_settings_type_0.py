from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_backup_job_backup_oracle_logs_settings import BackupServerBackupJobBackupOracleLogsSettings
from ..models.backup_server_backup_job_retain_log_backups_type import BackupServerBackupJobRetainLogBackupsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_log_shipping_servers_type_0 import (
        BackupServerBackupJobLogShippingServersType0,
    )


T = TypeVar("T", bound="BackupServerBackupJobOracleSettingsType0")


@_attrs_define
class BackupServerBackupJobOracleSettingsType0:
    """Oracle archived log settings.

    Attributes:
        use_guest_credentials (bool): Indicates whether Veeam Backup & Replication uses credentials specified in the
            guest processing settings to access Oracle database.
        archive_logs (BackupServerBackupJobBackupOracleLogsSettings): Type of archived log processing.
        credentials_id (Union[None, UUID, Unset]): UID assigned to a credentials record that is used to access Oracle
            database in case the `useGuestCredentials` property has the `false` value.
        delete_hours_count (Union[Unset, int]): Time period during which archived logs must be kept, in hours.
            >Required if the `archiveLogs` property has the `deleteExpiredHours` value.
             Default: 24.
        delete_g_bs_count (Union[Unset, int]): Archive log size threshold, in GB.
            >Required if the `archiveLogs` praperty has the `deleteExpiredGBs` value.
             Default: 15.
        backup_logs (Union[Unset, bool]): Indicates whether archived logs must be backed up. Default: False.
        backup_minutes_count (Union[Unset, int]): Frequency of archived log backup, in minutes. Default: 15.
        retain_log_backups (Union[Unset, BackupServerBackupJobRetainLogBackupsType]): Type of log retention policy.
        keep_days_count (Union[Unset, int]): Number of days during which archived log backups must be stored. Default:
            15.
        log_shipping_servers (Union['BackupServerBackupJobLogShippingServersType0', None, Unset]): Log shipping servers
            used to transport transaction logs.
    """

    use_guest_credentials: bool
    archive_logs: BackupServerBackupJobBackupOracleLogsSettings
    credentials_id: Union[None, UUID, Unset] = UNSET
    delete_hours_count: Union[Unset, int] = 24
    delete_g_bs_count: Union[Unset, int] = 15
    backup_logs: Union[Unset, bool] = False
    backup_minutes_count: Union[Unset, int] = 15
    retain_log_backups: Union[Unset, BackupServerBackupJobRetainLogBackupsType] = UNSET
    keep_days_count: Union[Unset, int] = 15
    log_shipping_servers: Union["BackupServerBackupJobLogShippingServersType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.backup_server_backup_job_log_shipping_servers_type_0 import (
            BackupServerBackupJobLogShippingServersType0,
        )

        use_guest_credentials = self.use_guest_credentials

        archive_logs = self.archive_logs.value

        credentials_id: Union[None, Unset, str]
        if isinstance(self.credentials_id, Unset):
            credentials_id = UNSET
        elif isinstance(self.credentials_id, UUID):
            credentials_id = str(self.credentials_id)
        else:
            credentials_id = self.credentials_id

        delete_hours_count = self.delete_hours_count

        delete_g_bs_count = self.delete_g_bs_count

        backup_logs = self.backup_logs

        backup_minutes_count = self.backup_minutes_count

        retain_log_backups: Union[Unset, str] = UNSET
        if not isinstance(self.retain_log_backups, Unset):
            retain_log_backups = self.retain_log_backups.value

        keep_days_count = self.keep_days_count

        log_shipping_servers: Union[None, Unset, dict[str, Any]]
        if isinstance(self.log_shipping_servers, Unset):
            log_shipping_servers = UNSET
        elif isinstance(self.log_shipping_servers, BackupServerBackupJobLogShippingServersType0):
            log_shipping_servers = self.log_shipping_servers.to_dict()
        else:
            log_shipping_servers = self.log_shipping_servers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "useGuestCredentials": use_guest_credentials,
                "archiveLogs": archive_logs,
            }
        )
        if credentials_id is not UNSET:
            field_dict["credentialsId"] = credentials_id
        if delete_hours_count is not UNSET:
            field_dict["deleteHoursCount"] = delete_hours_count
        if delete_g_bs_count is not UNSET:
            field_dict["deleteGBsCount"] = delete_g_bs_count
        if backup_logs is not UNSET:
            field_dict["backupLogs"] = backup_logs
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
        from ..models.backup_server_backup_job_log_shipping_servers_type_0 import (
            BackupServerBackupJobLogShippingServersType0,
        )

        d = dict(src_dict)
        use_guest_credentials = d.pop("useGuestCredentials")

        archive_logs = BackupServerBackupJobBackupOracleLogsSettings(d.pop("archiveLogs"))

        def _parse_credentials_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                credentials_id_type_0 = UUID(data)

                return credentials_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        credentials_id = _parse_credentials_id(d.pop("credentialsId", UNSET))

        delete_hours_count = d.pop("deleteHoursCount", UNSET)

        delete_g_bs_count = d.pop("deleteGBsCount", UNSET)

        backup_logs = d.pop("backupLogs", UNSET)

        backup_minutes_count = d.pop("backupMinutesCount", UNSET)

        _retain_log_backups = d.pop("retainLogBackups", UNSET)
        retain_log_backups: Union[Unset, BackupServerBackupJobRetainLogBackupsType]
        if isinstance(_retain_log_backups, Unset):
            retain_log_backups = UNSET
        else:
            retain_log_backups = BackupServerBackupJobRetainLogBackupsType(_retain_log_backups)

        keep_days_count = d.pop("keepDaysCount", UNSET)

        def _parse_log_shipping_servers(
            data: object,
        ) -> Union["BackupServerBackupJobLogShippingServersType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_log_shipping_servers_type_0 = (
                    BackupServerBackupJobLogShippingServersType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_log_shipping_servers_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobLogShippingServersType0", None, Unset], data)

        log_shipping_servers = _parse_log_shipping_servers(d.pop("logShippingServers", UNSET))

        backup_server_backup_job_oracle_settings_type_0 = cls(
            use_guest_credentials=use_guest_credentials,
            archive_logs=archive_logs,
            credentials_id=credentials_id,
            delete_hours_count=delete_hours_count,
            delete_g_bs_count=delete_g_bs_count,
            backup_logs=backup_logs,
            backup_minutes_count=backup_minutes_count,
            retain_log_backups=retain_log_backups,
            keep_days_count=keep_days_count,
            log_shipping_servers=log_shipping_servers,
        )

        backup_server_backup_job_oracle_settings_type_0.additional_properties = d
        return backup_server_backup_job_oracle_settings_type_0

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
