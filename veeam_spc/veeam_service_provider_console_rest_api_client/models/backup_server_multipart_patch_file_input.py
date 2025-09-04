from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerMultipartPatchFileInput")


@_attrs_define
class BackupServerMultipartPatchFileInput:
    """
    Attributes:
        name (str): Name of a file.
        file_size (int): File size, in bytes.
        target_directory (Union[Unset, str]): Path to a target directory under %VBR_ROOT%.
    """

    name: str
    file_size: int
    target_directory: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        file_size = self.file_size

        target_directory = self.target_directory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "fileSize": file_size,
            }
        )
        if target_directory is not UNSET:
            field_dict["targetDirectory"] = target_directory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        file_size = d.pop("fileSize")

        target_directory = d.pop("targetDirectory", UNSET)

        backup_server_multipart_patch_file_input = cls(
            name=name,
            file_size=file_size,
            target_directory=target_directory,
        )

        backup_server_multipart_patch_file_input.additional_properties = d
        return backup_server_multipart_patch_file_input

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
