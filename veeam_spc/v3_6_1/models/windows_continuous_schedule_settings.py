from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.windows_periodically_schedule_window_settings import WindowsPeriodicallyScheduleWindowSettings


T = TypeVar("T", bound="WindowsContinuousScheduleSettings")


@_attrs_define
class WindowsContinuousScheduleSettings:
    """
    Attributes:
        backup_window_settings (Union[Unset, WindowsPeriodicallyScheduleWindowSettings]):
    """

    backup_window_settings: Union[Unset, "WindowsPeriodicallyScheduleWindowSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_window_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.backup_window_settings, Unset):
            backup_window_settings = self.backup_window_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_window_settings is not UNSET:
            field_dict["backupWindowSettings"] = backup_window_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.windows_periodically_schedule_window_settings import WindowsPeriodicallyScheduleWindowSettings

        d = dict(src_dict)
        _backup_window_settings = d.pop("backupWindowSettings", UNSET)
        backup_window_settings: Union[Unset, WindowsPeriodicallyScheduleWindowSettings]
        if isinstance(_backup_window_settings, Unset):
            backup_window_settings = UNSET
        else:
            backup_window_settings = WindowsPeriodicallyScheduleWindowSettings.from_dict(_backup_window_settings)

        windows_continuous_schedule_settings = cls(
            backup_window_settings=backup_window_settings,
        )

        windows_continuous_schedule_settings.additional_properties = d
        return windows_continuous_schedule_settings

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
