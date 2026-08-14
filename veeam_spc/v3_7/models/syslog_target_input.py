from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.syslog_target_input_protocol import SyslogTargetInputProtocol
from ..types import UNSET, Unset

T = TypeVar("T", bound="SyslogTargetInput")


@_attrs_define
class SyslogTargetInput:
    """
    Example:
        {'serverAddress': 'syslog01.tech.local', 'port': 514, 'protocol': 'Udp', 'enabled': True}

    Attributes:
        server_address (str): Host name or IP address of the remote syslog server.
        port (int | Unset): Port number for the remote syslog server. Default: 514.
        protocol (SyslogTargetInputProtocol | Unset): Transport protocol for syslog messages. Default:
            SyslogTargetInputProtocol.UDP.
        enabled (bool | Unset): Whether events are forwarded to this syslog server. Default: True.
    """

    server_address: str
    port: int | Unset = 514
    protocol: SyslogTargetInputProtocol | Unset = SyslogTargetInputProtocol.UDP
    enabled: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_address = self.server_address

        port = self.port

        protocol: str | Unset = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serverAddress": server_address,
            }
        )
        if port is not UNSET:
            field_dict["port"] = port
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        server_address = d.pop("serverAddress")

        port = d.pop("port", UNSET)

        _protocol = d.pop("protocol", UNSET)
        protocol: SyslogTargetInputProtocol | Unset
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = SyslogTargetInputProtocol(_protocol)

        enabled = d.pop("enabled", UNSET)

        syslog_target_input = cls(
            server_address=server_address,
            port=port,
            protocol=protocol,
            enabled=enabled,
        )

        syslog_target_input.additional_properties = d
        return syslog_target_input

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
