from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_job_schedule_options_periodically_kind import BackupServerJobScheduleOptionsPeriodicallyKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_job_time_period import BackupServerJobTimePeriod


T = TypeVar("T", bound="BackupServerJobScheduleOptionsPeriodically")


@_attrs_define
class BackupServerJobScheduleOptionsPeriodically:
    """
    Attributes:
        kind (Union[Unset, BackupServerJobScheduleOptionsPeriodicallyKind]): Measurement units of the intervals between
            periodical job runs.
        full_period (Union[None, Unset, int]): Numerical value of the intervals between periodical job runs.
        schedule (Union[None, Unset, list['BackupServerJobTimePeriod']]): Permitted time window of a job.
    """

    kind: Union[Unset, BackupServerJobScheduleOptionsPeriodicallyKind] = UNSET
    full_period: Union[None, Unset, int] = UNSET
    schedule: Union[None, Unset, list["BackupServerJobTimePeriod"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        full_period: Union[None, Unset, int]
        if isinstance(self.full_period, Unset):
            full_period = UNSET
        else:
            full_period = self.full_period

        schedule: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.schedule, Unset):
            schedule = UNSET
        elif isinstance(self.schedule, list):
            schedule = []
            for schedule_type_0_item_data in self.schedule:
                schedule_type_0_item = schedule_type_0_item_data.to_dict()
                schedule.append(schedule_type_0_item)

        else:
            schedule = self.schedule

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if full_period is not UNSET:
            field_dict["fullPeriod"] = full_period
        if schedule is not UNSET:
            field_dict["schedule"] = schedule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_job_time_period import BackupServerJobTimePeriod

        d = dict(src_dict)
        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, BackupServerJobScheduleOptionsPeriodicallyKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = BackupServerJobScheduleOptionsPeriodicallyKind(_kind)

        def _parse_full_period(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        full_period = _parse_full_period(d.pop("fullPeriod", UNSET))

        def _parse_schedule(data: object) -> Union[None, Unset, list["BackupServerJobTimePeriod"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                schedule_type_0 = []
                _schedule_type_0 = data
                for schedule_type_0_item_data in _schedule_type_0:
                    schedule_type_0_item = BackupServerJobTimePeriod.from_dict(schedule_type_0_item_data)

                    schedule_type_0.append(schedule_type_0_item)

                return schedule_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["BackupServerJobTimePeriod"]], data)

        schedule = _parse_schedule(d.pop("schedule", UNSET))

        backup_server_job_schedule_options_periodically = cls(
            kind=kind,
            full_period=full_period,
            schedule=schedule,
        )

        backup_server_job_schedule_options_periodically.additional_properties = d
        return backup_server_job_schedule_options_periodically

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
