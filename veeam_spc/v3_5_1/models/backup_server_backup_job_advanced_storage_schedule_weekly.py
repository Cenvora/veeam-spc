from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.days_of_week import DaysOfWeek
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerBackupJobAdvancedStorageScheduleWeekly")


@_attrs_define
class BackupServerBackupJobAdvancedStorageScheduleWeekly:
    """Weekly schedule settings.

    Attributes:
        is_enabled (bool): Indicates whether the weekly schedule is enabled. Default: False.
        days (Union[Unset, list[DaysOfWeek]]): Array of week days when the operation is performed.
    """

    is_enabled: bool = False
    days: Union[Unset, list[DaysOfWeek]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        days: Union[Unset, list[str]] = UNSET
        if not isinstance(self.days, Unset):
            days = []
            for days_item_data in self.days:
                days_item = days_item_data.value
                days.append(days_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isEnabled": is_enabled,
            }
        )
        if days is not UNSET:
            field_dict["days"] = days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_enabled = d.pop("isEnabled")

        days = []
        _days = d.pop("days", UNSET)
        for days_item_data in _days or []:
            days_item = DaysOfWeek(days_item_data)

            days.append(days_item)

        backup_server_backup_job_advanced_storage_schedule_weekly = cls(
            is_enabled=is_enabled,
            days=days,
        )

        backup_server_backup_job_advanced_storage_schedule_weekly.additional_properties = d
        return backup_server_backup_job_advanced_storage_schedule_weekly

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
