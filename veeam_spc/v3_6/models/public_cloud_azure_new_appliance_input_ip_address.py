from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.public_cloud_azure_new_appliance_input_ip_address_appliance_ip import (
        PublicCloudAzureNewApplianceInputIpAddressApplianceIp,
    )


T = TypeVar("T", bound="PublicCloudAzureNewApplianceInputIpAddress")


@_attrs_define
class PublicCloudAzureNewApplianceInputIpAddress:
    """
    Attributes:
        backup_server_ip_addresses (str): Array of IP addresses of a Veeam Cloud Connect site.
        appliance_ip (PublicCloudAzureNewApplianceInputIpAddressApplianceIp): Veeam Backup for Public Clouds appliance
            IP address.
            > Send only one of the following properties.
    """

    backup_server_ip_addresses: str
    appliance_ip: "PublicCloudAzureNewApplianceInputIpAddressApplianceIp"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_server_ip_addresses = self.backup_server_ip_addresses

        appliance_ip = self.appliance_ip.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backupServerIpAddresses": backup_server_ip_addresses,
                "applianceIp": appliance_ip,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_cloud_azure_new_appliance_input_ip_address_appliance_ip import (
            PublicCloudAzureNewApplianceInputIpAddressApplianceIp,
        )

        d = dict(src_dict)
        backup_server_ip_addresses = d.pop("backupServerIpAddresses")

        appliance_ip = PublicCloudAzureNewApplianceInputIpAddressApplianceIp.from_dict(d.pop("applianceIp"))

        public_cloud_azure_new_appliance_input_ip_address = cls(
            backup_server_ip_addresses=backup_server_ip_addresses,
            appliance_ip=appliance_ip,
        )

        public_cloud_azure_new_appliance_input_ip_address.additional_properties = d
        return public_cloud_azure_new_appliance_input_ip_address

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
