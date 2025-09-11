from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mac_backup_target_target_type import MacBackupTargetTargetType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mac_backup_server_settings import MacBackupServerSettings
    from ..models.mac_shared_folder_target import MacSharedFolderTarget


T = TypeVar("T", bound="MacBackupTarget")


@_attrs_define
class MacBackupTarget:
    """
    Attributes:
        target_type (MacBackupTargetTargetType): Type of a target location for the created backup.
        local_path (Union[Unset, str]): Path to the folder where backup files must be stored.
            > Required for the `LocalFolder` target location.
        shared_folder (Union[Unset, MacSharedFolderTarget]):
        backup_repository (Union[Unset, MacBackupServerSettings]):
        enable_deleted_files_retention (Union[Unset, bool]): Defines whether the deleted backup files must be removed
            after a specific time period. Default: False.
        remove_deleted_items_data_after (Union[Unset, int]): Number of days for which the deleted backup files are
            stored. Default: 30.
    """

    target_type: MacBackupTargetTargetType
    local_path: Union[Unset, str] = UNSET
    shared_folder: Union[Unset, "MacSharedFolderTarget"] = UNSET
    backup_repository: Union[Unset, "MacBackupServerSettings"] = UNSET
    enable_deleted_files_retention: Union[Unset, bool] = False
    remove_deleted_items_data_after: Union[Unset, int] = 30
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_type = self.target_type.value

        local_path = self.local_path

        shared_folder: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shared_folder, Unset):
            shared_folder = self.shared_folder.to_dict()

        backup_repository: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.backup_repository, Unset):
            backup_repository = self.backup_repository.to_dict()

        enable_deleted_files_retention = self.enable_deleted_files_retention

        remove_deleted_items_data_after = self.remove_deleted_items_data_after

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targetType": target_type,
            }
        )
        if local_path is not UNSET:
            field_dict["localPath"] = local_path
        if shared_folder is not UNSET:
            field_dict["sharedFolder"] = shared_folder
        if backup_repository is not UNSET:
            field_dict["backupRepository"] = backup_repository
        if enable_deleted_files_retention is not UNSET:
            field_dict["enableDeletedFilesRetention"] = enable_deleted_files_retention
        if remove_deleted_items_data_after is not UNSET:
            field_dict["removeDeletedItemsDataAfter"] = remove_deleted_items_data_after

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mac_backup_server_settings import MacBackupServerSettings
        from ..models.mac_shared_folder_target import MacSharedFolderTarget

        d = dict(src_dict)
        target_type = MacBackupTargetTargetType(d.pop("targetType"))

        local_path = d.pop("localPath", UNSET)

        _shared_folder = d.pop("sharedFolder", UNSET)
        shared_folder: Union[Unset, MacSharedFolderTarget]
        if isinstance(_shared_folder, Unset):
            shared_folder = UNSET
        else:
            shared_folder = MacSharedFolderTarget.from_dict(_shared_folder)

        _backup_repository = d.pop("backupRepository", UNSET)
        backup_repository: Union[Unset, MacBackupServerSettings]
        if isinstance(_backup_repository, Unset):
            backup_repository = UNSET
        else:
            backup_repository = MacBackupServerSettings.from_dict(_backup_repository)

        enable_deleted_files_retention = d.pop("enableDeletedFilesRetention", UNSET)

        remove_deleted_items_data_after = d.pop("removeDeletedItemsDataAfter", UNSET)

        mac_backup_target = cls(
            target_type=target_type,
            local_path=local_path,
            shared_folder=shared_folder,
            backup_repository=backup_repository,
            enable_deleted_files_retention=enable_deleted_files_retention,
            remove_deleted_items_data_after=remove_deleted_items_data_after,
        )

        mac_backup_target.additional_properties = d
        return mac_backup_target

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
