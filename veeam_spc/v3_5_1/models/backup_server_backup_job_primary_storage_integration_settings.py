from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerBackupJobPrimaryStorageIntegrationSettings")


@_attrs_define
class BackupServerBackupJobPrimaryStorageIntegrationSettings:
    """Backup from Storage Snapshots settings.

    Attributes:
        is_enabled (Union[Unset, bool]): Indicates whether Backup from Storage Snapshots is enabled. Default: True.
        limit_processed_vm (Union[Unset, bool]): Indicates whether the number of processed VMs for one storage snapshot
            is limited. Default: False.
        limit_processed_vm_count (Union[Unset, int]): Maximum number of processed VMs for one storage snapshot. Default:
            10.
        failover_to_standard_backup (Union[Unset, bool]): Indicates whether failover to regular VM snapshot processing
            is enabled in case Veeam Backup & Replication fails to create storage snapshot. Default: False.
    """

    is_enabled: Union[Unset, bool] = True
    limit_processed_vm: Union[Unset, bool] = False
    limit_processed_vm_count: Union[Unset, int] = 10
    failover_to_standard_backup: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        limit_processed_vm = self.limit_processed_vm

        limit_processed_vm_count = self.limit_processed_vm_count

        failover_to_standard_backup = self.failover_to_standard_backup

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if limit_processed_vm is not UNSET:
            field_dict["limitProcessedVm"] = limit_processed_vm
        if limit_processed_vm_count is not UNSET:
            field_dict["limitProcessedVmCount"] = limit_processed_vm_count
        if failover_to_standard_backup is not UNSET:
            field_dict["failoverToStandardBackup"] = failover_to_standard_backup

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_enabled = d.pop("isEnabled", UNSET)

        limit_processed_vm = d.pop("limitProcessedVm", UNSET)

        limit_processed_vm_count = d.pop("limitProcessedVmCount", UNSET)

        failover_to_standard_backup = d.pop("failoverToStandardBackup", UNSET)

        backup_server_backup_job_primary_storage_integration_settings = cls(
            is_enabled=is_enabled,
            limit_processed_vm=limit_processed_vm,
            limit_processed_vm_count=limit_processed_vm_count,
            failover_to_standard_backup=failover_to_standard_backup,
        )

        backup_server_backup_job_primary_storage_integration_settings.additional_properties = d
        return backup_server_backup_job_primary_storage_integration_settings

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
