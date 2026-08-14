from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinuxVbrManagementAgentInstallationConfiguration")


@_attrs_define
class LinuxVbrManagementAgentInstallationConfiguration:
    """
    Example:
        {'hostname': 'vbr-linux01.tech.local', 'port': 10006, 'trustedThumbprint':
            '9F86D081884C7D659A2FEAA0C55AD015A3BF4F1B', 'sshUsername': 'root', 'sshPassword': 'P@ssw0rd123!', 'description':
            'Linux VBR management agent deployed via VSPC'}

    Attributes:
        hostname (str): Hostname or IP address of a target Linux Veeam Backup & Replication server.
        port (int): TCP port of the Veeam Updater service on a target server.
        trusted_thumbprint (str): SHA-1 thumbprint of the trusted TLS certificate. Veeam Service Provider Console
            rejects the connection if the target server certificate does not match this thumbprint.
        ssh_username (str): User name for SSH authentication to the target server.
        ssh_password (str): Password for SSH authentication to the target server.
        description (str | Unset): Description of the deployment.
    """

    hostname: str
    port: int
    trusted_thumbprint: str
    ssh_username: str
    ssh_password: str
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hostname = self.hostname

        port = self.port

        trusted_thumbprint = self.trusted_thumbprint

        ssh_username = self.ssh_username

        ssh_password = self.ssh_password

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hostname": hostname,
                "port": port,
                "trustedThumbprint": trusted_thumbprint,
                "sshUsername": ssh_username,
                "sshPassword": ssh_password,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hostname = d.pop("hostname")

        port = d.pop("port")

        trusted_thumbprint = d.pop("trustedThumbprint")

        ssh_username = d.pop("sshUsername")

        ssh_password = d.pop("sshPassword")

        description = d.pop("description", UNSET)

        linux_vbr_management_agent_installation_configuration = cls(
            hostname=hostname,
            port=port,
            trusted_thumbprint=trusted_thumbprint,
            ssh_username=ssh_username,
            ssh_password=ssh_password,
            description=description,
        )

        linux_vbr_management_agent_installation_configuration.additional_properties = d
        return linux_vbr_management_agent_installation_configuration

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
