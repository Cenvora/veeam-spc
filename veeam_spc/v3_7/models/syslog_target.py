from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.syslog_target_protocol import SyslogTargetProtocol

T = TypeVar("T", bound="SyslogTarget")


@_attrs_define
class SyslogTarget:
    """
    Attributes:
        instance_uid (UUID): Unique identifier of the syslog target.
        server_address (str): Host name or IP address of the remote syslog server.
        port (int): Port number for the remote syslog server. Default: 514.
        protocol (SyslogTargetProtocol): Transport protocol for syslog messages. Default: SyslogTargetProtocol.UDP.
        enabled (bool): Whether events are forwarded to this syslog server.
    """

    instance_uid: UUID
    server_address: str
    enabled: bool
    port: int = 514
    protocol: SyslogTargetProtocol = SyslogTargetProtocol.UDP
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid = str(self.instance_uid)

        server_address = self.server_address

        port = self.port

        protocol = self.protocol.value

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instanceUid": instance_uid,
                "serverAddress": server_address,
                "port": port,
                "protocol": protocol,
                "enabled": enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        instance_uid = UUID(d.pop("instanceUid"))

        server_address = d.pop("serverAddress")

        port = d.pop("port")

        protocol = SyslogTargetProtocol(d.pop("protocol"))

        enabled = d.pop("enabled")

        syslog_target = cls(
            instance_uid=instance_uid,
            server_address=server_address,
            port=port,
            protocol=protocol,
            enabled=enabled,
        )

        syslog_target.additional_properties = d
        return syslog_target

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
