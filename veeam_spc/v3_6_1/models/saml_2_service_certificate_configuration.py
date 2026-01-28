from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

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
        use (Union[Unset, Saml2ServiceCertificateConfigurationUse]): Type of certificate purpose. Default:
            Saml2ServiceCertificateConfigurationUse.BOTH.
        status (Union[Unset, Saml2ServiceCertificateConfigurationStatus]): Indicates whether certificate is currently in
            use or will be used in the future. Default: Saml2ServiceCertificateConfigurationStatus.CURRENT.
        private_key_content (Union[None, Unset, str]): Private key content in base64 format.
            > You can use the `GenerateNewPkcs12KeyPair` operation to generate a key.
            > For identity provider configuration, this property is required.
        certificate_thumbprint (Union[None, Unset, str]): Thumbprint of a currently used certificate.
        store_name (Union[None, Unset, str]): Name of a certificate store.
        store_location (Union[None, Unset, str]): Location of a certificate store.
        x_509_find_type (Union[None, Unset, str]): Type of an expression used to serch for a certificate according to
        metadata_publish_override (Union[Unset, Saml2ServiceCertificateConfigurationMetadataPublishOverride]): Type of
            certificate usage rule that overrides the default certificate usage rule.
            > For datails on certificate usage rules, see the [Sustainsys.Saml2
            documentation](https://saml2.sustainsys.com/en/v2/config-elements/service-certificates.html).
    """

    use: Union[Unset, Saml2ServiceCertificateConfigurationUse] = Saml2ServiceCertificateConfigurationUse.BOTH
    status: Union[Unset, Saml2ServiceCertificateConfigurationStatus] = (
        Saml2ServiceCertificateConfigurationStatus.CURRENT
    )
    private_key_content: Union[None, Unset, str] = UNSET
    certificate_thumbprint: Union[None, Unset, str] = UNSET
    store_name: Union[None, Unset, str] = UNSET
    store_location: Union[None, Unset, str] = UNSET
    x_509_find_type: Union[None, Unset, str] = UNSET
    metadata_publish_override: Union[Unset, Saml2ServiceCertificateConfigurationMetadataPublishOverride] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        use: Union[Unset, str] = UNSET
        if not isinstance(self.use, Unset):
            use = self.use.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        private_key_content: Union[None, Unset, str]
        if isinstance(self.private_key_content, Unset):
            private_key_content = UNSET
        else:
            private_key_content = self.private_key_content

        certificate_thumbprint: Union[None, Unset, str]
        if isinstance(self.certificate_thumbprint, Unset):
            certificate_thumbprint = UNSET
        else:
            certificate_thumbprint = self.certificate_thumbprint

        store_name: Union[None, Unset, str]
        if isinstance(self.store_name, Unset):
            store_name = UNSET
        else:
            store_name = self.store_name

        store_location: Union[None, Unset, str]
        if isinstance(self.store_location, Unset):
            store_location = UNSET
        else:
            store_location = self.store_location

        x_509_find_type: Union[None, Unset, str]
        if isinstance(self.x_509_find_type, Unset):
            x_509_find_type = UNSET
        else:
            x_509_find_type = self.x_509_find_type

        metadata_publish_override: Union[Unset, str] = UNSET
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
        use: Union[Unset, Saml2ServiceCertificateConfigurationUse]
        if isinstance(_use, Unset):
            use = UNSET
        else:
            use = Saml2ServiceCertificateConfigurationUse(_use)

        _status = d.pop("status", UNSET)
        status: Union[Unset, Saml2ServiceCertificateConfigurationStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = Saml2ServiceCertificateConfigurationStatus(_status)

        def _parse_private_key_content(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        private_key_content = _parse_private_key_content(d.pop("privateKeyContent", UNSET))

        def _parse_certificate_thumbprint(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        certificate_thumbprint = _parse_certificate_thumbprint(d.pop("certificateThumbprint", UNSET))

        def _parse_store_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        store_name = _parse_store_name(d.pop("storeName", UNSET))

        def _parse_store_location(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        store_location = _parse_store_location(d.pop("storeLocation", UNSET))

        def _parse_x_509_find_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        x_509_find_type = _parse_x_509_find_type(d.pop("x509FindType", UNSET))

        _metadata_publish_override = d.pop("metadataPublishOverride", UNSET)
        metadata_publish_override: Union[Unset, Saml2ServiceCertificateConfigurationMetadataPublishOverride]
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
