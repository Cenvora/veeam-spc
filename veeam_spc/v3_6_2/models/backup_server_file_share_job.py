from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_file_share_job_archive_retention_unit import BackupServerFileShareJobArchiveRetentionUnit
from ..models.backup_server_file_share_job_retention_unit import BackupServerFileShareJobRetentionUnit
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedded_for_backup_server_job_children import EmbeddedForBackupServerJobChildren


T = TypeVar("T", bound="BackupServerFileShareJob")


@_attrs_define
class BackupServerFileShareJob:
    """
    Attributes:
        instance_uid (UUID | Unset): UID assigned to a job in Veeam Backup & Replication.
        unique_uid (UUID | Unset): UID assigned to a job in Veeam Service Provider Console.
        target_repository_uid (UUID | Unset): UID assigned to a target backup repository.
        archive_repository_uid (UUID | Unset): UID assigned to an archive repository.
        retention (int | Unset): Duration of file retention.
        retention_unit (BackupServerFileShareJobRetentionUnit | Unset): Measurement units of file retention duration.
        is_archive_retention_enabled (bool | Unset): Indicates whether long-term file retention is enabled.
        archive_retention (int | Unset): Duration of long-term file retention.
        archive_retention_unit (BackupServerFileShareJobArchiveRetentionUnit | Unset): Measurement units of long-term
            file retention duration.
        field_embedded (EmbeddedForBackupServerJobChildren | Unset): Resource representation of the related Veeam Backup
            & Replication server job entity.
    """

    instance_uid: UUID | Unset = UNSET
    unique_uid: UUID | Unset = UNSET
    target_repository_uid: UUID | Unset = UNSET
    archive_repository_uid: UUID | Unset = UNSET
    retention: int | Unset = UNSET
    retention_unit: BackupServerFileShareJobRetentionUnit | Unset = UNSET
    is_archive_retention_enabled: bool | Unset = UNSET
    archive_retention: int | Unset = UNSET
    archive_retention_unit: BackupServerFileShareJobArchiveRetentionUnit | Unset = UNSET
    field_embedded: EmbeddedForBackupServerJobChildren | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        unique_uid: str | Unset = UNSET
        if not isinstance(self.unique_uid, Unset):
            unique_uid = str(self.unique_uid)

        target_repository_uid: str | Unset = UNSET
        if not isinstance(self.target_repository_uid, Unset):
            target_repository_uid = str(self.target_repository_uid)

        archive_repository_uid: str | Unset = UNSET
        if not isinstance(self.archive_repository_uid, Unset):
            archive_repository_uid = str(self.archive_repository_uid)

        retention = self.retention

        retention_unit: str | Unset = UNSET
        if not isinstance(self.retention_unit, Unset):
            retention_unit = self.retention_unit.value

        is_archive_retention_enabled = self.is_archive_retention_enabled

        archive_retention = self.archive_retention

        archive_retention_unit: str | Unset = UNSET
        if not isinstance(self.archive_retention_unit, Unset):
            archive_retention_unit = self.archive_retention_unit.value

        field_embedded: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_embedded, Unset):
            field_embedded = self.field_embedded.to_dict()

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
        from ..models.embedded_for_backup_server_job_children import EmbeddedForBackupServerJobChildren

        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _unique_uid = d.pop("uniqueUid", UNSET)
        unique_uid: UUID | Unset
        if isinstance(_unique_uid, Unset):
            unique_uid = UNSET
        else:
            unique_uid = UUID(_unique_uid)

        _target_repository_uid = d.pop("targetRepositoryUid", UNSET)
        target_repository_uid: UUID | Unset
        if isinstance(_target_repository_uid, Unset):
            target_repository_uid = UNSET
        else:
            target_repository_uid = UUID(_target_repository_uid)

        _archive_repository_uid = d.pop("archiveRepositoryUid", UNSET)
        archive_repository_uid: UUID | Unset
        if isinstance(_archive_repository_uid, Unset):
            archive_repository_uid = UNSET
        else:
            archive_repository_uid = UUID(_archive_repository_uid)

        retention = d.pop("retention", UNSET)

        _retention_unit = d.pop("retentionUnit", UNSET)
        retention_unit: BackupServerFileShareJobRetentionUnit | Unset
        if isinstance(_retention_unit, Unset):
            retention_unit = UNSET
        else:
            retention_unit = BackupServerFileShareJobRetentionUnit(_retention_unit)

        is_archive_retention_enabled = d.pop("isArchiveRetentionEnabled", UNSET)

        archive_retention = d.pop("archiveRetention", UNSET)

        _archive_retention_unit = d.pop("archiveRetentionUnit", UNSET)
        archive_retention_unit: BackupServerFileShareJobArchiveRetentionUnit | Unset
        if isinstance(_archive_retention_unit, Unset):
            archive_retention_unit = UNSET
        else:
            archive_retention_unit = BackupServerFileShareJobArchiveRetentionUnit(_archive_retention_unit)

        _field_embedded = d.pop("_embedded", UNSET)
        field_embedded: EmbeddedForBackupServerJobChildren | Unset
        if isinstance(_field_embedded, Unset):
            field_embedded = UNSET
        else:
            field_embedded = EmbeddedForBackupServerJobChildren.from_dict(_field_embedded)

        backup_server_file_share_job = cls(
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

        backup_server_file_share_job.additional_properties = d
        return backup_server_file_share_job

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
