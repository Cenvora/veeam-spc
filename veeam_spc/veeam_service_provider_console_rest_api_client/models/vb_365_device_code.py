from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365DeviceCode")


@_attrs_define
class Vb365DeviceCode:
    """
    Attributes:
        user_code (Union[Unset, str]): Device code.
        verification_url (Union[Unset, str]): Verification URL.
        expires_in (Union[Unset, int]): Lifespan of the code in milliseconds.
        message (Union[Unset, str]): Help message.
    """

    user_code: Union[Unset, str] = UNSET
    verification_url: Union[Unset, str] = UNSET
    expires_in: Union[Unset, int] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_code = self.user_code

        verification_url = self.verification_url

        expires_in = self.expires_in

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_code is not UNSET:
            field_dict["userCode"] = user_code
        if verification_url is not UNSET:
            field_dict["verificationUrl"] = verification_url
        if expires_in is not UNSET:
            field_dict["expiresIn"] = expires_in
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_code = d.pop("userCode", UNSET)

        verification_url = d.pop("verificationUrl", UNSET)

        expires_in = d.pop("expiresIn", UNSET)

        message = d.pop("message", UNSET)

        vb_365_device_code = cls(
            user_code=user_code,
            verification_url=verification_url,
            expires_in=expires_in,
            message=message,
        )

        vb_365_device_code.additional_properties = d
        return vb_365_device_code

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
