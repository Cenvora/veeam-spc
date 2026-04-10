from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_repository import BackupRepository


T = TypeVar("T", bound="EmbeddedForBackupServerRepositoryChildren")


@_attrs_define
class EmbeddedForBackupServerRepositoryChildren:
    """Resource representation of the related backup repository.

    Attributes:
        backup_repository (BackupRepository | Unset):  Example: {'instanceUid': '85C41EAE-A598-49C5-B92C-9E5138D170EC',
            'name': 'BACKUPREPOSITORY01', 'backupServerUid': 'DF997BD3-4AE9-4841-8152-8FF5CC703EAB'}.
    """

    backup_repository: BackupRepository | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_repository, Unset):
            backup_repository = self.backup_repository.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_repository is not UNSET:
            field_dict["backupRepository"] = backup_repository

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_repository import BackupRepository

        d = dict(src_dict)
        _backup_repository = d.pop("backupRepository", UNSET)
        backup_repository: BackupRepository | Unset
        if isinstance(_backup_repository, Unset):
            backup_repository = UNSET
        else:
            backup_repository = BackupRepository.from_dict(_backup_repository)

        embedded_for_backup_server_repository_children = cls(
            backup_repository=backup_repository,
        )

        embedded_for_backup_server_repository_children.additional_properties = d
        return embedded_for_backup_server_repository_children

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
