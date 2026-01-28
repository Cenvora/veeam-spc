from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudAzureNewApplianceInputNetworkType0")


@_attrs_define
class PublicCloudAzureNewApplianceInputNetworkType0:
    """Veeam Backup for Public Clouds appliance network resources.
    >If you send the `null` value, all required resources will be created automatically.

        Attributes:
            network_id (str): ID assigned to a network.
            subnet_name (str): Name of a subnet.
            security_group_id (Union[None, Unset, str]): ID assigned to a security group. Send the `null` value to create a
                new security group.
    """

    network_id: str
    subnet_name: str
    security_group_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network_id = self.network_id

        subnet_name = self.subnet_name

        security_group_id: Union[None, Unset, str]
        if isinstance(self.security_group_id, Unset):
            security_group_id = UNSET
        else:
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

        def _parse_security_group_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        security_group_id = _parse_security_group_id(d.pop("securityGroupId", UNSET))

        public_cloud_azure_new_appliance_input_network_type_0 = cls(
            network_id=network_id,
            subnet_name=subnet_name,
            security_group_id=security_group_id,
        )

        public_cloud_azure_new_appliance_input_network_type_0.additional_properties = d
        return public_cloud_azure_new_appliance_input_network_type_0

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
