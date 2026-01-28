from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinuxFileLevelBackupSource")


@_attrs_define
class LinuxFileLevelBackupSource:
    """
    Attributes:
        directories (Union[None, list[str]]): Array of paths to folders containing the files that must be protected.
        inclusion_masks (Union[None, Unset, list[str]]): Array of inclusion masks.
            > Use `*` to represent any amount of letters, and `?` to represent a single letter.
        exclusion_masks (Union[None, Unset, list[str]]): Array of exclusion masks.
            > Use `*` to represent any amount of letters, and `?` to represent a single letter. You can additionally specify
            path to a folder.
    """

    directories: Union[None, list[str]]
    inclusion_masks: Union[None, Unset, list[str]] = UNSET
    exclusion_masks: Union[None, Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        directories: Union[None, list[str]]
        if isinstance(self.directories, list):
            directories = self.directories

        else:
            directories = self.directories

        inclusion_masks: Union[None, Unset, list[str]]
        if isinstance(self.inclusion_masks, Unset):
            inclusion_masks = UNSET
        elif isinstance(self.inclusion_masks, list):
            inclusion_masks = self.inclusion_masks

        else:
            inclusion_masks = self.inclusion_masks

        exclusion_masks: Union[None, Unset, list[str]]
        if isinstance(self.exclusion_masks, Unset):
            exclusion_masks = UNSET
        elif isinstance(self.exclusion_masks, list):
            exclusion_masks = self.exclusion_masks

        else:
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
        if exclusion_masks is not UNSET:
            field_dict["exclusionMasks"] = exclusion_masks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_directories(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                directories_type_0 = cast(list[str], data)

                return directories_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        directories = _parse_directories(d.pop("directories"))

        def _parse_inclusion_masks(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                inclusion_masks_type_0 = cast(list[str], data)

                return inclusion_masks_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        inclusion_masks = _parse_inclusion_masks(d.pop("inclusionMasks", UNSET))

        def _parse_exclusion_masks(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclusion_masks_type_0 = cast(list[str], data)

                return exclusion_masks_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        exclusion_masks = _parse_exclusion_masks(d.pop("exclusionMasks", UNSET))

        linux_file_level_backup_source = cls(
            directories=directories,
            inclusion_masks=inclusion_masks,
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
