from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.o_auth_2_client_settings_kind import OAuth2ClientSettingsKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="OAuth2ClientSettings")


@_attrs_define
class OAuth2ClientSettings:
    """
    Attributes:
        kind (OAuth2ClientSettingsKind): Type of OAuth 2.0 identity provider.
        client_id (str): ID assigned to a client.
        client_secret (Union[None, Unset, str]): Client secret.
        scope (Union[None, Unset, str]): Access token scope.
            > Leave empty to use default scope.
        tenant_id (Union[None, Unset, str]): Tenant ID for Azure OAuth 2.0 service provider.
    """

    kind: OAuth2ClientSettingsKind
    client_id: str
    client_secret: Union[None, Unset, str] = UNSET
    scope: Union[None, Unset, str] = UNSET
    tenant_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        client_id = self.client_id

        client_secret: Union[None, Unset, str]
        if isinstance(self.client_secret, Unset):
            client_secret = UNSET
        else:
            client_secret = self.client_secret

        scope: Union[None, Unset, str]
        if isinstance(self.scope, Unset):
            scope = UNSET
        else:
            scope = self.scope

        tenant_id: Union[None, Unset, str]
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = self.tenant_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "clientId": client_id,
            }
        )
        if client_secret is not UNSET:
            field_dict["clientSecret"] = client_secret
        if scope is not UNSET:
            field_dict["scope"] = scope
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = OAuth2ClientSettingsKind(d.pop("kind"))

        client_id = d.pop("clientId")

        def _parse_client_secret(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        client_secret = _parse_client_secret(d.pop("clientSecret", UNSET))

        def _parse_scope(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        scope = _parse_scope(d.pop("scope", UNSET))

        def _parse_tenant_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tenant_id = _parse_tenant_id(d.pop("tenantId", UNSET))

        o_auth_2_client_settings = cls(
            kind=kind,
            client_id=client_id,
            client_secret=client_secret,
            scope=scope,
            tenant_id=tenant_id,
        )

        o_auth_2_client_settings.additional_properties = d
        return o_auth_2_client_settings

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
