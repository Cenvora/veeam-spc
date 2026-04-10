from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_file_tape_job_object_source_type import BackupServerFileTapeJobObjectSourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerFileTapeJobObjectSource")


@_attrs_define
class BackupServerFileTapeJobObjectSource:
    """
    Attributes:
        path (Union[Unset, str]): Path to a location where protected files and folders reside.
        type_ (Union[Unset, BackupServerFileTapeJobObjectSourceType]): Type of a protected unit.
    """

    path: Union[Unset, str] = UNSET
    type_: Union[Unset, BackupServerFileTapeJobObjectSourceType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, BackupServerFileTapeJobObjectSourceType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BackupServerFileTapeJobObjectSourceType(_type_)

        backup_server_file_tape_job_object_source = cls(
            path=path,
            type_=type_,
        )

        backup_server_file_tape_job_object_source.additional_properties = d
        return backup_server_file_tape_job_object_source

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
