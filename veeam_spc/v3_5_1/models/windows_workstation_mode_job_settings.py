from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.windows_workstation_job_retention_settings import WindowsWorkstationJobRetentionSettings
    from ..models.windows_workstation_job_schedule_settings import WindowsWorkstationJobScheduleSettings


T = TypeVar("T", bound="WindowsWorkstationModeJobSettings")


@_attrs_define
class WindowsWorkstationModeJobSettings:
    """
    Attributes:
        schedule_setting (Union[Unset, WindowsWorkstationJobScheduleSettings]):
        retention_settings (Union[Unset, WindowsWorkstationJobRetentionSettings]):
    """

    schedule_setting: Union[Unset, "WindowsWorkstationJobScheduleSettings"] = UNSET
    retention_settings: Union[Unset, "WindowsWorkstationJobRetentionSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_setting: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schedule_setting, Unset):
            schedule_setting = self.schedule_setting.to_dict()

        retention_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.retention_settings, Unset):
            retention_settings = self.retention_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schedule_setting is not UNSET:
            field_dict["scheduleSetting"] = schedule_setting
        if retention_settings is not UNSET:
            field_dict["retentionSettings"] = retention_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.windows_workstation_job_retention_settings import WindowsWorkstationJobRetentionSettings
        from ..models.windows_workstation_job_schedule_settings import WindowsWorkstationJobScheduleSettings

        d = dict(src_dict)
        _schedule_setting = d.pop("scheduleSetting", UNSET)
        schedule_setting: Union[Unset, WindowsWorkstationJobScheduleSettings]
        if isinstance(_schedule_setting, Unset):
            schedule_setting = UNSET
        else:
            schedule_setting = WindowsWorkstationJobScheduleSettings.from_dict(_schedule_setting)

        _retention_settings = d.pop("retentionSettings", UNSET)
        retention_settings: Union[Unset, WindowsWorkstationJobRetentionSettings]
        if isinstance(_retention_settings, Unset):
            retention_settings = UNSET
        else:
            retention_settings = WindowsWorkstationJobRetentionSettings.from_dict(_retention_settings)

        windows_workstation_mode_job_settings = cls(
            schedule_setting=schedule_setting,
            retention_settings=retention_settings,
        )

        windows_workstation_mode_job_settings.additional_properties = d
        return windows_workstation_mode_job_settings

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
