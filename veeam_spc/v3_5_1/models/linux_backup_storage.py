from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.linux_backup_storage_block_size import LinuxBackupStorageBlockSize
from ..models.linux_backup_storage_compression_level import LinuxBackupStorageCompressionLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="LinuxBackupStorage")


@_attrs_define
class LinuxBackupStorage:
    """
    Attributes:
        compression_level (Union[Unset, LinuxBackupStorageCompressionLevel]): Compression level for the backup. Default:
            LinuxBackupStorageCompressionLevel.OPTIMAL.
        block_size (Union[Unset, LinuxBackupStorageBlockSize]): Type of data block size. Default:
            LinuxBackupStorageBlockSize.LOCAL.
        encryption_enabled (Union[Unset, bool]): Indicates whether encryption is enabled.
            > Encryption cannot be enabled for backup files stored on the Veeam backup repository.
             Default: False.
        password (Union[Unset, str]): Password used for encryption.
            > Required if encryption is enabled.
        password_hint (Union[Unset, str]): Hint for the password.
            > The hint must not consist of the password.
        is_snapshot_required (Union[Unset, bool]): Indicates whether Veeam Agent for Linux must create a snapshot of a
            backed-up volume during backup. Default: True.
    """

    compression_level: Union[Unset, LinuxBackupStorageCompressionLevel] = LinuxBackupStorageCompressionLevel.OPTIMAL
    block_size: Union[Unset, LinuxBackupStorageBlockSize] = LinuxBackupStorageBlockSize.LOCAL
    encryption_enabled: Union[Unset, bool] = False
    password: Union[Unset, str] = UNSET
    password_hint: Union[Unset, str] = UNSET
    is_snapshot_required: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        compression_level: Union[Unset, str] = UNSET
        if not isinstance(self.compression_level, Unset):
            compression_level = self.compression_level.value

        block_size: Union[Unset, str] = UNSET
        if not isinstance(self.block_size, Unset):
            block_size = self.block_size.value

        encryption_enabled = self.encryption_enabled

        password = self.password

        password_hint = self.password_hint

        is_snapshot_required = self.is_snapshot_required

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
        if is_snapshot_required is not UNSET:
            field_dict["isSnapshotRequired"] = is_snapshot_required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _compression_level = d.pop("compressionLevel", UNSET)
        compression_level: Union[Unset, LinuxBackupStorageCompressionLevel]
        if isinstance(_compression_level, Unset):
            compression_level = UNSET
        else:
            compression_level = LinuxBackupStorageCompressionLevel(_compression_level)

        _block_size = d.pop("blockSize", UNSET)
        block_size: Union[Unset, LinuxBackupStorageBlockSize]
        if isinstance(_block_size, Unset):
            block_size = UNSET
        else:
            block_size = LinuxBackupStorageBlockSize(_block_size)

        encryption_enabled = d.pop("encryptionEnabled", UNSET)

        password = d.pop("password", UNSET)

        password_hint = d.pop("passwordHint", UNSET)

        is_snapshot_required = d.pop("isSnapshotRequired", UNSET)

        linux_backup_storage = cls(
            compression_level=compression_level,
            block_size=block_size,
            encryption_enabled=encryption_enabled,
            password=password,
            password_hint=password_hint,
            is_snapshot_required=is_snapshot_required,
        )

        linux_backup_storage.additional_properties = d
        return linux_backup_storage

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
