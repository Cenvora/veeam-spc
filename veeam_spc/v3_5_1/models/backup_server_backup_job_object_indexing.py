from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_backup_job_guest_fs_indexing_mode import BackupServerBackupJobGuestFSIndexingMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerBackupJobObjectIndexing")


@_attrs_define
class BackupServerBackupJobObjectIndexing:
    """Guest OS indexing options for a VM.

    Attributes:
        guest_fs_indexing_mode (BackupServerBackupJobGuestFSIndexingMode): Indexing mode.
        indexing_list (Union[Unset, list[str]]): Array of folders.
            >Environmental variables and full paths to folders can be used.
    """

    guest_fs_indexing_mode: BackupServerBackupJobGuestFSIndexingMode
    indexing_list: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        guest_fs_indexing_mode = self.guest_fs_indexing_mode.value

        indexing_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.indexing_list, Unset):
            indexing_list = self.indexing_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "guestFSIndexingMode": guest_fs_indexing_mode,
            }
        )
        if indexing_list is not UNSET:
            field_dict["indexingList"] = indexing_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        guest_fs_indexing_mode = BackupServerBackupJobGuestFSIndexingMode(d.pop("guestFSIndexingMode"))

        indexing_list = cast(list[str], d.pop("indexingList", UNSET))

        backup_server_backup_job_object_indexing = cls(
            guest_fs_indexing_mode=guest_fs_indexing_mode,
            indexing_list=indexing_list,
        )

        backup_server_backup_job_object_indexing.additional_properties = d
        return backup_server_backup_job_object_indexing

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
