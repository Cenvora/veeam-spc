from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerBackupJobFullBackupMaintenanceRemoveDataType0")


@_attrs_define
class BackupServerBackupJobFullBackupMaintenanceRemoveDataType0:
    """Backup data settings for deleted VMs.

    Attributes:
        is_enabled (bool): Indicates whether Veeam Backup & Replication keeps the backup data of the deleted VMs.
        after_days (Union[Unset, int]): Number of days during which Veeam Backup & Replication keeps the backup data of
            the deleted VMs. Default: 14.
    """

    is_enabled: bool
    after_days: Union[Unset, int] = 14
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        after_days = self.after_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isEnabled": is_enabled,
            }
        )
        if after_days is not UNSET:
            field_dict["afterDays"] = after_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_enabled = d.pop("isEnabled")

        after_days = d.pop("afterDays", UNSET)

        backup_server_backup_job_full_backup_maintenance_remove_data_type_0 = cls(
            is_enabled=is_enabled,
            after_days=after_days,
        )

        backup_server_backup_job_full_backup_maintenance_remove_data_type_0.additional_properties = d
        return backup_server_backup_job_full_backup_maintenance_remove_data_type_0

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
