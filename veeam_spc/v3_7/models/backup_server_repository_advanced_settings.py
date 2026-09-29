from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_rotated_drive_cleanup_mode_nullable import BackupServerRotatedDriveCleanupModeNullable
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerRepositoryAdvancedSettings")


@_attrs_define
class BackupServerRepositoryAdvancedSettings:
    """
    Attributes:
        align_data_blocks (bool | None | Unset): Indicates whether data blocks must be aligned.
        decompress_before_storing (bool | None | Unset): Indicates whether data must be decompressed before storing.
        per_vm_backup (bool | None | Unset): Indicates whether per-VM backup is enabled.
        rotated_drive_cleanup_mode (BackupServerRotatedDriveCleanupModeNullable | Unset): Cleanup mode for rotated
            drives.
        rotated_drives (bool | None | Unset): Indicates whether repository drives must be rotated.
    """

    align_data_blocks: bool | None | Unset = UNSET
    decompress_before_storing: bool | None | Unset = UNSET
    per_vm_backup: bool | None | Unset = UNSET
    rotated_drive_cleanup_mode: BackupServerRotatedDriveCleanupModeNullable | Unset = UNSET
    rotated_drives: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        align_data_blocks: bool | None | Unset
        if isinstance(self.align_data_blocks, Unset):
            align_data_blocks = UNSET
        else:
            align_data_blocks = self.align_data_blocks

        decompress_before_storing: bool | None | Unset
        if isinstance(self.decompress_before_storing, Unset):
            decompress_before_storing = UNSET
        else:
            decompress_before_storing = self.decompress_before_storing

        per_vm_backup: bool | None | Unset
        if isinstance(self.per_vm_backup, Unset):
            per_vm_backup = UNSET
        else:
            per_vm_backup = self.per_vm_backup

        rotated_drive_cleanup_mode: str | Unset = UNSET
        if not isinstance(self.rotated_drive_cleanup_mode, Unset):
            rotated_drive_cleanup_mode = self.rotated_drive_cleanup_mode.value

        rotated_drives: bool | None | Unset
        if isinstance(self.rotated_drives, Unset):
            rotated_drives = UNSET
        else:
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

        def _parse_align_data_blocks(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        align_data_blocks = _parse_align_data_blocks(d.pop("alignDataBlocks", UNSET))

        def _parse_decompress_before_storing(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        decompress_before_storing = _parse_decompress_before_storing(d.pop("decompressBeforeStoring", UNSET))

        def _parse_per_vm_backup(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        per_vm_backup = _parse_per_vm_backup(d.pop("perVmBackup", UNSET))

        _rotated_drive_cleanup_mode = d.pop("rotatedDriveCleanupMode", UNSET)
        rotated_drive_cleanup_mode: BackupServerRotatedDriveCleanupModeNullable | Unset
        if isinstance(_rotated_drive_cleanup_mode, Unset):
            rotated_drive_cleanup_mode = UNSET
        else:
            rotated_drive_cleanup_mode = BackupServerRotatedDriveCleanupModeNullable(_rotated_drive_cleanup_mode)

        def _parse_rotated_drives(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        rotated_drives = _parse_rotated_drives(d.pop("rotatedDrives", UNSET))

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
