from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudAzureDeviceCode")


@_attrs_define
class PublicCloudAzureDeviceCode:
    """
    Attributes:
        user_code (Union[Unset, str]): Verification code used to authenticate to the Azure CLI.
        verification_url (Union[Unset, str]): Redirect URI used to authenticate to the Azure CLI.
        device_code_token (Union[Unset, str]): Verification code used to start an authentication session.
    """

    user_code: Union[Unset, str] = UNSET
    verification_url: Union[Unset, str] = UNSET
    device_code_token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_code = self.user_code

        verification_url = self.verification_url

        device_code_token = self.device_code_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_code is not UNSET:
            field_dict["userCode"] = user_code
        if verification_url is not UNSET:
            field_dict["verificationUrl"] = verification_url
        if device_code_token is not UNSET:
            field_dict["deviceCodeToken"] = device_code_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_code = d.pop("userCode", UNSET)

        verification_url = d.pop("verificationUrl", UNSET)

        device_code_token = d.pop("deviceCodeToken", UNSET)

        public_cloud_azure_device_code = cls(
            user_code=user_code,
            verification_url=verification_url,
            device_code_token=device_code_token,
        )

        public_cloud_azure_device_code.additional_properties = d
        return public_cloud_azure_device_code

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
