from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_multipart_patch_action import BackupServerMultipartPatchAction

if TYPE_CHECKING:
    from ..models.backup_server_multipart_patch_file_input import BackupServerMultipartPatchFileInput


T = TypeVar("T", bound="CreateBackupServerMultipartPatchInput")


@_attrs_define
class CreateBackupServerMultipartPatchInput:
    """
    Attributes:
        files (list['BackupServerMultipartPatchFileInput']): Array of files included in a Veeam Backup & Replication
            server patch upload.
        action (BackupServerMultipartPatchAction): Action that must be performed on a Veeam Backup & Replication server
            patch.
        stop_all_activities (bool): Indicates whether all Veeam Backup & Replication activities must be stopped before
            patch installation begins.
        reboot_automatically (bool): Indicates whether a Veeam Backup & Replication server must be rebooted after the
            patch installation is finished.
    """

    files: list["BackupServerMultipartPatchFileInput"]
    action: BackupServerMultipartPatchAction
    stop_all_activities: bool
    reboot_automatically: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)

        action = self.action.value

        stop_all_activities = self.stop_all_activities

        reboot_automatically = self.reboot_automatically

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "files": files,
                "action": action,
                "stopAllActivities": stop_all_activities,
                "rebootAutomatically": reboot_automatically,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_multipart_patch_file_input import BackupServerMultipartPatchFileInput

        d = dict(src_dict)
        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = BackupServerMultipartPatchFileInput.from_dict(files_item_data)

            files.append(files_item)

        action = BackupServerMultipartPatchAction(d.pop("action"))

        stop_all_activities = d.pop("stopAllActivities")

        reboot_automatically = d.pop("rebootAutomatically")

        create_backup_server_multipart_patch_input = cls(
            files=files,
            action=action,
            stop_all_activities=stop_all_activities,
            reboot_automatically=reboot_automatically,
        )

        create_backup_server_multipart_patch_input.additional_properties = d
        return create_backup_server_multipart_patch_input

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
