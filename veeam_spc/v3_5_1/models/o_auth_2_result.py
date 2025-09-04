from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OAuth2Result")


@_attrs_define
class OAuth2Result:
    """
    Attributes:
        access_token (Union[Unset, str]): Access token.
        token_type (Union[Unset, str]): Token type.
        refresh_token (Union[Unset, str]): Refresh token.
        mfa_token (Union[Unset, str]): MFA token.
        encrypted_code (Union[Unset, str]): Encrypted authorization code.
        expires_in (Union[Unset, int]): Date and time when an access token will expire.
    """

    access_token: Union[Unset, str] = UNSET
    token_type: Union[Unset, str] = UNSET
    refresh_token: Union[Unset, str] = UNSET
    mfa_token: Union[Unset, str] = UNSET
    encrypted_code: Union[Unset, str] = UNSET
    expires_in: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        token_type = self.token_type

        refresh_token = self.refresh_token

        mfa_token = self.mfa_token

        encrypted_code = self.encrypted_code

        expires_in = self.expires_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if token_type is not UNSET:
            field_dict["token_type"] = token_type
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token
        if mfa_token is not UNSET:
            field_dict["mfa_token"] = mfa_token
        if encrypted_code is not UNSET:
            field_dict["encrypted_code"] = encrypted_code
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_token = d.pop("access_token", UNSET)

        token_type = d.pop("token_type", UNSET)

        refresh_token = d.pop("refresh_token", UNSET)

        mfa_token = d.pop("mfa_token", UNSET)

        encrypted_code = d.pop("encrypted_code", UNSET)

        expires_in = d.pop("expires_in", UNSET)

        o_auth_2_result = cls(
            access_token=access_token,
            token_type=token_type,
            refresh_token=refresh_token,
            mfa_token=mfa_token,
            encrypted_code=encrypted_code,
            expires_in=expires_in,
        )

        o_auth_2_result.additional_properties = d
        return o_auth_2_result

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
