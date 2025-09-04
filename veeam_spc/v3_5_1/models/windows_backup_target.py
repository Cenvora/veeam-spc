from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.windows_backup_target_target_type import WindowsBackupTargetTargetType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.windows_backup_repository_target import WindowsBackupRepositoryTarget
    from ..models.windows_cloud_repository_target import WindowsCloudRepositoryTarget
    from ..models.windows_shared_folder_target import WindowsSharedFolderTarget


T = TypeVar("T", bound="WindowsBackupTarget")


@_attrs_define
class WindowsBackupTarget:
    """
    Attributes:
        target_type (WindowsBackupTargetTargetType): Target location for the created backup.
            > To store entire computer backups on the `LocalFolder` target location, you must use an external drive.
            > The `OneDrive` and `ObjectStorage` target locations cannot be assigned using RESTful API.
        local_path (Union[None, Unset, str]): Path to the folder where backup files must be stored.
            > Required for the `LocalFolder` target location.
        shared_folder (Union[Unset, WindowsSharedFolderTarget]):
        backup_repository (Union[Unset, WindowsBackupRepositoryTarget]):
        cloud_repository (Union[Unset, WindowsCloudRepositoryTarget]):
    """

    target_type: WindowsBackupTargetTargetType
    local_path: Union[None, Unset, str] = UNSET
    shared_folder: Union[Unset, "WindowsSharedFolderTarget"] = UNSET
    backup_repository: Union[Unset, "WindowsBackupRepositoryTarget"] = UNSET
    cloud_repository: Union[Unset, "WindowsCloudRepositoryTarget"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_type = self.target_type.value

        local_path: Union[None, Unset, str]
        if isinstance(self.local_path, Unset):
            local_path = UNSET
        else:
            local_path = self.local_path

        shared_folder: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shared_folder, Unset):
            shared_folder = self.shared_folder.to_dict()

        backup_repository: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.backup_repository, Unset):
            backup_repository = self.backup_repository.to_dict()

        cloud_repository: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cloud_repository, Unset):
            cloud_repository = self.cloud_repository.to_dict()

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
        if cloud_repository is not UNSET:
            field_dict["cloudRepository"] = cloud_repository

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.windows_backup_repository_target import WindowsBackupRepositoryTarget
        from ..models.windows_cloud_repository_target import WindowsCloudRepositoryTarget
        from ..models.windows_shared_folder_target import WindowsSharedFolderTarget

        d = dict(src_dict)
        target_type = WindowsBackupTargetTargetType(d.pop("targetType"))

        def _parse_local_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        local_path = _parse_local_path(d.pop("localPath", UNSET))

        _shared_folder = d.pop("sharedFolder", UNSET)
        shared_folder: Union[Unset, WindowsSharedFolderTarget]
        if isinstance(_shared_folder, Unset):
            shared_folder = UNSET
        else:
            shared_folder = WindowsSharedFolderTarget.from_dict(_shared_folder)

        _backup_repository = d.pop("backupRepository", UNSET)
        backup_repository: Union[Unset, WindowsBackupRepositoryTarget]
        if isinstance(_backup_repository, Unset):
            backup_repository = UNSET
        else:
            backup_repository = WindowsBackupRepositoryTarget.from_dict(_backup_repository)

        _cloud_repository = d.pop("cloudRepository", UNSET)
        cloud_repository: Union[Unset, WindowsCloudRepositoryTarget]
        if isinstance(_cloud_repository, Unset):
            cloud_repository = UNSET
        else:
            cloud_repository = WindowsCloudRepositoryTarget.from_dict(_cloud_repository)

        windows_backup_target = cls(
            target_type=target_type,
            local_path=local_path,
            shared_folder=shared_folder,
            backup_repository=backup_repository,
            cloud_repository=cloud_repository,
        )

        windows_backup_target.additional_properties = d
        return windows_backup_target

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
