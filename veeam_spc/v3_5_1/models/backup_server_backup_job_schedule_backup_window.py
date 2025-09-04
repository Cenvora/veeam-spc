from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_window_setting import BackupServerBackupJobWindowSetting


T = TypeVar("T", bound="BackupServerBackupJobScheduleBackupWindow")


@_attrs_define
class BackupServerBackupJobScheduleBackupWindow:
    """Backup window settings.

    Attributes:
        is_enabled (bool): Indicates whether backup window is enabled. Default: False.
        backup_window (Union[Unset, BackupServerBackupJobWindowSetting]): Array of daily schemes that define backup
            window.
    """

    is_enabled: bool = False
    backup_window: Union[Unset, "BackupServerBackupJobWindowSetting"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        backup_window: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.backup_window, Unset):
            backup_window = self.backup_window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isEnabled": is_enabled,
            }
        )
        if backup_window is not UNSET:
            field_dict["backupWindow"] = backup_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_backup_job_window_setting import BackupServerBackupJobWindowSetting

        d = dict(src_dict)
        is_enabled = d.pop("isEnabled")

        _backup_window = d.pop("backupWindow", UNSET)
        backup_window: Union[Unset, BackupServerBackupJobWindowSetting]
        if isinstance(_backup_window, Unset):
            backup_window = UNSET
        else:
            backup_window = BackupServerBackupJobWindowSetting.from_dict(_backup_window)

        backup_server_backup_job_schedule_backup_window = cls(
            is_enabled=is_enabled,
            backup_window=backup_window,
        )

        backup_server_backup_job_schedule_backup_window.additional_properties = d
        return backup_server_backup_job_schedule_backup_window

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
