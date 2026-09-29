from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vdc_vault_tenant_status_readonly import VdcVaultTenantStatusReadonly
from ..types import UNSET, Unset

T = TypeVar("T", bound="VdcVaultTenant")


@_attrs_define
class VdcVaultTenant:
    """
    Attributes:
        instance_uid (UUID | Unset): UID assigned to a Veeam Data Cloud Vault tenant.
        name (str | Unset): Name of a Veeam Data Cloud Vault tenant.
        subscription_uid (UUID | Unset): UID assigned to a Veeam Data Cloud Vault subscription.
        organization_uid (None | Unset | UUID): UID assigned to a mapped company. The `null` value indicates that no
            company is mapped to the Veeam Data Cloud Vault tenant.
        vdc_status (VdcVaultTenantStatusReadonly | Unset): Status of a Veeam Data Cloud Vault tenant.
    """

    instance_uid: UUID | Unset = UNSET
    name: str | Unset = UNSET
    subscription_uid: UUID | Unset = UNSET
    organization_uid: None | Unset | UUID = UNSET
    vdc_status: VdcVaultTenantStatusReadonly | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        subscription_uid: str | Unset = UNSET
        if not isinstance(self.subscription_uid, Unset):
            subscription_uid = str(self.subscription_uid)

        organization_uid: None | str | Unset
        if isinstance(self.organization_uid, Unset):
            organization_uid = UNSET
        elif isinstance(self.organization_uid, UUID):
            organization_uid = str(self.organization_uid)
        else:
            organization_uid = self.organization_uid

        vdc_status: str | Unset = UNSET
        if not isinstance(self.vdc_status, Unset):
            vdc_status = self.vdc_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if name is not UNSET:
            field_dict["name"] = name
        if subscription_uid is not UNSET:
            field_dict["subscriptionUid"] = subscription_uid
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if vdc_status is not UNSET:
            field_dict["vdcStatus"] = vdc_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        name = d.pop("name", UNSET)

        _subscription_uid = d.pop("subscriptionUid", UNSET)
        subscription_uid: UUID | Unset
        if isinstance(_subscription_uid, Unset):
            subscription_uid = UNSET
        else:
            subscription_uid = UUID(_subscription_uid)

        def _parse_organization_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_uid_type_0 = UUID(data)

                return organization_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        organization_uid = _parse_organization_uid(d.pop("organizationUid", UNSET))

        _vdc_status = d.pop("vdcStatus", UNSET)
        vdc_status: VdcVaultTenantStatusReadonly | Unset
        if isinstance(_vdc_status, Unset):
            vdc_status = UNSET
        else:
            vdc_status = VdcVaultTenantStatusReadonly(_vdc_status)

        vdc_vault_tenant = cls(
            instance_uid=instance_uid,
            name=name,
            subscription_uid=subscription_uid,
            organization_uid=organization_uid,
            vdc_status=vdc_status,
        )

        vdc_vault_tenant.additional_properties = d
        return vdc_vault_tenant

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
