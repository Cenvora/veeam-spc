from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudGoogleSubNetworks")


@_attrs_define
class PublicCloudGoogleSubNetworks:
    """
    Attributes:
        sub_network_id (Union[Unset, str]): ID assigned to a subnet.
        name (Union[Unset, str]): Name of a subnet.
        range_ (Union[Unset, str]): IP address range of a subnet.
    """

    sub_network_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    range_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sub_network_id = self.sub_network_id

        name = self.name

        range_ = self.range_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sub_network_id is not UNSET:
            field_dict["subNetworkId"] = sub_network_id
        if name is not UNSET:
            field_dict["name"] = name
        if range_ is not UNSET:
            field_dict["range"] = range_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sub_network_id = d.pop("subNetworkId", UNSET)

        name = d.pop("name", UNSET)

        range_ = d.pop("range", UNSET)

        public_cloud_google_sub_networks = cls(
            sub_network_id=sub_network_id,
            name=name,
            range_=range_,
        )

        public_cloud_google_sub_networks.additional_properties = d
        return public_cloud_google_sub_networks

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
