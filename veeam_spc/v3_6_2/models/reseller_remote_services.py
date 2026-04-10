from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reseller_backup_agents_management import ResellerBackupAgentsManagement


T = TypeVar("T", bound="ResellerRemoteServices")


@_attrs_define
class ResellerRemoteServices:
    """
    Attributes:
        backup_agents_management (ResellerBackupAgentsManagement | Unset):
        vb_365_management_enabled (bool | Unset): Indicates whether a reseller is allowed to manage remote Microsoft 365
            servers.
             Default: False.
        backup_servers_management_enabled (bool | Unset): Indicates whether a reseller is allowed to manage remote Veaam
            Backup & Replication servers.
             Default: False.
        vb_public_cloud_management_enabled (bool | Unset): Indicates whether a reseller is alowed to manage remote
            public cloud appliances. Default: False.
    """

    backup_agents_management: ResellerBackupAgentsManagement | Unset = UNSET
    vb_365_management_enabled: bool | Unset = False
    backup_servers_management_enabled: bool | Unset = False
    vb_public_cloud_management_enabled: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_agents_management: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_agents_management, Unset):
            backup_agents_management = self.backup_agents_management.to_dict()

        vb_365_management_enabled = self.vb_365_management_enabled

        backup_servers_management_enabled = self.backup_servers_management_enabled

        vb_public_cloud_management_enabled = self.vb_public_cloud_management_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_agents_management is not UNSET:
            field_dict["backupAgentsManagement"] = backup_agents_management
        if vb_365_management_enabled is not UNSET:
            field_dict["vb365ManagementEnabled"] = vb_365_management_enabled
        if backup_servers_management_enabled is not UNSET:
            field_dict["backupServersManagementEnabled"] = backup_servers_management_enabled
        if vb_public_cloud_management_enabled is not UNSET:
            field_dict["vbPublicCloudManagementEnabled"] = vb_public_cloud_management_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reseller_backup_agents_management import ResellerBackupAgentsManagement

        d = dict(src_dict)
        _backup_agents_management = d.pop("backupAgentsManagement", UNSET)
        backup_agents_management: ResellerBackupAgentsManagement | Unset
        if isinstance(_backup_agents_management, Unset):
            backup_agents_management = UNSET
        else:
            backup_agents_management = ResellerBackupAgentsManagement.from_dict(_backup_agents_management)

        vb_365_management_enabled = d.pop("vb365ManagementEnabled", UNSET)

        backup_servers_management_enabled = d.pop("backupServersManagementEnabled", UNSET)

        vb_public_cloud_management_enabled = d.pop("vbPublicCloudManagementEnabled", UNSET)

        reseller_remote_services = cls(
            backup_agents_management=backup_agents_management,
            vb_365_management_enabled=vb_365_management_enabled,
            backup_servers_management_enabled=backup_servers_management_enabled,
            vb_public_cloud_management_enabled=vb_public_cloud_management_enabled,
        )

        reseller_remote_services.additional_properties = d
        return reseller_remote_services

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
