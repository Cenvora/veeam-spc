from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudGoogleNewApplianceInputNetwork")


@_attrs_define
class PublicCloudGoogleNewApplianceInputNetwork:
    """Veeam Backup for Google Cloud appliance network resources.
    > If you provide the `null` value, all required resources will be created automatically.

        Attributes:
            network_id (str): ID assigned to a network.
            subnet_id (str): ID assigned to a subnet.
            network_tag_id (Union[Unset, str]): ID assigned to a network tag.
                > Provide the `null` value to create a new network tag.
    """

    network_id: str
    subnet_id: str
    network_tag_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network_id = self.network_id

        subnet_id = self.subnet_id

        network_tag_id = self.network_tag_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "networkId": network_id,
                "subnetId": subnet_id,
            }
        )
        if network_tag_id is not UNSET:
            field_dict["networkTagId"] = network_tag_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        network_id = d.pop("networkId")

        subnet_id = d.pop("subnetId")

        network_tag_id = d.pop("networkTagId", UNSET)

        public_cloud_google_new_appliance_input_network = cls(
            network_id=network_id,
            subnet_id=subnet_id,
            network_tag_id=network_tag_id,
        )

        public_cloud_google_new_appliance_input_network.additional_properties = d
        return public_cloud_google_new_appliance_input_network

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
