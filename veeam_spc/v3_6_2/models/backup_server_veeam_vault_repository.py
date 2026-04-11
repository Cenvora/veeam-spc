from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_mount_servers_settings import BackupServerMountServersSettings
    from ..models.backup_server_veeam_data_cloud_storage_account import BackupServerVeeamDataCloudStorageAccount
    from ..models.backup_server_veeam_data_cloud_storage_container import BackupServerVeeamDataCloudStorageContainer
    from ..models.embedded_for_backup_server_repository_children_type_0 import (
        EmbeddedForBackupServerRepositoryChildrenType0,
    )


T = TypeVar("T", bound="BackupServerVeeamVaultRepository")


@_attrs_define
class BackupServerVeeamVaultRepository:
    """
    Attributes:
        name (str): Name of a repository.
        account (BackupServerVeeamDataCloudStorageAccount): Veeam account settings.
        container (BackupServerVeeamDataCloudStorageContainer): Storage container settings.
        instance_uid (UUID | Unset): UID assigned to a repository.
        description (None | str | Unset): Description of a repository.
        unique_id (None | str | Unset): Unique identifier assigned to a repository.
        task_limit_enabled (bool | None | Unset): Indicates whether the number of concurrent task is limited.
        max_task_count (int | None | Unset): Maximum number of concurrent tasks.
        mount_server (BackupServerMountServersSettings | Unset):
        field_embedded (EmbeddedForBackupServerRepositoryChildrenType0 | None | Unset): Resource representation of the
            related backup repository.
    """

    name: str
    account: BackupServerVeeamDataCloudStorageAccount
    container: BackupServerVeeamDataCloudStorageContainer
    instance_uid: UUID | Unset = UNSET
    description: None | str | Unset = UNSET
    unique_id: None | str | Unset = UNSET
    task_limit_enabled: bool | None | Unset = UNSET
    max_task_count: int | None | Unset = UNSET
    mount_server: BackupServerMountServersSettings | Unset = UNSET
    field_embedded: EmbeddedForBackupServerRepositoryChildrenType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.embedded_for_backup_server_repository_children_type_0 import (
            EmbeddedForBackupServerRepositoryChildrenType0,
        )

        name = self.name

        account = self.account.to_dict()

        container = self.container.to_dict()

        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        unique_id: None | str | Unset
        if isinstance(self.unique_id, Unset):
            unique_id = UNSET
        else:
            unique_id = self.unique_id

        task_limit_enabled: bool | None | Unset
        if isinstance(self.task_limit_enabled, Unset):
            task_limit_enabled = UNSET
        else:
            task_limit_enabled = self.task_limit_enabled

        max_task_count: int | None | Unset
        if isinstance(self.max_task_count, Unset):
            max_task_count = UNSET
        else:
            max_task_count = self.max_task_count

        mount_server: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mount_server, Unset):
            mount_server = self.mount_server.to_dict()

        field_embedded: dict[str, Any] | None | Unset
        if isinstance(self.field_embedded, Unset):
            field_embedded = UNSET
        elif isinstance(self.field_embedded, EmbeddedForBackupServerRepositoryChildrenType0):
            field_embedded = self.field_embedded.to_dict()
        else:
            field_embedded = self.field_embedded

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "account": account,
                "container": container,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if description is not UNSET:
            field_dict["description"] = description
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id
        if task_limit_enabled is not UNSET:
            field_dict["taskLimitEnabled"] = task_limit_enabled
        if max_task_count is not UNSET:
            field_dict["maxTaskCount"] = max_task_count
        if mount_server is not UNSET:
            field_dict["mountServer"] = mount_server
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_mount_servers_settings import BackupServerMountServersSettings
        from ..models.backup_server_veeam_data_cloud_storage_account import BackupServerVeeamDataCloudStorageAccount
        from ..models.backup_server_veeam_data_cloud_storage_container import BackupServerVeeamDataCloudStorageContainer
        from ..models.embedded_for_backup_server_repository_children_type_0 import (
            EmbeddedForBackupServerRepositoryChildrenType0,
        )

        d = dict(src_dict)
        name = d.pop("name")

        account = BackupServerVeeamDataCloudStorageAccount.from_dict(d.pop("account"))

        container = BackupServerVeeamDataCloudStorageContainer.from_dict(d.pop("container"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_unique_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unique_id = _parse_unique_id(d.pop("uniqueId", UNSET))

        def _parse_task_limit_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        task_limit_enabled = _parse_task_limit_enabled(d.pop("taskLimitEnabled", UNSET))

        def _parse_max_task_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_task_count = _parse_max_task_count(d.pop("maxTaskCount", UNSET))

        _mount_server = d.pop("mountServer", UNSET)
        mount_server: BackupServerMountServersSettings | Unset
        if isinstance(_mount_server, Unset):
            mount_server = UNSET
        else:
            mount_server = BackupServerMountServersSettings.from_dict(_mount_server)

        def _parse_field_embedded(data: object) -> EmbeddedForBackupServerRepositoryChildrenType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_embedded_for_backup_server_repository_children_type_0 = (
                    EmbeddedForBackupServerRepositoryChildrenType0.from_dict(data)
                )

                return componentsschemas_embedded_for_backup_server_repository_children_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EmbeddedForBackupServerRepositoryChildrenType0 | None | Unset, data)

        field_embedded = _parse_field_embedded(d.pop("_embedded", UNSET))

        backup_server_veeam_vault_repository = cls(
            name=name,
            account=account,
            container=container,
            instance_uid=instance_uid,
            description=description,
            unique_id=unique_id,
            task_limit_enabled=task_limit_enabled,
            max_task_count=max_task_count,
            mount_server=mount_server,
            field_embedded=field_embedded,
        )

        backup_server_veeam_vault_repository.additional_properties = d
        return backup_server_veeam_vault_repository

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
