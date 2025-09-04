from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.linux_backup_volume_source_settings import LinuxBackupVolumeSourceSettings


T = TypeVar("T", bound="LinuxVolumeLevelBackupSource")


@_attrs_define
class LinuxVolumeLevelBackupSource:
    """
    Attributes:
        volumes (list['LinuxBackupVolumeSourceSettings']): Array of source directories.
    """

    volumes: list["LinuxBackupVolumeSourceSettings"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        volumes = []
        for volumes_item_data in self.volumes:
            volumes_item = volumes_item_data.to_dict()
            volumes.append(volumes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "volumes": volumes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linux_backup_volume_source_settings import LinuxBackupVolumeSourceSettings

        d = dict(src_dict)
        volumes = []
        _volumes = d.pop("volumes")
        for volumes_item_data in _volumes:
            volumes_item = LinuxBackupVolumeSourceSettings.from_dict(volumes_item_data)

            volumes.append(volumes_item)

        linux_volume_level_backup_source = cls(
            volumes=volumes,
        )

        linux_volume_level_backup_source.additional_properties = d
        return linux_volume_level_backup_source

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
