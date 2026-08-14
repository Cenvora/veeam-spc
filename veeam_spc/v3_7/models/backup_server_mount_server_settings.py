from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_v_power_nfs_port_settings import BackupServerVPowerNFSPortSettings


T = TypeVar("T", bound="BackupServerMountServerSettings")


@_attrs_define
class BackupServerMountServerSettings:
    """
    Attributes:
        mount_server_id (UUID): UID assigned to a mount server.
        v_power_nfs_enabled (bool): Indicates whether the Veeam vPower NFS Service is allowed to access an object
            storage repository.
        write_cache_folder (str): Path to a write cache folder.
        v_power_nfs_port_settings (BackupServerVPowerNFSPortSettings | Unset):
    """

    mount_server_id: UUID
    v_power_nfs_enabled: bool
    write_cache_folder: str
    v_power_nfs_port_settings: BackupServerVPowerNFSPortSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mount_server_id = str(self.mount_server_id)

        v_power_nfs_enabled = self.v_power_nfs_enabled

        write_cache_folder = self.write_cache_folder

        v_power_nfs_port_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.v_power_nfs_port_settings, Unset):
            v_power_nfs_port_settings = self.v_power_nfs_port_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mountServerId": mount_server_id,
                "vPowerNFSEnabled": v_power_nfs_enabled,
                "writeCacheFolder": write_cache_folder,
            }
        )
        if v_power_nfs_port_settings is not UNSET:
            field_dict["vPowerNFSPortSettings"] = v_power_nfs_port_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_v_power_nfs_port_settings import BackupServerVPowerNFSPortSettings

        d = dict(src_dict)
        mount_server_id = UUID(d.pop("mountServerId"))

        v_power_nfs_enabled = d.pop("vPowerNFSEnabled")

        write_cache_folder = d.pop("writeCacheFolder")

        _v_power_nfs_port_settings = d.pop("vPowerNFSPortSettings", UNSET)
        v_power_nfs_port_settings: BackupServerVPowerNFSPortSettings | Unset
        if isinstance(_v_power_nfs_port_settings, Unset):
            v_power_nfs_port_settings = UNSET
        else:
            v_power_nfs_port_settings = BackupServerVPowerNFSPortSettings.from_dict(_v_power_nfs_port_settings)

        backup_server_mount_server_settings = cls(
            mount_server_id=mount_server_id,
            v_power_nfs_enabled=v_power_nfs_enabled,
            write_cache_folder=write_cache_folder,
            v_power_nfs_port_settings=v_power_nfs_port_settings,
        )

        backup_server_mount_server_settings.additional_properties = d
        return backup_server_mount_server_settings

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
