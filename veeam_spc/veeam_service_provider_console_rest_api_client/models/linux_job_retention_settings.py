from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinuxJobRetentionSettings")


@_attrs_define
class LinuxJobRetentionSettings:
    """
    Attributes:
        restore_points_count (Union[Unset, int]): Number of restore points that must be kept in the target location.
            Default: 7.
    """

    restore_points_count: Union[Unset, int] = 7
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        restore_points_count = self.restore_points_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if restore_points_count is not UNSET:
            field_dict["restorePointsCount"] = restore_points_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        restore_points_count = d.pop("restorePointsCount", UNSET)

        linux_job_retention_settings = cls(
            restore_points_count=restore_points_count,
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
