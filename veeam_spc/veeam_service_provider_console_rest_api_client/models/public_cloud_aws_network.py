from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudAwsNetwork")


@_attrs_define
class PublicCloudAwsNetwork:
    """
    Attributes:
        network_id (Union[Unset, str]): ID assigned to a network.
        network_name (Union[Unset, str]): Name of a network.
    """

    network_id: Union[Unset, str] = UNSET
    network_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network_id = self.network_id

        network_name = self.network_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if network_id is not UNSET:
            field_dict["networkId"] = network_id
        if network_name is not UNSET:
            field_dict["networkName"] = network_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        network_id = d.pop("networkId", UNSET)

        network_name = d.pop("networkName", UNSET)

        public_cloud_aws_network = cls(
            network_id=network_id,
            network_name=network_name,
        )

        public_cloud_aws_network.additional_properties = d
        return public_cloud_aws_network

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
