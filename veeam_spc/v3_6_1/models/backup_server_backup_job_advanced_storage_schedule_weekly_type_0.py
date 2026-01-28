from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.days_of_week import DaysOfWeek
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerBackupJobAdvancedStorageScheduleWeeklyType0")


@_attrs_define
class BackupServerBackupJobAdvancedStorageScheduleWeeklyType0:
    """Weekly schedule settings.

    Attributes:
        is_enabled (bool): Indicates whether the weekly schedule is enabled. Default: False.
        days (Union[None, Unset, list[DaysOfWeek]]): Array of week days when the operation is performed.
    """

    is_enabled: bool = False
    days: Union[None, Unset, list[DaysOfWeek]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        days: Union[None, Unset, list[str]]
        if isinstance(self.days, Unset):
            days = UNSET
        elif isinstance(self.days, list):
            days = []
            for days_type_0_item_data in self.days:
                days_type_0_item = days_type_0_item_data.value
                days.append(days_type_0_item)

        else:
            days = self.days

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

        def _parse_days(data: object) -> Union[None, Unset, list[DaysOfWeek]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                days_type_0 = []
                _days_type_0 = data
                for days_type_0_item_data in _days_type_0:
                    days_type_0_item = DaysOfWeek(days_type_0_item_data)

                    days_type_0.append(days_type_0_item)

                return days_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[DaysOfWeek]], data)

        days = _parse_days(d.pop("days", UNSET))

        backup_server_backup_job_advanced_storage_schedule_weekly_type_0 = cls(
            is_enabled=is_enabled,
            days=days,
        )

        backup_server_backup_job_advanced_storage_schedule_weekly_type_0.additional_properties = d
        return backup_server_backup_job_advanced_storage_schedule_weekly_type_0

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
