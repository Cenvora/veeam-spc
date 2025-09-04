from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudAzureNewApplianceInputNetwork")


@_attrs_define
class PublicCloudAzureNewApplianceInputNetwork:
    """Veeam Backup for Public Clouds appliance network resources.
    >If you send the `null` value, all required resources will be created automatically.

        Attributes:
            network_id (str): ID assigned to a network.
            subnet_name (str): Name of a subnet.
            security_group_id (Union[Unset, str]): ID assigned to a security group. Send the `null` value to create a new
                security group.
    """

    network_id: str
    subnet_name: str
    security_group_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network_id = self.network_id

        subnet_name = self.subnet_name

        security_group_id = self.security_group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "networkId": network_id,
                "subnetName": subnet_name,
            }
        )
        if security_group_id is not UNSET:
            field_dict["securityGroupId"] = security_group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        network_id = d.pop("networkId")

        subnet_name = d.pop("subnetName")

        security_group_id = d.pop("securityGroupId", UNSET)

        public_cloud_azure_new_appliance_input_network = cls(
            network_id=network_id,
            subnet_name=subnet_name,
            security_group_id=security_group_id,
        )

        public_cloud_azure_new_appliance_input_network.additional_properties = d
        return public_cloud_azure_new_appliance_input_network

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
