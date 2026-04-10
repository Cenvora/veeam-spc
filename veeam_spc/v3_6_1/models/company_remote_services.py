from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_backup_agents_management_type_0 import CompanyBackupAgentsManagementType0
    from ..models.company_backup_server_management_type_0 import CompanyBackupServerManagementType0
    from ..models.company_vb_365_server_management_type_0 import CompanyVb365ServerManagementType0


T = TypeVar("T", bound="CompanyRemoteServices")


@_attrs_define
class CompanyRemoteServices:
    """
    Attributes:
        is_backup_resources_enabled (Union[Unset, bool]): Indicates whether cloud backup resources are allocated to a
            company. Default: True.
        backup_agents_management (Union['CompanyBackupAgentsManagementType0', None, Unset]): Number of Veeam backup
            agents that a company is allowed to manage.
        backup_servers_management (Union['CompanyBackupServerManagementType0', None, Unset]): Managed Veeam Backup &
            Replication server quota.
        vb_365_servers_management (Union['CompanyVb365ServerManagementType0', None, Unset]): Managed Veeam Backup for
            Microsoft 365 server quota.
        is_vb_public_cloud_management_enabled (Union[Unset, bool]): Indicates whether a company is allowed to manage
            public cloud appliances.' Default: False.
    """

    is_backup_resources_enabled: Union[Unset, bool] = True
    backup_agents_management: Union["CompanyBackupAgentsManagementType0", None, Unset] = UNSET
    backup_servers_management: Union["CompanyBackupServerManagementType0", None, Unset] = UNSET
    vb_365_servers_management: Union["CompanyVb365ServerManagementType0", None, Unset] = UNSET
    is_vb_public_cloud_management_enabled: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.company_backup_agents_management_type_0 import CompanyBackupAgentsManagementType0
        from ..models.company_backup_server_management_type_0 import CompanyBackupServerManagementType0
        from ..models.company_vb_365_server_management_type_0 import CompanyVb365ServerManagementType0

        is_backup_resources_enabled = self.is_backup_resources_enabled

        backup_agents_management: Union[None, Unset, dict[str, Any]]
        if isinstance(self.backup_agents_management, Unset):
            backup_agents_management = UNSET
        elif isinstance(self.backup_agents_management, CompanyBackupAgentsManagementType0):
            backup_agents_management = self.backup_agents_management.to_dict()
        else:
            backup_agents_management = self.backup_agents_management

        backup_servers_management: Union[None, Unset, dict[str, Any]]
        if isinstance(self.backup_servers_management, Unset):
            backup_servers_management = UNSET
        elif isinstance(self.backup_servers_management, CompanyBackupServerManagementType0):
            backup_servers_management = self.backup_servers_management.to_dict()
        else:
            backup_servers_management = self.backup_servers_management

        vb_365_servers_management: Union[None, Unset, dict[str, Any]]
        if isinstance(self.vb_365_servers_management, Unset):
            vb_365_servers_management = UNSET
        elif isinstance(self.vb_365_servers_management, CompanyVb365ServerManagementType0):
            vb_365_servers_management = self.vb_365_servers_management.to_dict()
        else:
            vb_365_servers_management = self.vb_365_servers_management

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
        from ..models.company_backup_agents_management_type_0 import CompanyBackupAgentsManagementType0
        from ..models.company_backup_server_management_type_0 import CompanyBackupServerManagementType0
        from ..models.company_vb_365_server_management_type_0 import CompanyVb365ServerManagementType0

        d = dict(src_dict)
        is_backup_resources_enabled = d.pop("isBackupResourcesEnabled", UNSET)

        def _parse_backup_agents_management(data: object) -> Union["CompanyBackupAgentsManagementType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_company_backup_agents_management_type_0 = (
                    CompanyBackupAgentsManagementType0.from_dict(data)
                )

                return componentsschemas_company_backup_agents_management_type_0
            except:  # noqa: E722
                pass
            return cast(Union["CompanyBackupAgentsManagementType0", None, Unset], data)

        backup_agents_management = _parse_backup_agents_management(d.pop("backupAgentsManagement", UNSET))

        def _parse_backup_servers_management(data: object) -> Union["CompanyBackupServerManagementType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_company_backup_server_management_type_0 = (
                    CompanyBackupServerManagementType0.from_dict(data)
                )

                return componentsschemas_company_backup_server_management_type_0
            except:  # noqa: E722
                pass
            return cast(Union["CompanyBackupServerManagementType0", None, Unset], data)

        backup_servers_management = _parse_backup_servers_management(d.pop("backupServersManagement", UNSET))

        def _parse_vb_365_servers_management(data: object) -> Union["CompanyVb365ServerManagementType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_company_vb_365_server_management_type_0 = CompanyVb365ServerManagementType0.from_dict(
                    data
                )

                return componentsschemas_company_vb_365_server_management_type_0
            except:  # noqa: E722
                pass
            return cast(Union["CompanyVb365ServerManagementType0", None, Unset], data)

        vb_365_servers_management = _parse_vb_365_servers_management(d.pop("vb365ServersManagement", UNSET))

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
