from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_backup_agents_management import CompanyBackupAgentsManagement
    from ..models.company_backup_server_management import CompanyBackupServerManagement
    from ..models.company_vb_365_server_management import CompanyVb365ServerManagement


T = TypeVar("T", bound="CompanyRemoteServices")


@_attrs_define
class CompanyRemoteServices:
    """
    Attributes:
        is_backup_resources_enabled (Union[Unset, bool]): Indicates whether cloud backup resources are allocated to a
            company. Default: True.
        backup_agents_management (Union[Unset, CompanyBackupAgentsManagement]): Number of Veeam backup agents that a
            company is allowed to manage.
        backup_servers_management (Union[Unset, CompanyBackupServerManagement]): Managed Veeam Backup & Replication
            server quota.
        vb_365_servers_management (Union[Unset, CompanyVb365ServerManagement]): Managed Veeam Backup for Microsoft 365
            server quota.
        is_vb_public_cloud_management_enabled (Union[Unset, bool]): Indicates whether a company is allowed to manage
            public cloud appliances.' Default: False.
    """

    is_backup_resources_enabled: Union[Unset, bool] = True
    backup_agents_management: Union[Unset, "CompanyBackupAgentsManagement"] = UNSET
    backup_servers_management: Union[Unset, "CompanyBackupServerManagement"] = UNSET
    vb_365_servers_management: Union[Unset, "CompanyVb365ServerManagement"] = UNSET
    is_vb_public_cloud_management_enabled: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_backup_resources_enabled = self.is_backup_resources_enabled

        backup_agents_management: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.backup_agents_management, Unset):
            backup_agents_management = self.backup_agents_management.to_dict()

        backup_servers_management: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.backup_servers_management, Unset):
            backup_servers_management = self.backup_servers_management.to_dict()

        vb_365_servers_management: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vb_365_servers_management, Unset):
            vb_365_servers_management = self.vb_365_servers_management.to_dict()

        is_vb_public_cloud_management_enabled = self.is_vb_public_cloud_management_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_backup_resources_enabled is not UNSET:
            field_dict["isBackupResourcesEnabled"] = is_backup_resources_enabled
        if backup_agents_management is not UNSET:
            field_dict["backupAgentsManagement"] = backup_agents_management
        if backup_servers_management is not UNSET:
            field_dict["backupServersManagement"] = backup_servers_management
        if vb_365_servers_management is not UNSET:
            field_dict["vb365ServersManagement"] = vb_365_servers_management
        if is_vb_public_cloud_management_enabled is not UNSET:
            field_dict["isVbPublicCloudManagementEnabled"] = is_vb_public_cloud_management_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_backup_agents_management import CompanyBackupAgentsManagement
        from ..models.company_backup_server_management import CompanyBackupServerManagement
        from ..models.company_vb_365_server_management import CompanyVb365ServerManagement

        d = dict(src_dict)
        is_backup_resources_enabled = d.pop("isBackupResourcesEnabled", UNSET)

        _backup_agents_management = d.pop("backupAgentsManagement", UNSET)
        backup_agents_management: Union[Unset, CompanyBackupAgentsManagement]
        if isinstance(_backup_agents_management, Unset):
            backup_agents_management = UNSET
        else:
            backup_agents_management = CompanyBackupAgentsManagement.from_dict(_backup_agents_management)

        _backup_servers_management = d.pop("backupServersManagement", UNSET)
        backup_servers_management: Union[Unset, CompanyBackupServerManagement]
        if isinstance(_backup_servers_management, Unset):
            backup_servers_management = UNSET
        else:
            backup_servers_management = CompanyBackupServerManagement.from_dict(_backup_servers_management)

        _vb_365_servers_management = d.pop("vb365ServersManagement", UNSET)
        vb_365_servers_management: Union[Unset, CompanyVb365ServerManagement]
        if isinstance(_vb_365_servers_management, Unset):
            vb_365_servers_management = UNSET
        else:
            vb_365_servers_management = CompanyVb365ServerManagement.from_dict(_vb_365_servers_management)

        is_vb_public_cloud_management_enabled = d.pop("isVbPublicCloudManagementEnabled", UNSET)

        company_remote_services = cls(
            is_backup_resources_enabled=is_backup_resources_enabled,
            backup_agents_management=backup_agents_management,
            backup_servers_management=backup_servers_management,
            vb_365_servers_management=vb_365_servers_management,
            is_vb_public_cloud_management_enabled=is_vb_public_cloud_management_enabled,
        )

        company_remote_services.additional_properties = d
        return company_remote_services

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
