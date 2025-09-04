from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_encryption_type_nullable import BackupServerEncryptionTypeNullable
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerBackupJobStorageSettingsEncryption")


@_attrs_define
class BackupServerBackupJobStorageSettingsEncryption:
    """Backup file encryption settings.

    Attributes:
        is_enabled (Union[Unset, bool]): Indicates whether backup file content encryption is enabled. Default: False.
        encryption_type (Union[Unset, BackupServerEncryptionTypeNullable]): Type of backup file content encryption.
        encryption_password_id (Union[Unset, UUID]): ID assigned to a password used for encryption.
            >For exported objects, the property value is `null`.
        encryption_password_tag (Union[Unset, str]): Tag used to identify the password.
        kms_server_id (Union[Unset, UUID]): ID assigned to a Key Management Server.
    """

    is_enabled: Union[Unset, bool] = False
    encryption_type: Union[Unset, BackupServerEncryptionTypeNullable] = UNSET
    encryption_password_id: Union[Unset, UUID] = UNSET
    encryption_password_tag: Union[Unset, str] = UNSET
    kms_server_id: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        encryption_type: Union[Unset, str] = UNSET
        if not isinstance(self.encryption_type, Unset):
            encryption_type = self.encryption_type.value

        encryption_password_id: Union[Unset, str] = UNSET
        if not isinstance(self.encryption_password_id, Unset):
            encryption_password_id = str(self.encryption_password_id)

        encryption_password_tag = self.encryption_password_tag

        kms_server_id: Union[Unset, str] = UNSET
        if not isinstance(self.kms_server_id, Unset):
            kms_server_id = str(self.kms_server_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if encryption_type is not UNSET:
            field_dict["encryptionType"] = encryption_type
        if encryption_password_id is not UNSET:
            field_dict["encryptionPasswordId"] = encryption_password_id
        if encryption_password_tag is not UNSET:
            field_dict["encryptionPasswordTag"] = encryption_password_tag
        if kms_server_id is not UNSET:
            field_dict["kmsServerId"] = kms_server_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_enabled = d.pop("isEnabled", UNSET)

        _encryption_type = d.pop("encryptionType", UNSET)
        encryption_type: Union[Unset, BackupServerEncryptionTypeNullable]
        if isinstance(_encryption_type, Unset):
            encryption_type = UNSET
        else:
            encryption_type = BackupServerEncryptionTypeNullable(_encryption_type)

        _encryption_password_id = d.pop("encryptionPasswordId", UNSET)
        encryption_password_id: Union[Unset, UUID]
        if isinstance(_encryption_password_id, Unset):
            encryption_password_id = UNSET
        else:
            encryption_password_id = UUID(_encryption_password_id)

        encryption_password_tag = d.pop("encryptionPasswordTag", UNSET)

        _kms_server_id = d.pop("kmsServerId", UNSET)
        kms_server_id: Union[Unset, UUID]
        if isinstance(_kms_server_id, Unset):
            kms_server_id = UNSET
        else:
            kms_server_id = UUID(_kms_server_id)

        backup_server_backup_job_storage_settings_encryption = cls(
            is_enabled=is_enabled,
            encryption_type=encryption_type,
            encryption_password_id=encryption_password_id,
            encryption_password_tag=encryption_password_tag,
            kms_server_id=kms_server_id,
        )

        backup_server_backup_job_storage_settings_encryption.additional_properties = d
        return backup_server_backup_job_storage_settings_encryption

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
