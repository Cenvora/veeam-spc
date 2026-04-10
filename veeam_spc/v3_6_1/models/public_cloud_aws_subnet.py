from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudAwsSubnet")


@_attrs_define
class PublicCloudAwsSubnet:
    """
    Attributes:
        subnet_id (Union[Unset, str]): ID assigned to a subnet.
        subnet_name (Union[Unset, str]): AWS name of a subnet.
        range_ (Union[Unset, str]): Range of IP addresses present in a subnet.
        display_name (Union[Unset, str]): Display name of a subnet.
    """

    subnet_id: Union[Unset, str] = UNSET
    subnet_name: Union[Unset, str] = UNSET
    range_: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subnet_id = self.subnet_id

        subnet_name = self.subnet_name

        range_ = self.range_

        display_name = self.display_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subnet_id is not UNSET:
            field_dict["subnetId"] = subnet_id
        if subnet_name is not UNSET:
            field_dict["subnetName"] = subnet_name
        if range_ is not UNSET:
            field_dict["range"] = range_
        if display_name is not UNSET:
            field_dict["displayName"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subnet_id = d.pop("subnetId", UNSET)

        subnet_name = d.pop("subnetName", UNSET)

        range_ = d.pop("range", UNSET)

        display_name = d.pop("displayName", UNSET)

        public_cloud_aws_subnet = cls(
            subnet_id=subnet_id,
            subnet_name=subnet_name,
            range_=range_,
            display_name=display_name,
        )

        public_cloud_aws_subnet.additional_properties = d
        return public_cloud_aws_subnet

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
