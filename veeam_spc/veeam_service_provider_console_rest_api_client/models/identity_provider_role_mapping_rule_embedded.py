from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identity_provider import IdentityProvider


T = TypeVar("T", bound="IdentityProviderRoleMappingRuleEmbedded")


@_attrs_define
class IdentityProviderRoleMappingRuleEmbedded:
    """Resource representation of the related identity provider entity.

    Attributes:
        provider_info (Union[Unset, IdentityProvider]):  Example: {'name': 'adfs', 'displayName': 'Microsoft Entra ID
            Federation Services', 'template': 'ADFS', 'type': 'SAML2', 'organizationUid':
            '0242e3ca-1cc2-4d90-8285-0e7a9b375418', 'enabled': True}.
    """

    provider_info: Union[Unset, "IdentityProvider"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.provider_info, Unset):
            provider_info = self.provider_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if provider_info is not UNSET:
            field_dict["providerInfo"] = provider_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.identity_provider import IdentityProvider

        d = dict(src_dict)
        _provider_info = d.pop("providerInfo", UNSET)
        provider_info: Union[Unset, IdentityProvider]
        if isinstance(_provider_info, Unset):
            provider_info = UNSET
        else:
            provider_info = IdentityProvider.from_dict(_provider_info)

        identity_provider_role_mapping_rule_embedded = cls(
            provider_info=provider_info,
        )

        identity_provider_role_mapping_rule_embedded.additional_properties = d
        return identity_provider_role_mapping_rule_embedded

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
