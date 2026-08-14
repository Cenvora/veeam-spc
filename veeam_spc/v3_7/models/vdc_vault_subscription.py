from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vdc_vault_subscription_edition import VdcVaultSubscriptionEdition
from ..models.vdc_vault_subscription_managed_organization_type import VdcVaultSubscriptionManagedOrganizationType
from ..models.vdc_vault_subscription_status import VdcVaultSubscriptionStatus
from ..models.vdc_vault_subscription_type import VdcVaultSubscriptionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="VdcVaultSubscription")


@_attrs_define
class VdcVaultSubscription:
    """
    Attributes:
        instance_uid (UUID | Unset): UID assigned to a Veeam Data Cloud Vault subscription.
        name (str | Unset): Veeam Data Cloud Vault subscription name.
        edition (VdcVaultSubscriptionEdition | Unset): Edition of a Veeam Data Cloud Vault subscription.
        type_ (VdcVaultSubscriptionType | Unset): Type of a Veeam Data Cloud Vault subscription.
        status (VdcVaultSubscriptionStatus | Unset): Status of a Veeam Data Cloud Vault subscription.
        managed_organization_type (VdcVaultSubscriptionManagedOrganizationType | Unset): Type of an organization managed
            by a Veeam Data Cloud Vault subscription.
    """

    instance_uid: UUID | Unset = UNSET
    name: str | Unset = UNSET
    edition: VdcVaultSubscriptionEdition | Unset = UNSET
    type_: VdcVaultSubscriptionType | Unset = UNSET
    status: VdcVaultSubscriptionStatus | Unset = UNSET
    managed_organization_type: VdcVaultSubscriptionManagedOrganizationType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        edition: str | Unset = UNSET
        if not isinstance(self.edition, Unset):
            edition = self.edition.value

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        managed_organization_type: str | Unset = UNSET
        if not isinstance(self.managed_organization_type, Unset):
            managed_organization_type = self.managed_organization_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if name is not UNSET:
            field_dict["name"] = name
        if edition is not UNSET:
            field_dict["edition"] = edition
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if managed_organization_type is not UNSET:
            field_dict["managedOrganizationType"] = managed_organization_type

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

        _edition = d.pop("edition", UNSET)
        edition: VdcVaultSubscriptionEdition | Unset
        if isinstance(_edition, Unset):
            edition = UNSET
        else:
            edition = VdcVaultSubscriptionEdition(_edition)

        _type_ = d.pop("type", UNSET)
        type_: VdcVaultSubscriptionType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = VdcVaultSubscriptionType(_type_)

        _status = d.pop("status", UNSET)
        status: VdcVaultSubscriptionStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = VdcVaultSubscriptionStatus(_status)

        _managed_organization_type = d.pop("managedOrganizationType", UNSET)
        managed_organization_type: VdcVaultSubscriptionManagedOrganizationType | Unset
        if isinstance(_managed_organization_type, Unset):
            managed_organization_type = UNSET
        else:
            managed_organization_type = VdcVaultSubscriptionManagedOrganizationType(_managed_organization_type)

        vdc_vault_subscription = cls(
            instance_uid=instance_uid,
            name=name,
            edition=edition,
            type_=type_,
            status=status,
            managed_organization_type=managed_organization_type,
        )

        vdc_vault_subscription.additional_properties = d
        return vdc_vault_subscription

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
