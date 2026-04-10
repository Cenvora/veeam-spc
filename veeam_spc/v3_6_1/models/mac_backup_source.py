from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mac_personal_files_backup_advanced_settings import MacPersonalFilesBackupAdvancedSettings


T = TypeVar("T", bound="MacBackupSource")


@_attrs_define
class MacBackupSource:
    """
    Attributes:
        backup_directly_from_live_file_system (Union[Unset, bool]): Indicates whether backup is performed without
            creating snapshot. Required when backing up data stored in shared folders and file systems that are not
            supported by Veeam snapshot module. Default: False.
        include_usb_drives (Union[Unset, bool]): Indicates whether external USB drives are included in the backup.
            > USB flash drives are not supported.
             Default: False.
        include_directories (Union[None, Unset, list[str]]):  Array of paths to folders containing the files that must
            be protected.
        inclusion_masks (Union[None, Unset, list[str]]): Array of inclusion masks.
            > Use `*` to represent any amount of letters, and `?` to represent a single letter.
        exclude_directories (Union[None, Unset, list[str]]): Array of paths to folders containing the files that must be
            excluded from the backup.
        exclusion_masks (Union[None, Unset, list[str]]): Array of exclusion masks.
            > Use `*` to represent any amount of letters, and `?` to represent a single letter. You can additionally specify
            path to a folder.
        personal_files_advanced_settings (Union[Unset, MacPersonalFilesBackupAdvancedSettings]):
    """

    backup_directly_from_live_file_system: Union[Unset, bool] = False
    include_usb_drives: Union[Unset, bool] = False
    include_directories: Union[None, Unset, list[str]] = UNSET
    inclusion_masks: Union[None, Unset, list[str]] = UNSET
    exclude_directories: Union[None, Unset, list[str]] = UNSET
    exclusion_masks: Union[None, Unset, list[str]] = UNSET
    personal_files_advanced_settings: Union[Unset, "MacPersonalFilesBackupAdvancedSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_directly_from_live_file_system = self.backup_directly_from_live_file_system

        include_usb_drives = self.include_usb_drives

        include_directories: Union[None, Unset, list[str]]
        if isinstance(self.include_directories, Unset):
            include_directories = UNSET
        elif isinstance(self.include_directories, list):
            include_directories = self.include_directories

        else:
            include_directories = self.include_directories

        inclusion_masks: Union[None, Unset, list[str]]
        if isinstance(self.inclusion_masks, Unset):
            inclusion_masks = UNSET
        elif isinstance(self.inclusion_masks, list):
            inclusion_masks = self.inclusion_masks

        else:
            inclusion_masks = self.inclusion_masks

        exclude_directories: Union[None, Unset, list[str]]
        if isinstance(self.exclude_directories, Unset):
            exclude_directories = UNSET
        elif isinstance(self.exclude_directories, list):
            exclude_directories = self.exclude_directories

        else:
            exclude_directories = self.exclude_directories

        exclusion_masks: Union[None, Unset, list[str]]
        if isinstance(self.exclusion_masks, Unset):
            exclusion_masks = UNSET
        elif isinstance(self.exclusion_masks, list):
            exclusion_masks = self.exclusion_masks

        else:
            exclusion_masks = self.exclusion_masks

        personal_files_advanced_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.personal_files_advanced_settings, Unset):
            personal_files_advanced_settings = self.personal_files_advanced_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_directly_from_live_file_system is not UNSET:
            field_dict["backupDirectlyFromLiveFileSystem"] = backup_directly_from_live_file_system
        if include_usb_drives is not UNSET:
            field_dict["includeUsbDrives"] = include_usb_drives
        if include_directories is not UNSET:
            field_dict["includeDirectories"] = include_directories
        if inclusion_masks is not UNSET:
            field_dict["inclusionMasks"] = inclusion_masks
        if exclude_directories is not UNSET:
            field_dict["excludeDirectories"] = exclude_directories
        if exclusion_masks is not UNSET:
            field_dict["exclusionMasks"] = exclusion_masks
        if personal_files_advanced_settings is not UNSET:
            field_dict["personalFilesAdvancedSettings"] = personal_files_advanced_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mac_personal_files_backup_advanced_settings import MacPersonalFilesBackupAdvancedSettings

        d = dict(src_dict)
        backup_directly_from_live_file_system = d.pop("backupDirectlyFromLiveFileSystem", UNSET)

        include_usb_drives = d.pop("includeUsbDrives", UNSET)

        def _parse_include_directories(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                include_directories_type_0 = cast(list[str], data)

                return include_directories_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        include_directories = _parse_include_directories(d.pop("includeDirectories", UNSET))

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

        def _parse_exclude_directories(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclude_directories_type_0 = cast(list[str], data)

                return exclude_directories_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        exclude_directories = _parse_exclude_directories(d.pop("excludeDirectories", UNSET))

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

        _personal_files_advanced_settings = d.pop("personalFilesAdvancedSettings", UNSET)
        personal_files_advanced_settings: Union[Unset, MacPersonalFilesBackupAdvancedSettings]
        if isinstance(_personal_files_advanced_settings, Unset):
            personal_files_advanced_settings = UNSET
        else:
            personal_files_advanced_settings = MacPersonalFilesBackupAdvancedSettings.from_dict(
                _personal_files_advanced_settings
            )

        mac_backup_source = cls(
            backup_directly_from_live_file_system=backup_directly_from_live_file_system,
            include_usb_drives=include_usb_drives,
            include_directories=include_directories,
            inclusion_masks=inclusion_masks,
            exclude_directories=exclude_directories,
            exclusion_masks=exclusion_masks,
            personal_files_advanced_settings=personal_files_advanced_settings,
        )

        mac_backup_source.additional_properties = d
        return mac_backup_source

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
