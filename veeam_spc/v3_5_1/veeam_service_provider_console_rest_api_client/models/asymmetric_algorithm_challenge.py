import datetime
from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import File

T = TypeVar("T", bound="AsymmetricAlgorithmChallenge")


@_attrs_define
class AsymmetricAlgorithmChallenge:
    """
    Attributes:
        challenge (File): Decryption challenge.
        expiration_time (datetime.datetime): Date and time when a challenge will expire.
    """

    challenge: File
    expiration_time: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        challenge = self.challenge.to_tuple()

        expiration_time = self.expiration_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "challenge": challenge,
                "expirationTime": expiration_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        challenge = File(payload=BytesIO(d.pop("challenge")))

        expiration_time = isoparse(d.pop("expirationTime"))

        asymmetric_algorithm_challenge = cls(
            challenge=challenge,
            expiration_time=expiration_time,
        )

        asymmetric_algorithm_challenge.additional_properties = d
        return asymmetric_algorithm_challenge

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
