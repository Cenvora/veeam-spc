from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VdcVaultTenantInput")


@_attrs_define
class VdcVaultTenantInput:
    """
    Attributes:
        tenant_name (str): Name of a Veeam Data Cloud Vault tenant.
        subscription_uid (UUID): UID assigned to a Veeam Data Cloud Vault subscription.
    """

    tenant_name: str
    subscription_uid: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tenant_name = self.tenant_name

        subscription_uid = str(self.subscription_uid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tenantName": tenant_name,
                "subscriptionUid": subscription_uid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tenant_name = d.pop("tenantName")

        subscription_uid = UUID(d.pop("subscriptionUid"))

        vdc_vault_tenant_input = cls(
            tenant_name=tenant_name,
            subscription_uid=subscription_uid,
        )

        vdc_vault_tenant_input.additional_properties = d
        return vdc_vault_tenant_input

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
