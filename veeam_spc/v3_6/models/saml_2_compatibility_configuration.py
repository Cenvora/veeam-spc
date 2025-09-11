from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Saml2CompatibilityConfiguration")


@_attrs_define
class Saml2CompatibilityConfiguration:
    """Configuration for processing of identity provider with non-standard behavior.

    Attributes:
        ignore_missing_in_response_to (Union[Unset, bool]): Indicates whether SAML2 must ignore the lack of the
            `InResponseTo` attribute in identity provider responses. Default: False.
        ignore_authentication_context_in_response (Union[Unset, bool]): Indicates whether SAML2 must ignore the
            `<AuthnContext>` element in identity provider responses.
        unpack_entities_descriptor_in_identity_provider_metadata (Union[Unset, bool]): Indicates whether SAML2 must
            automatically use the `EntityDescriptor` value in case it is the only such value in the `EntitiesDescriptor`
            element of the identity provider metadata.
    """

    ignore_missing_in_response_to: Union[Unset, bool] = False
    ignore_authentication_context_in_response: Union[Unset, bool] = UNSET
    unpack_entities_descriptor_in_identity_provider_metadata: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ignore_missing_in_response_to = self.ignore_missing_in_response_to

        ignore_authentication_context_in_response = self.ignore_authentication_context_in_response

        unpack_entities_descriptor_in_identity_provider_metadata = (
            self.unpack_entities_descriptor_in_identity_provider_metadata
        )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ignore_missing_in_response_to is not UNSET:
            field_dict["ignoreMissingInResponseTo"] = ignore_missing_in_response_to
        if ignore_authentication_context_in_response is not UNSET:
            field_dict["ignoreAuthenticationContextInResponse"] = ignore_authentication_context_in_response
        if unpack_entities_descriptor_in_identity_provider_metadata is not UNSET:
            field_dict["unpackEntitiesDescriptorInIdentityProviderMetadata"] = (
                unpack_entities_descriptor_in_identity_provider_metadata
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ignore_missing_in_response_to = d.pop("ignoreMissingInResponseTo", UNSET)

        ignore_authentication_context_in_response = d.pop("ignoreAuthenticationContextInResponse", UNSET)

        unpack_entities_descriptor_in_identity_provider_metadata = d.pop(
            "unpackEntitiesDescriptorInIdentityProviderMetadata", UNSET
        )

        saml_2_compatibility_configuration = cls(
            ignore_missing_in_response_to=ignore_missing_in_response_to,
            ignore_authentication_context_in_response=ignore_authentication_context_in_response,
            unpack_entities_descriptor_in_identity_provider_metadata=unpack_entities_descriptor_in_identity_provider_metadata,
        )

        saml_2_compatibility_configuration.additional_properties = d
        return saml_2_compatibility_configuration

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
