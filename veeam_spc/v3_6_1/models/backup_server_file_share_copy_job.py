from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_file_share_copy_job_retention_unit import BackupServerFileShareCopyJobRetentionUnit
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedded_for_backup_server_job_children_type_0 import EmbeddedForBackupServerJobChildrenType0


T = TypeVar("T", bound="BackupServerFileShareCopyJob")


@_attrs_define
class BackupServerFileShareCopyJob:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Backup & Replication.
        unique_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Service Provider Console.
        source_file_share_job_uid (Union[Unset, UUID]): UID assigned to a source file share job in Veeam Backup &
            Replication
        source_file_share_job_unique_uid (Union[Unset, UUID]): UID assigned to a source file share job in Veeam Service
            Provider Console.
        target_repository_uid (Union[Unset, UUID]): UID assigned to a target backup repository.
        retention (Union[Unset, int]): Duration of backup file retention.
        retention_unit (Union[Unset, BackupServerFileShareCopyJobRetentionUnit]): Measurement units of backup file
            retention duration.
        source_size (Union[None, Unset, int]): Size of a job source, in bytes.
        field_embedded (Union['EmbeddedForBackupServerJobChildrenType0', None, Unset]): Resource representation of the
            related Veeam Backup & Replication server job entity.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    unique_uid: Union[Unset, UUID] = UNSET
    source_file_share_job_uid: Union[Unset, UUID] = UNSET
    source_file_share_job_unique_uid: Union[Unset, UUID] = UNSET
    target_repository_uid: Union[Unset, UUID] = UNSET
    retention: Union[Unset, int] = UNSET
    retention_unit: Union[Unset, BackupServerFileShareCopyJobRetentionUnit] = UNSET
    source_size: Union[None, Unset, int] = UNSET
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

        source_file_share_job_uid: Union[Unset, str] = UNSET
        if not isinstance(self.source_file_share_job_uid, Unset):
            source_file_share_job_uid = str(self.source_file_share_job_uid)

        source_file_share_job_unique_uid: Union[Unset, str] = UNSET
        if not isinstance(self.source_file_share_job_unique_uid, Unset):
            source_file_share_job_unique_uid = str(self.source_file_share_job_unique_uid)

        target_repository_uid: Union[Unset, str] = UNSET
        if not isinstance(self.target_repository_uid, Unset):
            target_repository_uid = str(self.target_repository_uid)

        retention = self.retention

        retention_unit: Union[Unset, str] = UNSET
        if not isinstance(self.retention_unit, Unset):
            retention_unit = self.retention_unit.value

        source_size: Union[None, Unset, int]
        if isinstance(self.source_size, Unset):
            source_size = UNSET
        else:
            source_size = self.source_size

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
        if source_file_share_job_uid is not UNSET:
            field_dict["sourceFileShareJobUid"] = source_file_share_job_uid
        if source_file_share_job_unique_uid is not UNSET:
            field_dict["sourceFileShareJobUniqueUid"] = source_file_share_job_unique_uid
        if target_repository_uid is not UNSET:
            field_dict["targetRepositoryUid"] = target_repository_uid
        if retention is not UNSET:
            field_dict["retention"] = retention
        if retention_unit is not UNSET:
            field_dict["retentionUnit"] = retention_unit
        if source_size is not UNSET:
            field_dict["sourceSize"] = source_size
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

        _source_file_share_job_uid = d.pop("sourceFileShareJobUid", UNSET)
        source_file_share_job_uid: Union[Unset, UUID]
        if isinstance(_source_file_share_job_uid, Unset):
            source_file_share_job_uid = UNSET
        else:
            source_file_share_job_uid = UUID(_source_file_share_job_uid)

        _source_file_share_job_unique_uid = d.pop("sourceFileShareJobUniqueUid", UNSET)
        source_file_share_job_unique_uid: Union[Unset, UUID]
        if isinstance(_source_file_share_job_unique_uid, Unset):
            source_file_share_job_unique_uid = UNSET
        else:
            source_file_share_job_unique_uid = UUID(_source_file_share_job_unique_uid)

        _target_repository_uid = d.pop("targetRepositoryUid", UNSET)
        target_repository_uid: Union[Unset, UUID]
        if isinstance(_target_repository_uid, Unset):
            target_repository_uid = UNSET
        else:
            target_repository_uid = UUID(_target_repository_uid)

        retention = d.pop("retention", UNSET)

        _retention_unit = d.pop("retentionUnit", UNSET)
        retention_unit: Union[Unset, BackupServerFileShareCopyJobRetentionUnit]
        if isinstance(_retention_unit, Unset):
            retention_unit = UNSET
        else:
            retention_unit = BackupServerFileShareCopyJobRetentionUnit(_retention_unit)

        def _parse_source_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        source_size = _parse_source_size(d.pop("sourceSize", UNSET))

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

        backup_server_file_share_copy_job = cls(
            instance_uid=instance_uid,
            unique_uid=unique_uid,
            source_file_share_job_uid=source_file_share_job_uid,
            source_file_share_job_unique_uid=source_file_share_job_unique_uid,
            target_repository_uid=target_repository_uid,
            retention=retention,
            retention_unit=retention_unit,
            source_size=source_size,
            field_embedded=field_embedded,
        )

        backup_server_file_share_copy_job.additional_properties = d
        return backup_server_file_share_copy_job

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
