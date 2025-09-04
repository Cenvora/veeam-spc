from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyServices")


@_attrs_define
class CompanyServices:
    """
    Attributes:
        is_backup_agent_management_enabled (Union[Unset, bool]): Indicates whether Veeam backup agent management tools
            are displayed to company users. Default: True.
        is_backup_server_management_enabled (Union[Unset, bool]): Indicates whether Veeam Backup & Replication server
            management tools are displayed to company users. Default: True.
        is_vb_public_cloud_management_enabled (Union[Unset, bool]): Indicates whether integration with Veeam Backup for
            Public Clouds is available to company users. Default: True.
        backup_agent_server_quota (Union[None, Unset, int]): Maximum number of Veeam backup server agents that a company
            can manage.
        backup_agent_workstation_quota (Union[None, Unset, int]): Maximum number of Veeam backup workstation agents that
            a company can manage.
        storage_quota (Union[None, Unset, int]): Amount of space allocated to a company, in bytes.
    """

    is_backup_agent_management_enabled: Union[Unset, bool] = True
    is_backup_server_management_enabled: Union[Unset, bool] = True
    is_vb_public_cloud_management_enabled: Union[Unset, bool] = True
    backup_agent_server_quota: Union[None, Unset, int] = UNSET
    backup_agent_workstation_quota: Union[None, Unset, int] = UNSET
    storage_quota: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_backup_agent_management_enabled = self.is_backup_agent_management_enabled

        is_backup_server_management_enabled = self.is_backup_server_management_enabled

        is_vb_public_cloud_management_enabled = self.is_vb_public_cloud_management_enabled

        backup_agent_server_quota: Union[None, Unset, int]
        if isinstance(self.backup_agent_server_quota, Unset):
            backup_agent_server_quota = UNSET
        else:
            backup_agent_server_quota = self.backup_agent_server_quota

        backup_agent_workstation_quota: Union[None, Unset, int]
        if isinstance(self.backup_agent_workstation_quota, Unset):
            backup_agent_workstation_quota = UNSET
        else:
            backup_agent_workstation_quota = self.backup_agent_workstation_quota

        storage_quota: Union[None, Unset, int]
        if isinstance(self.storage_quota, Unset):
            storage_quota = UNSET
        else:
            storage_quota = self.storage_quota

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_backup_agent_management_enabled is not UNSET:
            field_dict["isBackupAgentManagementEnabled"] = is_backup_agent_management_enabled
        if is_backup_server_management_enabled is not UNSET:
            field_dict["isBackupServerManagementEnabled"] = is_backup_server_management_enabled
        if is_vb_public_cloud_management_enabled is not UNSET:
            field_dict["isVBPublicCloudManagementEnabled"] = is_vb_public_cloud_management_enabled
        if backup_agent_server_quota is not UNSET:
            field_dict["backupAgentServerQuota"] = backup_agent_server_quota
        if backup_agent_workstation_quota is not UNSET:
            field_dict["backupAgentWorkstationQuota"] = backup_agent_workstation_quota
        if storage_quota is not UNSET:
            field_dict["storageQuota"] = storage_quota

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_backup_agent_management_enabled = d.pop("isBackupAgentManagementEnabled", UNSET)

        is_backup_server_management_enabled = d.pop("isBackupServerManagementEnabled", UNSET)

        is_vb_public_cloud_management_enabled = d.pop("isVBPublicCloudManagementEnabled", UNSET)

        def _parse_backup_agent_server_quota(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        backup_agent_server_quota = _parse_backup_agent_server_quota(d.pop("backupAgentServerQuota", UNSET))

        def _parse_backup_agent_workstation_quota(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        backup_agent_workstation_quota = _parse_backup_agent_workstation_quota(
            d.pop("backupAgentWorkstationQuota", UNSET)
        )

        def _parse_storage_quota(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        storage_quota = _parse_storage_quota(d.pop("storageQuota", UNSET))

        company_services = cls(
            is_backup_agent_management_enabled=is_backup_agent_management_enabled,
            is_backup_server_management_enabled=is_backup_server_management_enabled,
            is_vb_public_cloud_management_enabled=is_vb_public_cloud_management_enabled,
            backup_agent_server_quota=backup_agent_server_quota,
            backup_agent_workstation_quota=backup_agent_workstation_quota,
            storage_quota=storage_quota,
        )

        company_services.additional_properties = d
        return company_services

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
