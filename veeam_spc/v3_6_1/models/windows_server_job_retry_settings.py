from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WindowsServerJobRetrySettings")


@_attrs_define
class WindowsServerJobRetrySettings:
    """
    Attributes:
        enabled (Union[Unset, bool]): Indicates whether Veeam Agent for Microsoft Windows must attempt to run the backup
            job again if the job fails. Default: True.
        retry_times (Union[Unset, int]): Number of attempts to run a job. Default: 3.
        wait_timeout_minutes (Union[Unset, int]): Time interval between attempts to run a job. Default: 10.
    """

    enabled: Union[Unset, bool] = True
    retry_times: Union[Unset, int] = 3
    wait_timeout_minutes: Union[Unset, int] = 10
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        retry_times = self.retry_times

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

        retry_times = d.pop("retryTimes", UNSET)

        wait_timeout_minutes = d.pop("waitTimeoutMinutes", UNSET)

        windows_server_job_retry_settings = cls(
            enabled=enabled,
            retry_times=retry_times,
            wait_timeout_minutes=wait_timeout_minutes,
        )

        windows_server_job_retry_settings.additional_properties = d
        return windows_server_job_retry_settings

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
