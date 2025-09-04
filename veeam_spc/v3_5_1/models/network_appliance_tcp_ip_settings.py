from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NetworkApplianceTcpIpSettings")


@_attrs_define
class NetworkApplianceTcpIpSettings:
    """
    Attributes:
        dhcp_enabled (Union[Unset, bool]): Indicates whether IP address is automatically assigned to network extension
            appliance by a DHCP server. Default: True.
        ip_address (Union[Unset, str]): IP address of a network extension appliance.
            > The `null` value indicates that IP address is automatically assigned by a DHCP server.
        subnet_mask (Union[Unset, str]): Subnet mask of a network extension appliance.
            > The `null` value indicates that IP address is automatically assigned by a DHCP server.
        default_gateway (Union[Unset, str]): Default gateway of a network extension appliance.
            > The `null` value indicates that IP address is automatically assigned by a DHCP server.
    """

    dhcp_enabled: Union[Unset, bool] = True
    ip_address: Union[Unset, str] = UNSET
    subnet_mask: Union[Unset, str] = UNSET
    default_gateway: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dhcp_enabled = self.dhcp_enabled

        ip_address = self.ip_address

        subnet_mask = self.subnet_mask

        default_gateway = self.default_gateway

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dhcp_enabled is not UNSET:
            field_dict["dhcpEnabled"] = dhcp_enabled
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if subnet_mask is not UNSET:
            field_dict["subnetMask"] = subnet_mask
        if default_gateway is not UNSET:
            field_dict["defaultGateway"] = default_gateway

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dhcp_enabled = d.pop("dhcpEnabled", UNSET)

        ip_address = d.pop("ipAddress", UNSET)

        subnet_mask = d.pop("subnetMask", UNSET)

        default_gateway = d.pop("defaultGateway", UNSET)

        network_appliance_tcp_ip_settings = cls(
            dhcp_enabled=dhcp_enabled,
            ip_address=ip_address,
            subnet_mask=subnet_mask,
            default_gateway=default_gateway,
        )

        network_appliance_tcp_ip_settings.additional_properties = d
        return network_appliance_tcp_ip_settings

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
