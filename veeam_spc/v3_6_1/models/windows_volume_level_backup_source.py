from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.windows_volume_level_backup_source_mode import WindowsVolumeLevelBackupSourceMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="WindowsVolumeLevelBackupSource")


@_attrs_define
class WindowsVolumeLevelBackupSource:
    r"""
    Attributes:
        mode (Union[Unset, WindowsVolumeLevelBackupSourceMode]): Filter type. Default:
            WindowsVolumeLevelBackupSourceMode.INCLUSIONMODE.
        backup_operating_system (Union[Unset, bool]): Indicates whether agent operating system is included in a backup
            scope.
            >Available only if the `InclusionMode` filter type is selected.
             Default: False.
        inclusions (Union[None, Unset, list[str]]): Array of drive letters of volumes that must be included in the
            backup scope.
            > Drive letters must be specified in the following format: `C:\`.
        exclusions (Union[None, Unset, list[str]]): Array of drive letters of volumes that must be excluded from the
            backup scope.
            > Drive letters must be specified in the following format: `C:\`.
    """

    mode: Union[Unset, WindowsVolumeLevelBackupSourceMode] = WindowsVolumeLevelBackupSourceMode.INCLUSIONMODE
    backup_operating_system: Union[Unset, bool] = False
    inclusions: Union[None, Unset, list[str]] = UNSET
    exclusions: Union[None, Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        backup_operating_system = self.backup_operating_system

        inclusions: Union[None, Unset, list[str]]
        if isinstance(self.inclusions, Unset):
            inclusions = UNSET
        elif isinstance(self.inclusions, list):
            inclusions = self.inclusions

        else:
            inclusions = self.inclusions

        exclusions: Union[None, Unset, list[str]]
        if isinstance(self.exclusions, Unset):
            exclusions = UNSET
        elif isinstance(self.exclusions, list):
            exclusions = self.exclusions

        else:
            exclusions = self.exclusions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if backup_operating_system is not UNSET:
            field_dict["backupOperatingSystem"] = backup_operating_system
        if inclusions is not UNSET:
            field_dict["inclusions"] = inclusions
        if exclusions is not UNSET:
            field_dict["exclusions"] = exclusions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, WindowsVolumeLevelBackupSourceMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = WindowsVolumeLevelBackupSourceMode(_mode)

        backup_operating_system = d.pop("backupOperatingSystem", UNSET)

        def _parse_inclusions(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                inclusions_type_0 = cast(list[str], data)

                return inclusions_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        inclusions = _parse_inclusions(d.pop("inclusions", UNSET))

        def _parse_exclusions(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclusions_type_0 = cast(list[str], data)

                return exclusions_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        exclusions = _parse_exclusions(d.pop("exclusions", UNSET))

        windows_volume_level_backup_source = cls(
            mode=mode,
            backup_operating_system=backup_operating_system,
            inclusions=inclusions,
            exclusions=exclusions,
        )

        windows_volume_level_backup_source.additional_properties = d
        return windows_volume_level_backup_source

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
