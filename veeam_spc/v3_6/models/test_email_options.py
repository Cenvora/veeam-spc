from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TestEmailOptions")


@_attrs_define
class TestEmailOptions:
    """
    Attributes:
        from_ (str): Email address from which test notification message is sent.
        to (str): Email address to which test notification message is sent.
        sender_name (Union[Unset, str]): Name of a sender.
    """

    from_: str
    to: str
    sender_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        to = self.to

        sender_name = self.sender_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
            }
        )
        if sender_name is not UNSET:
            field_dict["senderName"] = sender_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_ = d.pop("from")

        to = d.pop("to")

        sender_name = d.pop("senderName", UNSET)

        test_email_options = cls(
            from_=from_,
            to=to,
            sender_name=sender_name,
        )

        test_email_options.additional_properties = d
        return test_email_options

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
