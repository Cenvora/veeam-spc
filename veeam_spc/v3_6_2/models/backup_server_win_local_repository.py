from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_mount_servers_settings import BackupServerMountServersSettings
    from ..models.backup_server_windows_local_repository_settings import BackupServerWindowsLocalRepositorySettings
    from ..models.embedded_for_backup_server_repository_children import EmbeddedForBackupServerRepositoryChildren


T = TypeVar("T", bound="BackupServerWinLocalRepository")


@_attrs_define
class BackupServerWinLocalRepository:
    """
    Attributes:
        description (str): Description of a repository.
        name (str): Name of a repository.
        host_id (UUID): Host ID associated with the repository.
        repository (BackupServerWindowsLocalRepositorySettings):
        instance_uid (UUID | Unset): UID assigned to a repository.
        unique_id (str | Unset): Unique ID assigned to a repository.
        import_backup (bool | Unset): Indicates whether Veeam Backup & Replication will search a repository for existing
            backups and import them automatically.
        import_index (bool | Unset): Indicates whether Veeam Backup & Replication will import the guest OS file system
            index.
        mount_server (BackupServerMountServersSettings | Unset):
        field_embedded (EmbeddedForBackupServerRepositoryChildren | Unset): Resource representation of the related
            backup repository.
    """

    description: str
    name: str
    host_id: UUID
    repository: BackupServerWindowsLocalRepositorySettings
    instance_uid: UUID | Unset = UNSET
    unique_id: str | Unset = UNSET
    import_backup: bool | Unset = UNSET
    import_index: bool | Unset = UNSET
    mount_server: BackupServerMountServersSettings | Unset = UNSET
    field_embedded: EmbeddedForBackupServerRepositoryChildren | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        host_id = str(self.host_id)

        repository = self.repository.to_dict()

        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        unique_id = self.unique_id

        import_backup = self.import_backup

        import_index = self.import_index

        mount_server: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mount_server, Unset):
            mount_server = self.mount_server.to_dict()

        field_embedded: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_embedded, Unset):
            field_embedded = self.field_embedded.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "name": name,
                "hostId": host_id,
                "repository": repository,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id
        if import_backup is not UNSET:
            field_dict["importBackup"] = import_backup
        if import_index is not UNSET:
            field_dict["importIndex"] = import_index
        if mount_server is not UNSET:
            field_dict["mountServer"] = mount_server
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_mount_servers_settings import BackupServerMountServersSettings
        from ..models.backup_server_windows_local_repository_settings import BackupServerWindowsLocalRepositorySettings
        from ..models.embedded_for_backup_server_repository_children import EmbeddedForBackupServerRepositoryChildren

        d = dict(src_dict)
        description = d.pop("description")

        name = d.pop("name")

        host_id = UUID(d.pop("hostId"))

        repository = BackupServerWindowsLocalRepositorySettings.from_dict(d.pop("repository"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        unique_id = d.pop("uniqueId", UNSET)

        import_backup = d.pop("importBackup", UNSET)

        import_index = d.pop("importIndex", UNSET)

        _mount_server = d.pop("mountServer", UNSET)
        mount_server: BackupServerMountServersSettings | Unset
        if isinstance(_mount_server, Unset):
            mount_server = UNSET
        else:
            mount_server = BackupServerMountServersSettings.from_dict(_mount_server)

        _field_embedded = d.pop("_embedded", UNSET)
        field_embedded: EmbeddedForBackupServerRepositoryChildren | Unset
        if isinstance(_field_embedded, Unset):
            field_embedded = UNSET
        else:
            field_embedded = EmbeddedForBackupServerRepositoryChildren.from_dict(_field_embedded)

        backup_server_win_local_repository = cls(
            description=description,
            name=name,
            host_id=host_id,
            repository=repository,
            instance_uid=instance_uid,
            unique_id=unique_id,
            import_backup=import_backup,
            import_index=import_index,
            mount_server=mount_server,
            field_embedded=field_embedded,
        )

        backup_server_win_local_repository.additional_properties = d
        return backup_server_win_local_repository

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
