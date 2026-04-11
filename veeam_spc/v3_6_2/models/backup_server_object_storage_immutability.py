from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_object_storage_immutability_immutability_mode import (
    BackupServerObjectStorageImmutabilityImmutabilityMode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerObjectStorageImmutability")


@_attrs_define
class BackupServerObjectStorageImmutability:
    """
    Attributes:
        is_enabled (bool | None | Unset): Indicates whether stored backups are immutable. Default: False.
        days_count (int | None | Unset): Immutability duration, in days.
        immutability_mode (BackupServerObjectStorageImmutabilityImmutabilityMode | Unset): Immutability mode.
    """

    is_enabled: bool | None | Unset = False
    days_count: int | None | Unset = UNSET
    immutability_mode: BackupServerObjectStorageImmutabilityImmutabilityMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled: bool | None | Unset
        if isinstance(self.is_enabled, Unset):
            is_enabled = UNSET
        else:
            is_enabled = self.is_enabled

        days_count: int | None | Unset
        if isinstance(self.days_count, Unset):
            days_count = UNSET
        else:
            days_count = self.days_count

        immutability_mode: str | Unset = UNSET
        if not isinstance(self.immutability_mode, Unset):
            immutability_mode = self.immutability_mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if days_count is not UNSET:
            field_dict["daysCount"] = days_count
        if immutability_mode is not UNSET:
            field_dict["immutabilityMode"] = immutability_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_is_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_enabled = _parse_is_enabled(d.pop("isEnabled", UNSET))

        def _parse_days_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        days_count = _parse_days_count(d.pop("daysCount", UNSET))

        _immutability_mode = d.pop("immutabilityMode", UNSET)
        immutability_mode: BackupServerObjectStorageImmutabilityImmutabilityMode | Unset
        if isinstance(_immutability_mode, Unset):
            immutability_mode = UNSET
        else:
            immutability_mode = BackupServerObjectStorageImmutabilityImmutabilityMode(_immutability_mode)

        backup_server_object_storage_immutability = cls(
            is_enabled=is_enabled,
            days_count=days_count,
            immutability_mode=immutability_mode,
        )

        backup_server_object_storage_immutability.additional_properties = d
        return backup_server_object_storage_immutability

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
