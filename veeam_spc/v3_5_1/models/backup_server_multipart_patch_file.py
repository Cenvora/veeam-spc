from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerMultipartPatchFile")


@_attrs_define
class BackupServerMultipartPatchFile:
    """
    Attributes:
        name (Union[Unset, str]): Name of a file included in a Veeam Backup & Replication server patch upload.
        file_stream_uid (Union[Unset, UUID]): UID assigned a file included in a Veeam Backup & Replication server patch
            upload.
    """

    name: Union[Unset, str] = UNSET
    file_stream_uid: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        file_stream_uid: Union[Unset, str] = UNSET
        if not isinstance(self.file_stream_uid, Unset):
            file_stream_uid = str(self.file_stream_uid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if file_stream_uid is not UNSET:
            field_dict["fileStreamUid"] = file_stream_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _file_stream_uid = d.pop("fileStreamUid", UNSET)
        file_stream_uid: Union[Unset, UUID]
        if isinstance(_file_stream_uid, Unset):
            file_stream_uid = UNSET
        else:
            file_stream_uid = UUID(_file_stream_uid)

        backup_server_multipart_patch_file = cls(
            name=name,
            file_stream_uid=file_stream_uid,
        )

        backup_server_multipart_patch_file.additional_properties = d
        return backup_server_multipart_patch_file

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
