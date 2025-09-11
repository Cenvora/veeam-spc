from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudBackupServerPublicAddress")


@_attrs_define
class PublicCloudBackupServerPublicAddress:
    """
    Attributes:
        backup_server_ip_addresses (Union[Unset, str]): Array of IP addresses of a Veeam Cloud Connect site.
    """

    backup_server_ip_addresses: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_server_ip_addresses = self.backup_server_ip_addresses

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_server_ip_addresses is not UNSET:
            field_dict["backupServerIpAddresses"] = backup_server_ip_addresses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backup_server_ip_addresses = d.pop("backupServerIpAddresses", UNSET)

        public_cloud_backup_server_public_address = cls(
            backup_server_ip_addresses=backup_server_ip_addresses,
        )

        public_cloud_backup_server_public_address.additional_properties = d
        return public_cloud_backup_server_public_address

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
