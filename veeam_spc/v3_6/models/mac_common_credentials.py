from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MacCommonCredentials")


@_attrs_define
class MacCommonCredentials:
    """
    Attributes:
        username (str): User name.
        password (Union[Unset, str]): Password.
        domain (Union[Unset, str]): Domain.
    """

    username: str
    password: Union[Unset, str] = UNSET
    domain: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        domain = self.domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password
        if domain is not UNSET:
            field_dict["domain"] = domain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        password = d.pop("password", UNSET)

        domain = d.pop("domain", UNSET)

        mac_common_credentials = cls(
            username=username,
            password=password,
            domain=domain,
        )

        mac_common_credentials.additional_properties = d
        return mac_common_credentials

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
