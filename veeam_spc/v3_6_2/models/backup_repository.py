from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_repository_info import BackupRepositoryInfo


T = TypeVar("T", bound="BackupRepository")


@_attrs_define
class BackupRepository:
    """
    Example:
        {'instanceUid': '85C41EAE-A598-49C5-B92C-9E5138D170EC', 'name': 'BACKUPREPOSITORY01', 'backupServerUid':
            'DF997BD3-4AE9-4841-8152-8FF5CC703EAB'}

    Attributes:
        instance_uid (UUID | Unset): UID assigned to a backup repository.
        name (str | Unset): Name of a backup repository.
        backup_server_uid (UUID | Unset): UID assigned to a Veeam Backup & Replication server.
        tags (list[str] | Unset): Array of assigned tags.
        field_embedded (BackupRepositoryInfo | Unset):
    """

    instance_uid: UUID | Unset = UNSET
    name: str | Unset = UNSET
    backup_server_uid: UUID | Unset = UNSET
    tags: list[str] | Unset = UNSET
    field_embedded: BackupRepositoryInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        backup_server_uid: str | Unset = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_embedded: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_embedded, Unset):
            field_embedded = self.field_embedded.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if name is not UNSET:
            field_dict["name"] = name
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if tags is not UNSET:
            field_dict["tags"] = tags
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_repository_info import BackupRepositoryInfo

        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        name = d.pop("name", UNSET)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: UUID | Unset
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        tags = cast(list[str], d.pop("tags", UNSET))

        _field_embedded = d.pop("_embedded", UNSET)
        field_embedded: BackupRepositoryInfo | Unset
        if isinstance(_field_embedded, Unset):
            field_embedded = UNSET
        else:
            field_embedded = BackupRepositoryInfo.from_dict(_field_embedded)

        backup_repository = cls(
            instance_uid=instance_uid,
            name=name,
            backup_server_uid=backup_server_uid,
            tags=tags,
            field_embedded=field_embedded,
        )

        backup_repository.additional_properties = d
        return backup_repository

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
