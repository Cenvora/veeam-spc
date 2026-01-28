from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationBillingSettings")


@_attrs_define
class NotificationBillingSettings:
    """
    Attributes:
        sender_name (Union[None, Unset, str]): Name of a sender.
        from_ (Union[None, Unset, str]): Email address from which notifications are sent.
        subject (Union[Unset, str]): Text that is displayed as a subject of notification. Default: '%company%:
            %invoicePeriod%'.
    """

    sender_name: Union[None, Unset, str] = UNSET
    from_: Union[None, Unset, str] = UNSET
    subject: Union[Unset, str] = "%company%: %invoicePeriod%"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sender_name: Union[None, Unset, str]
        if isinstance(self.sender_name, Unset):
            sender_name = UNSET
        else:
            sender_name = self.sender_name

        from_: Union[None, Unset, str]
        if isinstance(self.from_, Unset):
            from_ = UNSET
        else:
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

        def _parse_sender_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sender_name = _parse_sender_name(d.pop("senderName", UNSET))

        def _parse_from_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        from_ = _parse_from_(d.pop("from", UNSET))

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
