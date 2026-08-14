from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.windows_workstation_job_periodical_schedule_settings_finalizing_action import (
    WindowsWorkstationJobPeriodicalScheduleSettingsFinalizingAction,
)
from ..models.windows_workstation_job_periodical_schedule_settings_shutdown_action import (
    WindowsWorkstationJobPeriodicalScheduleSettingsShutdownAction,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.windows_daily_schedule_settings import WindowsDailyScheduleSettings


T = TypeVar("T", bound="WindowsWorkstationJobPeriodicalScheduleSettings")


@_attrs_define
class WindowsWorkstationJobPeriodicalScheduleSettings:
    """
    Attributes:
        daily_schedule_settings (WindowsDailyScheduleSettings | Unset):
        shutdown_action (WindowsWorkstationJobPeriodicalScheduleSettingsShutdownAction | Unset): Action that Veeam Agent
            for Microsoft Windows must perform in case your computer is powered off at the time when the scheduled backup
            job must start. Default: WindowsWorkstationJobPeriodicalScheduleSettingsShutdownAction.SKIPBACKUP.
        finalizing_action (WindowsWorkstationJobPeriodicalScheduleSettingsFinalizingAction | Unset): Finalizing action
            that must be performed after the backup job completes successfully. Default:
            WindowsWorkstationJobPeriodicalScheduleSettingsFinalizingAction.KEEPRUNNING.
    """

    daily_schedule_settings: WindowsDailyScheduleSettings | Unset = UNSET
    shutdown_action: WindowsWorkstationJobPeriodicalScheduleSettingsShutdownAction | Unset = (
        WindowsWorkstationJobPeriodicalScheduleSettingsShutdownAction.SKIPBACKUP
    )
    finalizing_action: WindowsWorkstationJobPeriodicalScheduleSettingsFinalizingAction | Unset = (
        WindowsWorkstationJobPeriodicalScheduleSettingsFinalizingAction.KEEPRUNNING
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        daily_schedule_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.daily_schedule_settings, Unset):
            daily_schedule_settings = self.daily_schedule_settings.to_dict()

        shutdown_action: str | Unset = UNSET
        if not isinstance(self.shutdown_action, Unset):
            shutdown_action = self.shutdown_action.value

        finalizing_action: str | Unset = UNSET
        if not isinstance(self.finalizing_action, Unset):
            finalizing_action = self.finalizing_action.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if daily_schedule_settings is not UNSET:
            field_dict["dailyScheduleSettings"] = daily_schedule_settings
        if shutdown_action is not UNSET:
            field_dict["shutdownAction"] = shutdown_action
        if finalizing_action is not UNSET:
            field_dict["finalizingAction"] = finalizing_action

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.windows_daily_schedule_settings import WindowsDailyScheduleSettings

        d = dict(src_dict)
        _daily_schedule_settings = d.pop("dailyScheduleSettings", UNSET)
        daily_schedule_settings: WindowsDailyScheduleSettings | Unset
        if isinstance(_daily_schedule_settings, Unset):
            daily_schedule_settings = UNSET
        else:
            daily_schedule_settings = WindowsDailyScheduleSettings.from_dict(_daily_schedule_settings)

        _shutdown_action = d.pop("shutdownAction", UNSET)
        shutdown_action: WindowsWorkstationJobPeriodicalScheduleSettingsShutdownAction | Unset
        if isinstance(_shutdown_action, Unset):
            shutdown_action = UNSET
        else:
            shutdown_action = WindowsWorkstationJobPeriodicalScheduleSettingsShutdownAction(_shutdown_action)

        _finalizing_action = d.pop("finalizingAction", UNSET)
        finalizing_action: WindowsWorkstationJobPeriodicalScheduleSettingsFinalizingAction | Unset
        if isinstance(_finalizing_action, Unset):
            finalizing_action = UNSET
        else:
            finalizing_action = WindowsWorkstationJobPeriodicalScheduleSettingsFinalizingAction(_finalizing_action)

        windows_workstation_job_periodical_schedule_settings = cls(
            daily_schedule_settings=daily_schedule_settings,
            shutdown_action=shutdown_action,
            finalizing_action=finalizing_action,
        )

        windows_workstation_job_periodical_schedule_settings.additional_properties = d
        return windows_workstation_job_periodical_schedule_settings

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
