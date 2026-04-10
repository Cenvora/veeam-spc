from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_object_storage_backup_job_archive_retention_unit import (
    BackupServerObjectStorageBackupJobArchiveRetentionUnit,
)
from ..models.backup_server_object_storage_backup_job_retention_unit import (
    BackupServerObjectStorageBackupJobRetentionUnit,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedded_for_backup_server_job_children_type_0 import EmbeddedForBackupServerJobChildrenType0


T = TypeVar("T", bound="BackupServerObjectStorageBackupJob")


@_attrs_define
class BackupServerObjectStorageBackupJob:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Backup & Replication.
        unique_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Service Provider Console.
        target_repository_uid (Union[Unset, UUID]): UID assigned to a target backup repository.
        archive_repository_uid (Union[None, UUID, Unset]): UID assigned to an archive repository.
        retention (Union[Unset, int]): Duration of file retention.
        retention_unit (Union[Unset, BackupServerObjectStorageBackupJobRetentionUnit]): Measurement units of file
            retention duration.
        is_archive_retention_enabled (Union[Unset, bool]): Indicates whether long-term file retention is enabled.
        archive_retention (Union[Unset, int]): Duration of long-term file retention.
        archive_retention_unit (Union[Unset, BackupServerObjectStorageBackupJobArchiveRetentionUnit]): Measurement units
            of long-term file retention duration.
        field_embedded (Union['EmbeddedForBackupServerJobChildrenType0', None, Unset]): Resource representation of the
            related Veeam Backup & Replication server job entity.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    unique_uid: Union[Unset, UUID] = UNSET
    target_repository_uid: Union[Unset, UUID] = UNSET
    archive_repository_uid: Union[None, UUID, Unset] = UNSET
    retention: Union[Unset, int] = UNSET
    retention_unit: Union[Unset, BackupServerObjectStorageBackupJobRetentionUnit] = UNSET
    is_archive_retention_enabled: Union[Unset, bool] = UNSET
    archive_retention: Union[Unset, int] = UNSET
    archive_retention_unit: Union[Unset, BackupServerObjectStorageBackupJobArchiveRetentionUnit] = UNSET
    field_embedded: Union["EmbeddedForBackupServerJobChildrenType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.embedded_for_backup_server_job_children_type_0 import EmbeddedForBackupServerJobChildrenType0

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        unique_uid: Union[Unset, str] = UNSET
        if not isinstance(self.unique_uid, Unset):
            unique_uid = str(self.unique_uid)

        target_repository_uid: Union[Unset, str] = UNSET
        if not isinstance(self.target_repository_uid, Unset):
            target_repository_uid = str(self.target_repository_uid)

        archive_repository_uid: Union[None, Unset, str]
        if isinstance(self.archive_repository_uid, Unset):
            archive_repository_uid = UNSET
        elif isinstance(self.archive_repository_uid, UUID):
            archive_repository_uid = str(self.archive_repository_uid)
        else:
            archive_repository_uid = self.archive_repository_uid

        retention = self.retention

        retention_unit: Union[Unset, str] = UNSET
        if not isinstance(self.retention_unit, Unset):
            retention_unit = self.retention_unit.value

        is_archive_retention_enabled = self.is_archive_retention_enabled

        archive_retention = self.archive_retention

        archive_retention_unit: Union[Unset, str] = UNSET
        if not isinstance(self.archive_retention_unit, Unset):
            archive_retention_unit = self.archive_retention_unit.value

        field_embedded: Union[None, Unset, dict[str, Any]]
        if isinstance(self.field_embedded, Unset):
            field_embedded = UNSET
        elif isinstance(self.field_embedded, EmbeddedForBackupServerJobChildrenType0):
            field_embedded = self.field_embedded.to_dict()
        else:
            field_embedded = self.field_embedded

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if unique_uid is not UNSET:
            field_dict["uniqueUid"] = unique_uid
        if target_repository_uid is not UNSET:
            field_dict["targetRepositoryUid"] = target_repository_uid
        if archive_repository_uid is not UNSET:
            field_dict["archiveRepositoryUid"] = archive_repository_uid
        if retention is not UNSET:
            field_dict["retention"] = retention
        if retention_unit is not UNSET:
            field_dict["retentionUnit"] = retention_unit
        if is_archive_retention_enabled is not UNSET:
            field_dict["isArchiveRetentionEnabled"] = is_archive_retention_enabled
        if archive_retention is not UNSET:
            field_dict["archiveRetention"] = archive_retention
        if archive_retention_unit is not UNSET:
            field_dict["archiveRetentionUnit"] = archive_retention_unit
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedded_for_backup_server_job_children_type_0 import EmbeddedForBackupServerJobChildrenType0

        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _unique_uid = d.pop("uniqueUid", UNSET)
        unique_uid: Union[Unset, UUID]
        if isinstance(_unique_uid, Unset):
            unique_uid = UNSET
        else:
            unique_uid = UUID(_unique_uid)

        _target_repository_uid = d.pop("targetRepositoryUid", UNSET)
        target_repository_uid: Union[Unset, UUID]
        if isinstance(_target_repository_uid, Unset):
            target_repository_uid = UNSET
        else:
            target_repository_uid = UUID(_target_repository_uid)

        def _parse_archive_repository_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                archive_repository_uid_type_0 = UUID(data)

                return archive_repository_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        archive_repository_uid = _parse_archive_repository_uid(d.pop("archiveRepositoryUid", UNSET))

        retention = d.pop("retention", UNSET)

        _retention_unit = d.pop("retentionUnit", UNSET)
        retention_unit: Union[Unset, BackupServerObjectStorageBackupJobRetentionUnit]
        if isinstance(_retention_unit, Unset):
            retention_unit = UNSET
        else:
            retention_unit = BackupServerObjectStorageBackupJobRetentionUnit(_retention_unit)

        is_archive_retention_enabled = d.pop("isArchiveRetentionEnabled", UNSET)

        archive_retention = d.pop("archiveRetention", UNSET)

        _archive_retention_unit = d.pop("archiveRetentionUnit", UNSET)
        archive_retention_unit: Union[Unset, BackupServerObjectStorageBackupJobArchiveRetentionUnit]
        if isinstance(_archive_retention_unit, Unset):
            archive_retention_unit = UNSET
        else:
            archive_retention_unit = BackupServerObjectStorageBackupJobArchiveRetentionUnit(_archive_retention_unit)

        def _parse_field_embedded(data: object) -> Union["EmbeddedForBackupServerJobChildrenType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_embedded_for_backup_server_job_children_type_0 = (
                    EmbeddedForBackupServerJobChildrenType0.from_dict(data)
                )

                return componentsschemas_embedded_for_backup_server_job_children_type_0
            except:  # noqa: E722
                pass
            return cast(Union["EmbeddedForBackupServerJobChildrenType0", None, Unset], data)

        field_embedded = _parse_field_embedded(d.pop("_embedded", UNSET))

        backup_server_object_storage_backup_job = cls(
            instance_uid=instance_uid,
            unique_uid=unique_uid,
            target_repository_uid=target_repository_uid,
            archive_repository_uid=archive_repository_uid,
            retention=retention,
            retention_unit=retention_unit,
            is_archive_retention_enabled=is_archive_retention_enabled,
            archive_retention=archive_retention,
            archive_retention_unit=archive_retention_unit,
            field_embedded=field_embedded,
        )

        backup_server_object_storage_backup_job.additional_properties = d
        return backup_server_object_storage_backup_job

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
