from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Saml2OrganizationConfiguration")


@_attrs_define
class Saml2OrganizationConfiguration:
    """Organization that supplies a SAML2 entity.

    Attributes:
        name (str): Official name of an organization.
        display_name (str): Friendly name of an organization.
        url (str): URL of an organization public website.
        language (Union[Unset, str]): Language specification of the organization metadata. Default: 'en'.
    """

    name: str
    display_name: str
    url: str
    language: Union[Unset, str] = "en"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        display_name = self.display_name

        url = self.url

        language = self.language

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "displayName": display_name,
                "url": url,
            }
        )
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        display_name = d.pop("displayName")

        url = d.pop("url")

        language = d.pop("language", UNSET)

        saml_2_organization_configuration = cls(
            name=name,
            display_name=display_name,
            url=url,
            language=language,
        )

        saml_2_organization_configuration.additional_properties = d
        return saml_2_organization_configuration

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
