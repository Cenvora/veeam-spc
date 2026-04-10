from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monthly_or_weekly_schedule_settings import MonthlyOrWeeklyScheduleSettings


T = TypeVar("T", bound="WindowsFullBackupFileMaintenanceSettings")


@_attrs_define
class WindowsFullBackupFileMaintenanceSettings:
    """
    Attributes:
        enable_deleted_files_retention (Union[Unset, bool]): [For Veeam backup repository and cloud repository targets]
            Defines whether the deleted backup files must be removed after a specific time period. Default: False.
        remove_deleted_items_data_after (Union[Unset, int]): [For Veeam backup repository and cloud repository targets]
            Number of days for which the deleted backup files are stored. Default: 30.
        defragment_and_compact_full_backup_file_settings (Union[Unset, MonthlyOrWeeklyScheduleSettings]):
    """

    enable_deleted_files_retention: Union[Unset, bool] = False
    remove_deleted_items_data_after: Union[Unset, int] = 30
    defragment_and_compact_full_backup_file_settings: Union[Unset, "MonthlyOrWeeklyScheduleSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable_deleted_files_retention = self.enable_deleted_files_retention

        remove_deleted_items_data_after = self.remove_deleted_items_data_after

        defragment_and_compact_full_backup_file_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.defragment_and_compact_full_backup_file_settings, Unset):
            defragment_and_compact_full_backup_file_settings = (
                self.defragment_and_compact_full_backup_file_settings.to_dict()
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable_deleted_files_retention is not UNSET:
            field_dict["enableDeletedFilesRetention"] = enable_deleted_files_retention
        if remove_deleted_items_data_after is not UNSET:
            field_dict["removeDeletedItemsDataAfter"] = remove_deleted_items_data_after
        if defragment_and_compact_full_backup_file_settings is not UNSET:
            field_dict["defragmentAndCompactFullBackupFileSettings"] = defragment_and_compact_full_backup_file_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monthly_or_weekly_schedule_settings import MonthlyOrWeeklyScheduleSettings

        d = dict(src_dict)
        enable_deleted_files_retention = d.pop("enableDeletedFilesRetention", UNSET)

        remove_deleted_items_data_after = d.pop("removeDeletedItemsDataAfter", UNSET)

        _defragment_and_compact_full_backup_file_settings = d.pop("defragmentAndCompactFullBackupFileSettings", UNSET)
        defragment_and_compact_full_backup_file_settings: Union[Unset, MonthlyOrWeeklyScheduleSettings]
        if isinstance(_defragment_and_compact_full_backup_file_settings, Unset):
            defragment_and_compact_full_backup_file_settings = UNSET
        else:
            defragment_and_compact_full_backup_file_settings = MonthlyOrWeeklyScheduleSettings.from_dict(
                _defragment_and_compact_full_backup_file_settings
            )

        windows_full_backup_file_maintenance_settings = cls(
            enable_deleted_files_retention=enable_deleted_files_retention,
            remove_deleted_items_data_after=remove_deleted_items_data_after,
            defragment_and_compact_full_backup_file_settings=defragment_and_compact_full_backup_file_settings,
        )

        windows_full_backup_file_maintenance_settings.additional_properties = d
        return windows_full_backup_file_maintenance_settings

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
