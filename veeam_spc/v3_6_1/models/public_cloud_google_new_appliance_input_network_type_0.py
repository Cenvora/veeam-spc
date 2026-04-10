from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudGoogleNewApplianceInputNetworkType0")


@_attrs_define
class PublicCloudGoogleNewApplianceInputNetworkType0:
    """Veeam Backup for Google Cloud appliance network resources.
    > If you provide the `null` value, all required resources will be created automatically.

        Attributes:
            network_id (str): ID assigned to a network.
            subnet_id (str): ID assigned to a subnet.
            network_tag_id (Union[None, Unset, str]): ID assigned to a network tag.
                > Provide the `null` value to create a new network tag.
    """

    network_id: str
    subnet_id: str
    network_tag_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network_id = self.network_id

        subnet_id = self.subnet_id

        network_tag_id: Union[None, Unset, str]
        if isinstance(self.network_tag_id, Unset):
            network_tag_id = UNSET
        else:
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

        def _parse_network_tag_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        network_tag_id = _parse_network_tag_id(d.pop("networkTagId", UNSET))

        public_cloud_google_new_appliance_input_network_type_0 = cls(
            network_id=network_id,
            subnet_id=subnet_id,
            network_tag_id=network_tag_id,
        )

        public_cloud_google_new_appliance_input_network_type_0.additional_properties = d
        return public_cloud_google_new_appliance_input_network_type_0

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
