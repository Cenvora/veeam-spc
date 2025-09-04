from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.windows_server_job_retention_settings_retention_mode import WindowsServerJobRetentionSettingsRetentionMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="WindowsServerJobRetentionSettings")


@_attrs_define
class WindowsServerJobRetentionSettings:
    """
    Attributes:
        retention_mode (Union[Unset, WindowsServerJobRetentionSettingsRetentionMode]): Retention policy type.
            > The `Days` type is available only for Veeam Agent for Microsoft Windows version 5.0 or later. For earlier
            versions the `RestorePoints` type is used.'
             Default: WindowsServerJobRetentionSettingsRetentionMode.RESTOREPOINTS.
        retention_count (Union[Unset, int]): Retention policy counter value. Default: 7.
    """

    retention_mode: Union[Unset, WindowsServerJobRetentionSettingsRetentionMode] = (
        WindowsServerJobRetentionSettingsRetentionMode.RESTOREPOINTS
    )
    retention_count: Union[Unset, int] = 7
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        retention_mode: Union[Unset, str] = UNSET
        if not isinstance(self.retention_mode, Unset):
            retention_mode = self.retention_mode.value

        retention_count = self.retention_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if retention_mode is not UNSET:
            field_dict["retentionMode"] = retention_mode
        if retention_count is not UNSET:
            field_dict["retentionCount"] = retention_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _retention_mode = d.pop("retentionMode", UNSET)
        retention_mode: Union[Unset, WindowsServerJobRetentionSettingsRetentionMode]
        if isinstance(_retention_mode, Unset):
            retention_mode = UNSET
        else:
            retention_mode = WindowsServerJobRetentionSettingsRetentionMode(_retention_mode)

        retention_count = d.pop("retentionCount", UNSET)

        windows_server_job_retention_settings = cls(
            retention_mode=retention_mode,
            retention_count=retention_count,
        )

        windows_server_job_retention_settings.additional_properties = d
        return windows_server_job_retention_settings

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
