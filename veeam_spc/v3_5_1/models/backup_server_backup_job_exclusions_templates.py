from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerBackupJobExclusionsTemplates")


@_attrs_define
class BackupServerBackupJobExclusionsTemplates:
    """Excluded VM templates.

    Attributes:
        is_enabled (Union[Unset, bool]): Indicates whether VM templates are excluded from a backup job. Default: True.
        exclude_from_incremental (Union[Unset, bool]): Indicates whether VM templates are excluded from the incremental
            backup. Default: True.
    """

    is_enabled: Union[Unset, bool] = True
    exclude_from_incremental: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        exclude_from_incremental = self.exclude_from_incremental

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if exclude_from_incremental is not UNSET:
            field_dict["excludeFromIncremental"] = exclude_from_incremental

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_enabled = d.pop("isEnabled", UNSET)

        exclude_from_incremental = d.pop("excludeFromIncremental", UNSET)

        backup_server_backup_job_exclusions_templates = cls(
            is_enabled=is_enabled,
            exclude_from_incremental=exclude_from_incremental,
        )

        backup_server_backup_job_exclusions_templates.additional_properties = d
        return backup_server_backup_job_exclusions_templates

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
