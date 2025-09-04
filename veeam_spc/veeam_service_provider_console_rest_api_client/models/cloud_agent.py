from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudAgent")


@_attrs_define
class CloudAgent:
    """Information about a Veeam Cloud Connect server on which a management agent is deployed.

    Attributes:
        site_name (str): Name of a Veeam Cloud Connect site.
        site_uid (Union[Unset, UUID]): UID assigned to a Veeam Cloud Connect server on which a management agent is
            installed.
        description (Union[Unset, str]): Description of a Veeam Cloud Connect site.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup & Replication server.
        management_agent_uid (Union[Unset, UUID]): UID assigned to a management agent.
        maintenance_mode_is_enabled (Union[Unset, bool]): Indicates whether the maintenance mode is enabled for a Veeam
            Cloud Connect site.
            > Can be changed by performing the `SetSiteMaintenanceMode` operation.
        tenant_management_in_cloud_connect_is_enabled (Union[Unset, bool]): Indicates whether tenant and cloud resource
            management in Veeam Service Provider Console and Veeam Backup & Replication console is allowed.
            > Can be changed by performing the `SetSiteTenantManagementMode` operation.
    """

    site_name: str
    site_uid: Union[Unset, UUID] = UNSET
    description: Union[Unset, str] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    management_agent_uid: Union[Unset, UUID] = UNSET
    maintenance_mode_is_enabled: Union[Unset, bool] = UNSET
    tenant_management_in_cloud_connect_is_enabled: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_name = self.site_name

        site_uid: Union[Unset, str] = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        description = self.description

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        management_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.management_agent_uid, Unset):
            management_agent_uid = str(self.management_agent_uid)

        maintenance_mode_is_enabled = self.maintenance_mode_is_enabled

        tenant_management_in_cloud_connect_is_enabled = self.tenant_management_in_cloud_connect_is_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "siteName": site_name,
            }
        )
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid
        if description is not UNSET:
            field_dict["description"] = description
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if management_agent_uid is not UNSET:
            field_dict["managementAgentUid"] = management_agent_uid
        if maintenance_mode_is_enabled is not UNSET:
            field_dict["maintenanceModeIsEnabled"] = maintenance_mode_is_enabled
        if tenant_management_in_cloud_connect_is_enabled is not UNSET:
            field_dict["tenantManagementInCloudConnectIsEnabled"] = tenant_management_in_cloud_connect_is_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        site_name = d.pop("siteName")

        _site_uid = d.pop("siteUid", UNSET)
        site_uid: Union[Unset, UUID]
        if isinstance(_site_uid, Unset):
            site_uid = UNSET
        else:
            site_uid = UUID(_site_uid)

        description = d.pop("description", UNSET)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: Union[Unset, UUID]
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        _management_agent_uid = d.pop("managementAgentUid", UNSET)
        management_agent_uid: Union[Unset, UUID]
        if isinstance(_management_agent_uid, Unset):
            management_agent_uid = UNSET
        else:
            management_agent_uid = UUID(_management_agent_uid)

        maintenance_mode_is_enabled = d.pop("maintenanceModeIsEnabled", UNSET)

        tenant_management_in_cloud_connect_is_enabled = d.pop("tenantManagementInCloudConnectIsEnabled", UNSET)

        cloud_agent = cls(
            site_name=site_name,
            site_uid=site_uid,
            description=description,
            backup_server_uid=backup_server_uid,
            management_agent_uid=management_agent_uid,
            maintenance_mode_is_enabled=maintenance_mode_is_enabled,
            tenant_management_in_cloud_connect_is_enabled=tenant_management_in_cloud_connect_is_enabled,
        )

        cloud_agent.additional_properties = d
        return cloud_agent

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
