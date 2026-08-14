from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_job_time_period import BackupServerJobTimePeriod


T = TypeVar("T", bound="BackupServerJobScheduleOptionsBackupWindow")


@_attrs_define
class BackupServerJobScheduleOptionsBackupWindow:
    """
    Attributes:
        time_periods (list[BackupServerJobTimePeriod] | Unset): Array of the backup window periods.
    """

    time_periods: list[BackupServerJobTimePeriod] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_periods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.time_periods, Unset):
            time_periods = []
            for time_periods_item_data in self.time_periods:
                time_periods_item = time_periods_item_data.to_dict()
                time_periods.append(time_periods_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time_periods is not UNSET:
            field_dict["timePeriods"] = time_periods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_job_time_period import BackupServerJobTimePeriod

        d = dict(src_dict)
        _time_periods = d.pop("timePeriods", UNSET)
        time_periods: list[BackupServerJobTimePeriod] | Unset = UNSET
        if _time_periods is not UNSET:
            time_periods = []
            for time_periods_item_data in _time_periods:
                time_periods_item = BackupServerJobTimePeriod.from_dict(time_periods_item_data)

                time_periods.append(time_periods_item)

        backup_server_job_schedule_options_backup_window = cls(
            time_periods=time_periods,
        )

        backup_server_job_schedule_options_backup_window.additional_properties = d
        return backup_server_job_schedule_options_backup_window

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
