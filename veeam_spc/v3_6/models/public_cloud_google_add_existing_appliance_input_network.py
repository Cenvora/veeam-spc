from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PublicCloudGoogleAddExistingApplianceInputNetwork")


@_attrs_define
class PublicCloudGoogleAddExistingApplianceInputNetwork:
    """Veeam Backup for Google Cloud appliance connection settings.
    > Send `null` to connect a Veeam Backup for Google Cloud appliance directly to the internet.

        Attributes:
            private_network_address (str): IP address or DNS name of a private network.
    """

    private_network_address: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        private_network_address = self.private_network_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "privateNetworkAddress": private_network_address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        private_network_address = d.pop("privateNetworkAddress")

        public_cloud_google_add_existing_appliance_input_network = cls(
            private_network_address=private_network_address,
        )

        public_cloud_google_add_existing_appliance_input_network.additional_properties = d
        return public_cloud_google_add_existing_appliance_input_network

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
