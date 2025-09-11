from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WindowsWorkstationJobRetentionSettings")


@_attrs_define
class WindowsWorkstationJobRetentionSettings:
    """
    Attributes:
        retention_days (Union[Unset, int]): Number of days for which backup files must be stored in the target location.
            Days without backups are not included. Default: 7.
    """

    retention_days: Union[Unset, int] = 7
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        retention_days = self.retention_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if retention_days is not UNSET:
            field_dict["retentionDays"] = retention_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        retention_days = d.pop("retentionDays", UNSET)

        windows_workstation_job_retention_settings = cls(
            retention_days=retention_days,
        )

        windows_workstation_job_retention_settings.additional_properties = d
        return windows_workstation_job_retention_settings

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
