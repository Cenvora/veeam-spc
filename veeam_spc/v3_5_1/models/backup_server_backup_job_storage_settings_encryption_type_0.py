from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_encryption_type_nullable import BackupServerEncryptionTypeNullable
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerBackupJobStorageSettingsEncryptionType0")


@_attrs_define
class BackupServerBackupJobStorageSettingsEncryptionType0:
    """Backup file encryption settings.

    Attributes:
        is_enabled (Union[Unset, bool]): Indicates whether backup file content encryption is enabled. Default: False.
        encryption_type (Union[Unset, BackupServerEncryptionTypeNullable]): Type of backup file content encryption.
        encryption_password_id (Union[None, UUID, Unset]): ID assigned to a password used for encryption.
            >For exported objects, the property value is `null`.
        encryption_password_tag (Union[None, Unset, str]): Tag used to identify the password.
        kms_server_id (Union[None, UUID, Unset]): ID assigned to a Key Management Server.
    """

    is_enabled: Union[Unset, bool] = False
    encryption_type: Union[Unset, BackupServerEncryptionTypeNullable] = UNSET
    encryption_password_id: Union[None, UUID, Unset] = UNSET
    encryption_password_tag: Union[None, Unset, str] = UNSET
    kms_server_id: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        encryption_type: Union[Unset, str] = UNSET
        if not isinstance(self.encryption_type, Unset):
            encryption_type = self.encryption_type.value

        encryption_password_id: Union[None, Unset, str]
        if isinstance(self.encryption_password_id, Unset):
            encryption_password_id = UNSET
        elif isinstance(self.encryption_password_id, UUID):
            encryption_password_id = str(self.encryption_password_id)
        else:
            encryption_password_id = self.encryption_password_id

        encryption_password_tag: Union[None, Unset, str]
        if isinstance(self.encryption_password_tag, Unset):
            encryption_password_tag = UNSET
        else:
            encryption_password_tag = self.encryption_password_tag

        kms_server_id: Union[None, Unset, str]
        if isinstance(self.kms_server_id, Unset):
            kms_server_id = UNSET
        elif isinstance(self.kms_server_id, UUID):
            kms_server_id = str(self.kms_server_id)
        else:
            kms_server_id = self.kms_server_id

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

        def _parse_encryption_password_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                encryption_password_id_type_0 = UUID(data)

                return encryption_password_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        encryption_password_id = _parse_encryption_password_id(d.pop("encryptionPasswordId", UNSET))

        def _parse_encryption_password_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        encryption_password_tag = _parse_encryption_password_tag(d.pop("encryptionPasswordTag", UNSET))

        def _parse_kms_server_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kms_server_id_type_0 = UUID(data)

                return kms_server_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        kms_server_id = _parse_kms_server_id(d.pop("kmsServerId", UNSET))

        backup_server_backup_job_storage_settings_encryption_type_0 = cls(
            is_enabled=is_enabled,
            encryption_type=encryption_type,
            encryption_password_id=encryption_password_id,
            encryption_password_tag=encryption_password_tag,
            kms_server_id=kms_server_id,
        )

        backup_server_backup_job_storage_settings_encryption_type_0.additional_properties = d
        return backup_server_backup_job_storage_settings_encryption_type_0

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
