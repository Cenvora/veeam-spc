from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.windows_personal_files_backup_advanced_settings import WindowsPersonalFilesBackupAdvancedSettings


T = TypeVar("T", bound="WindowsFileLevelBackupSource")


@_attrs_define
class WindowsFileLevelBackupSource:
    """
    Attributes:
        include_directories (Union[Unset, list[str]]): Array of paths to folders containing the files that must be
            protected.
            > Can be skipped, if the `osfilesIncluded` or `personalFilesIncluded` property has the `true` value.'
        exclude_directories (Union[Unset, list[str]]): Array of paths to folders containing the files that must not be
            protected.
            > Can be skipped, if the `osfilesIncluded` or `personalFilesIncluded` property has the `true` value.'
        inclusion_masks (Union[Unset, list[str]]): Array of file names and/or masks for file types that must be
            protected.
        exclusion_masks (Union[Unset, list[str]]): Array of file names and/or masks for file types that must not be
            protected.
        osfiles_included (Union[Unset, bool]): Indicates whether the job must protect the OS data.
            > The `true` value automatically applies the `true` value to the `personalFilesIncluded` property.
             Default: False.
        exclude_one_drive_folders (Union[Unset, bool]): Indicates whether the OneDrive folders must be excluded from the
            backup scope. Default: False.
        personal_files_included (Union[Unset, bool]): Indicates whether the job must protect the user profile folder
            including all user settings and data.
            > Has the `true` value if the `osfilesIncluded` property has the `true` value.'
             Default: False.
        personal_files_advanced_settings (Union[Unset, WindowsPersonalFilesBackupAdvancedSettings]):
    """

    include_directories: Union[Unset, list[str]] = UNSET
    exclude_directories: Union[Unset, list[str]] = UNSET
    inclusion_masks: Union[Unset, list[str]] = UNSET
    exclusion_masks: Union[Unset, list[str]] = UNSET
    osfiles_included: Union[Unset, bool] = False
    exclude_one_drive_folders: Union[Unset, bool] = False
    personal_files_included: Union[Unset, bool] = False
    personal_files_advanced_settings: Union[Unset, "WindowsPersonalFilesBackupAdvancedSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        include_directories: Union[Unset, list[str]] = UNSET
        if not isinstance(self.include_directories, Unset):
            include_directories = self.include_directories

        exclude_directories: Union[Unset, list[str]] = UNSET
        if not isinstance(self.exclude_directories, Unset):
            exclude_directories = self.exclude_directories

        inclusion_masks: Union[Unset, list[str]] = UNSET
        if not isinstance(self.inclusion_masks, Unset):
            inclusion_masks = self.inclusion_masks

        exclusion_masks: Union[Unset, list[str]] = UNSET
        if not isinstance(self.exclusion_masks, Unset):
            exclusion_masks = self.exclusion_masks

        osfiles_included = self.osfiles_included

        exclude_one_drive_folders = self.exclude_one_drive_folders

        personal_files_included = self.personal_files_included

        personal_files_advanced_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.personal_files_advanced_settings, Unset):
            personal_files_advanced_settings = self.personal_files_advanced_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if include_directories is not UNSET:
            field_dict["includeDirectories"] = include_directories
        if exclude_directories is not UNSET:
            field_dict["excludeDirectories"] = exclude_directories
        if inclusion_masks is not UNSET:
            field_dict["inclusionMasks"] = inclusion_masks
        if exclusion_masks is not UNSET:
            field_dict["exclusionMasks"] = exclusion_masks
        if osfiles_included is not UNSET:
            field_dict["osfilesIncluded"] = osfiles_included
        if exclude_one_drive_folders is not UNSET:
            field_dict["excludeOneDriveFolders"] = exclude_one_drive_folders
        if personal_files_included is not UNSET:
            field_dict["personalFilesIncluded"] = personal_files_included
        if personal_files_advanced_settings is not UNSET:
            field_dict["personalFilesAdvancedSettings"] = personal_files_advanced_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.windows_personal_files_backup_advanced_settings import WindowsPersonalFilesBackupAdvancedSettings

        d = dict(src_dict)
        include_directories = cast(list[str], d.pop("includeDirectories", UNSET))

        exclude_directories = cast(list[str], d.pop("excludeDirectories", UNSET))

        inclusion_masks = cast(list[str], d.pop("inclusionMasks", UNSET))

        exclusion_masks = cast(list[str], d.pop("exclusionMasks", UNSET))

        osfiles_included = d.pop("osfilesIncluded", UNSET)

        exclude_one_drive_folders = d.pop("excludeOneDriveFolders", UNSET)

        personal_files_included = d.pop("personalFilesIncluded", UNSET)

        _personal_files_advanced_settings = d.pop("personalFilesAdvancedSettings", UNSET)
        personal_files_advanced_settings: Union[Unset, WindowsPersonalFilesBackupAdvancedSettings]
        if isinstance(_personal_files_advanced_settings, Unset):
            personal_files_advanced_settings = UNSET
        else:
            personal_files_advanced_settings = WindowsPersonalFilesBackupAdvancedSettings.from_dict(
                _personal_files_advanced_settings
            )

        windows_file_level_backup_source = cls(
            include_directories=include_directories,
            exclude_directories=exclude_directories,
            inclusion_masks=inclusion_masks,
            exclusion_masks=exclusion_masks,
            osfiles_included=osfiles_included,
            exclude_one_drive_folders=exclude_one_drive_folders,
            personal_files_included=personal_files_included,
            personal_files_advanced_settings=personal_files_advanced_settings,
        )

        windows_file_level_backup_source.additional_properties = d
        return windows_file_level_backup_source

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
