from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.linux_indexing_settings_indexing_type import LinuxIndexingSettingsIndexingType
from ..types import UNSET, Unset

T = TypeVar("T", bound="LinuxIndexingSettings")


@_attrs_define
class LinuxIndexingSettings:
    """
    Attributes:
        indexing_type (Union[Unset, LinuxIndexingSettingsIndexingType]): Indexing mode. Default:
            LinuxIndexingSettingsIndexingType.NONE.
        included_folders (Union[None, Unset, list[str]]): Array of paths to the indexed folders.
            > Required for the `SpecifiedFolders` indexing mode.'
        excluded_folders (Union[None, Unset, list[str]]): Array of paths to folders that are excluded from the indexing
            scope.
            > Required for the `ExceptSpecifiedFolders` indexing mode.
    """

    indexing_type: Union[Unset, LinuxIndexingSettingsIndexingType] = LinuxIndexingSettingsIndexingType.NONE
    included_folders: Union[None, Unset, list[str]] = UNSET
    excluded_folders: Union[None, Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        indexing_type: Union[Unset, str] = UNSET
        if not isinstance(self.indexing_type, Unset):
            indexing_type = self.indexing_type.value

        included_folders: Union[None, Unset, list[str]]
        if isinstance(self.included_folders, Unset):
            included_folders = UNSET
        elif isinstance(self.included_folders, list):
            included_folders = self.included_folders

        else:
            included_folders = self.included_folders

        excluded_folders: Union[None, Unset, list[str]]
        if isinstance(self.excluded_folders, Unset):
            excluded_folders = UNSET
        elif isinstance(self.excluded_folders, list):
            excluded_folders = self.excluded_folders

        else:
            excluded_folders = self.excluded_folders

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if indexing_type is not UNSET:
            field_dict["indexingType"] = indexing_type
        if included_folders is not UNSET:
            field_dict["includedFolders"] = included_folders
        if excluded_folders is not UNSET:
            field_dict["excludedFolders"] = excluded_folders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _indexing_type = d.pop("indexingType", UNSET)
        indexing_type: Union[Unset, LinuxIndexingSettingsIndexingType]
        if isinstance(_indexing_type, Unset):
            indexing_type = UNSET
        else:
            indexing_type = LinuxIndexingSettingsIndexingType(_indexing_type)

        def _parse_included_folders(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                included_folders_type_0 = cast(list[str], data)

                return included_folders_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        included_folders = _parse_included_folders(d.pop("includedFolders", UNSET))

        def _parse_excluded_folders(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                excluded_folders_type_0 = cast(list[str], data)

                return excluded_folders_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        excluded_folders = _parse_excluded_folders(d.pop("excludedFolders", UNSET))

        linux_indexing_settings = cls(
            indexing_type=indexing_type,
            included_folders=included_folders,
            excluded_folders=excluded_folders,
        )

        linux_indexing_settings.additional_properties = d
        return linux_indexing_settings

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
