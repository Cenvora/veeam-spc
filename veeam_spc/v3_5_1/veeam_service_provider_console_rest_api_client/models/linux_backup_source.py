from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.linux_backup_source_backup_mode import LinuxBackupSourceBackupMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linux_file_level_backup_source import LinuxFileLevelBackupSource
    from ..models.linux_volume_level_backup_source import LinuxVolumeLevelBackupSource


T = TypeVar("T", bound="LinuxBackupSource")


@_attrs_define
class LinuxBackupSource:
    """
    Attributes:
        backup_mode (LinuxBackupSourceBackupMode): Backup mode.
        volume_level_options (Union[Unset, LinuxVolumeLevelBackupSource]):
        file_level_options (Union[Unset, LinuxFileLevelBackupSource]):
    """

    backup_mode: LinuxBackupSourceBackupMode
    volume_level_options: Union[Unset, "LinuxVolumeLevelBackupSource"] = UNSET
    file_level_options: Union[Unset, "LinuxFileLevelBackupSource"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_mode = self.backup_mode.value

        volume_level_options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.volume_level_options, Unset):
            volume_level_options = self.volume_level_options.to_dict()

        file_level_options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.file_level_options, Unset):
            file_level_options = self.file_level_options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backupMode": backup_mode,
            }
        )
        if volume_level_options is not UNSET:
            field_dict["volumeLevelOptions"] = volume_level_options
        if file_level_options is not UNSET:
            field_dict["fileLevelOptions"] = file_level_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linux_file_level_backup_source import LinuxFileLevelBackupSource
        from ..models.linux_volume_level_backup_source import LinuxVolumeLevelBackupSource

        d = dict(src_dict)
        backup_mode = LinuxBackupSourceBackupMode(d.pop("backupMode"))

        _volume_level_options = d.pop("volumeLevelOptions", UNSET)
        volume_level_options: Union[Unset, LinuxVolumeLevelBackupSource]
        if isinstance(_volume_level_options, Unset):
            volume_level_options = UNSET
        else:
            volume_level_options = LinuxVolumeLevelBackupSource.from_dict(_volume_level_options)

        _file_level_options = d.pop("fileLevelOptions", UNSET)
        file_level_options: Union[Unset, LinuxFileLevelBackupSource]
        if isinstance(_file_level_options, Unset):
            file_level_options = UNSET
        else:
            file_level_options = LinuxFileLevelBackupSource.from_dict(_file_level_options)

        linux_backup_source = cls(
            backup_mode=backup_mode,
            volume_level_options=volume_level_options,
            file_level_options=file_level_options,
        )

        linux_backup_source.additional_properties = d
        return linux_backup_source

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
