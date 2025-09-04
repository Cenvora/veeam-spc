from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudAzureSubnet")


@_attrs_define
class PublicCloudAzureSubnet:
    """
    Attributes:
        address_space (Union[Unset, str]): IP range for a subnet.
        subnet_name (Union[Unset, str]): Name of a subnet.
    """

    address_space: Union[Unset, str] = UNSET
    subnet_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_space = self.address_space

        subnet_name = self.subnet_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_space is not UNSET:
            field_dict["addressSpace"] = address_space
        if subnet_name is not UNSET:
            field_dict["subnetName"] = subnet_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address_space = d.pop("addressSpace", UNSET)

        subnet_name = d.pop("subnetName", UNSET)

        public_cloud_azure_subnet = cls(
            address_space=address_space,
            subnet_name=subnet_name,
        )

        public_cloud_azure_subnet.additional_properties = d
        return public_cloud_azure_subnet

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
