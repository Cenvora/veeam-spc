from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_v_power_nfs_port_settings import BackupServerVPowerNFSPortSettings


T = TypeVar("T", bound="BackupServerMountServerOptions")


@_attrs_define
class BackupServerMountServerOptions:
    """
    Attributes:
        v_power_nfs_enabled (bool | None | Unset): Indicates whether the Veeam vPower NFS Service is allowed to access
            an object storage repository.
        write_cache_folder (str | Unset): Path to a write cache folder.
        v_power_nfs_port_settings (BackupServerVPowerNFSPortSettings | Unset):
    """

    v_power_nfs_enabled: bool | None | Unset = UNSET
    write_cache_folder: str | Unset = UNSET
    v_power_nfs_port_settings: BackupServerVPowerNFSPortSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        v_power_nfs_enabled: bool | None | Unset
        if isinstance(self.v_power_nfs_enabled, Unset):
            v_power_nfs_enabled = UNSET
        else:
            v_power_nfs_enabled = self.v_power_nfs_enabled

        write_cache_folder = self.write_cache_folder

        v_power_nfs_port_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.v_power_nfs_port_settings, Unset):
            v_power_nfs_port_settings = self.v_power_nfs_port_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if v_power_nfs_enabled is not UNSET:
            field_dict["vPowerNFSEnabled"] = v_power_nfs_enabled
        if write_cache_folder is not UNSET:
            field_dict["writeCacheFolder"] = write_cache_folder
        if v_power_nfs_port_settings is not UNSET:
            field_dict["vPowerNFSPortSettings"] = v_power_nfs_port_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_v_power_nfs_port_settings import BackupServerVPowerNFSPortSettings

        d = dict(src_dict)

        def _parse_v_power_nfs_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        v_power_nfs_enabled = _parse_v_power_nfs_enabled(d.pop("vPowerNFSEnabled", UNSET))

        write_cache_folder = d.pop("writeCacheFolder", UNSET)

        _v_power_nfs_port_settings = d.pop("vPowerNFSPortSettings", UNSET)
        v_power_nfs_port_settings: BackupServerVPowerNFSPortSettings | Unset
        if isinstance(_v_power_nfs_port_settings, Unset):
            v_power_nfs_port_settings = UNSET
        else:
            v_power_nfs_port_settings = BackupServerVPowerNFSPortSettings.from_dict(_v_power_nfs_port_settings)

        backup_server_mount_server_options = cls(
            v_power_nfs_enabled=v_power_nfs_enabled,
            write_cache_folder=write_cache_folder,
            v_power_nfs_port_settings=v_power_nfs_port_settings,
        )

        backup_server_mount_server_options.additional_properties = d
        return backup_server_mount_server_options

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
