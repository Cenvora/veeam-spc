from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookTestResult")


@_attrs_define
class WebhookTestResult:
    """
    Attributes:
        is_successful (bool | Unset): Whether the test payload was delivered successfully.
        http_status_code (int | Unset): HTTP status code returned by the webhook endpoint.
        error_message (str | Unset): A short, non-sensitive summary if the delivery failed. The full response body is
            recorded only in the server log.
    """

    is_successful: bool | Unset = UNSET
    http_status_code: int | Unset = UNSET
    error_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_successful = self.is_successful

        http_status_code = self.http_status_code

        error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_successful is not UNSET:
            field_dict["isSuccessful"] = is_successful
        if http_status_code is not UNSET:
            field_dict["httpStatusCode"] = http_status_code
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_successful = d.pop("isSuccessful", UNSET)

        http_status_code = d.pop("httpStatusCode", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        webhook_test_result = cls(
            is_successful=is_successful,
            http_status_code=http_status_code,
            error_message=error_message,
        )

        webhook_test_result.additional_properties = d
        return webhook_test_result

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
