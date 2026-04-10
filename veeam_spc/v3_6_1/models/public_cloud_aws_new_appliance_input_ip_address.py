from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.public_cloud_aws_new_appliance_input_ip_address_appliance_ip import (
        PublicCloudAwsNewApplianceInputIpAddressApplianceIp,
    )


T = TypeVar("T", bound="PublicCloudAwsNewApplianceInputIpAddress")


@_attrs_define
class PublicCloudAwsNewApplianceInputIpAddress:
    """
    Attributes:
        appliance_ip (PublicCloudAwsNewApplianceInputIpAddressApplianceIp): Veeam Backup for Public Clouds appliance IP
            address.
            > Send only one of the following properties.
        backup_server_ip_addresses (str): Array of IP addresses of a Veeam Cloud Connect site.
    """

    appliance_ip: "PublicCloudAwsNewApplianceInputIpAddressApplianceIp"
    backup_server_ip_addresses: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        appliance_ip = self.appliance_ip.to_dict()

        backup_server_ip_addresses = self.backup_server_ip_addresses

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applianceIp": appliance_ip,
                "backupServerIpAddresses": backup_server_ip_addresses,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_cloud_aws_new_appliance_input_ip_address_appliance_ip import (
            PublicCloudAwsNewApplianceInputIpAddressApplianceIp,
        )

        d = dict(src_dict)
        appliance_ip = PublicCloudAwsNewApplianceInputIpAddressApplianceIp.from_dict(d.pop("applianceIp"))

        backup_server_ip_addresses = d.pop("backupServerIpAddresses")

        public_cloud_aws_new_appliance_input_ip_address = cls(
            appliance_ip=appliance_ip,
            backup_server_ip_addresses=backup_server_ip_addresses,
        )

        public_cloud_aws_new_appliance_input_ip_address.additional_properties = d
        return public_cloud_aws_new_appliance_input_ip_address

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
