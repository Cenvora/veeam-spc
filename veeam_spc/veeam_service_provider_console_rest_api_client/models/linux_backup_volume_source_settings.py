from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.linux_backup_volume_source_settings_volume_type import LinuxBackupVolumeSourceSettingsVolumeType

T = TypeVar("T", bound="LinuxBackupVolumeSourceSettings")


@_attrs_define
class LinuxBackupVolumeSourceSettings:
    """
    Attributes:
        volume_type (LinuxBackupVolumeSourceSettingsVolumeType): Volume type.
        path (str): Path to a block device or mount point.
    """

    volume_type: LinuxBackupVolumeSourceSettingsVolumeType
    path: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        volume_type = self.volume_type.value

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "volumeType": volume_type,
                "path": path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        volume_type = LinuxBackupVolumeSourceSettingsVolumeType(d.pop("volumeType"))

        path = d.pop("path")

        linux_backup_volume_source_settings = cls(
            volume_type=volume_type,
            path=path,
        )

        linux_backup_volume_source_settings.additional_properties = d
        return linux_backup_volume_source_settings

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
