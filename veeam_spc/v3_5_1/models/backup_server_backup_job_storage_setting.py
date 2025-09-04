from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_compression_level import BackupServerCompressionLevel
from ..models.backup_server_storage_optimization import BackupServerStorageOptimization
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_storage_settings_encryption import (
        BackupServerBackupJobStorageSettingsEncryption,
    )


T = TypeVar("T", bound="BackupServerBackupJobStorageSetting")


@_attrs_define
class BackupServerBackupJobStorageSetting:
    """Storage settings.

    Attributes:
        enable_inline_data_deduplication (Union[Unset, bool]): Indicates whether VM data deduplication is enabled.
            Default: True.
        exclude_swap_file_blocks (Union[Unset, bool]): Indicates whether swap file block exclusion is enabled. Default:
            True.
        exclude_deleted_file_blocks (Union[Unset, bool]): Indicates whether deleted file block copy is enabled. Default:
            True.
        compression_level (Union[Unset, BackupServerCompressionLevel]): Compression level.
        storage_optimization (Union[Unset, BackupServerStorageOptimization]): Storage optimization type.
            >256 KB - WANTarget
            >512 KB - LANTarget
            >1024 KB - LocalTarget
            >2048 KB - LocalTargetLarge
            >4096 KB - LocalTargetLarge4096
            >8192 KB - LocalTargetLarge8192
        encryption (Union[Unset, BackupServerBackupJobStorageSettingsEncryption]): Backup file encryption settings.
    """

    enable_inline_data_deduplication: Union[Unset, bool] = True
    exclude_swap_file_blocks: Union[Unset, bool] = True
    exclude_deleted_file_blocks: Union[Unset, bool] = True
    compression_level: Union[Unset, BackupServerCompressionLevel] = UNSET
    storage_optimization: Union[Unset, BackupServerStorageOptimization] = UNSET
    encryption: Union[Unset, "BackupServerBackupJobStorageSettingsEncryption"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable_inline_data_deduplication = self.enable_inline_data_deduplication

        exclude_swap_file_blocks = self.exclude_swap_file_blocks

        exclude_deleted_file_blocks = self.exclude_deleted_file_blocks

        compression_level: Union[Unset, str] = UNSET
        if not isinstance(self.compression_level, Unset):
            compression_level = self.compression_level.value

        storage_optimization: Union[Unset, str] = UNSET
        if not isinstance(self.storage_optimization, Unset):
            storage_optimization = self.storage_optimization.value

        encryption: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.encryption, Unset):
            encryption = self.encryption.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable_inline_data_deduplication is not UNSET:
            field_dict["enableInlineDataDeduplication"] = enable_inline_data_deduplication
        if exclude_swap_file_blocks is not UNSET:
            field_dict["excludeSwapFileBlocks"] = exclude_swap_file_blocks
        if exclude_deleted_file_blocks is not UNSET:
            field_dict["excludeDeletedFileBlocks"] = exclude_deleted_file_blocks
        if compression_level is not UNSET:
            field_dict["compressionLevel"] = compression_level
        if storage_optimization is not UNSET:
            field_dict["storageOptimization"] = storage_optimization
        if encryption is not UNSET:
            field_dict["encryption"] = encryption

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_backup_job_storage_settings_encryption import (
            BackupServerBackupJobStorageSettingsEncryption,
        )

        d = dict(src_dict)
        enable_inline_data_deduplication = d.pop("enableInlineDataDeduplication", UNSET)

        exclude_swap_file_blocks = d.pop("excludeSwapFileBlocks", UNSET)

        exclude_deleted_file_blocks = d.pop("excludeDeletedFileBlocks", UNSET)

        _compression_level = d.pop("compressionLevel", UNSET)
        compression_level: Union[Unset, BackupServerCompressionLevel]
        if isinstance(_compression_level, Unset):
            compression_level = UNSET
        else:
            compression_level = BackupServerCompressionLevel(_compression_level)

        _storage_optimization = d.pop("storageOptimization", UNSET)
        storage_optimization: Union[Unset, BackupServerStorageOptimization]
        if isinstance(_storage_optimization, Unset):
            storage_optimization = UNSET
        else:
            storage_optimization = BackupServerStorageOptimization(_storage_optimization)

        _encryption = d.pop("encryption", UNSET)
        encryption: Union[Unset, BackupServerBackupJobStorageSettingsEncryption]
        if isinstance(_encryption, Unset):
            encryption = UNSET
        else:
            encryption = BackupServerBackupJobStorageSettingsEncryption.from_dict(_encryption)

        backup_server_backup_job_storage_setting = cls(
            enable_inline_data_deduplication=enable_inline_data_deduplication,
            exclude_swap_file_blocks=exclude_swap_file_blocks,
            exclude_deleted_file_blocks=exclude_deleted_file_blocks,
            compression_level=compression_level,
            storage_optimization=storage_optimization,
            encryption=encryption,
        )

        backup_server_backup_job_storage_setting.additional_properties = d
        return backup_server_backup_job_storage_setting

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
