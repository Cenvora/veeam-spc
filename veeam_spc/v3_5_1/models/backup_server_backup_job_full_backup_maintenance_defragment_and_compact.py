from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_advanced_storage_schedule_monthly import (
        BackupServerBackupJobAdvancedStorageScheduleMonthly,
    )
    from ..models.backup_server_backup_job_advanced_storage_schedule_weekly import (
        BackupServerBackupJobAdvancedStorageScheduleWeekly,
    )


T = TypeVar("T", bound="BackupServerBackupJobFullBackupMaintenanceDefragmentAndCompact")


@_attrs_define
class BackupServerBackupJobFullBackupMaintenanceDefragmentAndCompact:
    """Compact operation settings.

    Attributes:
        is_enabled (bool): Indicates whether periodical full backup compact feature is enabled.
        weekly (Union[Unset, BackupServerBackupJobAdvancedStorageScheduleWeekly]): Weekly schedule settings.
        monthly (Union[Unset, BackupServerBackupJobAdvancedStorageScheduleMonthly]): Monthly schedule settings.
    """

    is_enabled: bool
    weekly: Union[Unset, "BackupServerBackupJobAdvancedStorageScheduleWeekly"] = UNSET
    monthly: Union[Unset, "BackupServerBackupJobAdvancedStorageScheduleMonthly"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        weekly: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.weekly, Unset):
            weekly = self.weekly.to_dict()

        monthly: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.monthly, Unset):
            monthly = self.monthly.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isEnabled": is_enabled,
            }
        )
        if weekly is not UNSET:
            field_dict["weekly"] = weekly
        if monthly is not UNSET:
            field_dict["monthly"] = monthly

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_backup_job_advanced_storage_schedule_monthly import (
            BackupServerBackupJobAdvancedStorageScheduleMonthly,
        )
        from ..models.backup_server_backup_job_advanced_storage_schedule_weekly import (
            BackupServerBackupJobAdvancedStorageScheduleWeekly,
        )

        d = dict(src_dict)
        is_enabled = d.pop("isEnabled")

        _weekly = d.pop("weekly", UNSET)
        weekly: Union[Unset, BackupServerBackupJobAdvancedStorageScheduleWeekly]
        if isinstance(_weekly, Unset):
            weekly = UNSET
        else:
            weekly = BackupServerBackupJobAdvancedStorageScheduleWeekly.from_dict(_weekly)

        _monthly = d.pop("monthly", UNSET)
        monthly: Union[Unset, BackupServerBackupJobAdvancedStorageScheduleMonthly]
        if isinstance(_monthly, Unset):
            monthly = UNSET
        else:
            monthly = BackupServerBackupJobAdvancedStorageScheduleMonthly.from_dict(_monthly)

        backup_server_backup_job_full_backup_maintenance_defragment_and_compact = cls(
            is_enabled=is_enabled,
            weekly=weekly,
            monthly=monthly,
        )

        backup_server_backup_job_full_backup_maintenance_defragment_and_compact.additional_properties = d
        return backup_server_backup_job_full_backup_maintenance_defragment_and_compact

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
