from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SmtpSettingsPasswordCredentialType0")


@_attrs_define
class SmtpSettingsPasswordCredentialType0:
    """Credentials required to access an SMTP server.

    Attributes:
        user_name (None | str): User name.
        password (None | str | Unset): Password.
        sasl_mechanism (None | str | Unset): SASL mechanism that is used for authentication with the specified username
            and password.
    """

    user_name: None | str
    password: None | str | Unset = UNSET
    sasl_mechanism: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_name: None | str
        user_name = self.user_name

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        sasl_mechanism: None | str | Unset
        if isinstance(self.sasl_mechanism, Unset):
            sasl_mechanism = UNSET
        else:
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

        def _parse_user_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        user_name = _parse_user_name(d.pop("userName"))

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        def _parse_sasl_mechanism(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sasl_mechanism = _parse_sasl_mechanism(d.pop("saslMechanism", UNSET))

        smtp_settings_password_credential_type_0 = cls(
            user_name=user_name,
            password=password,
            sasl_mechanism=sasl_mechanism,
        )

        smtp_settings_password_credential_type_0.additional_properties = d
        return smtp_settings_password_credential_type_0

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
