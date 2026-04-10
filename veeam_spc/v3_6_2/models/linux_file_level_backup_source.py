from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinuxFileLevelBackupSource")


@_attrs_define
class LinuxFileLevelBackupSource:
    """
    Attributes:
        directories (list[str]): Array of paths to folders containing the files that must be protected.
        inclusion_masks (list[str] | Unset): Array of inclusion masks.
            > Use `*` to represent any amount of letters, and `?` to represent a single letter.
        exclude_directories (list[str] | Unset): Array of paths to folders containing the files that must be excluded
            from the backup.
        exclusion_masks (list[str] | Unset): Array of exclusion masks.
            > Use `*` to represent any amount of letters, and `?` to represent a single letter. You can additionally specify
            path to a folder.
    """

    directories: list[str]
    inclusion_masks: list[str] | Unset = UNSET
    exclude_directories: list[str] | Unset = UNSET
    exclusion_masks: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        directories = self.directories

        inclusion_masks: list[str] | Unset = UNSET
        if not isinstance(self.inclusion_masks, Unset):
            inclusion_masks = self.inclusion_masks

        exclude_directories: list[str] | Unset = UNSET
        if not isinstance(self.exclude_directories, Unset):
            exclude_directories = self.exclude_directories

        exclusion_masks: list[str] | Unset = UNSET
        if not isinstance(self.exclusion_masks, Unset):
            exclusion_masks = self.exclusion_masks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "directories": directories,
            }
        )
        if inclusion_masks is not UNSET:
            field_dict["inclusionMasks"] = inclusion_masks
        if exclude_directories is not UNSET:
            field_dict["excludeDirectories"] = exclude_directories
        if exclusion_masks is not UNSET:
            field_dict["exclusionMasks"] = exclusion_masks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        directories = cast(list[str], d.pop("directories"))

        inclusion_masks = cast(list[str], d.pop("inclusionMasks", UNSET))

        exclude_directories = cast(list[str], d.pop("excludeDirectories", UNSET))

        exclusion_masks = cast(list[str], d.pop("exclusionMasks", UNSET))

        linux_file_level_backup_source = cls(
            directories=directories,
            inclusion_masks=inclusion_masks,
            exclude_directories=exclude_directories,
            exclusion_masks=exclusion_masks,
        )

        linux_file_level_backup_source.additional_properties = d
        return linux_file_level_backup_source

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
