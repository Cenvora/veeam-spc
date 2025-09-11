from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vb_365_organization_region import Vb365OrganizationRegion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vb_365_microsoft_365_connection_settings import Vb365Microsoft365ConnectionSettings
    from ..models.vb_365_on_premises_microsoft_exchange_settings import Vb365OnPremisesMicrosoftExchangeSettings
    from ..models.vb_365_on_premises_microsoft_share_point_settings import Vb365OnPremisesMicrosoftSharePointSettings
    from ..models.vb_365_organization_children_embedded import Vb365OrganizationChildrenEmbedded


T = TypeVar("T", bound="Vb365HybridOrganization")


@_attrs_define
class Vb365HybridOrganization:
    """
    Attributes:
        exchange_and_share_point_online_connection_settings (Vb365Microsoft365ConnectionSettings):
        instance_uid (Union[Unset, UUID]): UID assigned to a hybrid Microsoft organization.
        name (Union[Unset, str]): Name of a hybrid Microsoft organization.
        is_teams_online (Union[Unset, bool]): Indicates whether an organization contains Microsoft Teams components.
            > If the property has the `true` value, the `exchangeAndSharePointOnlineConnectionSettings`,
            `sharePointSettings` and `exchangeSettings` properties become required.
             Default: False.
        is_teams_chats_online (Union[Unset, bool]): Indicates whether an organization contains Microsoft Teams chats.
            Cannot be enabled if the `isTeamsOnline` property has the `false` value.
             Default: False.
        region (Union[Unset, Vb365OrganizationRegion]): Region where a Microsoft organization is located.
            > Available only for Microsoft 365 and hybrid organizations.
        share_point_settings (Union[Unset, Vb365OnPremisesMicrosoftSharePointSettings]):
        exchange_settings (Union[Unset, Vb365OnPremisesMicrosoftExchangeSettings]):
        field_embedded (Union[Unset, Vb365OrganizationChildrenEmbedded]):
    """

    exchange_and_share_point_online_connection_settings: "Vb365Microsoft365ConnectionSettings"
    instance_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    is_teams_online: Union[Unset, bool] = False
    is_teams_chats_online: Union[Unset, bool] = False
    region: Union[Unset, Vb365OrganizationRegion] = UNSET
    share_point_settings: Union[Unset, "Vb365OnPremisesMicrosoftSharePointSettings"] = UNSET
    exchange_settings: Union[Unset, "Vb365OnPremisesMicrosoftExchangeSettings"] = UNSET
    field_embedded: Union[Unset, "Vb365OrganizationChildrenEmbedded"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exchange_and_share_point_online_connection_settings = (
            self.exchange_and_share_point_online_connection_settings.to_dict()
        )

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        is_teams_online = self.is_teams_online

        is_teams_chats_online = self.is_teams_chats_online

        region: Union[Unset, str] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.value

        share_point_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.share_point_settings, Unset):
            share_point_settings = self.share_point_settings.to_dict()

        exchange_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.exchange_settings, Unset):
            exchange_settings = self.exchange_settings.to_dict()

        field_embedded: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_embedded, Unset):
            field_embedded = self.field_embedded.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exchangeAndSharePointOnlineConnectionSettings": exchange_and_share_point_online_connection_settings,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if name is not UNSET:
            field_dict["name"] = name
        if is_teams_online is not UNSET:
            field_dict["isTeamsOnline"] = is_teams_online
        if is_teams_chats_online is not UNSET:
            field_dict["isTeamsChatsOnline"] = is_teams_chats_online
        if region is not UNSET:
            field_dict["region"] = region
        if share_point_settings is not UNSET:
            field_dict["sharePointSettings"] = share_point_settings
        if exchange_settings is not UNSET:
            field_dict["exchangeSettings"] = exchange_settings
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vb_365_microsoft_365_connection_settings import Vb365Microsoft365ConnectionSettings
        from ..models.vb_365_on_premises_microsoft_exchange_settings import Vb365OnPremisesMicrosoftExchangeSettings
        from ..models.vb_365_on_premises_microsoft_share_point_settings import (
            Vb365OnPremisesMicrosoftSharePointSettings,
        )
        from ..models.vb_365_organization_children_embedded import Vb365OrganizationChildrenEmbedded

        d = dict(src_dict)
        exchange_and_share_point_online_connection_settings = Vb365Microsoft365ConnectionSettings.from_dict(
            d.pop("exchangeAndSharePointOnlineConnectionSettings")
        )

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        name = d.pop("name", UNSET)

        is_teams_online = d.pop("isTeamsOnline", UNSET)

        is_teams_chats_online = d.pop("isTeamsChatsOnline", UNSET)

        _region = d.pop("region", UNSET)
        region: Union[Unset, Vb365OrganizationRegion]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = Vb365OrganizationRegion(_region)

        _share_point_settings = d.pop("sharePointSettings", UNSET)
        share_point_settings: Union[Unset, Vb365OnPremisesMicrosoftSharePointSettings]
        if isinstance(_share_point_settings, Unset):
            share_point_settings = UNSET
        else:
            share_point_settings = Vb365OnPremisesMicrosoftSharePointSettings.from_dict(_share_point_settings)

        _exchange_settings = d.pop("exchangeSettings", UNSET)
        exchange_settings: Union[Unset, Vb365OnPremisesMicrosoftExchangeSettings]
        if isinstance(_exchange_settings, Unset):
            exchange_settings = UNSET
        else:
            exchange_settings = Vb365OnPremisesMicrosoftExchangeSettings.from_dict(_exchange_settings)

        _field_embedded = d.pop("_embedded", UNSET)
        field_embedded: Union[Unset, Vb365OrganizationChildrenEmbedded]
        if isinstance(_field_embedded, Unset):
            field_embedded = UNSET
        else:
            field_embedded = Vb365OrganizationChildrenEmbedded.from_dict(_field_embedded)

        vb_365_hybrid_organization = cls(
            exchange_and_share_point_online_connection_settings=exchange_and_share_point_online_connection_settings,
            instance_uid=instance_uid,
            name=name,
            is_teams_online=is_teams_online,
            is_teams_chats_online=is_teams_chats_online,
            region=region,
            share_point_settings=share_point_settings,
            exchange_settings=exchange_settings,
            field_embedded=field_embedded,
        )

        vb_365_hybrid_organization.additional_properties = d
        return vb_365_hybrid_organization

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
