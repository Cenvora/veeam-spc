from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationLoginUrlAndSuggestion")


@_attrs_define
class OrganizationLoginUrlAndSuggestion:
    """
    Attributes:
        login_url (Union[Unset, str]): Current portal URL of a company.
            > Has the `null` value if the URL is not configured.
        login_url_is_inherited (Union[Unset, bool]): Indicates whether an portal URL is inherited from the manager
            organization.
        login_url_suggestion (Union[Unset, str]): Suggested portal URL based on the organization alias and the current
            request URL.
            > Has the `null` value if the URL is already configured.
    """

    login_url: Union[Unset, str] = UNSET
    login_url_is_inherited: Union[Unset, bool] = UNSET
    login_url_suggestion: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        login_url = self.login_url

        login_url_is_inherited = self.login_url_is_inherited

        login_url_suggestion = self.login_url_suggestion

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if login_url is not UNSET:
            field_dict["loginUrl"] = login_url
        if login_url_is_inherited is not UNSET:
            field_dict["loginUrlIsInherited"] = login_url_is_inherited
        if login_url_suggestion is not UNSET:
            field_dict["loginUrlSuggestion"] = login_url_suggestion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        login_url = d.pop("loginUrl", UNSET)

        login_url_is_inherited = d.pop("loginUrlIsInherited", UNSET)

        login_url_suggestion = d.pop("loginUrlSuggestion", UNSET)

        organization_login_url_and_suggestion = cls(
            login_url=login_url,
            login_url_is_inherited=login_url_is_inherited,
            login_url_suggestion=login_url_suggestion,
        )

        organization_login_url_and_suggestion.additional_properties = d
        return organization_login_url_and_suggestion

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
