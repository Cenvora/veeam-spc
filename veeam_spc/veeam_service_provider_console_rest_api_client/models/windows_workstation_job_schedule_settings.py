from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.windows_workstation_job_event_trigger_settings import WindowsWorkstationJobEventTriggerSettings
    from ..models.windows_workstation_job_periodical_schedule_settings import (
        WindowsWorkstationJobPeriodicalScheduleSettings,
    )


T = TypeVar("T", bound="WindowsWorkstationJobScheduleSettings")


@_attrs_define
class WindowsWorkstationJobScheduleSettings:
    """
    Attributes:
        periodical_schedule_enabled (Union[Unset, bool]): Indicates whether backup must be performed periodically.
            Default: True.
        periodical_schedule_settings (Union[Unset, WindowsWorkstationJobPeriodicalScheduleSettings]):
        event_trigger_settings (Union[Unset, WindowsWorkstationJobEventTriggerSettings]):
    """

    periodical_schedule_enabled: Union[Unset, bool] = True
    periodical_schedule_settings: Union[Unset, "WindowsWorkstationJobPeriodicalScheduleSettings"] = UNSET
    event_trigger_settings: Union[Unset, "WindowsWorkstationJobEventTriggerSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        periodical_schedule_enabled = self.periodical_schedule_enabled

        periodical_schedule_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.periodical_schedule_settings, Unset):
            periodical_schedule_settings = self.periodical_schedule_settings.to_dict()

        event_trigger_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event_trigger_settings, Unset):
            event_trigger_settings = self.event_trigger_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if periodical_schedule_enabled is not UNSET:
            field_dict["periodicalScheduleEnabled"] = periodical_schedule_enabled
        if periodical_schedule_settings is not UNSET:
            field_dict["periodicalScheduleSettings"] = periodical_schedule_settings
        if event_trigger_settings is not UNSET:
            field_dict["eventTriggerSettings"] = event_trigger_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.windows_workstation_job_event_trigger_settings import WindowsWorkstationJobEventTriggerSettings
        from ..models.windows_workstation_job_periodical_schedule_settings import (
            WindowsWorkstationJobPeriodicalScheduleSettings,
        )

        d = dict(src_dict)
        periodical_schedule_enabled = d.pop("periodicalScheduleEnabled", UNSET)

        _periodical_schedule_settings = d.pop("periodicalScheduleSettings", UNSET)
        periodical_schedule_settings: Union[Unset, WindowsWorkstationJobPeriodicalScheduleSettings]
        if isinstance(_periodical_schedule_settings, Unset):
            periodical_schedule_settings = UNSET
        else:
            periodical_schedule_settings = WindowsWorkstationJobPeriodicalScheduleSettings.from_dict(
                _periodical_schedule_settings
            )

        _event_trigger_settings = d.pop("eventTriggerSettings", UNSET)
        event_trigger_settings: Union[Unset, WindowsWorkstationJobEventTriggerSettings]
        if isinstance(_event_trigger_settings, Unset):
            event_trigger_settings = UNSET
        else:
            event_trigger_settings = WindowsWorkstationJobEventTriggerSettings.from_dict(_event_trigger_settings)

        windows_workstation_job_schedule_settings = cls(
            periodical_schedule_enabled=periodical_schedule_enabled,
            periodical_schedule_settings=periodical_schedule_settings,
            event_trigger_settings=event_trigger_settings,
        )

        windows_workstation_job_schedule_settings.additional_properties = d
        return windows_workstation_job_schedule_settings

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
