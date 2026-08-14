from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_rotated_drive_cleanup_mode_nullable import BackupServerRotatedDriveCleanupModeNullable
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerRepositoryAdvancedSettings")


@_attrs_define
class BackupServerRepositoryAdvancedSettings:
    """
    Attributes:
        align_data_blocks (bool | Unset): Indicates whether data blocks must be aligned.
        decompress_before_storing (bool | Unset): Indicates whether data must be decompressed before storing.
        per_vm_backup (bool | Unset): Indicates whether per-VM backup is enabled.
        rotated_drive_cleanup_mode (BackupServerRotatedDriveCleanupModeNullable | Unset): Cleanup mode for rotated
            drives.
        rotated_drives (bool | Unset): Indicates whether repository drives must be rotated.
    """

    align_data_blocks: bool | Unset = UNSET
    decompress_before_storing: bool | Unset = UNSET
    per_vm_backup: bool | Unset = UNSET
    rotated_drive_cleanup_mode: BackupServerRotatedDriveCleanupModeNullable | Unset = UNSET
    rotated_drives: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        align_data_blocks = self.align_data_blocks

        decompress_before_storing = self.decompress_before_storing

        per_vm_backup = self.per_vm_backup

        rotated_drive_cleanup_mode: str | Unset = UNSET
        if not isinstance(self.rotated_drive_cleanup_mode, Unset):
            rotated_drive_cleanup_mode = self.rotated_drive_cleanup_mode.value

        rotated_drives = self.rotated_drives

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if align_data_blocks is not UNSET:
            field_dict["alignDataBlocks"] = align_data_blocks
        if decompress_before_storing is not UNSET:
            field_dict["decompressBeforeStoring"] = decompress_before_storing
        if per_vm_backup is not UNSET:
            field_dict["perVmBackup"] = per_vm_backup
        if rotated_drive_cleanup_mode is not UNSET:
            field_dict["rotatedDriveCleanupMode"] = rotated_drive_cleanup_mode
        if rotated_drives is not UNSET:
            field_dict["rotatedDrives"] = rotated_drives

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        align_data_blocks = d.pop("alignDataBlocks", UNSET)

        decompress_before_storing = d.pop("decompressBeforeStoring", UNSET)

        per_vm_backup = d.pop("perVmBackup", UNSET)

        _rotated_drive_cleanup_mode = d.pop("rotatedDriveCleanupMode", UNSET)
        rotated_drive_cleanup_mode: BackupServerRotatedDriveCleanupModeNullable | Unset
        if isinstance(_rotated_drive_cleanup_mode, Unset):
            rotated_drive_cleanup_mode = UNSET
        else:
            rotated_drive_cleanup_mode = BackupServerRotatedDriveCleanupModeNullable(_rotated_drive_cleanup_mode)

        rotated_drives = d.pop("rotatedDrives", UNSET)

        backup_server_repository_advanced_settings = cls(
            align_data_blocks=align_data_blocks,
            decompress_before_storing=decompress_before_storing,
            per_vm_backup=per_vm_backup,
            rotated_drive_cleanup_mode=rotated_drive_cleanup_mode,
            rotated_drives=rotated_drives,
        )

        backup_server_repository_advanced_settings.additional_properties = d
        return backup_server_repository_advanced_settings

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
