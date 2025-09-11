from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_schedule_window_day import JobScheduleWindowDay


T = TypeVar("T", bound="WindowsPeriodicallyScheduleWindowSettings")


@_attrs_define
class WindowsPeriodicallyScheduleWindowSettings:
    """
    Attributes:
        schedule_window (Union[Unset, list['JobScheduleWindowDay']]): Permitted time window for a job.
            > By default includes all days and all hours.
        shift_for_minutes (Union[Unset, int]): Exact time of the job start within an hour, in minutes. Default: 0.
    """

    schedule_window: Union[Unset, list["JobScheduleWindowDay"]] = UNSET
    shift_for_minutes: Union[Unset, int] = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_window: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.schedule_window, Unset):
            schedule_window = []
            for schedule_window_item_data in self.schedule_window:
                schedule_window_item = schedule_window_item_data.to_dict()
                schedule_window.append(schedule_window_item)

        shift_for_minutes = self.shift_for_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schedule_window is not UNSET:
            field_dict["scheduleWindow"] = schedule_window
        if shift_for_minutes is not UNSET:
            field_dict["shiftForMinutes"] = shift_for_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_schedule_window_day import JobScheduleWindowDay

        d = dict(src_dict)
        schedule_window = []
        _schedule_window = d.pop("scheduleWindow", UNSET)
        for schedule_window_item_data in _schedule_window or []:
            schedule_window_item = JobScheduleWindowDay.from_dict(schedule_window_item_data)

            schedule_window.append(schedule_window_item)

        shift_for_minutes = d.pop("shiftForMinutes", UNSET)

        windows_periodically_schedule_window_settings = cls(
            schedule_window=schedule_window,
            shift_for_minutes=shift_for_minutes,
        )

        windows_periodically_schedule_window_settings.additional_properties = d
        return windows_periodically_schedule_window_settings

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
