from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_agent_job_source_backup_mode import BackupServerAgentJobSourceBackupMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_agent_job_source_file_system_items import BackupServerAgentJobSourceFileSystemItems


T = TypeVar("T", bound="BackupServerAgentJobSource")


@_attrs_define
class BackupServerAgentJobSource:
    """
    Attributes:
        backup_mode (Union[Unset, BackupServerAgentJobSourceBackupMode]): Backup mode.
        backup_user_folders (Union[Unset, bool]): Indicates whether a backup job protects individual folders.
        backup_operating_system (Union[Unset, bool]): Indicates whether agent operating system is included in a backup
            scope.
        file_system_items (Union[Unset, BackupServerAgentJobSourceFileSystemItems]): Files and folders of an agent
            computer are included in a backup scope.
    """

    backup_mode: Union[Unset, BackupServerAgentJobSourceBackupMode] = UNSET
    backup_user_folders: Union[Unset, bool] = UNSET
    backup_operating_system: Union[Unset, bool] = UNSET
    file_system_items: Union[Unset, "BackupServerAgentJobSourceFileSystemItems"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_mode: Union[Unset, str] = UNSET
        if not isinstance(self.backup_mode, Unset):
            backup_mode = self.backup_mode.value

        backup_user_folders = self.backup_user_folders

        backup_operating_system = self.backup_operating_system

        file_system_items: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.file_system_items, Unset):
            file_system_items = self.file_system_items.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_mode is not UNSET:
            field_dict["backupMode"] = backup_mode
        if backup_user_folders is not UNSET:
            field_dict["backupUserFolders"] = backup_user_folders
        if backup_operating_system is not UNSET:
            field_dict["backupOperatingSystem"] = backup_operating_system
        if file_system_items is not UNSET:
            field_dict["fileSystemItems"] = file_system_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_agent_job_source_file_system_items import BackupServerAgentJobSourceFileSystemItems

        d = dict(src_dict)
        _backup_mode = d.pop("backupMode", UNSET)
        backup_mode: Union[Unset, BackupServerAgentJobSourceBackupMode]
        if isinstance(_backup_mode, Unset):
            backup_mode = UNSET
        else:
            backup_mode = BackupServerAgentJobSourceBackupMode(_backup_mode)

        backup_user_folders = d.pop("backupUserFolders", UNSET)

        backup_operating_system = d.pop("backupOperatingSystem", UNSET)

        _file_system_items = d.pop("fileSystemItems", UNSET)
        file_system_items: Union[Unset, BackupServerAgentJobSourceFileSystemItems]
        if isinstance(_file_system_items, Unset):
            file_system_items = UNSET
        else:
            file_system_items = BackupServerAgentJobSourceFileSystemItems.from_dict(_file_system_items)

        backup_server_agent_job_source = cls(
            backup_mode=backup_mode,
            backup_user_folders=backup_user_folders,
            backup_operating_system=backup_operating_system,
            file_system_items=file_system_items,
        )

        backup_server_agent_job_source.additional_properties = d
        return backup_server_agent_job_source

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
