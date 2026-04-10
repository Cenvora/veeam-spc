from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vb_365_on_premises_microsoft_exchange_settings import Vb365OnPremisesMicrosoftExchangeSettings
    from ..models.vb_365_on_premises_microsoft_share_point_settings import Vb365OnPremisesMicrosoftSharePointSettings
    from ..models.vb_365_organization_children_embedded import Vb365OrganizationChildrenEmbedded


T = TypeVar("T", bound="Vb365OnPremisesMicrosoftOrganization")


@_attrs_define
class Vb365OnPremisesMicrosoftOrganization:
    """
    Attributes:
        name (str): Name of an on-premises Microsoft organization.
        instance_uid (UUID | Unset): UID assigned to an on-premises Microsoft organization in Veeam Service Provider
            Console.
        share_point_settings (Vb365OnPremisesMicrosoftSharePointSettings | Unset):
        exchange_settings (Vb365OnPremisesMicrosoftExchangeSettings | Unset):
        field_embedded (Vb365OrganizationChildrenEmbedded | Unset):
    """

    name: str
    instance_uid: UUID | Unset = UNSET
    share_point_settings: Vb365OnPremisesMicrosoftSharePointSettings | Unset = UNSET
    exchange_settings: Vb365OnPremisesMicrosoftExchangeSettings | Unset = UNSET
    field_embedded: Vb365OrganizationChildrenEmbedded | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        share_point_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.share_point_settings, Unset):
            share_point_settings = self.share_point_settings.to_dict()

        exchange_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.exchange_settings, Unset):
            exchange_settings = self.exchange_settings.to_dict()

        field_embedded: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_embedded, Unset):
            field_embedded = self.field_embedded.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if share_point_settings is not UNSET:
            field_dict["sharePointSettings"] = share_point_settings
        if exchange_settings is not UNSET:
            field_dict["exchangeSettings"] = exchange_settings
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vb_365_on_premises_microsoft_exchange_settings import Vb365OnPremisesMicrosoftExchangeSettings
        from ..models.vb_365_on_premises_microsoft_share_point_settings import (
            Vb365OnPremisesMicrosoftSharePointSettings,
        )
        from ..models.vb_365_organization_children_embedded import Vb365OrganizationChildrenEmbedded

        d = dict(src_dict)
        name = d.pop("name")

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _share_point_settings = d.pop("sharePointSettings", UNSET)
        share_point_settings: Vb365OnPremisesMicrosoftSharePointSettings | Unset
        if isinstance(_share_point_settings, Unset):
            share_point_settings = UNSET
        else:
            share_point_settings = Vb365OnPremisesMicrosoftSharePointSettings.from_dict(_share_point_settings)

        _exchange_settings = d.pop("exchangeSettings", UNSET)
        exchange_settings: Vb365OnPremisesMicrosoftExchangeSettings | Unset
        if isinstance(_exchange_settings, Unset):
            exchange_settings = UNSET
        else:
            exchange_settings = Vb365OnPremisesMicrosoftExchangeSettings.from_dict(_exchange_settings)

        _field_embedded = d.pop("_embedded", UNSET)
        field_embedded: Vb365OrganizationChildrenEmbedded | Unset
        if isinstance(_field_embedded, Unset):
            field_embedded = UNSET
        else:
            field_embedded = Vb365OrganizationChildrenEmbedded.from_dict(_field_embedded)

        vb_365_on_premises_microsoft_organization = cls(
            name=name,
            instance_uid=instance_uid,
            share_point_settings=share_point_settings,
            exchange_settings=exchange_settings,
            field_embedded=field_embedded,
        )

        vb_365_on_premises_microsoft_organization.additional_properties = d
        return vb_365_on_premises_microsoft_organization

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
