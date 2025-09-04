from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerBackupJobScheduleAfterThisJob")


@_attrs_define
class BackupServerBackupJobScheduleAfterThisJob:
    """Job chaining settings.

    Attributes:
        is_enabled (bool): Indicates whether job chaining is enabled.
        job_name (Union[Unset, str]): Name of a preceding job.
    """

    is_enabled: bool
    job_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        job_name = self.job_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isEnabled": is_enabled,
            }
        )
        if job_name is not UNSET:
            field_dict["jobName"] = job_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_enabled = d.pop("isEnabled")

        job_name = d.pop("jobName", UNSET)

        backup_server_backup_job_schedule_after_this_job = cls(
            is_enabled=is_enabled,
            job_name=job_name,
        )

        backup_server_backup_job_schedule_after_this_job.additional_properties = d
        return backup_server_backup_job_schedule_after_this_job

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
