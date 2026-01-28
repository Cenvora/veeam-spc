from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_repository_info_type_0 import BackupRepositoryInfoType0


T = TypeVar("T", bound="BackupRepository")


@_attrs_define
class BackupRepository:
    """
    Example:
        {'instanceUid': '85C41EAE-A598-49C5-B92C-9E5138D170EC', 'name': 'BACKUPREPOSITORY01', 'backupServerUid':
            'DF997BD3-4AE9-4841-8152-8FF5CC703EAB'}

    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a backup repository.
        name (Union[Unset, str]): Name of a backup repository.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup & Replication server.
        field_embedded (Union['BackupRepositoryInfoType0', None, Unset]):
    """

    instance_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    field_embedded: Union["BackupRepositoryInfoType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.backup_repository_info_type_0 import BackupRepositoryInfoType0

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        field_embedded: Union[None, Unset, dict[str, Any]]
        if isinstance(self.field_embedded, Unset):
            field_embedded = UNSET
        elif isinstance(self.field_embedded, BackupRepositoryInfoType0):
            field_embedded = self.field_embedded.to_dict()
        else:
            field_embedded = self.field_embedded

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if name is not UNSET:
            field_dict["name"] = name
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_repository_info_type_0 import BackupRepositoryInfoType0

        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        name = d.pop("name", UNSET)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: Union[Unset, UUID]
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        def _parse_field_embedded(data: object) -> Union["BackupRepositoryInfoType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_repository_info_type_0 = BackupRepositoryInfoType0.from_dict(data)

                return componentsschemas_backup_repository_info_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupRepositoryInfoType0", None, Unset], data)

        field_embedded = _parse_field_embedded(d.pop("_embedded", UNSET))

        backup_repository = cls(
            instance_uid=instance_uid,
            name=name,
            backup_server_uid=backup_server_uid,
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
