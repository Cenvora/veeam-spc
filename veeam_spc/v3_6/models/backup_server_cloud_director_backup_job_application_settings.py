from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_application_settings_vss import BackupServerApplicationSettingsVSS
from ..models.backup_server_transaction_logs_settings import BackupServerTransactionLogsSettings
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_backup_fs_exclusions import BackupServerBackupJobBackupFSExclusions
    from ..models.backup_server_backup_job_oracle_settings import BackupServerBackupJobOracleSettings
    from ..models.backup_server_backup_job_script_settings import BackupServerBackupJobScriptSettings
    from ..models.backup_server_backup_job_sql_settings import BackupServerBackupJobSQLSettings
    from ..models.backup_server_cloud_director_object import BackupServerCloudDirectorObject


T = TypeVar("T", bound="BackupServerCloudDirectorBackupJobApplicationSettings")


@_attrs_define
class BackupServerCloudDirectorBackupJobApplicationSettings:
    """
    Attributes:
        vm_object (BackupServerCloudDirectorObject): VMware Cloud Director object.
        vss (Union[Unset, BackupServerApplicationSettingsVSS]): Behavior scenario for application-aware processing.
        use_persistent_guest_agent (Union[Unset, bool]): Indicates whether persistent guest agents are used on protected
            VMs for application-aware processing. Default: False.
        transaction_logs (Union[Unset, BackupServerTransactionLogsSettings]): Indicates whether Veeam Backup &
            Replication must process application logs or create copy-only backups.
        sql (Union[Unset, BackupServerBackupJobSQLSettings]): Microsoft SQL Server transaction log settings.
        oracle (Union[Unset, BackupServerBackupJobOracleSettings]): Oracle archived log settings.
        exclusions (Union[Unset, BackupServerBackupJobBackupFSExclusions]): VM guest OS file exclusion.
        scripts (Union[Unset, BackupServerBackupJobScriptSettings]): Pre-freeze and post-thaw scripts.
    """

    vm_object: "BackupServerCloudDirectorObject"
    vss: Union[Unset, BackupServerApplicationSettingsVSS] = UNSET
    use_persistent_guest_agent: Union[Unset, bool] = False
    transaction_logs: Union[Unset, BackupServerTransactionLogsSettings] = UNSET
    sql: Union[Unset, "BackupServerBackupJobSQLSettings"] = UNSET
    oracle: Union[Unset, "BackupServerBackupJobOracleSettings"] = UNSET
    exclusions: Union[Unset, "BackupServerBackupJobBackupFSExclusions"] = UNSET
    scripts: Union[Unset, "BackupServerBackupJobScriptSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vm_object = self.vm_object.to_dict()

        vss: Union[Unset, str] = UNSET
        if not isinstance(self.vss, Unset):
            vss = self.vss.value

        use_persistent_guest_agent = self.use_persistent_guest_agent

        transaction_logs: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_logs, Unset):
            transaction_logs = self.transaction_logs.value

        sql: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sql, Unset):
            sql = self.sql.to_dict()

        oracle: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.oracle, Unset):
            oracle = self.oracle.to_dict()

        exclusions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.exclusions, Unset):
            exclusions = self.exclusions.to_dict()

        scripts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.scripts, Unset):
            scripts = self.scripts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vmObject": vm_object,
            }
        )
        if vss is not UNSET:
            field_dict["vss"] = vss
        if use_persistent_guest_agent is not UNSET:
            field_dict["usePersistentGuestAgent"] = use_persistent_guest_agent
        if transaction_logs is not UNSET:
            field_dict["transactionLogs"] = transaction_logs
        if sql is not UNSET:
            field_dict["sql"] = sql
        if oracle is not UNSET:
            field_dict["oracle"] = oracle
        if exclusions is not UNSET:
            field_dict["exclusions"] = exclusions
        if scripts is not UNSET:
            field_dict["scripts"] = scripts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_backup_job_backup_fs_exclusions import BackupServerBackupJobBackupFSExclusions
        from ..models.backup_server_backup_job_oracle_settings import BackupServerBackupJobOracleSettings
        from ..models.backup_server_backup_job_script_settings import BackupServerBackupJobScriptSettings
        from ..models.backup_server_backup_job_sql_settings import BackupServerBackupJobSQLSettings
        from ..models.backup_server_cloud_director_object import BackupServerCloudDirectorObject

        d = dict(src_dict)
        vm_object = BackupServerCloudDirectorObject.from_dict(d.pop("vmObject"))

        _vss = d.pop("vss", UNSET)
        vss: Union[Unset, BackupServerApplicationSettingsVSS]
        if isinstance(_vss, Unset):
            vss = UNSET
        else:
            vss = BackupServerApplicationSettingsVSS(_vss)

        use_persistent_guest_agent = d.pop("usePersistentGuestAgent", UNSET)

        _transaction_logs = d.pop("transactionLogs", UNSET)
        transaction_logs: Union[Unset, BackupServerTransactionLogsSettings]
        if isinstance(_transaction_logs, Unset):
            transaction_logs = UNSET
        else:
            transaction_logs = BackupServerTransactionLogsSettings(_transaction_logs)

        _sql = d.pop("sql", UNSET)
        sql: Union[Unset, BackupServerBackupJobSQLSettings]
        if isinstance(_sql, Unset):
            sql = UNSET
        else:
            sql = BackupServerBackupJobSQLSettings.from_dict(_sql)

        _oracle = d.pop("oracle", UNSET)
        oracle: Union[Unset, BackupServerBackupJobOracleSettings]
        if isinstance(_oracle, Unset):
            oracle = UNSET
        else:
            oracle = BackupServerBackupJobOracleSettings.from_dict(_oracle)

        _exclusions = d.pop("exclusions", UNSET)
        exclusions: Union[Unset, BackupServerBackupJobBackupFSExclusions]
        if isinstance(_exclusions, Unset):
            exclusions = UNSET
        else:
            exclusions = BackupServerBackupJobBackupFSExclusions.from_dict(_exclusions)

        _scripts = d.pop("scripts", UNSET)
        scripts: Union[Unset, BackupServerBackupJobScriptSettings]
        if isinstance(_scripts, Unset):
            scripts = UNSET
        else:
            scripts = BackupServerBackupJobScriptSettings.from_dict(_scripts)

        backup_server_cloud_director_backup_job_application_settings = cls(
            vm_object=vm_object,
            vss=vss,
            use_persistent_guest_agent=use_persistent_guest_agent,
            transaction_logs=transaction_logs,
            sql=sql,
            oracle=oracle,
            exclusions=exclusions,
            scripts=scripts,
        )

        backup_server_cloud_director_backup_job_application_settings.additional_properties = d
        return backup_server_cloud_director_backup_job_application_settings

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
