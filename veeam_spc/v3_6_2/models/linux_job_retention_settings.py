from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinuxJobRetentionSettings")


@_attrs_define
class LinuxJobRetentionSettings:
    """
    Attributes:
        restore_points_count (int | Unset): Number of restore points that must be kept in the target location.
        retention_days (int | Unset): Number of days for which backup files must be stored in the target location. Days
            without backups are not included.
    """

    restore_points_count: int | Unset = UNSET
    retention_days: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        restore_points_count = self.restore_points_count

        retention_days = self.retention_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if restore_points_count is not UNSET:
            field_dict["restorePointsCount"] = restore_points_count
        if retention_days is not UNSET:
            field_dict["retentionDays"] = retention_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        restore_points_count = d.pop("restorePointsCount", UNSET)

        retention_days = d.pop("retentionDays", UNSET)

        linux_job_retention_settings = cls(
            restore_points_count=restore_points_count,
            retention_days=retention_days,
        )

        linux_job_retention_settings.additional_properties = d
        return linux_job_retention_settings

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
