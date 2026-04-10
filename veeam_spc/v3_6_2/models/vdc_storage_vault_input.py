from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VdcStorageVaultInput")


@_attrs_define
class VdcStorageVaultInput:
    """
    Attributes:
        tenant_uid (UUID): UID assigned to a Veeam Data Cloud Vault tenant.
        name (str): Name of a storage vault.
        data_center_id (str): ID assigned to a data center.
        quota_enforced (bool): Indicates whether maximum amount of available storage space is a hard quota.
        storage_quota (int | Unset): Maximum amount of storage space available on storage vault.
    """

    tenant_uid: UUID
    name: str
    data_center_id: str
    quota_enforced: bool
    storage_quota: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tenant_uid = str(self.tenant_uid)

        name = self.name

        data_center_id = self.data_center_id

        quota_enforced = self.quota_enforced

        storage_quota = self.storage_quota

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tenantUid": tenant_uid,
                "name": name,
                "dataCenterId": data_center_id,
                "quotaEnforced": quota_enforced,
            }
        )
        if storage_quota is not UNSET:
            field_dict["storageQuota"] = storage_quota

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tenant_uid = UUID(d.pop("tenantUid"))

        name = d.pop("name")

        data_center_id = d.pop("dataCenterId")

        quota_enforced = d.pop("quotaEnforced")

        storage_quota = d.pop("storageQuota", UNSET)

        vdc_storage_vault_input = cls(
            tenant_uid=tenant_uid,
            name=name,
            data_center_id=data_center_id,
            quota_enforced=quota_enforced,
            storage_quota=storage_quota,
        )

        vdc_storage_vault_input.additional_properties = d
        return vdc_storage_vault_input

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
