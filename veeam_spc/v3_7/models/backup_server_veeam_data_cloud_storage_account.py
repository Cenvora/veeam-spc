from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_object_storage_connection import BackupServerObjectStorageConnection
    from ..models.backup_server_veeam_data_cloud_vault_model import BackupServerVeeamDataCloudVaultModel


T = TypeVar("T", bound="BackupServerVeeamDataCloudStorageAccount")


@_attrs_define
class BackupServerVeeamDataCloudStorageAccount:
    """Veeam account settings.

    Attributes:
        vault (BackupServerVeeamDataCloudVaultModel): Veeam Data Cloud Vault parameters.
        connection_settings (BackupServerObjectStorageConnection | Unset):
    """

    vault: BackupServerVeeamDataCloudVaultModel
    connection_settings: BackupServerObjectStorageConnection | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vault = self.vault.to_dict()

        connection_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connection_settings, Unset):
            connection_settings = self.connection_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vault": vault,
            }
        )
        if connection_settings is not UNSET:
            field_dict["connectionSettings"] = connection_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_object_storage_connection import BackupServerObjectStorageConnection
        from ..models.backup_server_veeam_data_cloud_vault_model import BackupServerVeeamDataCloudVaultModel

        d = dict(src_dict)
        vault = BackupServerVeeamDataCloudVaultModel.from_dict(d.pop("vault"))

        _connection_settings = d.pop("connectionSettings", UNSET)
        connection_settings: BackupServerObjectStorageConnection | Unset
        if isinstance(_connection_settings, Unset):
            connection_settings = UNSET
        else:
            connection_settings = BackupServerObjectStorageConnection.from_dict(_connection_settings)

        backup_server_veeam_data_cloud_storage_account = cls(
            vault=vault,
            connection_settings=connection_settings,
        )

        backup_server_veeam_data_cloud_storage_account.additional_properties = d
        return backup_server_veeam_data_cloud_storage_account

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
