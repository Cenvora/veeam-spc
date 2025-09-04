from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_backup_job_script_processing_mode import BackupServerBackupJobScriptProcessingMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_linux_script_type_0 import BackupServerBackupJobLinuxScriptType0
    from ..models.backup_server_backup_job_windows_script_type_0 import BackupServerBackupJobWindowsScriptType0


T = TypeVar("T", bound="BackupServerBackupJobScriptSettingsType0")


@_attrs_define
class BackupServerBackupJobScriptSettingsType0:
    """Pre-freeze and post-thaw scripts.

    Attributes:
        script_processing_mode (BackupServerBackupJobScriptProcessingMode): Scenario for scripts execution.
        windows_scripts (Union['BackupServerBackupJobWindowsScriptType0', None, Unset]): Paths to pre-freeze and post-
            thaw scripts for Microsoft Windows VMs.
        linux_scripts (Union['BackupServerBackupJobLinuxScriptType0', None, Unset]): Paths to pre-freeze and post-thaw
            scripts for Linux VMs.
    """

    script_processing_mode: BackupServerBackupJobScriptProcessingMode
    windows_scripts: Union["BackupServerBackupJobWindowsScriptType0", None, Unset] = UNSET
    linux_scripts: Union["BackupServerBackupJobLinuxScriptType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.backup_server_backup_job_linux_script_type_0 import BackupServerBackupJobLinuxScriptType0
        from ..models.backup_server_backup_job_windows_script_type_0 import BackupServerBackupJobWindowsScriptType0

        script_processing_mode = self.script_processing_mode.value

        windows_scripts: Union[None, Unset, dict[str, Any]]
        if isinstance(self.windows_scripts, Unset):
            windows_scripts = UNSET
        elif isinstance(self.windows_scripts, BackupServerBackupJobWindowsScriptType0):
            windows_scripts = self.windows_scripts.to_dict()
        else:
            windows_scripts = self.windows_scripts

        linux_scripts: Union[None, Unset, dict[str, Any]]
        if isinstance(self.linux_scripts, Unset):
            linux_scripts = UNSET
        elif isinstance(self.linux_scripts, BackupServerBackupJobLinuxScriptType0):
            linux_scripts = self.linux_scripts.to_dict()
        else:
            linux_scripts = self.linux_scripts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scriptProcessingMode": script_processing_mode,
            }
        )
        if windows_scripts is not UNSET:
            field_dict["windowsScripts"] = windows_scripts
        if linux_scripts is not UNSET:
            field_dict["linuxScripts"] = linux_scripts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_backup_job_linux_script_type_0 import BackupServerBackupJobLinuxScriptType0
        from ..models.backup_server_backup_job_windows_script_type_0 import BackupServerBackupJobWindowsScriptType0

        d = dict(src_dict)
        script_processing_mode = BackupServerBackupJobScriptProcessingMode(d.pop("scriptProcessingMode"))

        def _parse_windows_scripts(data: object) -> Union["BackupServerBackupJobWindowsScriptType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_windows_script_type_0 = (
                    BackupServerBackupJobWindowsScriptType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_windows_script_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobWindowsScriptType0", None, Unset], data)

        windows_scripts = _parse_windows_scripts(d.pop("windowsScripts", UNSET))

        def _parse_linux_scripts(data: object) -> Union["BackupServerBackupJobLinuxScriptType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_linux_script_type_0 = (
                    BackupServerBackupJobLinuxScriptType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_linux_script_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobLinuxScriptType0", None, Unset], data)

        linux_scripts = _parse_linux_scripts(d.pop("linuxScripts", UNSET))

        backup_server_backup_job_script_settings_type_0 = cls(
            script_processing_mode=script_processing_mode,
            windows_scripts=windows_scripts,
            linux_scripts=linux_scripts,
        )

        backup_server_backup_job_script_settings_type_0.additional_properties = d
        return backup_server_backup_job_script_settings_type_0

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
