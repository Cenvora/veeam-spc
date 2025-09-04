from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.windows_workstation_job_event_trigger_settings_not_often_time_unit import (
    WindowsWorkstationJobEventTriggerSettingsNotOftenTimeUnit,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="WindowsWorkstationJobEventTriggerSettings")


@_attrs_define
class WindowsWorkstationJobEventTriggerSettings:
    """
    Attributes:
        backup_on_lock (Union[Unset, bool]): Indicates whether a scheduled backup job must start when the user locks the
            computer. Default: False.
        backup_on_log_off (Union[Unset, bool]): Indicates whether a scheduled backup job must start when the user
            working with the computer performs a logout operation. Default: False.
        backup_on_target_connection (Union[Unset, bool]): Indicates whether a scheduled backup job must start when the
            backup storage becomes available. Default: False.
        eject_target_on_backup_complete (Union[Unset, bool]): Indicates whether Veeam Agent for Microsoft Windows must
            unmount the storage device after the backup job completes successfully.
            > Cannot be enabled if the `backupOnTargetConnection` property has the `false` value.
             Default: False.
        backup_not_often (Union[Unset, int]): Minutely, hourly or daily interval between the backup job sessions.
            Default: 2.
        not_often_time_unit (Union[Unset, WindowsWorkstationJobEventTriggerSettingsNotOftenTimeUnit]): Measurement units
            of interval between the backup job sessions. Default:
            WindowsWorkstationJobEventTriggerSettingsNotOftenTimeUnit.HOURS.
    """

    backup_on_lock: Union[Unset, bool] = False
    backup_on_log_off: Union[Unset, bool] = False
    backup_on_target_connection: Union[Unset, bool] = False
    eject_target_on_backup_complete: Union[Unset, bool] = False
    backup_not_often: Union[Unset, int] = 2
    not_often_time_unit: Union[Unset, WindowsWorkstationJobEventTriggerSettingsNotOftenTimeUnit] = (
        WindowsWorkstationJobEventTriggerSettingsNotOftenTimeUnit.HOURS
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_on_lock = self.backup_on_lock

        backup_on_log_off = self.backup_on_log_off

        backup_on_target_connection = self.backup_on_target_connection

        eject_target_on_backup_complete = self.eject_target_on_backup_complete

        backup_not_often = self.backup_not_often

        not_often_time_unit: Union[Unset, str] = UNSET
        if not isinstance(self.not_often_time_unit, Unset):
            not_often_time_unit = self.not_often_time_unit.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_on_lock is not UNSET:
            field_dict["backupOnLock"] = backup_on_lock
        if backup_on_log_off is not UNSET:
            field_dict["backupOnLogOff"] = backup_on_log_off
        if backup_on_target_connection is not UNSET:
            field_dict["backupOnTargetConnection"] = backup_on_target_connection
        if eject_target_on_backup_complete is not UNSET:
            field_dict["ejectTargetOnBackupComplete"] = eject_target_on_backup_complete
        if backup_not_often is not UNSET:
            field_dict["backupNotOften"] = backup_not_often
        if not_often_time_unit is not UNSET:
            field_dict["notOftenTimeUnit"] = not_often_time_unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backup_on_lock = d.pop("backupOnLock", UNSET)

        backup_on_log_off = d.pop("backupOnLogOff", UNSET)

        backup_on_target_connection = d.pop("backupOnTargetConnection", UNSET)

        eject_target_on_backup_complete = d.pop("ejectTargetOnBackupComplete", UNSET)

        backup_not_often = d.pop("backupNotOften", UNSET)

        _not_often_time_unit = d.pop("notOftenTimeUnit", UNSET)
        not_often_time_unit: Union[Unset, WindowsWorkstationJobEventTriggerSettingsNotOftenTimeUnit]
        if isinstance(_not_often_time_unit, Unset):
            not_often_time_unit = UNSET
        else:
            not_often_time_unit = WindowsWorkstationJobEventTriggerSettingsNotOftenTimeUnit(_not_often_time_unit)

        windows_workstation_job_event_trigger_settings = cls(
            backup_on_lock=backup_on_lock,
            backup_on_log_off=backup_on_log_off,
            backup_on_target_connection=backup_on_target_connection,
            eject_target_on_backup_complete=eject_target_on_backup_complete,
            backup_not_often=backup_not_often,
            not_often_time_unit=not_often_time_unit,
        )

        windows_workstation_job_event_trigger_settings.additional_properties = d
        return windows_workstation_job_event_trigger_settings

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
