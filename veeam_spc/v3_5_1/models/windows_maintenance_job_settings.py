from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monthly_or_weekly_schedule_settings import MonthlyOrWeeklyScheduleSettings
    from ..models.windows_full_backup_file_maintenance_settings import WindowsFullBackupFileMaintenanceSettings


T = TypeVar("T", bound="WindowsMaintenanceJobSettings")


@_attrs_define
class WindowsMaintenanceJobSettings:
    """
    Attributes:
        backup_health_check_settings (Union[Unset, MonthlyOrWeeklyScheduleSettings]):
        full_backup_file_maintenance_settings (Union[Unset, WindowsFullBackupFileMaintenanceSettings]):
        full_health_check (Union[Unset, bool]): Indicates whether a full health check is enabled for an object storage.
            Default: False.
    """

    backup_health_check_settings: Union[Unset, "MonthlyOrWeeklyScheduleSettings"] = UNSET
    full_backup_file_maintenance_settings: Union[Unset, "WindowsFullBackupFileMaintenanceSettings"] = UNSET
    full_health_check: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_health_check_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.backup_health_check_settings, Unset):
            backup_health_check_settings = self.backup_health_check_settings.to_dict()

        full_backup_file_maintenance_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.full_backup_file_maintenance_settings, Unset):
            full_backup_file_maintenance_settings = self.full_backup_file_maintenance_settings.to_dict()

        full_health_check = self.full_health_check

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_health_check_settings is not UNSET:
            field_dict["backupHealthCheckSettings"] = backup_health_check_settings
        if full_backup_file_maintenance_settings is not UNSET:
            field_dict["fullBackupFileMaintenanceSettings"] = full_backup_file_maintenance_settings
        if full_health_check is not UNSET:
            field_dict["fullHealthCheck"] = full_health_check

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monthly_or_weekly_schedule_settings import MonthlyOrWeeklyScheduleSettings
        from ..models.windows_full_backup_file_maintenance_settings import WindowsFullBackupFileMaintenanceSettings

        d = dict(src_dict)
        _backup_health_check_settings = d.pop("backupHealthCheckSettings", UNSET)
        backup_health_check_settings: Union[Unset, MonthlyOrWeeklyScheduleSettings]
        if isinstance(_backup_health_check_settings, Unset):
            backup_health_check_settings = UNSET
        else:
            backup_health_check_settings = MonthlyOrWeeklyScheduleSettings.from_dict(_backup_health_check_settings)

        _full_backup_file_maintenance_settings = d.pop("fullBackupFileMaintenanceSettings", UNSET)
        full_backup_file_maintenance_settings: Union[Unset, WindowsFullBackupFileMaintenanceSettings]
        if isinstance(_full_backup_file_maintenance_settings, Unset):
            full_backup_file_maintenance_settings = UNSET
        else:
            full_backup_file_maintenance_settings = WindowsFullBackupFileMaintenanceSettings.from_dict(
                _full_backup_file_maintenance_settings
            )

        full_health_check = d.pop("fullHealthCheck", UNSET)

        windows_maintenance_job_settings = cls(
            backup_health_check_settings=backup_health_check_settings,
            full_backup_file_maintenance_settings=full_backup_file_maintenance_settings,
            full_health_check=full_health_check,
        )

        windows_maintenance_job_settings.additional_properties = d
        return windows_maintenance_job_settings

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
