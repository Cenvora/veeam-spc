from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SmtpSettingsPasswordCredential")


@_attrs_define
class SmtpSettingsPasswordCredential:
    """Credentials required to access an SMTP server.

    Attributes:
        user_name (str): User name.
        password (Union[Unset, str]): Password.
        sasl_mechanism (Union[Unset, str]): SASL mechanism that is used for authentication with the specified username
            and password.
    """

    user_name: str
    password: Union[Unset, str] = UNSET
    sasl_mechanism: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_name = self.user_name

        password = self.password

        sasl_mechanism = self.sasl_mechanism

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userName": user_name,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password
        if sasl_mechanism is not UNSET:
            field_dict["saslMechanism"] = sasl_mechanism

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_name = d.pop("userName")

        password = d.pop("password", UNSET)

        sasl_mechanism = d.pop("saslMechanism", UNSET)

        smtp_settings_password_credential = cls(
            user_name=user_name,
            password=password,
            sasl_mechanism=sasl_mechanism,
        )

        smtp_settings_password_credential.additional_properties = d
        return smtp_settings_password_credential

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
