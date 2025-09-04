import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthenticationResult")


@_attrs_define
class AuthenticationResult:
    """
    Attributes:
        access_token (Union[Unset, str]): Access token.
        refresh_token (Union[Unset, str]): Refresh token.
        mfa_token (Union[Unset, str]): Multi-factor authentication token.
        expiration_time (Union[Unset, datetime.datetime]): Date and time when access token will expire.
    """

    access_token: Union[Unset, str] = UNSET
    refresh_token: Union[Unset, str] = UNSET
    mfa_token: Union[Unset, str] = UNSET
    expiration_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        refresh_token = self.refresh_token

        mfa_token = self.mfa_token

        expiration_time: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_time, Unset):
            expiration_time = self.expiration_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_token is not UNSET:
            field_dict["accessToken"] = access_token
        if refresh_token is not UNSET:
            field_dict["refreshToken"] = refresh_token
        if mfa_token is not UNSET:
            field_dict["mfaToken"] = mfa_token
        if expiration_time is not UNSET:
            field_dict["expirationTime"] = expiration_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_token = d.pop("accessToken", UNSET)

        refresh_token = d.pop("refreshToken", UNSET)

        mfa_token = d.pop("mfaToken", UNSET)

        _expiration_time = d.pop("expirationTime", UNSET)
        expiration_time: Union[Unset, datetime.datetime]
        if isinstance(_expiration_time, Unset):
            expiration_time = UNSET
        else:
            expiration_time = isoparse(_expiration_time)

        authentication_result = cls(
            access_token=access_token,
            refresh_token=refresh_token,
            mfa_token=mfa_token,
            expiration_time=expiration_time,
        )

        authentication_result.additional_properties = d
        return authentication_result

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
