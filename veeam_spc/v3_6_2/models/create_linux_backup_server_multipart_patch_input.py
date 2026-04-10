from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.backup_server_multipart_patch_file_input import BackupServerMultipartPatchFileInput


T = TypeVar("T", bound="CreateLinuxBackupServerMultipartPatchInput")


@_attrs_define
class CreateLinuxBackupServerMultipartPatchInput:
    """
    Attributes:
        file (BackupServerMultipartPatchFileInput):
        stop_all_activities (bool): Indicates whether all Veeam Backup & Replication activities must be stopped before
            patch installation begins.
    """

    file: BackupServerMultipartPatchFileInput
    stop_all_activities: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_dict()

        stop_all_activities = self.stop_all_activities

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
                "stopAllActivities": stop_all_activities,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_multipart_patch_file_input import BackupServerMultipartPatchFileInput

        d = dict(src_dict)
        file = BackupServerMultipartPatchFileInput.from_dict(d.pop("file"))

        stop_all_activities = d.pop("stopAllActivities")

        create_linux_backup_server_multipart_patch_input = cls(
            file=file,
            stop_all_activities=stop_all_activities,
        )

        create_linux_backup_server_multipart_patch_input.additional_properties = d
        return create_linux_backup_server_multipart_patch_input

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
