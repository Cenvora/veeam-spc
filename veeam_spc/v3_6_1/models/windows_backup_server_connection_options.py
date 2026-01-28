from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WindowsBackupServerConnectionOptions")


@_attrs_define
class WindowsBackupServerConnectionOptions:
    """
    Attributes:
        address (str): DNS name or IP address of a Veeam Backup & Replication server that manages the target backup
            repository.
        remote_repository_name (str): Name of a backup repository.
        port (Union[Unset, int]): Port over which Veeam Agent for Microsoft Windows must communicate with the backup
            repository. Default: 10001.
    """

    address: str
    remote_repository_name: str
    port: Union[Unset, int] = 10001
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        remote_repository_name = self.remote_repository_name

        port = self.port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "remoteRepositoryName": remote_repository_name,
            }
        )
        if port is not UNSET:
            field_dict["port"] = port

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address")

        remote_repository_name = d.pop("remoteRepositoryName")

        port = d.pop("port", UNSET)

        windows_backup_server_connection_options = cls(
            address=address,
            remote_repository_name=remote_repository_name,
            port=port,
        )

        windows_backup_server_connection_options.additional_properties = d
        return windows_backup_server_connection_options

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
