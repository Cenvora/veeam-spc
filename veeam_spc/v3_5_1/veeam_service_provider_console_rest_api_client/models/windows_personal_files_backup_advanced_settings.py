from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.windows_personal_files_backup_advanced_settings_exclusions_type_0_item import (
    WindowsPersonalFilesBackupAdvancedSettingsExclusionsType0Item,
)
from ..models.windows_personal_files_backup_advanced_settings_inclusions_type_0_item import (
    WindowsPersonalFilesBackupAdvancedSettingsInclusionsType0Item,
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
        inclusions (Union[None, Unset, list[WindowsPersonalFilesBackupAdvancedSettingsInclusionsType0Item]]): Profile
            folders that must be included in the backup scope.
        exclusions (Union[None, Unset, list[WindowsPersonalFilesBackupAdvancedSettingsExclusionsType0Item]]): Exclusions
            configured for personal file backup.
    """

    mode: Union[Unset, WindowsPersonalFilesBackupAdvancedSettingsMode] = (
        WindowsPersonalFilesBackupAdvancedSettingsMode.ALL
    )
    inclusions: Union[None, Unset, list[WindowsPersonalFilesBackupAdvancedSettingsInclusionsType0Item]] = UNSET
    exclusions: Union[None, Unset, list[WindowsPersonalFilesBackupAdvancedSettingsExclusionsType0Item]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        inclusions: Union[None, Unset, list[str]]
        if isinstance(self.inclusions, Unset):
            inclusions = UNSET
        elif isinstance(self.inclusions, list):
            inclusions = []
            for inclusions_type_0_item_data in self.inclusions:
                inclusions_type_0_item = inclusions_type_0_item_data.value
                inclusions.append(inclusions_type_0_item)

        else:
            inclusions = self.inclusions

        exclusions: Union[None, Unset, list[str]]
        if isinstance(self.exclusions, Unset):
            exclusions = UNSET
        elif isinstance(self.exclusions, list):
            exclusions = []
            for exclusions_type_0_item_data in self.exclusions:
                exclusions_type_0_item = exclusions_type_0_item_data.value
                exclusions.append(exclusions_type_0_item)

        else:
            exclusions = self.exclusions

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

        def _parse_inclusions(
            data: object,
        ) -> Union[None, Unset, list[WindowsPersonalFilesBackupAdvancedSettingsInclusionsType0Item]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                inclusions_type_0 = []
                _inclusions_type_0 = data
                for inclusions_type_0_item_data in _inclusions_type_0:
                    inclusions_type_0_item = WindowsPersonalFilesBackupAdvancedSettingsInclusionsType0Item(
                        inclusions_type_0_item_data
                    )

                    inclusions_type_0.append(inclusions_type_0_item)

                return inclusions_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[WindowsPersonalFilesBackupAdvancedSettingsInclusionsType0Item]], data)

        inclusions = _parse_inclusions(d.pop("inclusions", UNSET))

        def _parse_exclusions(
            data: object,
        ) -> Union[None, Unset, list[WindowsPersonalFilesBackupAdvancedSettingsExclusionsType0Item]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclusions_type_0 = []
                _exclusions_type_0 = data
                for exclusions_type_0_item_data in _exclusions_type_0:
                    exclusions_type_0_item = WindowsPersonalFilesBackupAdvancedSettingsExclusionsType0Item(
                        exclusions_type_0_item_data
                    )

                    exclusions_type_0.append(exclusions_type_0_item)

                return exclusions_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[WindowsPersonalFilesBackupAdvancedSettingsExclusionsType0Item]], data)

        exclusions = _parse_exclusions(d.pop("exclusions", UNSET))

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
