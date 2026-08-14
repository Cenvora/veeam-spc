from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CompleteResetPasswordRequestBody")


@_attrs_define
class CompleteResetPasswordRequestBody:
    """
    Example:
        {'code': 'E2DF8F84479511910E4469B624C72B359C84AC6AE340D7D225BC8FC237BB2E491C217849C5B45F23D0FD6D53BD1B75F37704D9
            08D647D25ADE5914760CEED5256C889432323F9B382826B650969C344C9ACE7E50F11A04F4256F97DA4A881F1EC2E53BB04D773BCD3B4A19
            35B958D253732CF3C493D868B24EBC0C17A9F4DB58DE07F91952D80E50', 'newPassword': 'password'}

    Attributes:
        code (str): Password reset code.
        new_password (str): New user password.
    """

    code: str
    new_password: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        new_password = self.new_password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "newPassword": new_password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        new_password = d.pop("newPassword")

        complete_reset_password_request_body = cls(
            code=code,
            new_password=new_password,
        )

        complete_reset_password_request_body.additional_properties = d
        return complete_reset_password_request_body

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
