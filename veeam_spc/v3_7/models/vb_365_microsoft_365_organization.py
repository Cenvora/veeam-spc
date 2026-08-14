from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vb_365_organization_region import Vb365OrganizationRegion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vb_365_microsoft_365_connection_settings import Vb365Microsoft365ConnectionSettings
    from ..models.vb_365_organization_children_embedded import Vb365OrganizationChildrenEmbedded


T = TypeVar("T", bound="Vb365Microsoft365Organization")


@_attrs_define
class Vb365Microsoft365Organization:
    """
    Example:
        {'isTeamsOnline': True, 'isTeamsChatsOnline': False, 'exchangeAndSharePointOnlineConnectionSettings':
            {'modernAppOnlyAuthenticationSettings': {'configureApplication': False, 'userCode': None, 'newApplicationName':
            None, 'applicationId': 'ae61e533-82c7-4cb6-a030-78ae589cf49d', 'applicationCertificate': 'MIIEoQIBAAKCAQBJ4W/TVQ
            eIynO0BL/f/lc65mUzZmput1JCZsMLcjQB9eAteBVl5NRN4O5jUrWqXwk1IX17qtDiu3L8O07e0HlL+nHkRYeUDaztVbyhtvKc+YwNwZTQP8IvnW
            Bpgrd2uJw167I7iQ5nuN2O7QL/8idBiKhgsOKz9frPMSp/QIXA3MQoi+Yp8TiyDvGps+iMn1KpLgkHehlXUFmuZvi27T6wSZGh97rHekpIj9bSir
            ZFcG+7qupx8HFE4wNdhvxcvbmNkfMaJTmmi3YzGKYESwNyvwAIuohq1MoeQmNf1Q50NO04GOOPY+66uykOQkDkTa8/Vu90O6cux6/Ntyt04hndAg
            MBAAECggEABtA/m+HPnBHvsb5uY531NX1h/+eGEUfe0jjf7AJQQY4HaqoUbx03ZydDVO2fy2KQWtIH3IvYT9CxvglKMMpRJWynbEHtSv4n4Itzpg
            ZVQZzSCcK8kqgOpI2DArgHa2+DGIXwHgV5yp8F79Rz3l7at/R+csxdW/NnegwyuyGcNDkOjp8//HcrHQXPjljF5mwh4UZCFUvscKVjQbsOpiMvGe
            GN3z0/ZfKHi2egEA4+t1NLJykDiovNamtxE2xDkU8TXwn9STI8owzmxGtAA4HXDMuUQ0UXqxN0ED3WLJeqEKa0vuQ34+so5sa6EiwhF3q5rs0HFM
            klvUOxfnhgcpxgkQKBgQCMsiDpIh8BDKTxF20b8Az7NDtvm78vxfhF2rnCYIh9Q+3VKxbvoiNNTTJmlGT4Hi5App3l2GKIvRVZ9mE/vbtcWDk71/
            GgyiyuLixJYrY9gy2kYTz84R8v4ZMhjLB+Ba7VXkGU2u/Mj5LXzsQWCYRelC9DWlgcoReRXMHUbP4XwKBgQCGbYgE1gvW5ZYyi3xTrUIw8Bz7iUt
            bkO2Dg8egWLAYzRJizis6fd30xIG3wNheMVa/qqU3RrvS62N0QHZBjXJTH27li8JVQ9mfVbGZxcRLEwimBSEf5SNFlucwq02kvdJnL6vx5fE0XUz
            iDPcgIUF9LO+VcCFKXE7kVNn1P/KHQwKBgDsxJc9vX4Pdgfc8V9cNIyj8TJUj/UdoDo+bnhSwsIbSLlwfyHRjrbY3zsqZ4JdIQWlQ+B/dJxWm5Cz
            Z83f3/WTh3zNxlZTOID/Q/qL4Qf4DFe/4RyyyaAnUvMmcYpTcb6qrQSnJ4P0U18fyjdLQblYtpmrhK5mx7eMQq/QOwZAoGAU3ftTjtt7Ihv44CSu
            Q5KnEJrbJAKV5e8sr1/lYOcDDpBYVJsqwv+Zn4hoWw/rPTrzWTy40irVULNZSCljPx78TsCS8uk5faUSQgXl8ihoo/1/cgPklNfvFT/xkuHkXRAE
            cwa8r95Lq+EDpRIWg3sMQJW3S5brWV1ovdAwrRrLisCgYAk+F2L604Ss7zgEbBGJEQoD+OFVP29WSrKThtVLaabYP1N8qVr+W/P5ojRZ94aqZ0wB
            LfklfdejOp399llcoFoMShc1k+ScpYZb7k3cHhLGdZsm+gCNuVQZlpYWvhnSjOfEHafQRckxtPtvVTVda/uHtWNwoDv39eSXMS4WLprug==',
            'applicationCertificatePassword': 'Password1', 'sharePointSettings': {'sharePointSaveAllWebParts': False,
            'officeOrganizationName': 'mycompany.onmicrosoft.com'}, 'exchangeSettings': {'account':
            'admin@mycompany.onmicrosoft.com'}}, 'modernAuthenticationWithLegacyProtocolsSettings': None,
            'basicAuthenticationSettings': None}, 'region': 'Default'}

    Attributes:
        exchange_and_share_point_online_connection_settings (Vb365Microsoft365ConnectionSettings):
        instance_uid (UUID | Unset): UID assigned to a Microsoft 365 organization.
        name (str | Unset): Name of a Microsoft 365 organization.
        is_teams_online (bool | Unset): Indicates whether an organization contains Microsoft Teams components.
            > If the property has the `true` value, the `exchangeAndSharePointOnlineConnectionSettings` property becomes
            required.
             Default: False.
        is_teams_chats_online (bool | Unset): Indicates whether an organization contains Microsoft Teams chats.
            > Cannot be enabled if the `isTeamsOnline` property has the `false` value.
             Default: False.
        region (Vb365OrganizationRegion | Unset): Region where a Microsoft organization is located.
            > Available only for Microsoft 365 and hybrid organizations.
        field_embedded (Vb365OrganizationChildrenEmbedded | Unset):
    """

    exchange_and_share_point_online_connection_settings: Vb365Microsoft365ConnectionSettings
    instance_uid: UUID | Unset = UNSET
    name: str | Unset = UNSET
    is_teams_online: bool | Unset = False
    is_teams_chats_online: bool | Unset = False
    region: Vb365OrganizationRegion | Unset = UNSET
    field_embedded: Vb365OrganizationChildrenEmbedded | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exchange_and_share_point_online_connection_settings = (
            self.exchange_and_share_point_online_connection_settings.to_dict()
        )

        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        is_teams_online = self.is_teams_online

        is_teams_chats_online = self.is_teams_chats_online

        region: str | Unset = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.value

        field_embedded: dict[str, Any] | Unset = UNSET
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
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vb_365_microsoft_365_connection_settings import Vb365Microsoft365ConnectionSettings
        from ..models.vb_365_organization_children_embedded import Vb365OrganizationChildrenEmbedded

        d = dict(src_dict)
        exchange_and_share_point_online_connection_settings = Vb365Microsoft365ConnectionSettings.from_dict(
            d.pop("exchangeAndSharePointOnlineConnectionSettings")
        )

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        name = d.pop("name", UNSET)

        is_teams_online = d.pop("isTeamsOnline", UNSET)

        is_teams_chats_online = d.pop("isTeamsChatsOnline", UNSET)

        _region = d.pop("region", UNSET)
        region: Vb365OrganizationRegion | Unset
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = Vb365OrganizationRegion(_region)

        _field_embedded = d.pop("_embedded", UNSET)
        field_embedded: Vb365OrganizationChildrenEmbedded | Unset
        if isinstance(_field_embedded, Unset):
            field_embedded = UNSET
        else:
            field_embedded = Vb365OrganizationChildrenEmbedded.from_dict(_field_embedded)

        vb_365_microsoft_365_organization = cls(
            exchange_and_share_point_online_connection_settings=exchange_and_share_point_online_connection_settings,
            instance_uid=instance_uid,
            name=name,
            is_teams_online=is_teams_online,
            is_teams_chats_online=is_teams_chats_online,
            region=region,
            field_embedded=field_embedded,
        )

        vb_365_microsoft_365_organization.additional_properties = d
        return vb_365_microsoft_365_organization

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
