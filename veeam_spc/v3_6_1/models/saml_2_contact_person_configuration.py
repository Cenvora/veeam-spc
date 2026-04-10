from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

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
        company (Union[None, Unset, str]): Name of a contact person company.
        given_name (Union[None, Unset, str]): First name of a contact person
        surname (Union[None, Unset, str]): Last name of a contact person.
        phone_number (Union[None, Unset, str]): Telephone number of a contact person.
    """

    email: str
    type_: Union[Unset, Saml2ContactPersonConfigurationType] = Saml2ContactPersonConfigurationType.OTHER
    company: Union[None, Unset, str] = UNSET
    given_name: Union[None, Unset, str] = UNSET
    surname: Union[None, Unset, str] = UNSET
    phone_number: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        company: Union[None, Unset, str]
        if isinstance(self.company, Unset):
            company = UNSET
        else:
            company = self.company

        given_name: Union[None, Unset, str]
        if isinstance(self.given_name, Unset):
            given_name = UNSET
        else:
            given_name = self.given_name

        surname: Union[None, Unset, str]
        if isinstance(self.surname, Unset):
            surname = UNSET
        else:
            surname = self.surname

        phone_number: Union[None, Unset, str]
        if isinstance(self.phone_number, Unset):
            phone_number = UNSET
        else:
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

        def _parse_company(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company = _parse_company(d.pop("company", UNSET))

        def _parse_given_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        given_name = _parse_given_name(d.pop("givenName", UNSET))

        def _parse_surname(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        surname = _parse_surname(d.pop("surname", UNSET))

        def _parse_phone_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        phone_number = _parse_phone_number(d.pop("phoneNumber", UNSET))

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
