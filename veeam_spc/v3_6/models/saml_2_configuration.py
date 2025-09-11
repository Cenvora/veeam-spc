from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.saml_2_configuration_authenticate_request_signing_behavior import (
    Saml2ConfigurationAuthenticateRequestSigningBehavior,
)
from ..models.saml_2_configuration_min_incoming_signing_algorithm import Saml2ConfigurationMinIncomingSigningAlgorithm
from ..models.saml_2_configuration_outbound_signing_algorithm import Saml2ConfigurationOutboundSigningAlgorithm
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.saml_2_compatibility_configuration import Saml2CompatibilityConfiguration
    from ..models.saml_2_identity_provider_configuration import Saml2IdentityProviderConfiguration
    from ..models.saml_2_metadata_configuration import Saml2MetadataConfiguration
    from ..models.saml_2_requested_authn_context_configuration import Saml2RequestedAuthnContextConfiguration
    from ..models.saml_2_service_certificate_configuration import Saml2ServiceCertificateConfiguration


T = TypeVar("T", bound="Saml2Configuration")


@_attrs_define
class Saml2Configuration:
    """Represents the `<sustainsys.saml2>` element of SAML2 configuration. For details, see the [Sustainsys.Saml2
    documentation](https://saml2.sustainsys.com/en/v2/config-elements/sustainsys-saml2.html).

        Attributes:
            entity_id (str): Name that will be used for service provider when sending messages.
            return_url (str): URL to which users are redirected once the authentication is complete.
            outbound_signing_algorithm (Saml2ConfigurationOutboundSigningAlgorithm): Default signing algorithm for messages
                that SAML2 generates.
            min_incoming_signing_algorithm (Saml2ConfigurationMinIncomingSigningAlgorithm): Minimum strength of a signing
                algorithm for incoming messages.
                If the incoming message is signed with anything weaker, it can be rejected.
            metadata (Saml2MetadataConfiguration): Configuration of generated service provider metadata.
            identity_providers (list['Saml2IdentityProviderConfiguration']): Array of identity providers known to a service
                provider.
            service_certificates (list['Saml2ServiceCertificateConfiguration']): Array of certificates that a service
                provider uses for signing or decrypting SAML assertions.
            module_path (Union[Unset, str]): Base path of the SAML2 endpoints.
                 Default: '/Saml2'.
            authenticate_request_signing_behavior (Union[Unset, Saml2ConfigurationAuthenticateRequestSigningBehavior]): Type
                of AuthnRequest signing behavior.
                 Default: Saml2ConfigurationAuthenticateRequestSigningBehavior.IFIDPWANTAUTHNREQUESTSSIGNED.
            validate_certificates (Union[Unset, bool]): Indicates whether the certificate validation is enabled.
            public_origin (Union[Unset, str]): Base URL of the SAML2 endpoints for external addresses.
            requested_authn_context (Union[Unset, Saml2RequestedAuthnContextConfiguration]): Configuration of the
                `<requestedAuthnContext>` element.
            compatibility (Union[Unset, Saml2CompatibilityConfiguration]): Configuration for processing of identity provider
                with non-standard behavior.
    """

    entity_id: str
    return_url: str
    outbound_signing_algorithm: Saml2ConfigurationOutboundSigningAlgorithm
    min_incoming_signing_algorithm: Saml2ConfigurationMinIncomingSigningAlgorithm
    metadata: "Saml2MetadataConfiguration"
    identity_providers: list["Saml2IdentityProviderConfiguration"]
    service_certificates: list["Saml2ServiceCertificateConfiguration"]
    module_path: Union[Unset, str] = "/Saml2"
    authenticate_request_signing_behavior: Union[Unset, Saml2ConfigurationAuthenticateRequestSigningBehavior] = (
        Saml2ConfigurationAuthenticateRequestSigningBehavior.IFIDPWANTAUTHNREQUESTSSIGNED
    )
    validate_certificates: Union[Unset, bool] = UNSET
    public_origin: Union[Unset, str] = UNSET
    requested_authn_context: Union[Unset, "Saml2RequestedAuthnContextConfiguration"] = UNSET
    compatibility: Union[Unset, "Saml2CompatibilityConfiguration"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_id = self.entity_id

        return_url = self.return_url

        outbound_signing_algorithm = self.outbound_signing_algorithm.value

        min_incoming_signing_algorithm = self.min_incoming_signing_algorithm.value

        metadata = self.metadata.to_dict()

        identity_providers = []
        for identity_providers_item_data in self.identity_providers:
            identity_providers_item = identity_providers_item_data.to_dict()
            identity_providers.append(identity_providers_item)

        service_certificates = []
        for service_certificates_item_data in self.service_certificates:
            service_certificates_item = service_certificates_item_data.to_dict()
            service_certificates.append(service_certificates_item)

        module_path = self.module_path

        authenticate_request_signing_behavior: Union[Unset, str] = UNSET
        if not isinstance(self.authenticate_request_signing_behavior, Unset):
            authenticate_request_signing_behavior = self.authenticate_request_signing_behavior.value

        validate_certificates = self.validate_certificates

        public_origin = self.public_origin

        requested_authn_context: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.requested_authn_context, Unset):
            requested_authn_context = self.requested_authn_context.to_dict()

        compatibility: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.compatibility, Unset):
            compatibility = self.compatibility.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entityId": entity_id,
                "returnUrl": return_url,
                "outboundSigningAlgorithm": outbound_signing_algorithm,
                "minIncomingSigningAlgorithm": min_incoming_signing_algorithm,
                "metadata": metadata,
                "identityProviders": identity_providers,
                "serviceCertificates": service_certificates,
            }
        )
        if module_path is not UNSET:
            field_dict["modulePath"] = module_path
        if authenticate_request_signing_behavior is not UNSET:
            field_dict["authenticateRequestSigningBehavior"] = authenticate_request_signing_behavior
        if validate_certificates is not UNSET:
            field_dict["validateCertificates"] = validate_certificates
        if public_origin is not UNSET:
            field_dict["publicOrigin"] = public_origin
        if requested_authn_context is not UNSET:
            field_dict["requestedAuthnContext"] = requested_authn_context
        if compatibility is not UNSET:
            field_dict["compatibility"] = compatibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.saml_2_compatibility_configuration import Saml2CompatibilityConfiguration
        from ..models.saml_2_identity_provider_configuration import Saml2IdentityProviderConfiguration
        from ..models.saml_2_metadata_configuration import Saml2MetadataConfiguration
        from ..models.saml_2_requested_authn_context_configuration import Saml2RequestedAuthnContextConfiguration
        from ..models.saml_2_service_certificate_configuration import Saml2ServiceCertificateConfiguration

        d = dict(src_dict)
        entity_id = d.pop("entityId")

        return_url = d.pop("returnUrl")

        outbound_signing_algorithm = Saml2ConfigurationOutboundSigningAlgorithm(d.pop("outboundSigningAlgorithm"))

        min_incoming_signing_algorithm = Saml2ConfigurationMinIncomingSigningAlgorithm(
            d.pop("minIncomingSigningAlgorithm")
        )

        metadata = Saml2MetadataConfiguration.from_dict(d.pop("metadata"))

        identity_providers = []
        _identity_providers = d.pop("identityProviders")
        for identity_providers_item_data in _identity_providers:
            identity_providers_item = Saml2IdentityProviderConfiguration.from_dict(identity_providers_item_data)

            identity_providers.append(identity_providers_item)

        service_certificates = []
        _service_certificates = d.pop("serviceCertificates")
        for service_certificates_item_data in _service_certificates:
            service_certificates_item = Saml2ServiceCertificateConfiguration.from_dict(service_certificates_item_data)

            service_certificates.append(service_certificates_item)

        module_path = d.pop("modulePath", UNSET)

        _authenticate_request_signing_behavior = d.pop("authenticateRequestSigningBehavior", UNSET)
        authenticate_request_signing_behavior: Union[Unset, Saml2ConfigurationAuthenticateRequestSigningBehavior]
        if isinstance(_authenticate_request_signing_behavior, Unset):
            authenticate_request_signing_behavior = UNSET
        else:
            authenticate_request_signing_behavior = Saml2ConfigurationAuthenticateRequestSigningBehavior(
                _authenticate_request_signing_behavior
            )

        validate_certificates = d.pop("validateCertificates", UNSET)

        public_origin = d.pop("publicOrigin", UNSET)

        _requested_authn_context = d.pop("requestedAuthnContext", UNSET)
        requested_authn_context: Union[Unset, Saml2RequestedAuthnContextConfiguration]
        if isinstance(_requested_authn_context, Unset):
            requested_authn_context = UNSET
        else:
            requested_authn_context = Saml2RequestedAuthnContextConfiguration.from_dict(_requested_authn_context)

        _compatibility = d.pop("compatibility", UNSET)
        compatibility: Union[Unset, Saml2CompatibilityConfiguration]
        if isinstance(_compatibility, Unset):
            compatibility = UNSET
        else:
            compatibility = Saml2CompatibilityConfiguration.from_dict(_compatibility)

        saml_2_configuration = cls(
            entity_id=entity_id,
            return_url=return_url,
            outbound_signing_algorithm=outbound_signing_algorithm,
            min_incoming_signing_algorithm=min_incoming_signing_algorithm,
            metadata=metadata,
            identity_providers=identity_providers,
            service_certificates=service_certificates,
            module_path=module_path,
            authenticate_request_signing_behavior=authenticate_request_signing_behavior,
            validate_certificates=validate_certificates,
            public_origin=public_origin,
            requested_authn_context=requested_authn_context,
            compatibility=compatibility,
        )

        saml_2_configuration.additional_properties = d
        return saml_2_configuration

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
