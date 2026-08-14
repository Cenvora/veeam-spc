from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vdc_storage_vault_status_readonly import VdcStorageVaultStatusReadonly
from ..models.vdc_vault_platform import VdcVaultPlatform
from ..models.vdc_vault_type import VdcVaultType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vdc_storage_vault_embedded import VdcStorageVaultEmbedded


T = TypeVar("T", bound="VdcStorageVault")


@_attrs_define
class VdcStorageVault:
    """
    Attributes:
        quota_enforced (bool): Indicates whether maximum amount of available storage space is a hard quota.
        is_read_only (bool): Indicates whether storage vault parameters are read-only.
        instance_uid (UUID | Unset): UID assigned to a Veeam Data Cloud Vault tenant.
        name (str | Unset): UID assigned to a storage vault.
        tenant_uid (UUID | Unset): Name of a storage vault.
        country_id (str | Unset): ID assigned to a country in Veeam Data Cloud Vault.
        data_center_id (str | Unset): ID assigned to a data center.
        storage_quota (int | Unset): Maximum amount of storage space available on storage vault, in bytes.
        consumed_space (int | Unset): Amount of consumed storage space, in bytes.
        status (VdcStorageVaultStatusReadonly | Unset): Storage vault status.
        read_only_reason (str | Unset): Reason for storage vault parameters to be read-only.
        vault_type (VdcVaultType | Unset): Type of a Veeam Data Cloud storage vault.
        platform (VdcVaultPlatform | Unset): Cloud platform of a Veeam Data Cloud storage vault.
        field_embedded (VdcStorageVaultEmbedded | Unset):
    """

    quota_enforced: bool
    is_read_only: bool
    instance_uid: UUID | Unset = UNSET
    name: str | Unset = UNSET
    tenant_uid: UUID | Unset = UNSET
    country_id: str | Unset = UNSET
    data_center_id: str | Unset = UNSET
    storage_quota: int | Unset = UNSET
    consumed_space: int | Unset = UNSET
    status: VdcStorageVaultStatusReadonly | Unset = UNSET
    read_only_reason: str | Unset = UNSET
    vault_type: VdcVaultType | Unset = UNSET
    platform: VdcVaultPlatform | Unset = UNSET
    field_embedded: VdcStorageVaultEmbedded | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quota_enforced = self.quota_enforced

        is_read_only = self.is_read_only

        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        tenant_uid: str | Unset = UNSET
        if not isinstance(self.tenant_uid, Unset):
            tenant_uid = str(self.tenant_uid)

        country_id = self.country_id

        data_center_id = self.data_center_id

        storage_quota = self.storage_quota

        consumed_space = self.consumed_space

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        read_only_reason = self.read_only_reason

        vault_type: str | Unset = UNSET
        if not isinstance(self.vault_type, Unset):
            vault_type = self.vault_type.value

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        field_embedded: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_embedded, Unset):
            field_embedded = self.field_embedded.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quotaEnforced": quota_enforced,
                "isReadOnly": is_read_only,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if name is not UNSET:
            field_dict["name"] = name
        if tenant_uid is not UNSET:
            field_dict["tenantUid"] = tenant_uid
        if country_id is not UNSET:
            field_dict["countryId"] = country_id
        if data_center_id is not UNSET:
            field_dict["dataCenterId"] = data_center_id
        if storage_quota is not UNSET:
            field_dict["storageQuota"] = storage_quota
        if consumed_space is not UNSET:
            field_dict["consumedSpace"] = consumed_space
        if status is not UNSET:
            field_dict["status"] = status
        if read_only_reason is not UNSET:
            field_dict["readOnlyReason"] = read_only_reason
        if vault_type is not UNSET:
            field_dict["vaultType"] = vault_type
        if platform is not UNSET:
            field_dict["platform"] = platform
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vdc_storage_vault_embedded import VdcStorageVaultEmbedded

        d = dict(src_dict)
        quota_enforced = d.pop("quotaEnforced")

        is_read_only = d.pop("isReadOnly")

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        name = d.pop("name", UNSET)

        _tenant_uid = d.pop("tenantUid", UNSET)
        tenant_uid: UUID | Unset
        if isinstance(_tenant_uid, Unset):
            tenant_uid = UNSET
        else:
            tenant_uid = UUID(_tenant_uid)

        country_id = d.pop("countryId", UNSET)

        data_center_id = d.pop("dataCenterId", UNSET)

        storage_quota = d.pop("storageQuota", UNSET)

        consumed_space = d.pop("consumedSpace", UNSET)

        _status = d.pop("status", UNSET)
        status: VdcStorageVaultStatusReadonly | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = VdcStorageVaultStatusReadonly(_status)

        read_only_reason = d.pop("readOnlyReason", UNSET)

        _vault_type = d.pop("vaultType", UNSET)
        vault_type: VdcVaultType | Unset
        if isinstance(_vault_type, Unset):
            vault_type = UNSET
        else:
            vault_type = VdcVaultType(_vault_type)

        _platform = d.pop("platform", UNSET)
        platform: VdcVaultPlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = VdcVaultPlatform(_platform)

        _field_embedded = d.pop("_embedded", UNSET)
        field_embedded: VdcStorageVaultEmbedded | Unset
        if isinstance(_field_embedded, Unset):
            field_embedded = UNSET
        else:
            field_embedded = VdcStorageVaultEmbedded.from_dict(_field_embedded)

        vdc_storage_vault = cls(
            quota_enforced=quota_enforced,
            is_read_only=is_read_only,
            instance_uid=instance_uid,
            name=name,
            tenant_uid=tenant_uid,
            country_id=country_id,
            data_center_id=data_center_id,
            storage_quota=storage_quota,
            consumed_space=consumed_space,
            status=status,
            read_only_reason=read_only_reason,
            vault_type=vault_type,
            platform=platform,
            field_embedded=field_embedded,
        )

        vdc_storage_vault.additional_properties = d
        return vdc_storage_vault

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
