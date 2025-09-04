from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerBackupJobScheduleRetry")


@_attrs_define
class BackupServerBackupJobScheduleRetry:
    """Job retry settings.

    Attributes:
        is_enabled (Union[Unset, bool]): Indicates whether job retries are enabled. Default: False.
        retry_count (Union[Unset, int]): Number of retries set for the job.
            >Must be greater than zero.
             Default: 3.
        await_minutes (Union[Unset, int]): Time interval between job retries, in minutes.
            >Must be greater than zero.
             Default: 10.
    """

    is_enabled: Union[Unset, bool] = False
    retry_count: Union[Unset, int] = 3
    await_minutes: Union[Unset, int] = 10
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        retry_count = self.retry_count

        await_minutes = self.await_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if retry_count is not UNSET:
            field_dict["retryCount"] = retry_count
        if await_minutes is not UNSET:
            field_dict["awaitMinutes"] = await_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_enabled = d.pop("isEnabled", UNSET)

        retry_count = d.pop("retryCount", UNSET)

        await_minutes = d.pop("awaitMinutes", UNSET)

        backup_server_backup_job_schedule_retry = cls(
            is_enabled=is_enabled,
            retry_count=retry_count,
            await_minutes=await_minutes,
        )

        backup_server_backup_job_schedule_retry.additional_properties = d
        return backup_server_backup_job_schedule_retry

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
