from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudAppliancePublicAddress")


@_attrs_define
class PublicCloudAppliancePublicAddress:
    """
    Attributes:
        appliance_ip_address_id (Union[Unset, str]): Elastic IP address.
        ip_address (Union[Unset, str]): Public address of a Veeam Backup for Public Clouds appliance.
        name (Union[None, Unset, str]): Name of a Veeam Backup for Public Clouds appliance.
    """

    appliance_ip_address_id: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        appliance_ip_address_id = self.appliance_ip_address_id

        ip_address = self.ip_address

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appliance_ip_address_id is not UNSET:
            field_dict["applianceIpAddressId"] = appliance_ip_address_id
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        appliance_ip_address_id = d.pop("applianceIpAddressId", UNSET)

        ip_address = d.pop("ipAddress", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        public_cloud_appliance_public_address = cls(
            appliance_ip_address_id=appliance_ip_address_id,
            ip_address=ip_address,
            name=name,
        )

        public_cloud_appliance_public_address.additional_properties = d
        return public_cloud_appliance_public_address

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
