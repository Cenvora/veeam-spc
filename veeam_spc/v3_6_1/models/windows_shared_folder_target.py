from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_cache_settings import BackupCacheSettings
    from ..models.windows_policy_target_credentials import WindowsPolicyTargetCredentials


T = TypeVar("T", bound="WindowsSharedFolderTarget")


@_attrs_define
class WindowsSharedFolderTarget:
    r"""
    Attributes:
        path (str): UNC name of the network shared folder in which you want to store backup files. The UNC name must
            start with two back slashes (\\).
        credentials (Union[Unset, WindowsPolicyTargetCredentials]):
        backup_cache_settings (Union[Unset, BackupCacheSettings]):
    """

    path: str
    credentials: Union[Unset, "WindowsPolicyTargetCredentials"] = UNSET
    backup_cache_settings: Union[Unset, "BackupCacheSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        credentials: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        backup_cache_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.backup_cache_settings, Unset):
            backup_cache_settings = self.backup_cache_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
            }
        )
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if backup_cache_settings is not UNSET:
            field_dict["backupCacheSettings"] = backup_cache_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_cache_settings import BackupCacheSettings
        from ..models.windows_policy_target_credentials import WindowsPolicyTargetCredentials

        d = dict(src_dict)
        path = d.pop("path")

        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, WindowsPolicyTargetCredentials]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = WindowsPolicyTargetCredentials.from_dict(_credentials)

        _backup_cache_settings = d.pop("backupCacheSettings", UNSET)
        backup_cache_settings: Union[Unset, BackupCacheSettings]
        if isinstance(_backup_cache_settings, Unset):
            backup_cache_settings = UNSET
        else:
            backup_cache_settings = BackupCacheSettings.from_dict(_backup_cache_settings)

        windows_shared_folder_target = cls(
            path=path,
            credentials=credentials,
            backup_cache_settings=backup_cache_settings,
        )

        windows_shared_folder_target.additional_properties = d
        return windows_shared_folder_target

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
