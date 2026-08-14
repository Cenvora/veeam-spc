from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationBillingSettings")


@_attrs_define
class NotificationBillingSettings:
    """
    Attributes:
        sender_name (str | Unset): Name of a sender.
        from_ (str | Unset): Email address from which notifications are sent.
        subject (str | Unset): Text that is displayed as a subject of notification. Default: '%company%:
            %invoicePeriod%'.
    """

    sender_name: str | Unset = UNSET
    from_: str | Unset = UNSET
    subject: str | Unset = "%company%: %invoicePeriod%"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sender_name = self.sender_name

        from_ = self.from_

        subject = self.subject

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sender_name is not UNSET:
            field_dict["senderName"] = sender_name
        if from_ is not UNSET:
            field_dict["from"] = from_
        if subject is not UNSET:
            field_dict["subject"] = subject

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sender_name = d.pop("senderName", UNSET)

        from_ = d.pop("from", UNSET)

        subject = d.pop("subject", UNSET)

        notification_billing_settings = cls(
            sender_name=sender_name,
            from_=from_,
            subject=subject,
        )

        notification_billing_settings.additional_properties = d
        return notification_billing_settings

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
