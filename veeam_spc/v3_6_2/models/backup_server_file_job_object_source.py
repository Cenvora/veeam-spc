from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_file_job_object_source_type import BackupServerFileJobObjectSourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerFileJobObjectSource")


@_attrs_define
class BackupServerFileJobObjectSource:
    """
    Attributes:
        path (str | Unset): Path to a location of protected data.
        type_ (BackupServerFileJobObjectSourceType | Unset): Type of protected object.
        inclusion_masks (list[str] | Unset): Names and name masks of files that must be included into a backup scope.
        exclusion_masks (list[str] | Unset): Names and name masks of files that must be excluded from a backup scope.
    """

    path: str | Unset = UNSET
    type_: BackupServerFileJobObjectSourceType | Unset = UNSET
    inclusion_masks: list[str] | Unset = UNSET
    exclusion_masks: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        inclusion_masks: list[str] | Unset = UNSET
        if not isinstance(self.inclusion_masks, Unset):
            inclusion_masks = self.inclusion_masks

        exclusion_masks: list[str] | Unset = UNSET
        if not isinstance(self.exclusion_masks, Unset):
            exclusion_masks = self.exclusion_masks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if type_ is not UNSET:
            field_dict["type"] = type_
        if inclusion_masks is not UNSET:
            field_dict["inclusionMasks"] = inclusion_masks
        if exclusion_masks is not UNSET:
            field_dict["exclusionMasks"] = exclusion_masks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: BackupServerFileJobObjectSourceType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BackupServerFileJobObjectSourceType(_type_)

        inclusion_masks = cast(list[str], d.pop("inclusionMasks", UNSET))

        exclusion_masks = cast(list[str], d.pop("exclusionMasks", UNSET))

        backup_server_file_job_object_source = cls(
            path=path,
            type_=type_,
            inclusion_masks=inclusion_masks,
            exclusion_masks=exclusion_masks,
        )

        backup_server_file_job_object_source.additional_properties = d
        return backup_server_file_job_object_source

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
