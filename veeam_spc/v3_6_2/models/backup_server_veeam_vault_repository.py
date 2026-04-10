from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_mount_servers_settings import BackupServerMountServersSettings
    from ..models.backup_server_veeam_data_cloud_storage_account import BackupServerVeeamDataCloudStorageAccount
    from ..models.backup_server_veeam_data_cloud_storage_container import BackupServerVeeamDataCloudStorageContainer
    from ..models.embedded_for_backup_server_repository_children import EmbeddedForBackupServerRepositoryChildren


T = TypeVar("T", bound="BackupServerVeeamVaultRepository")


@_attrs_define
class BackupServerVeeamVaultRepository:
    """
    Attributes:
        name (str): Name of a repository.
        account (BackupServerVeeamDataCloudStorageAccount): Veeam account settings.
        container (BackupServerVeeamDataCloudStorageContainer): Storage container settings.
        instance_uid (UUID | Unset): UID assigned to a repository.
        description (str | Unset): Description of a repository.
        unique_id (str | Unset): Unique identifier assigned to a repository.
        task_limit_enabled (bool | Unset): Indicates whether the number of concurrent task is limited.
        max_task_count (int | Unset): Maximum number of concurrent tasks.
        mount_server (BackupServerMountServersSettings | Unset):
        field_embedded (EmbeddedForBackupServerRepositoryChildren | Unset): Resource representation of the related
            backup repository.
    """

    name: str
    account: BackupServerVeeamDataCloudStorageAccount
    container: BackupServerVeeamDataCloudStorageContainer
    instance_uid: UUID | Unset = UNSET
    description: str | Unset = UNSET
    unique_id: str | Unset = UNSET
    task_limit_enabled: bool | Unset = UNSET
    max_task_count: int | Unset = UNSET
    mount_server: BackupServerMountServersSettings | Unset = UNSET
    field_embedded: EmbeddedForBackupServerRepositoryChildren | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        account = self.account.to_dict()

        container = self.container.to_dict()

        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        description = self.description

        unique_id = self.unique_id

        task_limit_enabled = self.task_limit_enabled

        max_task_count = self.max_task_count

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
        from ..models.embedded_for_backup_server_repository_children import EmbeddedForBackupServerRepositoryChildren

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

        description = d.pop("description", UNSET)

        unique_id = d.pop("uniqueId", UNSET)

        task_limit_enabled = d.pop("taskLimitEnabled", UNSET)

        max_task_count = d.pop("maxTaskCount", UNSET)

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
