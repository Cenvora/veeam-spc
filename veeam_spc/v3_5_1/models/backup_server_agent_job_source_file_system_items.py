from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerAgentJobSourceFileSystemItems")


@_attrs_define
class BackupServerAgentJobSourceFileSystemItems:
    r"""Files and folders of an agent computer are included in a backup scope.

    Attributes:
        volumes (Union[Unset, list[str]]): Array of drive letters in the following format: `C:\`
        files_and_folders (Union[Unset, list[str]]): Array of protected files and folders.
    """

    volumes: Union[Unset, list[str]] = UNSET
    files_and_folders: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        volumes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.volumes, Unset):
            volumes = self.volumes

        files_and_folders: Union[Unset, list[str]] = UNSET
        if not isinstance(self.files_and_folders, Unset):
            files_and_folders = self.files_and_folders

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if volumes is not UNSET:
            field_dict["volumes"] = volumes
        if files_and_folders is not UNSET:
            field_dict["filesAndFolders"] = files_and_folders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        volumes = cast(list[str], d.pop("volumes", UNSET))

        files_and_folders = cast(list[str], d.pop("filesAndFolders", UNSET))

        backup_server_agent_job_source_file_system_items = cls(
            volumes=volumes,
            files_and_folders=files_and_folders,
        )

        backup_server_agent_job_source_file_system_items.additional_properties = d
        return backup_server_agent_job_source_file_system_items

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
