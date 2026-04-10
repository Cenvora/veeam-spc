from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_multipart_patch_file import BackupServerMultipartPatchFile


T = TypeVar("T", bound="BackupServerMultipartPatchInfo")


@_attrs_define
class BackupServerMultipartPatchInfo:
    """
    Attributes:
        upload_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup & Replication server patch upload.
        files (Union[Unset, list['BackupServerMultipartPatchFile']]): Array of files included in a Veeam Backup &
            Replication server patch upload.
    """

    upload_uid: Union[Unset, UUID] = UNSET
    files: Union[Unset, list["BackupServerMultipartPatchFile"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upload_uid: Union[Unset, str] = UNSET
        if not isinstance(self.upload_uid, Unset):
            upload_uid = str(self.upload_uid)

        files: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if upload_uid is not UNSET:
            field_dict["uploadUid"] = upload_uid
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_multipart_patch_file import BackupServerMultipartPatchFile

        d = dict(src_dict)
        _upload_uid = d.pop("uploadUid", UNSET)
        upload_uid: Union[Unset, UUID]
        if isinstance(_upload_uid, Unset):
            upload_uid = UNSET
        else:
            upload_uid = UUID(_upload_uid)

        files = []
        _files = d.pop("files", UNSET)
        for files_item_data in _files or []:
            files_item = BackupServerMultipartPatchFile.from_dict(files_item_data)

            files.append(files_item)

        backup_server_multipart_patch_info = cls(
            upload_uid=upload_uid,
            files=files,
        )

        backup_server_multipart_patch_info.additional_properties = d
        return backup_server_multipart_patch_info

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
