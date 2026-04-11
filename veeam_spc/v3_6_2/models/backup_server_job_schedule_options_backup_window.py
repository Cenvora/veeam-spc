from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
        time_periods (list[BackupServerJobTimePeriod] | None | Unset): Array of the backup window periods.
    """

    time_periods: list[BackupServerJobTimePeriod] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_periods: list[dict[str, Any]] | None | Unset
        if isinstance(self.time_periods, Unset):
            time_periods = UNSET
        elif isinstance(self.time_periods, list):
            time_periods = []
            for time_periods_type_0_item_data in self.time_periods:
                time_periods_type_0_item = time_periods_type_0_item_data.to_dict()
                time_periods.append(time_periods_type_0_item)

        else:
            time_periods = self.time_periods

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

        def _parse_time_periods(data: object) -> list[BackupServerJobTimePeriod] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                time_periods_type_0 = []
                _time_periods_type_0 = data
                for time_periods_type_0_item_data in _time_periods_type_0:
                    time_periods_type_0_item = BackupServerJobTimePeriod.from_dict(time_periods_type_0_item_data)

                    time_periods_type_0.append(time_periods_type_0_item)

                return time_periods_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BackupServerJobTimePeriod] | None | Unset, data)

        time_periods = _parse_time_periods(d.pop("timePeriods", UNSET))

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
