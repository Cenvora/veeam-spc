from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.saml_2_contact_person_configuration import Saml2ContactPersonConfiguration
    from ..models.saml_2_organization_configuration import Saml2OrganizationConfiguration
    from ..models.saml_2_requested_attribute import Saml2RequestedAttribute


T = TypeVar("T", bound="Saml2MetadataConfiguration")


@_attrs_define
class Saml2MetadataConfiguration:
    """Configuration of generated service provider metadata.

    Attributes:
        organization (Saml2OrganizationConfiguration): Organization that supplies a SAML2 entity.
        contact_person (Saml2ContactPersonConfiguration): Contact person for a service provider.
        cache_duration (Union[Unset, str]): Time period during which remote parties may cache metadata before
            refetching. Default: 'PT1H'.
        valid_duration (Union[Unset, str]): Maximum time period during which metadata remains valid in case a refresh
            attempt fails. Default: '7.00:00:00'.
        want_assertions_signed (Union[Unset, bool]): Indicates whether service provider requires signing Assertions in
            addition to signing the SAML response. Default: True.
        requested_attributes (Union[Unset, list['Saml2RequestedAttribute']]): Array of attributes that a service
            provider expects an identity provider to include in Assertions.
    """

    organization: "Saml2OrganizationConfiguration"
    contact_person: "Saml2ContactPersonConfiguration"
    cache_duration: Union[Unset, str] = "PT1H"
    valid_duration: Union[Unset, str] = "7.00:00:00"
    want_assertions_signed: Union[Unset, bool] = True
    requested_attributes: Union[Unset, list["Saml2RequestedAttribute"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization = self.organization.to_dict()

        contact_person = self.contact_person.to_dict()

        cache_duration = self.cache_duration

        valid_duration = self.valid_duration

        want_assertions_signed = self.want_assertions_signed

        requested_attributes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.requested_attributes, Unset):
            requested_attributes = []
            for requested_attributes_item_data in self.requested_attributes:
                requested_attributes_item = requested_attributes_item_data.to_dict()
                requested_attributes.append(requested_attributes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organization": organization,
                "contactPerson": contact_person,
            }
        )
        if cache_duration is not UNSET:
            field_dict["cacheDuration"] = cache_duration
        if valid_duration is not UNSET:
            field_dict["validDuration"] = valid_duration
        if want_assertions_signed is not UNSET:
            field_dict["wantAssertionsSigned"] = want_assertions_signed
        if requested_attributes is not UNSET:
            field_dict["requestedAttributes"] = requested_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.saml_2_contact_person_configuration import Saml2ContactPersonConfiguration
        from ..models.saml_2_organization_configuration import Saml2OrganizationConfiguration
        from ..models.saml_2_requested_attribute import Saml2RequestedAttribute

        d = dict(src_dict)
        organization = Saml2OrganizationConfiguration.from_dict(d.pop("organization"))

        contact_person = Saml2ContactPersonConfiguration.from_dict(d.pop("contactPerson"))

        cache_duration = d.pop("cacheDuration", UNSET)

        valid_duration = d.pop("validDuration", UNSET)

        want_assertions_signed = d.pop("wantAssertionsSigned", UNSET)

        requested_attributes = []
        _requested_attributes = d.pop("requestedAttributes", UNSET)
        for requested_attributes_item_data in _requested_attributes or []:
            requested_attributes_item = Saml2RequestedAttribute.from_dict(requested_attributes_item_data)

            requested_attributes.append(requested_attributes_item)

        saml_2_metadata_configuration = cls(
            organization=organization,
            contact_person=contact_person,
            cache_duration=cache_duration,
            valid_duration=valid_duration,
            want_assertions_signed=want_assertions_signed,
            requested_attributes=requested_attributes,
        )

        saml_2_metadata_configuration.additional_properties = d
        return saml_2_metadata_configuration

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
