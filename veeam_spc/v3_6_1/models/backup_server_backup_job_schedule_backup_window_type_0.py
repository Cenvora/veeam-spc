from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_window_setting_type_0 import BackupServerBackupJobWindowSettingType0


T = TypeVar("T", bound="BackupServerBackupJobScheduleBackupWindowType0")


@_attrs_define
class BackupServerBackupJobScheduleBackupWindowType0:
    """Backup window settings.

    Attributes:
        is_enabled (bool): Indicates whether backup window is enabled. Default: False.
        backup_window (Union['BackupServerBackupJobWindowSettingType0', None, Unset]): Array of daily schemes that
            define backup window.
    """

    is_enabled: bool = False
    backup_window: Union["BackupServerBackupJobWindowSettingType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.backup_server_backup_job_window_setting_type_0 import BackupServerBackupJobWindowSettingType0

        is_enabled = self.is_enabled

        backup_window: Union[None, Unset, dict[str, Any]]
        if isinstance(self.backup_window, Unset):
            backup_window = UNSET
        elif isinstance(self.backup_window, BackupServerBackupJobWindowSettingType0):
            backup_window = self.backup_window.to_dict()
        else:
            backup_window = self.backup_window

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
        from ..models.backup_server_backup_job_window_setting_type_0 import BackupServerBackupJobWindowSettingType0

        d = dict(src_dict)
        is_enabled = d.pop("isEnabled")

        def _parse_backup_window(data: object) -> Union["BackupServerBackupJobWindowSettingType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_window_setting_type_0 = (
                    BackupServerBackupJobWindowSettingType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_window_setting_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobWindowSettingType0", None, Unset], data)

        backup_window = _parse_backup_window(d.pop("backupWindow", UNSET))

        backup_server_backup_job_schedule_backup_window_type_0 = cls(
            is_enabled=is_enabled,
            backup_window=backup_window,
        )

        backup_server_backup_job_schedule_backup_window_type_0.additional_properties = d
        return backup_server_backup_job_schedule_backup_window_type_0

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
