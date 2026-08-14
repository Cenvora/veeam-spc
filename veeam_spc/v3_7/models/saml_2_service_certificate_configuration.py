from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.saml_2_service_certificate_configuration_metadata_publish_override import (
    Saml2ServiceCertificateConfigurationMetadataPublishOverride,
)
from ..models.saml_2_service_certificate_configuration_status import Saml2ServiceCertificateConfigurationStatus
from ..models.saml_2_service_certificate_configuration_use import Saml2ServiceCertificateConfigurationUse
from ..types import UNSET, Unset

T = TypeVar("T", bound="Saml2ServiceCertificateConfiguration")


@_attrs_define
class Saml2ServiceCertificateConfiguration:
    """Settings for certificate signing and encryption.

    Attributes:
        use (Saml2ServiceCertificateConfigurationUse | Unset): Type of certificate purpose. Default:
            Saml2ServiceCertificateConfigurationUse.BOTH.
        status (Saml2ServiceCertificateConfigurationStatus | Unset): Indicates whether certificate is currently in use
            or will be used in the future. Default: Saml2ServiceCertificateConfigurationStatus.CURRENT.
        private_key_content (str | Unset): Private key content in base64 format.
            > You can use the `GenerateNewPkcs12KeyPair` operation to generate a key.
            > For identity provider configuration, this property is required.
        certificate_thumbprint (str | Unset): Thumbprint of a currently used certificate.
        store_name (str | Unset): Name of a certificate store.
        store_location (str | Unset): Location of a certificate store.
        x_509_find_type (str | Unset): Type of an expression used to serch for a certificate according to
        metadata_publish_override (Saml2ServiceCertificateConfigurationMetadataPublishOverride | Unset): Type of
            certificate usage rule that overrides the default certificate usage rule.
            > For datails on certificate usage rules, see the [Sustainsys.Saml2
            documentation](https://saml2.sustainsys.com/en/v2/config-elements/service-certificates.html).
    """

    use: Saml2ServiceCertificateConfigurationUse | Unset = Saml2ServiceCertificateConfigurationUse.BOTH
    status: Saml2ServiceCertificateConfigurationStatus | Unset = Saml2ServiceCertificateConfigurationStatus.CURRENT
    private_key_content: str | Unset = UNSET
    certificate_thumbprint: str | Unset = UNSET
    store_name: str | Unset = UNSET
    store_location: str | Unset = UNSET
    x_509_find_type: str | Unset = UNSET
    metadata_publish_override: Saml2ServiceCertificateConfigurationMetadataPublishOverride | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        use: str | Unset = UNSET
        if not isinstance(self.use, Unset):
            use = self.use.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        private_key_content = self.private_key_content

        certificate_thumbprint = self.certificate_thumbprint

        store_name = self.store_name

        store_location = self.store_location

        x_509_find_type = self.x_509_find_type

        metadata_publish_override: str | Unset = UNSET
        if not isinstance(self.metadata_publish_override, Unset):
            metadata_publish_override = self.metadata_publish_override.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if use is not UNSET:
            field_dict["use"] = use
        if status is not UNSET:
            field_dict["status"] = status
        if private_key_content is not UNSET:
            field_dict["privateKeyContent"] = private_key_content
        if certificate_thumbprint is not UNSET:
            field_dict["certificateThumbprint"] = certificate_thumbprint
        if store_name is not UNSET:
            field_dict["storeName"] = store_name
        if store_location is not UNSET:
            field_dict["storeLocation"] = store_location
        if x_509_find_type is not UNSET:
            field_dict["x509FindType"] = x_509_find_type
        if metadata_publish_override is not UNSET:
            field_dict["metadataPublishOverride"] = metadata_publish_override

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _use = d.pop("use", UNSET)
        use: Saml2ServiceCertificateConfigurationUse | Unset
        if isinstance(_use, Unset):
            use = UNSET
        else:
            use = Saml2ServiceCertificateConfigurationUse(_use)

        _status = d.pop("status", UNSET)
        status: Saml2ServiceCertificateConfigurationStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = Saml2ServiceCertificateConfigurationStatus(_status)

        private_key_content = d.pop("privateKeyContent", UNSET)

        certificate_thumbprint = d.pop("certificateThumbprint", UNSET)

        store_name = d.pop("storeName", UNSET)

        store_location = d.pop("storeLocation", UNSET)

        x_509_find_type = d.pop("x509FindType", UNSET)

        _metadata_publish_override = d.pop("metadataPublishOverride", UNSET)
        metadata_publish_override: Saml2ServiceCertificateConfigurationMetadataPublishOverride | Unset
        if isinstance(_metadata_publish_override, Unset):
            metadata_publish_override = UNSET
        else:
            metadata_publish_override = Saml2ServiceCertificateConfigurationMetadataPublishOverride(
                _metadata_publish_override
            )

        saml_2_service_certificate_configuration = cls(
            use=use,
            status=status,
            private_key_content=private_key_content,
            certificate_thumbprint=certificate_thumbprint,
            store_name=store_name,
            store_location=store_location,
            x_509_find_type=x_509_find_type,
            metadata_publish_override=metadata_publish_override,
        )

        saml_2_service_certificate_configuration.additional_properties = d
        return saml_2_service_certificate_configuration

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
