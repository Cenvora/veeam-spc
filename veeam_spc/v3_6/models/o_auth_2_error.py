from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.o_auth_2_error_error import OAuth2ErrorError
from ..types import UNSET, Unset

T = TypeVar("T", bound="OAuth2Error")


@_attrs_define
class OAuth2Error:
    """
    Example:
        {'error': 'invalid_request', 'error_description': 'Cannot complete login due to incorrect username or password,
            or no sufficient rights.', 'error_uri': None}

    Attributes:
        error (Union[Unset, OAuth2ErrorError]): Error type.
        error_description (Union[Unset, str]): Error description.
        error_uri (Union[Unset, str]): Error URI.
    """

    error: Union[Unset, OAuth2ErrorError] = UNSET
    error_description: Union[Unset, str] = UNSET
    error_uri: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error: Union[Unset, str] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.value

        error_description = self.error_description

        error_uri = self.error_uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if error_description is not UNSET:
            field_dict["error_description"] = error_description
        if error_uri is not UNSET:
            field_dict["error_uri"] = error_uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _error = d.pop("error", UNSET)
        error: Union[Unset, OAuth2ErrorError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = OAuth2ErrorError(_error)

        error_description = d.pop("error_description", UNSET)

        error_uri = d.pop("error_uri", UNSET)

        o_auth_2_error = cls(
            error=error,
            error_description=error_description,
            error_uri=error_uri,
        )

        o_auth_2_error.additional_properties = d
        return o_auth_2_error

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
