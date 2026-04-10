from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mac_backup_storage_block_size import MacBackupStorageBlockSize
from ..models.mac_backup_storage_compression_level import MacBackupStorageCompressionLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="MacBackupStorage")


@_attrs_define
class MacBackupStorage:
    """
    Attributes:
        compression_level (MacBackupStorageCompressionLevel | Unset): Compression level for the backup. Default:
            MacBackupStorageCompressionLevel.OPTIMAL.
        block_size (MacBackupStorageBlockSize | Unset): Type of data block size. Default:
            MacBackupStorageBlockSize.LOCAL1MB.
        encryption_enabled (bool | Unset): Indicates whether encryption is enabled.
            > Encryption cannot be enabled for backup files stored on a Veeam backup repository.
             Default: False.
        password (str | Unset): Password used for encryption.
            > Required if encryption is enabled.
        password_hint (str | Unset): Hint for a password.
            > The hint must not consist of the password.
    """

    compression_level: MacBackupStorageCompressionLevel | Unset = MacBackupStorageCompressionLevel.OPTIMAL
    block_size: MacBackupStorageBlockSize | Unset = MacBackupStorageBlockSize.LOCAL1MB
    encryption_enabled: bool | Unset = False
    password: str | Unset = UNSET
    password_hint: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        compression_level: str | Unset = UNSET
        if not isinstance(self.compression_level, Unset):
            compression_level = self.compression_level.value

        block_size: str | Unset = UNSET
        if not isinstance(self.block_size, Unset):
            block_size = self.block_size.value

        encryption_enabled = self.encryption_enabled

        password = self.password

        password_hint = self.password_hint

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compression_level is not UNSET:
            field_dict["compressionLevel"] = compression_level
        if block_size is not UNSET:
            field_dict["blockSize"] = block_size
        if encryption_enabled is not UNSET:
            field_dict["encryptionEnabled"] = encryption_enabled
        if password is not UNSET:
            field_dict["password"] = password
        if password_hint is not UNSET:
            field_dict["passwordHint"] = password_hint

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _compression_level = d.pop("compressionLevel", UNSET)
        compression_level: MacBackupStorageCompressionLevel | Unset
        if isinstance(_compression_level, Unset):
            compression_level = UNSET
        else:
            compression_level = MacBackupStorageCompressionLevel(_compression_level)

        _block_size = d.pop("blockSize", UNSET)
        block_size: MacBackupStorageBlockSize | Unset
        if isinstance(_block_size, Unset):
            block_size = UNSET
        else:
            block_size = MacBackupStorageBlockSize(_block_size)

        encryption_enabled = d.pop("encryptionEnabled", UNSET)

        password = d.pop("password", UNSET)

        password_hint = d.pop("passwordHint", UNSET)

        mac_backup_storage = cls(
            compression_level=compression_level,
            block_size=block_size,
            encryption_enabled=encryption_enabled,
            password=password,
            password_hint=password_hint,
        )

        mac_backup_storage.additional_properties = d
        return mac_backup_storage

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
