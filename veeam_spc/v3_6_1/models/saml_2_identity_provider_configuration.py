from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.saml_2_identity_provider_configuration_binding import Saml2IdentityProviderConfigurationBinding
from ..models.saml_2_identity_provider_configuration_outbound_signing_algorithm import (
    Saml2IdentityProviderConfigurationOutboundSigningAlgorithm,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="Saml2IdentityProviderConfiguration")


@_attrs_define
class Saml2IdentityProviderConfiguration:
    """Identity provider configuration.

    Attributes:
        entity_id (str): Issuer name or unique URI that an identity provider uses when sending responses.
        sign_on_url (Union[None, Unset, str]): URL to which authentication requests are sent if metadata autoloading is
            not being used.
        want_authn_requests_signed (Union[None, Unset, bool]): Indicates whether an identity provider requires
            authentication requests signed.
            > If the property value is `null`, it is treated as the `false` value.
        binding (Union[Unset, Saml2IdentityProviderConfigurationBinding]): Type of binding that a services provider
            should use when sending requests to an identity provider.
        allow_unsolicited_authn_response (Union[Unset, bool]): Indicates whether an identity provider can initiate sign-
            on without prior authentication request.
             Default: False.
        load_metadata (Union[Unset, bool]): Indicates whether service provider loads the identity provider metadata for
            it to override the data in the configuration. Default: True.
        outbound_signing_algorithm (Union[Unset, Saml2IdentityProviderConfigurationOutboundSigningAlgorithm]): Overrides
            the default signing algorithm for messages sent to an identity provider.
        metadata_location (Union[None, Unset, str]): URL or path to a file containing identity provider metadata that is
            used instead of `entityId` value.
    """

    entity_id: str
    sign_on_url: Union[None, Unset, str] = UNSET
    want_authn_requests_signed: Union[None, Unset, bool] = UNSET
    binding: Union[Unset, Saml2IdentityProviderConfigurationBinding] = UNSET
    allow_unsolicited_authn_response: Union[Unset, bool] = False
    load_metadata: Union[Unset, bool] = True
    outbound_signing_algorithm: Union[Unset, Saml2IdentityProviderConfigurationOutboundSigningAlgorithm] = UNSET
    metadata_location: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_id = self.entity_id

        sign_on_url: Union[None, Unset, str]
        if isinstance(self.sign_on_url, Unset):
            sign_on_url = UNSET
        else:
            sign_on_url = self.sign_on_url

        want_authn_requests_signed: Union[None, Unset, bool]
        if isinstance(self.want_authn_requests_signed, Unset):
            want_authn_requests_signed = UNSET
        else:
            want_authn_requests_signed = self.want_authn_requests_signed

        binding: Union[Unset, str] = UNSET
        if not isinstance(self.binding, Unset):
            binding = self.binding.value

        allow_unsolicited_authn_response = self.allow_unsolicited_authn_response

        load_metadata = self.load_metadata

        outbound_signing_algorithm: Union[Unset, str] = UNSET
        if not isinstance(self.outbound_signing_algorithm, Unset):
            outbound_signing_algorithm = self.outbound_signing_algorithm.value

        metadata_location: Union[None, Unset, str]
        if isinstance(self.metadata_location, Unset):
            metadata_location = UNSET
        else:
            metadata_location = self.metadata_location

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entityId": entity_id,
            }
        )
        if sign_on_url is not UNSET:
            field_dict["signOnUrl"] = sign_on_url
        if want_authn_requests_signed is not UNSET:
            field_dict["wantAuthnRequestsSigned"] = want_authn_requests_signed
        if binding is not UNSET:
            field_dict["binding"] = binding
        if allow_unsolicited_authn_response is not UNSET:
            field_dict["allowUnsolicitedAuthnResponse"] = allow_unsolicited_authn_response
        if load_metadata is not UNSET:
            field_dict["loadMetadata"] = load_metadata
        if outbound_signing_algorithm is not UNSET:
            field_dict["outboundSigningAlgorithm"] = outbound_signing_algorithm
        if metadata_location is not UNSET:
            field_dict["metadataLocation"] = metadata_location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity_id = d.pop("entityId")

        def _parse_sign_on_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sign_on_url = _parse_sign_on_url(d.pop("signOnUrl", UNSET))

        def _parse_want_authn_requests_signed(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        want_authn_requests_signed = _parse_want_authn_requests_signed(d.pop("wantAuthnRequestsSigned", UNSET))

        _binding = d.pop("binding", UNSET)
        binding: Union[Unset, Saml2IdentityProviderConfigurationBinding]
        if isinstance(_binding, Unset):
            binding = UNSET
        else:
            binding = Saml2IdentityProviderConfigurationBinding(_binding)

        allow_unsolicited_authn_response = d.pop("allowUnsolicitedAuthnResponse", UNSET)

        load_metadata = d.pop("loadMetadata", UNSET)

        _outbound_signing_algorithm = d.pop("outboundSigningAlgorithm", UNSET)
        outbound_signing_algorithm: Union[Unset, Saml2IdentityProviderConfigurationOutboundSigningAlgorithm]
        if isinstance(_outbound_signing_algorithm, Unset):
            outbound_signing_algorithm = UNSET
        else:
            outbound_signing_algorithm = Saml2IdentityProviderConfigurationOutboundSigningAlgorithm(
                _outbound_signing_algorithm
            )

        def _parse_metadata_location(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        metadata_location = _parse_metadata_location(d.pop("metadataLocation", UNSET))

        saml_2_identity_provider_configuration = cls(
            entity_id=entity_id,
            sign_on_url=sign_on_url,
            want_authn_requests_signed=want_authn_requests_signed,
            binding=binding,
            allow_unsolicited_authn_response=allow_unsolicited_authn_response,
            load_metadata=load_metadata,
            outbound_signing_algorithm=outbound_signing_algorithm,
            metadata_location=metadata_location,
        )

        saml_2_identity_provider_configuration.additional_properties = d
        return saml_2_identity_provider_configuration

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
