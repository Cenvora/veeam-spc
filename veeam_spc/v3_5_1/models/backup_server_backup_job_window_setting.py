from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_window_day_hours import BackupServerBackupJobWindowDayHours


T = TypeVar("T", bound="BackupServerBackupJobWindowSetting")


@_attrs_define
class BackupServerBackupJobWindowSetting:
    """Array of daily schemes that define backup window.

    Attributes:
        days (list['BackupServerBackupJobWindowDayHours']):
    """

    days: list["BackupServerBackupJobWindowDayHours"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        days = []
        for days_item_data in self.days:
            days_item = days_item_data.to_dict()
            days.append(days_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "days": days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_backup_job_window_day_hours import BackupServerBackupJobWindowDayHours

        d = dict(src_dict)
        days = []
        _days = d.pop("days")
        for days_item_data in _days:
            days_item = BackupServerBackupJobWindowDayHours.from_dict(days_item_data)

            days.append(days_item)

        backup_server_backup_job_window_setting = cls(
            days=days,
        )

        backup_server_backup_job_window_setting.additional_properties = d
        return backup_server_backup_job_window_setting

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
