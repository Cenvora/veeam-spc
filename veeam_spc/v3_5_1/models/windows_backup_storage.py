from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.windows_backup_storage_compression_level import WindowsBackupStorageCompressionLevel
from ..models.windows_backup_storage_storage_optimization import WindowsBackupStorageStorageOptimization
from ..types import UNSET, Unset

T = TypeVar("T", bound="WindowsBackupStorage")


@_attrs_define
class WindowsBackupStorage:
    """
    Attributes:
        compression_level (Union[Unset, WindowsBackupStorageCompressionLevel]): Compression level for the backup.
            Default: WindowsBackupStorageCompressionLevel.OPTIMAL.
        storage_optimization (Union[Unset, WindowsBackupStorageStorageOptimization]): Type of a backup target. Default:
            WindowsBackupStorageStorageOptimization.LOCAL.
        encryption_enabled (Union[Unset, bool]): Indicates whether encryption is enabled.
            > Encryption cannot be enabled for backup files stored on the Veeam backup repository.
             Default: False.
        password (Union[None, Unset, str]): Password used for encryption.
            > Required if encryption is enabled.
        password_hint (Union[None, Unset, str]): Hint for the password.
            > Must not consist of the password itself.
    """

    compression_level: Union[Unset, WindowsBackupStorageCompressionLevel] = WindowsBackupStorageCompressionLevel.OPTIMAL
    storage_optimization: Union[Unset, WindowsBackupStorageStorageOptimization] = (
        WindowsBackupStorageStorageOptimization.LOCAL
    )
    encryption_enabled: Union[Unset, bool] = False
    password: Union[None, Unset, str] = UNSET
    password_hint: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        compression_level: Union[Unset, str] = UNSET
        if not isinstance(self.compression_level, Unset):
            compression_level = self.compression_level.value

        storage_optimization: Union[Unset, str] = UNSET
        if not isinstance(self.storage_optimization, Unset):
            storage_optimization = self.storage_optimization.value

        encryption_enabled = self.encryption_enabled

        password: Union[None, Unset, str]
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        password_hint: Union[None, Unset, str]
        if isinstance(self.password_hint, Unset):
            password_hint = UNSET
        else:
            password_hint = self.password_hint

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compression_level is not UNSET:
            field_dict["compressionLevel"] = compression_level
        if storage_optimization is not UNSET:
            field_dict["storageOptimization"] = storage_optimization
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
        compression_level: Union[Unset, WindowsBackupStorageCompressionLevel]
        if isinstance(_compression_level, Unset):
            compression_level = UNSET
        else:
            compression_level = WindowsBackupStorageCompressionLevel(_compression_level)

        _storage_optimization = d.pop("storageOptimization", UNSET)
        storage_optimization: Union[Unset, WindowsBackupStorageStorageOptimization]
        if isinstance(_storage_optimization, Unset):
            storage_optimization = UNSET
        else:
            storage_optimization = WindowsBackupStorageStorageOptimization(_storage_optimization)

        encryption_enabled = d.pop("encryptionEnabled", UNSET)

        def _parse_password(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        password = _parse_password(d.pop("password", UNSET))

        def _parse_password_hint(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        password_hint = _parse_password_hint(d.pop("passwordHint", UNSET))

        windows_backup_storage = cls(
            compression_level=compression_level,
            storage_optimization=storage_optimization,
            encryption_enabled=encryption_enabled,
            password=password,
            password_hint=password_hint,
        )

        windows_backup_storage.additional_properties = d
        return windows_backup_storage

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
