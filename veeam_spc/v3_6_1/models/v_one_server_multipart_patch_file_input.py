from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VOneServerMultipartPatchFileInput")


@_attrs_define
class VOneServerMultipartPatchFileInput:
    """
    Attributes:
        name (str): Name of a file.
        file_size (int): File size, in bytes.
    """

    name: str
    file_size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        file_size = self.file_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "fileSize": file_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        file_size = d.pop("fileSize")

        v_one_server_multipart_patch_file_input = cls(
            name=name,
            file_size=file_size,
        )

        v_one_server_multipart_patch_file_input.additional_properties = d
        return v_one_server_multipart_patch_file_input

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
