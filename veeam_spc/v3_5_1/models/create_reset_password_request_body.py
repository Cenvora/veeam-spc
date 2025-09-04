from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateResetPasswordRequestBody")


@_attrs_define
class CreateResetPasswordRequestBody:
    """
    Attributes:
        email (str): User email address.
        user_name (str): User name.
        return_url (Union[Unset, str]): Relative URL that contains the password reset code in query parameters. The URL
            is send to the user email address provided in the `email` property.
    """

    email: str
    user_name: str
    return_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        user_name = self.user_name

        return_url = self.return_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "userName": user_name,
            }
        )
        if return_url is not UNSET:
            field_dict["returnUrl"] = return_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        user_name = d.pop("userName")

        return_url = d.pop("returnUrl", UNSET)

        create_reset_password_request_body = cls(
            email=email,
            user_name=user_name,
            return_url=return_url,
        )

        create_reset_password_request_body.additional_properties = d
        return create_reset_password_request_body

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
