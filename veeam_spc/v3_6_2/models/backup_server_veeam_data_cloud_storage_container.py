from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_object_storage_consumption_limit import BackupServerObjectStorageConsumptionLimit
    from ..models.backup_server_object_storage_immutability import BackupServerObjectStorageImmutability


T = TypeVar("T", bound="BackupServerVeeamDataCloudStorageContainer")


@_attrs_define
class BackupServerVeeamDataCloudStorageContainer:
    """Storage container settings.

    Attributes:
        folder (str): Name of a storage container.
        storage_consumption_limit (BackupServerObjectStorageConsumptionLimit | Unset):
        immutability (BackupServerObjectStorageImmutability | Unset):
    """

    folder: str
    storage_consumption_limit: BackupServerObjectStorageConsumptionLimit | Unset = UNSET
    immutability: BackupServerObjectStorageImmutability | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        folder = self.folder

        storage_consumption_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage_consumption_limit, Unset):
            storage_consumption_limit = self.storage_consumption_limit.to_dict()

        immutability: dict[str, Any] | Unset = UNSET
        if not isinstance(self.immutability, Unset):
            immutability = self.immutability.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "folder": folder,
            }
        )
        if storage_consumption_limit is not UNSET:
            field_dict["storageConsumptionLimit"] = storage_consumption_limit
        if immutability is not UNSET:
            field_dict["immutability"] = immutability

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_object_storage_consumption_limit import BackupServerObjectStorageConsumptionLimit
        from ..models.backup_server_object_storage_immutability import BackupServerObjectStorageImmutability

        d = dict(src_dict)
        folder = d.pop("folder")

        _storage_consumption_limit = d.pop("storageConsumptionLimit", UNSET)
        storage_consumption_limit: BackupServerObjectStorageConsumptionLimit | Unset
        if isinstance(_storage_consumption_limit, Unset):
            storage_consumption_limit = UNSET
        else:
            storage_consumption_limit = BackupServerObjectStorageConsumptionLimit.from_dict(_storage_consumption_limit)

        _immutability = d.pop("immutability", UNSET)
        immutability: BackupServerObjectStorageImmutability | Unset
        if isinstance(_immutability, Unset):
            immutability = UNSET
        else:
            immutability = BackupServerObjectStorageImmutability.from_dict(_immutability)

        backup_server_veeam_data_cloud_storage_container = cls(
            folder=folder,
            storage_consumption_limit=storage_consumption_limit,
            immutability=immutability,
        )

        backup_server_veeam_data_cloud_storage_container.additional_properties = d
        return backup_server_veeam_data_cloud_storage_container

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
