from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.identity_provider_template import IdentityProviderTemplate
from ..models.identity_provider_type import IdentityProviderType
from ..types import UNSET, Unset

T = TypeVar("T", bound="IdentityProvider")


@_attrs_define
class IdentityProvider:
    """
    Example:
        {'name': 'adfs', 'displayName': 'Microsoft Entra ID Federation Services', 'template': 'ADFS', 'type': 'SAML2',
            'organizationUid': '0242e3ca-1cc2-4d90-8285-0e7a9b375418', 'enabled': True}

    Attributes:
        name (str): Name of an identity provider.
        display_name (str): Display name of an identity provider.
        template (IdentityProviderTemplate): Identity provider template.
        type_ (IdentityProviderType): Type of an identity provider.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization.
        enabled (Union[Unset, bool]): Indicates whether an identity provider is enabled. Default: True.
    """

    name: str
    display_name: str
    template: IdentityProviderTemplate
    type_: IdentityProviderType
    organization_uid: Union[Unset, UUID] = UNSET
    enabled: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        display_name = self.display_name

        template = self.template.value

        type_ = self.type_.value

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "displayName": display_name,
                "template": template,
                "type": type_,
            }
        )
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        display_name = d.pop("displayName")

        template = IdentityProviderTemplate(d.pop("template"))

        type_ = IdentityProviderType(d.pop("type"))

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        enabled = d.pop("enabled", UNSET)

        identity_provider = cls(
            name=name,
            display_name=display_name,
            template=template,
            type_=type_,
            organization_uid=organization_uid,
            enabled=enabled,
        )

        identity_provider.additional_properties = d
        return identity_provider

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
