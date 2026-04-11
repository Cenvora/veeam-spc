from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vdc_storage_vault_status_readonly import VdcStorageVaultStatusReadonly
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vdc_storage_vault_embedded_type_0 import VdcStorageVaultEmbeddedType0


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
        storage_quota (int | None | Unset): Maximum amount of storage space available on storage vault, in bytes.
        consumed_space (int | Unset): Amount of consumed storage space, in bytes.
        status (VdcStorageVaultStatusReadonly | Unset): Storage vault status.
        read_only_reason (None | str | Unset): Reason for storage vault parameters to be read-only.
        field_embedded (None | Unset | VdcStorageVaultEmbeddedType0):
    """

    quota_enforced: bool
    is_read_only: bool
    instance_uid: UUID | Unset = UNSET
    name: str | Unset = UNSET
    tenant_uid: UUID | Unset = UNSET
    country_id: str | Unset = UNSET
    data_center_id: str | Unset = UNSET
    storage_quota: int | None | Unset = UNSET
    consumed_space: int | Unset = UNSET
    status: VdcStorageVaultStatusReadonly | Unset = UNSET
    read_only_reason: None | str | Unset = UNSET
    field_embedded: None | Unset | VdcStorageVaultEmbeddedType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.vdc_storage_vault_embedded_type_0 import VdcStorageVaultEmbeddedType0

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

        storage_quota: int | None | Unset
        if isinstance(self.storage_quota, Unset):
            storage_quota = UNSET
        else:
            storage_quota = self.storage_quota

        consumed_space = self.consumed_space

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        read_only_reason: None | str | Unset
        if isinstance(self.read_only_reason, Unset):
            read_only_reason = UNSET
        else:
            read_only_reason = self.read_only_reason

        field_embedded: dict[str, Any] | None | Unset
        if isinstance(self.field_embedded, Unset):
            field_embedded = UNSET
        elif isinstance(self.field_embedded, VdcStorageVaultEmbeddedType0):
            field_embedded = self.field_embedded.to_dict()
        else:
            field_embedded = self.field_embedded

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
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vdc_storage_vault_embedded_type_0 import VdcStorageVaultEmbeddedType0

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

        def _parse_storage_quota(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        storage_quota = _parse_storage_quota(d.pop("storageQuota", UNSET))

        consumed_space = d.pop("consumedSpace", UNSET)

        _status = d.pop("status", UNSET)
        status: VdcStorageVaultStatusReadonly | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = VdcStorageVaultStatusReadonly(_status)

        def _parse_read_only_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        read_only_reason = _parse_read_only_reason(d.pop("readOnlyReason", UNSET))

        def _parse_field_embedded(data: object) -> None | Unset | VdcStorageVaultEmbeddedType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_vdc_storage_vault_embedded_type_0 = VdcStorageVaultEmbeddedType0.from_dict(data)

                return componentsschemas_vdc_storage_vault_embedded_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VdcStorageVaultEmbeddedType0, data)

        field_embedded = _parse_field_embedded(d.pop("_embedded", UNSET))

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
