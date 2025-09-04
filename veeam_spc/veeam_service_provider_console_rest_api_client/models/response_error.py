from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.response_error_type import ResponseErrorType

T = TypeVar("T", bound="ResponseError")


@_attrs_define
class ResponseError:
    r"""
    Attributes:
        message (str): Error message.
            > Every line break is represented by the `\r\n` control characters.
        type_ (ResponseErrorType): Error type.
        code (int): Error code.
    """

    message: str
    type_: ResponseErrorType
    code: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        type_ = self.type_.value

        code = self.code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "type": type_,
                "code": code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        type_ = ResponseErrorType(d.pop("type"))

        code = d.pop("code")

        response_error = cls(
            message=message,
            type_=type_,
            code=code,
        )

        response_error.additional_properties = d
        return response_error

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
