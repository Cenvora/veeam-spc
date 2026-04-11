from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_application_settings_vss import BackupServerApplicationSettingsVSS
from ..models.backup_server_transaction_logs_settings import BackupServerTransactionLogsSettings
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_backup_fs_exclusions_type_0 import (
        BackupServerBackupJobBackupFSExclusionsType0,
    )
    from ..models.backup_server_backup_job_oracle_settings_type_0 import BackupServerBackupJobOracleSettingsType0
    from ..models.backup_server_backup_job_script_settings_type_0 import BackupServerBackupJobScriptSettingsType0
    from ..models.backup_server_backup_job_sql_settings_type_0 import BackupServerBackupJobSQLSettingsType0
    from ..models.backup_server_vmware_object import BackupServerVmwareObject


T = TypeVar("T", bound="BackupServerBackupJobApplicationSettingsType0")


@_attrs_define
class BackupServerBackupJobApplicationSettingsType0:
    """
    Attributes:
        vm_object (BackupServerVmwareObject): VMware vSphere object.
        vss (BackupServerApplicationSettingsVSS | Unset): Behavior scenario for application-aware processing.
        use_persistent_guest_agent (bool | Unset): Indicates whether persistent guest agents are used on protected VMs
            for application-aware processing. Default: False.
        transaction_logs (BackupServerTransactionLogsSettings | Unset): Indicates whether Veeam Backup & Replication
            must process application logs or create copy-only backups.
        sql (BackupServerBackupJobSQLSettingsType0 | None | Unset): Microsoft SQL Server transaction log settings.
        oracle (BackupServerBackupJobOracleSettingsType0 | None | Unset): Oracle archived log settings.
        exclusions (BackupServerBackupJobBackupFSExclusionsType0 | None | Unset): VM guest OS file exclusion.
        scripts (BackupServerBackupJobScriptSettingsType0 | None | Unset): Pre-freeze and post-thaw scripts.
    """

    vm_object: BackupServerVmwareObject
    vss: BackupServerApplicationSettingsVSS | Unset = UNSET
    use_persistent_guest_agent: bool | Unset = False
    transaction_logs: BackupServerTransactionLogsSettings | Unset = UNSET
    sql: BackupServerBackupJobSQLSettingsType0 | None | Unset = UNSET
    oracle: BackupServerBackupJobOracleSettingsType0 | None | Unset = UNSET
    exclusions: BackupServerBackupJobBackupFSExclusionsType0 | None | Unset = UNSET
    scripts: BackupServerBackupJobScriptSettingsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.backup_server_backup_job_backup_fs_exclusions_type_0 import (
            BackupServerBackupJobBackupFSExclusionsType0,
        )
        from ..models.backup_server_backup_job_oracle_settings_type_0 import BackupServerBackupJobOracleSettingsType0
        from ..models.backup_server_backup_job_script_settings_type_0 import BackupServerBackupJobScriptSettingsType0
        from ..models.backup_server_backup_job_sql_settings_type_0 import BackupServerBackupJobSQLSettingsType0

        vm_object = self.vm_object.to_dict()

        vss: str | Unset = UNSET
        if not isinstance(self.vss, Unset):
            vss = self.vss.value

        use_persistent_guest_agent = self.use_persistent_guest_agent

        transaction_logs: str | Unset = UNSET
        if not isinstance(self.transaction_logs, Unset):
            transaction_logs = self.transaction_logs.value

        sql: dict[str, Any] | None | Unset
        if isinstance(self.sql, Unset):
            sql = UNSET
        elif isinstance(self.sql, BackupServerBackupJobSQLSettingsType0):
            sql = self.sql.to_dict()
        else:
            sql = self.sql

        oracle: dict[str, Any] | None | Unset
        if isinstance(self.oracle, Unset):
            oracle = UNSET
        elif isinstance(self.oracle, BackupServerBackupJobOracleSettingsType0):
            oracle = self.oracle.to_dict()
        else:
            oracle = self.oracle

        exclusions: dict[str, Any] | None | Unset
        if isinstance(self.exclusions, Unset):
            exclusions = UNSET
        elif isinstance(self.exclusions, BackupServerBackupJobBackupFSExclusionsType0):
            exclusions = self.exclusions.to_dict()
        else:
            exclusions = self.exclusions

        scripts: dict[str, Any] | None | Unset
        if isinstance(self.scripts, Unset):
            scripts = UNSET
        elif isinstance(self.scripts, BackupServerBackupJobScriptSettingsType0):
            scripts = self.scripts.to_dict()
        else:
            scripts = self.scripts

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
        from ..models.backup_server_backup_job_backup_fs_exclusions_type_0 import (
            BackupServerBackupJobBackupFSExclusionsType0,
        )
        from ..models.backup_server_backup_job_oracle_settings_type_0 import BackupServerBackupJobOracleSettingsType0
        from ..models.backup_server_backup_job_script_settings_type_0 import BackupServerBackupJobScriptSettingsType0
        from ..models.backup_server_backup_job_sql_settings_type_0 import BackupServerBackupJobSQLSettingsType0
        from ..models.backup_server_vmware_object import BackupServerVmwareObject

        d = dict(src_dict)
        vm_object = BackupServerVmwareObject.from_dict(d.pop("vmObject"))

        _vss = d.pop("vss", UNSET)
        vss: BackupServerApplicationSettingsVSS | Unset
        if isinstance(_vss, Unset):
            vss = UNSET
        else:
            vss = BackupServerApplicationSettingsVSS(_vss)

        use_persistent_guest_agent = d.pop("usePersistentGuestAgent", UNSET)

        _transaction_logs = d.pop("transactionLogs", UNSET)
        transaction_logs: BackupServerTransactionLogsSettings | Unset
        if isinstance(_transaction_logs, Unset):
            transaction_logs = UNSET
        else:
            transaction_logs = BackupServerTransactionLogsSettings(_transaction_logs)

        def _parse_sql(data: object) -> BackupServerBackupJobSQLSettingsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_sql_settings_type_0 = (
                    BackupServerBackupJobSQLSettingsType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_sql_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BackupServerBackupJobSQLSettingsType0 | None | Unset, data)

        sql = _parse_sql(d.pop("sql", UNSET))

        def _parse_oracle(data: object) -> BackupServerBackupJobOracleSettingsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_oracle_settings_type_0 = (
                    BackupServerBackupJobOracleSettingsType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_oracle_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BackupServerBackupJobOracleSettingsType0 | None | Unset, data)

        oracle = _parse_oracle(d.pop("oracle", UNSET))

        def _parse_exclusions(data: object) -> BackupServerBackupJobBackupFSExclusionsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_backup_fs_exclusions_type_0 = (
                    BackupServerBackupJobBackupFSExclusionsType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_backup_fs_exclusions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BackupServerBackupJobBackupFSExclusionsType0 | None | Unset, data)

        exclusions = _parse_exclusions(d.pop("exclusions", UNSET))

        def _parse_scripts(data: object) -> BackupServerBackupJobScriptSettingsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_script_settings_type_0 = (
                    BackupServerBackupJobScriptSettingsType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_script_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BackupServerBackupJobScriptSettingsType0 | None | Unset, data)

        scripts = _parse_scripts(d.pop("scripts", UNSET))

        backup_server_backup_job_application_settings_type_0 = cls(
            vm_object=vm_object,
            vss=vss,
            use_persistent_guest_agent=use_persistent_guest_agent,
            transaction_logs=transaction_logs,
            sql=sql,
            oracle=oracle,
            exclusions=exclusions,
            scripts=scripts,
        )

        backup_server_backup_job_application_settings_type_0.additional_properties = d
        return backup_server_backup_job_application_settings_type_0

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
