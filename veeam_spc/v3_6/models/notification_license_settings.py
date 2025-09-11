from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationLicenseSettings")


@_attrs_define
class NotificationLicenseSettings:
    """
    Attributes:
        sender_name (Union[Unset, str]): Name of a sender.
        from_ (Union[Unset, str]): Email address from which notifications must be sent.
        to (Union[Unset, str]): Email address at which notifications must be sent.
        enabled (Union[Unset, bool]): Indicates whether notifications are enabled.
    """

    sender_name: Union[Unset, str] = UNSET
    from_: Union[Unset, str] = UNSET
    to: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sender_name = self.sender_name

        from_ = self.from_

        to = self.to

        enabled = self.enabled

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sender_name = d.pop("senderName", UNSET)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        enabled = d.pop("enabled", UNSET)

        notification_license_settings = cls(
            sender_name=sender_name,
            from_=from_,
            to=to,
            enabled=enabled,
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
