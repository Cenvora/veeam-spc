from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationLicenseSettings")


@_attrs_define
class NotificationLicenseSettings:
    """
    Attributes:
        sender_name (str | Unset): Name of a sender.
        from_ (str | Unset): Email address from which notifications must be sent.
        to (str | Unset): Email address at which notifications must be sent.
        enabled (bool | Unset): Indicates whether notifications are enabled.
        include_csv (bool | Unset): Indicates whether a `CSV` file must be attached to notification emails.
    """

    sender_name: str | Unset = UNSET
    from_: str | Unset = UNSET
    to: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    include_csv: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sender_name = self.sender_name

        from_ = self.from_

        to = self.to

        enabled = self.enabled

        include_csv = self.include_csv

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sender_name is not UNSET:
            field_dict["senderName"] = sender_name
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if include_csv is not UNSET:
            field_dict["includeCsv"] = include_csv

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sender_name = d.pop("senderName", UNSET)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        enabled = d.pop("enabled", UNSET)

        include_csv = d.pop("includeCsv", UNSET)

        notification_license_settings = cls(
            sender_name=sender_name,
            from_=from_,
            to=to,
            enabled=enabled,
            include_csv=include_csv,
        )

        notification_license_settings.additional_properties = d
        return notification_license_settings

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
