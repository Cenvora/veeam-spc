from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.public_cloud_azure_new_appliance_input_ip_address_appliance_ip_new_ip_address_type import (
    PublicCloudAzureNewApplianceInputIpAddressApplianceIpNewIpAddressType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudAzureNewApplianceInputIpAddressApplianceIp")


@_attrs_define
class PublicCloudAzureNewApplianceInputIpAddressApplianceIp:
    """Veeam Backup for Public Clouds appliance IP address.
    > Send only one of the following properties.

        Attributes:
            appliance_ip_address_id (Union[Unset, str]): Veeam Backup for Public Clouds appliance elastic IP address.
            new_ip_address_type (Union[Unset, PublicCloudAzureNewApplianceInputIpAddressApplianceIpNewIpAddressType]): Type
                of a new IP address that must be generated automatically.
    """

    appliance_ip_address_id: Union[Unset, str] = UNSET
    new_ip_address_type: Union[Unset, PublicCloudAzureNewApplianceInputIpAddressApplianceIpNewIpAddressType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        appliance_ip_address_id = self.appliance_ip_address_id

        new_ip_address_type: Union[Unset, str] = UNSET
        if not isinstance(self.new_ip_address_type, Unset):
            new_ip_address_type = self.new_ip_address_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appliance_ip_address_id is not UNSET:
            field_dict["applianceIpAddressId"] = appliance_ip_address_id
        if new_ip_address_type is not UNSET:
            field_dict["newIpAddressType"] = new_ip_address_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        appliance_ip_address_id = d.pop("applianceIpAddressId", UNSET)

        _new_ip_address_type = d.pop("newIpAddressType", UNSET)
        new_ip_address_type: Union[Unset, PublicCloudAzureNewApplianceInputIpAddressApplianceIpNewIpAddressType]
        if isinstance(_new_ip_address_type, Unset):
            new_ip_address_type = UNSET
        else:
            new_ip_address_type = PublicCloudAzureNewApplianceInputIpAddressApplianceIpNewIpAddressType(
                _new_ip_address_type
            )

        public_cloud_azure_new_appliance_input_ip_address_appliance_ip = cls(
            appliance_ip_address_id=appliance_ip_address_id,
            new_ip_address_type=new_ip_address_type,
        )

        public_cloud_azure_new_appliance_input_ip_address_appliance_ip.additional_properties = d
        return public_cloud_azure_new_appliance_input_ip_address_appliance_ip

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
