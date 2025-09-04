from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudGoogleAvailabilityZone")


@_attrs_define
class PublicCloudGoogleAvailabilityZone:
    """
    Attributes:
        availability_zone_id (Union[Unset, str]): ID assigned to a Google Cloud availability zone.
    """

    availability_zone_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        availability_zone_id = self.availability_zone_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if availability_zone_id is not UNSET:
            field_dict["availabilityZoneId"] = availability_zone_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        availability_zone_id = d.pop("availabilityZoneId", UNSET)

        public_cloud_google_availability_zone = cls(
            availability_zone_id=availability_zone_id,
        )

        public_cloud_google_availability_zone.additional_properties = d
        return public_cloud_google_availability_zone

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
