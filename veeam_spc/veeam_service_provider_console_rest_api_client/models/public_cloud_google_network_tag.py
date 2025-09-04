from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudGoogleNetworkTag")


@_attrs_define
class PublicCloudGoogleNetworkTag:
    """
    Attributes:
        network_tag_id (Union[Unset, str]): ID assigned to a network tag.
        network_tag_name (Union[Unset, str]): Name of a network tag.
    """

    network_tag_id: Union[Unset, str] = UNSET
    network_tag_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network_tag_id = self.network_tag_id

        network_tag_name = self.network_tag_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if network_tag_id is not UNSET:
            field_dict["networkTagId"] = network_tag_id
        if network_tag_name is not UNSET:
            field_dict["networkTagName"] = network_tag_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        network_tag_id = d.pop("networkTagId", UNSET)

        network_tag_name = d.pop("networkTagName", UNSET)

        public_cloud_google_network_tag = cls(
            network_tag_id=network_tag_id,
            network_tag_name=network_tag_name,
        )

        public_cloud_google_network_tag.additional_properties = d
        return public_cloud_google_network_tag

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
