from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.windows_personal_files_backup_advanced_settings_exclusions_item import (
    WindowsPersonalFilesBackupAdvancedSettingsExclusionsItem,
)
from ..models.windows_personal_files_backup_advanced_settings_inclusions_item import (
    WindowsPersonalFilesBackupAdvancedSettingsInclusionsItem,
)
from ..models.windows_personal_files_backup_advanced_settings_mode import WindowsPersonalFilesBackupAdvancedSettingsMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="WindowsPersonalFilesBackupAdvancedSettings")


@_attrs_define
class WindowsPersonalFilesBackupAdvancedSettings:
    """
    Attributes:
        mode (Union[Unset, WindowsPersonalFilesBackupAdvancedSettingsMode]): Type of personal file protection. Default:
            WindowsPersonalFilesBackupAdvancedSettingsMode.ALL.
        inclusions (Union[Unset, list[WindowsPersonalFilesBackupAdvancedSettingsInclusionsItem]]): Profile folders that
            must be included in the backup scope.
        exclusions (Union[Unset, list[WindowsPersonalFilesBackupAdvancedSettingsExclusionsItem]]): Exclusions configured
            for personal file backup.
    """

    mode: Union[Unset, WindowsPersonalFilesBackupAdvancedSettingsMode] = (
        WindowsPersonalFilesBackupAdvancedSettingsMode.ALL
    )
    inclusions: Union[Unset, list[WindowsPersonalFilesBackupAdvancedSettingsInclusionsItem]] = UNSET
    exclusions: Union[Unset, list[WindowsPersonalFilesBackupAdvancedSettingsExclusionsItem]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        inclusions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.inclusions, Unset):
            inclusions = []
            for inclusions_item_data in self.inclusions:
                inclusions_item = inclusions_item_data.value
                inclusions.append(inclusions_item)

        exclusions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.exclusions, Unset):
            exclusions = []
            for exclusions_item_data in self.exclusions:
                exclusions_item = exclusions_item_data.value
                exclusions.append(exclusions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if inclusions is not UNSET:
            field_dict["inclusions"] = inclusions
        if exclusions is not UNSET:
            field_dict["exclusions"] = exclusions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, WindowsPersonalFilesBackupAdvancedSettingsMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = WindowsPersonalFilesBackupAdvancedSettingsMode(_mode)

        inclusions = []
        _inclusions = d.pop("inclusions", UNSET)
        for inclusions_item_data in _inclusions or []:
            inclusions_item = WindowsPersonalFilesBackupAdvancedSettingsInclusionsItem(inclusions_item_data)

            inclusions.append(inclusions_item)

        exclusions = []
        _exclusions = d.pop("exclusions", UNSET)
        for exclusions_item_data in _exclusions or []:
            exclusions_item = WindowsPersonalFilesBackupAdvancedSettingsExclusionsItem(exclusions_item_data)

            exclusions.append(exclusions_item)

        windows_personal_files_backup_advanced_settings = cls(
            mode=mode,
            inclusions=inclusions,
            exclusions=exclusions,
        )

        windows_personal_files_backup_advanced_settings.additional_properties = d
        return windows_personal_files_backup_advanced_settings

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
