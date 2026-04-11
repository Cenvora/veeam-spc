from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinuxScheduleRetrySettings")


@_attrs_define
class LinuxScheduleRetrySettings:
    """
    Attributes:
        enabled (bool | Unset): Indicates whether Veeam Agent for Linux must attempt to run the backup job again if the
            job fails. Default: False.
        retry_times (int | None | Unset): Number of attempts to run a job. Default: 3.
        wait_timeout_minutes (int | None | Unset): Time interval between attempts to run a job. Default: 10.
    """

    enabled: bool | Unset = False
    retry_times: int | None | Unset = 3
    wait_timeout_minutes: int | None | Unset = 10
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        retry_times: int | None | Unset
        if isinstance(self.retry_times, Unset):
            retry_times = UNSET
        else:
            retry_times = self.retry_times

        wait_timeout_minutes: int | None | Unset
        if isinstance(self.wait_timeout_minutes, Unset):
            wait_timeout_minutes = UNSET
        else:
            wait_timeout_minutes = self.wait_timeout_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if retry_times is not UNSET:
            field_dict["retryTimes"] = retry_times
        if wait_timeout_minutes is not UNSET:
            field_dict["waitTimeoutMinutes"] = wait_timeout_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        def _parse_retry_times(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retry_times = _parse_retry_times(d.pop("retryTimes", UNSET))

        def _parse_wait_timeout_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        wait_timeout_minutes = _parse_wait_timeout_minutes(d.pop("waitTimeoutMinutes", UNSET))

        linux_schedule_retry_settings = cls(
            enabled=enabled,
            retry_times=retry_times,
            wait_timeout_minutes=wait_timeout_minutes,
        )

        linux_schedule_retry_settings.additional_properties = d
        return linux_schedule_retry_settings

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
