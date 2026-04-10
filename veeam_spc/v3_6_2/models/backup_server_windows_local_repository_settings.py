from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_repository_advanced_settings import BackupServerRepositoryAdvancedSettings


T = TypeVar("T", bound="BackupServerWindowsLocalRepositorySettings")


@_attrs_define
class BackupServerWindowsLocalRepositorySettings:
    """
    Attributes:
        max_task_count (int | Unset): Maximum number of concurrent tasks.
        path (str | Unset): Path to the repository folder.
        read_write_limit_enabled (bool | Unset): Indicates whether read/write rate limit is enabled.
        read_write_rate (int | Unset): Read/write rate limit, in MB/s.
        task_limit_enabled (bool | Unset): Indicates whether task limit is enabled.
        advanced_settings (BackupServerRepositoryAdvancedSettings | Unset):
    """

    max_task_count: int | Unset = UNSET
    path: str | Unset = UNSET
    read_write_limit_enabled: bool | Unset = UNSET
    read_write_rate: int | Unset = UNSET
    task_limit_enabled: bool | Unset = UNSET
    advanced_settings: BackupServerRepositoryAdvancedSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_task_count = self.max_task_count

        path = self.path

        read_write_limit_enabled = self.read_write_limit_enabled

        read_write_rate = self.read_write_rate

        task_limit_enabled = self.task_limit_enabled

        advanced_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.advanced_settings, Unset):
            advanced_settings = self.advanced_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_task_count is not UNSET:
            field_dict["maxTaskCount"] = max_task_count
        if path is not UNSET:
            field_dict["path"] = path
        if read_write_limit_enabled is not UNSET:
            field_dict["readWriteLimitEnabled"] = read_write_limit_enabled
        if read_write_rate is not UNSET:
            field_dict["readWriteRate"] = read_write_rate
        if task_limit_enabled is not UNSET:
            field_dict["taskLimitEnabled"] = task_limit_enabled
        if advanced_settings is not UNSET:
            field_dict["advancedSettings"] = advanced_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_repository_advanced_settings import BackupServerRepositoryAdvancedSettings

        d = dict(src_dict)
        max_task_count = d.pop("maxTaskCount", UNSET)

        path = d.pop("path", UNSET)

        read_write_limit_enabled = d.pop("readWriteLimitEnabled", UNSET)

        read_write_rate = d.pop("readWriteRate", UNSET)

        task_limit_enabled = d.pop("taskLimitEnabled", UNSET)

        _advanced_settings = d.pop("advancedSettings", UNSET)
        advanced_settings: BackupServerRepositoryAdvancedSettings | Unset
        if isinstance(_advanced_settings, Unset):
            advanced_settings = UNSET
        else:
            advanced_settings = BackupServerRepositoryAdvancedSettings.from_dict(_advanced_settings)

        backup_server_windows_local_repository_settings = cls(
            max_task_count=max_task_count,
            path=path,
            read_write_limit_enabled=read_write_limit_enabled,
            read_write_rate=read_write_rate,
            task_limit_enabled=task_limit_enabled,
            advanced_settings=advanced_settings,
        )

        backup_server_windows_local_repository_settings.additional_properties = d
        return backup_server_windows_local_repository_settings

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
