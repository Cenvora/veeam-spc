from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vb_365_copy_job_schedule_policy_daily_type import Vb365CopyJobSchedulePolicyDailyType
from ..models.vb_365_copy_job_schedule_policy_periodically_every import Vb365CopyJobSchedulePolicyPeriodicallyEvery
from ..models.vb_365_copy_job_schedule_policy_schedule_policy_type import Vb365CopyJobSchedulePolicySchedulePolicyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vb_365_backup_window_settings import Vb365BackupWindowSettings


T = TypeVar("T", bound="Vb365CopyJobSchedulePolicy")


@_attrs_define
class Vb365CopyJobSchedulePolicy:
    """
    Attributes:
        schedule_policy_type (Vb365CopyJobSchedulePolicySchedulePolicyType | Unset): Type of a schedule policy.
        periodically_every (Vb365CopyJobSchedulePolicyPeriodicallyEvery | Unset): Type of a time interval for a
            periodically running job.
        daily_type (Vb365CopyJobSchedulePolicyDailyType | Unset): Days when the daily job runs.
        backup_window_enabled (bool | Unset): Indicates whether backup window is enabled. Default: False.
        backup_window_settings (Vb365BackupWindowSettings | Unset):
        daily_time (None | str | Unset): Time of the day when a daily job is started in the `hh:mm` format.
    """

    schedule_policy_type: Vb365CopyJobSchedulePolicySchedulePolicyType | Unset = UNSET
    periodically_every: Vb365CopyJobSchedulePolicyPeriodicallyEvery | Unset = UNSET
    daily_type: Vb365CopyJobSchedulePolicyDailyType | Unset = UNSET
    backup_window_enabled: bool | Unset = False
    backup_window_settings: Vb365BackupWindowSettings | Unset = UNSET
    daily_time: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_policy_type: str | Unset = UNSET
        if not isinstance(self.schedule_policy_type, Unset):
            schedule_policy_type = self.schedule_policy_type.value

        periodically_every: str | Unset = UNSET
        if not isinstance(self.periodically_every, Unset):
            periodically_every = self.periodically_every.value

        daily_type: str | Unset = UNSET
        if not isinstance(self.daily_type, Unset):
            daily_type = self.daily_type.value

        backup_window_enabled = self.backup_window_enabled

        backup_window_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_window_settings, Unset):
            backup_window_settings = self.backup_window_settings.to_dict()

        daily_time: None | str | Unset
        if isinstance(self.daily_time, Unset):
            daily_time = UNSET
        else:
            daily_time = self.daily_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schedule_policy_type is not UNSET:
            field_dict["schedulePolicyType"] = schedule_policy_type
        if periodically_every is not UNSET:
            field_dict["periodicallyEvery"] = periodically_every
        if daily_type is not UNSET:
            field_dict["dailyType"] = daily_type
        if backup_window_enabled is not UNSET:
            field_dict["backupWindowEnabled"] = backup_window_enabled
        if backup_window_settings is not UNSET:
            field_dict["backupWindowSettings"] = backup_window_settings
        if daily_time is not UNSET:
            field_dict["dailyTime"] = daily_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vb_365_backup_window_settings import Vb365BackupWindowSettings

        d = dict(src_dict)
        _schedule_policy_type = d.pop("schedulePolicyType", UNSET)
        schedule_policy_type: Vb365CopyJobSchedulePolicySchedulePolicyType | Unset
        if isinstance(_schedule_policy_type, Unset):
            schedule_policy_type = UNSET
        else:
            schedule_policy_type = Vb365CopyJobSchedulePolicySchedulePolicyType(_schedule_policy_type)

        _periodically_every = d.pop("periodicallyEvery", UNSET)
        periodically_every: Vb365CopyJobSchedulePolicyPeriodicallyEvery | Unset
        if isinstance(_periodically_every, Unset):
            periodically_every = UNSET
        else:
            periodically_every = Vb365CopyJobSchedulePolicyPeriodicallyEvery(_periodically_every)

        _daily_type = d.pop("dailyType", UNSET)
        daily_type: Vb365CopyJobSchedulePolicyDailyType | Unset
        if isinstance(_daily_type, Unset):
            daily_type = UNSET
        else:
            daily_type = Vb365CopyJobSchedulePolicyDailyType(_daily_type)

        backup_window_enabled = d.pop("backupWindowEnabled", UNSET)

        _backup_window_settings = d.pop("backupWindowSettings", UNSET)
        backup_window_settings: Vb365BackupWindowSettings | Unset
        if isinstance(_backup_window_settings, Unset):
            backup_window_settings = UNSET
        else:
            backup_window_settings = Vb365BackupWindowSettings.from_dict(_backup_window_settings)

        def _parse_daily_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        daily_time = _parse_daily_time(d.pop("dailyTime", UNSET))

        vb_365_copy_job_schedule_policy = cls(
            schedule_policy_type=schedule_policy_type,
            periodically_every=periodically_every,
            daily_type=daily_type,
            backup_window_enabled=backup_window_enabled,
            backup_window_settings=backup_window_settings,
            daily_time=daily_time,
        )

        vb_365_copy_job_schedule_policy.additional_properties = d
        return vb_365_copy_job_schedule_policy

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
