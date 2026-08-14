from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_veeam_vault_repository import BackupServerVeeamVaultRepository
    from ..models.response_error import ResponseError
    from ..models.response_metadata import ResponseMetadata


T = TypeVar("T", bound="PatchBackupServerVeeamVaultRepositoryResponse200")


@_attrs_define
class PatchBackupServerVeeamVaultRepositoryResponse200:
    r"""
    Attributes:
        data (BackupServerVeeamVaultRepository):  Example: {'description': 'Created by Veeam Service Provider Console
            VSPC1\\Administrator at 3/17/2026 2:03:57 PM.', 'name': 'ALpha Vault Repository', 'uniqueId':
            'F4B1ABA32F964CC5A5DF156E3DF5146E', 'taskLimitEnabled': False, 'maxTaskCount': 2, 'mountServer': {'type':
            'Windows', 'windows': {'mountServerId': '6745a759-2205-4cd2-b172-8ec8f7e60ef8', 'vPowerNFSEnabled': True,
            'writeCacheFolder': 'C:\\ProgramData\\Veeam\\Backup\\IRCache\\', 'vPowerNFSPortSettings': None}, 'linux': None},
            'account': {'vault': {'vaultId': 'b29dbf9c-93ec-4533-9b51-1df3a4e219f8', 'vaultName': 'vault1',
            'storageContainerName': 'immutable-vbr', 'isInitialized': True, 'folders': []}, 'connectionSettings':
            {'connectionType': 'Direct', 'gatewayServerIds': ['6745a759-2205-4cd2-b172-8ec8f7e60ef8']}}, 'container':
            {'folder': 'backup', 'storageConsumptionLimit': {'consumptionLimitCount': 10, 'isEnabled': False,
            'consumptionLimitKind': 'TB'}, 'immutability': {'isEnabled': True, 'daysCount': 10, 'immutabilityMode':
            'RepositorySettings'}}}.
        meta (ResponseMetadata | Unset):
        errors (list[ResponseError] | Unset):
    """

    data: BackupServerVeeamVaultRepository
    meta: ResponseMetadata | Unset = UNSET
    errors: list[ResponseError] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if meta is not UNSET:
            field_dict["meta"] = meta
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_veeam_vault_repository import BackupServerVeeamVaultRepository
        from ..models.response_error import ResponseError
        from ..models.response_metadata import ResponseMetadata

        d = dict(src_dict)
        data = BackupServerVeeamVaultRepository.from_dict(d.pop("data"))

        _meta = d.pop("meta", UNSET)
        meta: ResponseMetadata | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ResponseMetadata.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[ResponseError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = ResponseError.from_dict(errors_item_data)

                errors.append(errors_item)

        patch_backup_server_veeam_vault_repository_response_200 = cls(
            data=data,
            meta=meta,
            errors=errors,
        )

        patch_backup_server_veeam_vault_repository_response_200.additional_properties = d
        return patch_backup_server_veeam_vault_repository_response_200

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
