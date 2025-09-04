from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.windows_advanced_schedule_settings import WindowsAdvancedScheduleSettings
    from ..models.windows_backup_storage import WindowsBackupStorage
    from ..models.windows_maintenance_job_settings import WindowsMaintenanceJobSettings


T = TypeVar("T", bound="WindowsAdvancedJobSettings")


@_attrs_define
class WindowsAdvancedJobSettings:
    """
    Attributes:
        backup_storage (Union[Unset, WindowsBackupStorage]):
        schedule_settings (Union[Unset, WindowsAdvancedScheduleSettings]):
        maintenance_settings (Union[Unset, WindowsMaintenanceJobSettings]):
    """

    backup_storage: Union[Unset, "WindowsBackupStorage"] = UNSET
    schedule_settings: Union[Unset, "WindowsAdvancedScheduleSettings"] = UNSET
    maintenance_settings: Union[Unset, "WindowsMaintenanceJobSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_storage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.backup_storage, Unset):
            backup_storage = self.backup_storage.to_dict()

        schedule_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schedule_settings, Unset):
            schedule_settings = self.schedule_settings.to_dict()

        maintenance_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.maintenance_settings, Unset):
            maintenance_settings = self.maintenance_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_storage is not UNSET:
            field_dict["backupStorage"] = backup_storage
        if schedule_settings is not UNSET:
            field_dict["scheduleSettings"] = schedule_settings
        if maintenance_settings is not UNSET:
            field_dict["maintenanceSettings"] = maintenance_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.windows_advanced_schedule_settings import WindowsAdvancedScheduleSettings
        from ..models.windows_backup_storage import WindowsBackupStorage
        from ..models.windows_maintenance_job_settings import WindowsMaintenanceJobSettings

        d = dict(src_dict)
        _backup_storage = d.pop("backupStorage", UNSET)
        backup_storage: Union[Unset, WindowsBackupStorage]
        if isinstance(_backup_storage, Unset):
            backup_storage = UNSET
        else:
            backup_storage = WindowsBackupStorage.from_dict(_backup_storage)

        _schedule_settings = d.pop("scheduleSettings", UNSET)
        schedule_settings: Union[Unset, WindowsAdvancedScheduleSettings]
        if isinstance(_schedule_settings, Unset):
            schedule_settings = UNSET
        else:
            schedule_settings = WindowsAdvancedScheduleSettings.from_dict(_schedule_settings)

        _maintenance_settings = d.pop("maintenanceSettings", UNSET)
        maintenance_settings: Union[Unset, WindowsMaintenanceJobSettings]
        if isinstance(_maintenance_settings, Unset):
            maintenance_settings = UNSET
        else:
            maintenance_settings = WindowsMaintenanceJobSettings.from_dict(_maintenance_settings)

        windows_advanced_job_settings = cls(
            backup_storage=backup_storage,
            schedule_settings=schedule_settings,
            maintenance_settings=maintenance_settings,
        )

        windows_advanced_job_settings.additional_properties = d
        return windows_advanced_job_settings

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
