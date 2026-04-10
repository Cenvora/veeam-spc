from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerVPowerNFSPortSettings")


@_attrs_define
class BackupServerVPowerNFSPortSettings:
    """
    Attributes:
        mount_port (int | Unset): Port that the Veeam vPower NFS Service must use to mount the vPower NFS datastore.
        v_power_nfs_port (int | Unset): Port that the Veeam vPower NFS Service must use to connect to the target NFS
            share.
    """

    mount_port: int | Unset = UNSET
    v_power_nfs_port: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mount_port = self.mount_port

        v_power_nfs_port = self.v_power_nfs_port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mount_port is not UNSET:
            field_dict["mountPort"] = mount_port
        if v_power_nfs_port is not UNSET:
            field_dict["vPowerNFSPort"] = v_power_nfs_port

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mount_port = d.pop("mountPort", UNSET)

        v_power_nfs_port = d.pop("vPowerNFSPort", UNSET)

        backup_server_v_power_nfs_port_settings = cls(
            mount_port=mount_port,
            v_power_nfs_port=v_power_nfs_port,
        )

        backup_server_v_power_nfs_port_settings.additional_properties = d
        return backup_server_v_power_nfs_port_settings

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
