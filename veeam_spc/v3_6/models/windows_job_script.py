from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WindowsJobScript")


@_attrs_define
class WindowsJobScript:
    r"""
    Attributes:
        file_name (str): Script file name. Must match the following pattern: '^[^\\/:*?"<>|]+\.(exe|bat|cmd)$'.
        content (Union[Unset, str]): Script content in the Base64 format. The property is required and write-only.
    """

    file_name: str
    content: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_name = self.file_name

        content = self.content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fileName": file_name,
            }
        )
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_name = d.pop("fileName")

        content = d.pop("content", UNSET)

        windows_job_script = cls(
            file_name=file_name,
            content=content,
        )

        windows_job_script.additional_properties = d
        return windows_job_script

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
