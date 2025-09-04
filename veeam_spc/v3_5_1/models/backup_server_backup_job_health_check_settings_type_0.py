from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_advanced_storage_schedule_monthly_type_0 import (
        BackupServerBackupJobAdvancedStorageScheduleMonthlyType0,
    )
    from ..models.backup_server_backup_job_advanced_storage_schedule_weekly_type_0 import (
        BackupServerBackupJobAdvancedStorageScheduleWeeklyType0,
    )


T = TypeVar("T", bound="BackupServerBackupJobHealthCheckSettingsType0")


@_attrs_define
class BackupServerBackupJobHealthCheckSettingsType0:
    """Health check settings for the latest restore point in the backup chain.

    Attributes:
        is_enabled (bool): Indicates whether health checks are enabled.
        weekly (Union['BackupServerBackupJobAdvancedStorageScheduleWeeklyType0', None, Unset]): Weekly schedule
            settings.
        monthly (Union['BackupServerBackupJobAdvancedStorageScheduleMonthlyType0', None, Unset]): Monthly schedule
            settings.
    """

    is_enabled: bool
    weekly: Union["BackupServerBackupJobAdvancedStorageScheduleWeeklyType0", None, Unset] = UNSET
    monthly: Union["BackupServerBackupJobAdvancedStorageScheduleMonthlyType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.backup_server_backup_job_advanced_storage_schedule_monthly_type_0 import (
            BackupServerBackupJobAdvancedStorageScheduleMonthlyType0,
        )
        from ..models.backup_server_backup_job_advanced_storage_schedule_weekly_type_0 import (
            BackupServerBackupJobAdvancedStorageScheduleWeeklyType0,
        )

        is_enabled = self.is_enabled

        weekly: Union[None, Unset, dict[str, Any]]
        if isinstance(self.weekly, Unset):
            weekly = UNSET
        elif isinstance(self.weekly, BackupServerBackupJobAdvancedStorageScheduleWeeklyType0):
            weekly = self.weekly.to_dict()
        else:
            weekly = self.weekly

        monthly: Union[None, Unset, dict[str, Any]]
        if isinstance(self.monthly, Unset):
            monthly = UNSET
        elif isinstance(self.monthly, BackupServerBackupJobAdvancedStorageScheduleMonthlyType0):
            monthly = self.monthly.to_dict()
        else:
            monthly = self.monthly

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
        from ..models.backup_server_backup_job_advanced_storage_schedule_monthly_type_0 import (
            BackupServerBackupJobAdvancedStorageScheduleMonthlyType0,
        )
        from ..models.backup_server_backup_job_advanced_storage_schedule_weekly_type_0 import (
            BackupServerBackupJobAdvancedStorageScheduleWeeklyType0,
        )

        d = dict(src_dict)
        is_enabled = d.pop("isEnabled")

        def _parse_weekly(
            data: object,
        ) -> Union["BackupServerBackupJobAdvancedStorageScheduleWeeklyType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_advanced_storage_schedule_weekly_type_0 = (
                    BackupServerBackupJobAdvancedStorageScheduleWeeklyType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_advanced_storage_schedule_weekly_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobAdvancedStorageScheduleWeeklyType0", None, Unset], data)

        weekly = _parse_weekly(d.pop("weekly", UNSET))

        def _parse_monthly(
            data: object,
        ) -> Union["BackupServerBackupJobAdvancedStorageScheduleMonthlyType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_advanced_storage_schedule_monthly_type_0 = (
                    BackupServerBackupJobAdvancedStorageScheduleMonthlyType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_advanced_storage_schedule_monthly_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobAdvancedStorageScheduleMonthlyType0", None, Unset], data)

        monthly = _parse_monthly(d.pop("monthly", UNSET))

        backup_server_backup_job_health_check_settings_type_0 = cls(
            is_enabled=is_enabled,
            weekly=weekly,
            monthly=monthly,
        )

        backup_server_backup_job_health_check_settings_type_0.additional_properties = d
        return backup_server_backup_job_health_check_settings_type_0

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
