from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerJobScheduleOptionsChaining")


@_attrs_define
class BackupServerJobScheduleOptionsChaining:
    """
    Attributes:
        previous_job_id (UUID | Unset): UID assigned to the previous job in a chain.
        previous_job_name (str | Unset): Name of the previous job in a chain.
    """

    previous_job_id: UUID | Unset = UNSET
    previous_job_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        previous_job_id: str | Unset = UNSET
        if not isinstance(self.previous_job_id, Unset):
            previous_job_id = str(self.previous_job_id)

        previous_job_name = self.previous_job_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if previous_job_id is not UNSET:
            field_dict["previousJobId"] = previous_job_id
        if previous_job_name is not UNSET:
            field_dict["previousJobName"] = previous_job_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _previous_job_id = d.pop("previousJobId", UNSET)
        previous_job_id: UUID | Unset
        if isinstance(_previous_job_id, Unset):
            previous_job_id = UNSET
        else:
            previous_job_id = UUID(_previous_job_id)

        previous_job_name = d.pop("previousJobName", UNSET)

        backup_server_job_schedule_options_chaining = cls(
            previous_job_id=previous_job_id,
            previous_job_name=previous_job_name,
        )

        backup_server_job_schedule_options_chaining.additional_properties = d
        return backup_server_job_schedule_options_chaining

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
