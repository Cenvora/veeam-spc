from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.saml_2_contact_person_configuration_type import Saml2ContactPersonConfigurationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Saml2ContactPersonConfiguration")


@_attrs_define
class Saml2ContactPersonConfiguration:
    """Contact person for a service provider.

    Attributes:
        email (str): Email address of a contact person.
            > This property is required.
        type_ (Union[Unset, Saml2ContactPersonConfigurationType]): Type of contact. Common values include `Technical`,
            `Support`, or `Other`. Default: Saml2ContactPersonConfigurationType.OTHER.
        company (Union[Unset, str]): Name of a contact person company.
        given_name (Union[Unset, str]): First name of a contact person
        surname (Union[Unset, str]): Last name of a contact person.
        phone_number (Union[Unset, str]): Telephone number of a contact person.
    """

    email: str
    type_: Union[Unset, Saml2ContactPersonConfigurationType] = Saml2ContactPersonConfigurationType.OTHER
    company: Union[Unset, str] = UNSET
    given_name: Union[Unset, str] = UNSET
    surname: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        company = self.company

        given_name = self.given_name

        surname = self.surname

        phone_number = self.phone_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if company is not UNSET:
            field_dict["company"] = company
        if given_name is not UNSET:
            field_dict["givenName"] = given_name
        if surname is not UNSET:
            field_dict["surname"] = surname
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, Saml2ContactPersonConfigurationType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = Saml2ContactPersonConfigurationType(_type_)

        company = d.pop("company", UNSET)

        given_name = d.pop("givenName", UNSET)

        surname = d.pop("surname", UNSET)

        phone_number = d.pop("phoneNumber", UNSET)

        saml_2_contact_person_configuration = cls(
            email=email,
            type_=type_,
            company=company,
            given_name=given_name,
            surname=surname,
            phone_number=phone_number,
        )

        saml_2_contact_person_configuration.additional_properties = d
        return saml_2_contact_person_configuration

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
