from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MacConnectionSettings")


@_attrs_define
class MacConnectionSettings:
    """
    Attributes:
        server_name (str): DNS name or IP address of a Veeam Backup & Replication server.
        server_port (Union[Unset, int]): Number of a port over which Veeam Agent for Linux must communicate with a Veeam
            Backup & Replication server. Default: 10006.
    """

    server_name: str
    server_port: Union[Unset, int] = 10006
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_name = self.server_name

        server_port = self.server_port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serverName": server_name,
            }
        )
        if server_port is not UNSET:
            field_dict["serverPort"] = server_port

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        server_name = d.pop("serverName")

        server_port = d.pop("serverPort", UNSET)

        mac_connection_settings = cls(
            server_name=server_name,
            server_port=server_port,
        )

        mac_connection_settings.additional_properties = d
        return mac_connection_settings

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
