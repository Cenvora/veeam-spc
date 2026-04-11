from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vdc_vault_country import VdcVaultCountry
    from ..models.vdc_vault_data_center import VdcVaultDataCenter
    from ..models.vdc_vault_subscription import VdcVaultSubscription
    from ..models.vdc_vault_tenant import VdcVaultTenant


T = TypeVar("T", bound="VdcStorageVaultEmbeddedType0")


@_attrs_define
class VdcStorageVaultEmbeddedType0:
    """
    Attributes:
        country (VdcVaultCountry | Unset):
        data_center (VdcVaultDataCenter | Unset):
        tenant (VdcVaultTenant | Unset):
        subscription (VdcVaultSubscription | Unset):
    """

    country: VdcVaultCountry | Unset = UNSET
    data_center: VdcVaultDataCenter | Unset = UNSET
    tenant: VdcVaultTenant | Unset = UNSET
    subscription: VdcVaultSubscription | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country: dict[str, Any] | Unset = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.to_dict()

        data_center: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_center, Unset):
            data_center = self.data_center.to_dict()

        tenant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tenant, Unset):
            tenant = self.tenant.to_dict()

        subscription: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subscription, Unset):
            subscription = self.subscription.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country is not UNSET:
            field_dict["country"] = country
        if data_center is not UNSET:
            field_dict["dataCenter"] = data_center
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if subscription is not UNSET:
            field_dict["subscription"] = subscription

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vdc_vault_country import VdcVaultCountry
        from ..models.vdc_vault_data_center import VdcVaultDataCenter
        from ..models.vdc_vault_subscription import VdcVaultSubscription
        from ..models.vdc_vault_tenant import VdcVaultTenant

        d = dict(src_dict)
        _country = d.pop("country", UNSET)
        country: VdcVaultCountry | Unset
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = VdcVaultCountry.from_dict(_country)

        _data_center = d.pop("dataCenter", UNSET)
        data_center: VdcVaultDataCenter | Unset
        if isinstance(_data_center, Unset):
            data_center = UNSET
        else:
            data_center = VdcVaultDataCenter.from_dict(_data_center)

        _tenant = d.pop("tenant", UNSET)
        tenant: VdcVaultTenant | Unset
        if isinstance(_tenant, Unset):
            tenant = UNSET
        else:
            tenant = VdcVaultTenant.from_dict(_tenant)

        _subscription = d.pop("subscription", UNSET)
        subscription: VdcVaultSubscription | Unset
        if isinstance(_subscription, Unset):
            subscription = UNSET
        else:
            subscription = VdcVaultSubscription.from_dict(_subscription)

        vdc_storage_vault_embedded_type_0 = cls(
            country=country,
            data_center=data_center,
            tenant=tenant,
            subscription=subscription,
        )

        vdc_storage_vault_embedded_type_0.additional_properties = d
        return vdc_storage_vault_embedded_type_0

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
