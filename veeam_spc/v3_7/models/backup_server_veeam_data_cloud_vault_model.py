from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerVeeamDataCloudVaultModel")


@_attrs_define
class BackupServerVeeamDataCloudVaultModel:
    """Veeam Data Cloud Vault parameters.

    Attributes:
        vault_id (str): Veeam Data Cloud Vault ID.
        is_initialized (bool): Indicates whether a Veeam Data Cloud Vault is initialized.
        vault_name (None | str | Unset): Name of a Veeam Data Cloud Vault.
        storage_container_name (None | str | Unset): Name of a storage container.
        folders (list[str] | None | Unset): Array of folders located in the storage container.
    """

    vault_id: str
    is_initialized: bool
    vault_name: None | str | Unset = UNSET
    storage_container_name: None | str | Unset = UNSET
    folders: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vault_id = self.vault_id

        is_initialized = self.is_initialized

        vault_name: None | str | Unset
        if isinstance(self.vault_name, Unset):
            vault_name = UNSET
        else:
            vault_name = self.vault_name

        storage_container_name: None | str | Unset
        if isinstance(self.storage_container_name, Unset):
            storage_container_name = UNSET
        else:
            storage_container_name = self.storage_container_name

        folders: list[str] | None | Unset
        if isinstance(self.folders, Unset):
            folders = UNSET
        elif isinstance(self.folders, list):
            folders = self.folders

        else:
            folders = self.folders

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vaultId": vault_id,
                "isInitialized": is_initialized,
            }
        )
        if vault_name is not UNSET:
            field_dict["vaultName"] = vault_name
        if storage_container_name is not UNSET:
            field_dict["storageContainerName"] = storage_container_name
        if folders is not UNSET:
            field_dict["folders"] = folders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vault_id = d.pop("vaultId")

        is_initialized = d.pop("isInitialized")

        def _parse_vault_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vault_name = _parse_vault_name(d.pop("vaultName", UNSET))

        def _parse_storage_container_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_container_name = _parse_storage_container_name(d.pop("storageContainerName", UNSET))

        def _parse_folders(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                folders_type_0 = cast(list[str], data)

                return folders_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        folders = _parse_folders(d.pop("folders", UNSET))

        backup_server_veeam_data_cloud_vault_model = cls(
            vault_id=vault_id,
            is_initialized=is_initialized,
            vault_name=vault_name,
            storage_container_name=storage_container_name,
            folders=folders,
        )

        backup_server_veeam_data_cloud_vault_model.additional_properties = d
        return backup_server_veeam_data_cloud_vault_model

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
