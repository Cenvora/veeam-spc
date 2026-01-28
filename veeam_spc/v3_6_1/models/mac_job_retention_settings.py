from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MacJobRetentionSettings")


@_attrs_define
class MacJobRetentionSettings:
    """
    Attributes:
        restore_points_count (Union[None, Unset, int]): Number of restore points that must be kept in the target
            location.
        retention_days (Union[None, Unset, int]): Number of days for which backup files must be stored in the target
            location. Days without backups are not included.
    """

    restore_points_count: Union[None, Unset, int] = UNSET
    retention_days: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        restore_points_count: Union[None, Unset, int]
        if isinstance(self.restore_points_count, Unset):
            restore_points_count = UNSET
        else:
            restore_points_count = self.restore_points_count

        retention_days: Union[None, Unset, int]
        if isinstance(self.retention_days, Unset):
            retention_days = UNSET
        else:
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

        def _parse_restore_points_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        restore_points_count = _parse_restore_points_count(d.pop("restorePointsCount", UNSET))

        def _parse_retention_days(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        retention_days = _parse_retention_days(d.pop("retentionDays", UNSET))

        mac_job_retention_settings = cls(
            restore_points_count=restore_points_count,
            retention_days=retention_days,
        )

        mac_job_retention_settings.additional_properties = d
        return mac_job_retention_settings

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
