from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedded_for_backup_server_job_children import EmbeddedForBackupServerJobChildren


T = TypeVar("T", bound="BackupServerBackupTapeJob")


@_attrs_define
class BackupServerBackupTapeJob:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Backup & Replication.
        unique_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Service Provider Console.
        full_media_pool_uid (Union[Unset, UUID]): UID assigned to a media pool for full backups.
        incremental_media_pool_uid (Union[Unset, UUID]): UID assigned to a media pool for full backups.
        is_gfs_enabled (Union[Unset, bool]): Indicates whether a job runs by GFS scheme.
        field_embedded (Union[Unset, EmbeddedForBackupServerJobChildren]): Resource representation of the related Veeam
            Backup & Replication server job entity.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    unique_uid: Union[Unset, UUID] = UNSET
    full_media_pool_uid: Union[Unset, UUID] = UNSET
    incremental_media_pool_uid: Union[Unset, UUID] = UNSET
    is_gfs_enabled: Union[Unset, bool] = UNSET
    field_embedded: Union[Unset, "EmbeddedForBackupServerJobChildren"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        unique_uid: Union[Unset, str] = UNSET
        if not isinstance(self.unique_uid, Unset):
            unique_uid = str(self.unique_uid)

        full_media_pool_uid: Union[Unset, str] = UNSET
        if not isinstance(self.full_media_pool_uid, Unset):
            full_media_pool_uid = str(self.full_media_pool_uid)

        incremental_media_pool_uid: Union[Unset, str] = UNSET
        if not isinstance(self.incremental_media_pool_uid, Unset):
            incremental_media_pool_uid = str(self.incremental_media_pool_uid)

        is_gfs_enabled = self.is_gfs_enabled

        field_embedded: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_embedded, Unset):
            field_embedded = self.field_embedded.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if unique_uid is not UNSET:
            field_dict["uniqueUid"] = unique_uid
        if full_media_pool_uid is not UNSET:
            field_dict["fullMediaPoolUid"] = full_media_pool_uid
        if incremental_media_pool_uid is not UNSET:
            field_dict["incrementalMediaPoolUid"] = incremental_media_pool_uid
        if is_gfs_enabled is not UNSET:
            field_dict["isGfsEnabled"] = is_gfs_enabled
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedded_for_backup_server_job_children import EmbeddedForBackupServerJobChildren

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

        _full_media_pool_uid = d.pop("fullMediaPoolUid", UNSET)
        full_media_pool_uid: Union[Unset, UUID]
        if isinstance(_full_media_pool_uid, Unset):
            full_media_pool_uid = UNSET
        else:
            full_media_pool_uid = UUID(_full_media_pool_uid)

        _incremental_media_pool_uid = d.pop("incrementalMediaPoolUid", UNSET)
        incremental_media_pool_uid: Union[Unset, UUID]
        if isinstance(_incremental_media_pool_uid, Unset):
            incremental_media_pool_uid = UNSET
        else:
            incremental_media_pool_uid = UUID(_incremental_media_pool_uid)

        is_gfs_enabled = d.pop("isGfsEnabled", UNSET)

        _field_embedded = d.pop("_embedded", UNSET)
        field_embedded: Union[Unset, EmbeddedForBackupServerJobChildren]
        if isinstance(_field_embedded, Unset):
            field_embedded = UNSET
        else:
            field_embedded = EmbeddedForBackupServerJobChildren.from_dict(_field_embedded)

        backup_server_backup_tape_job = cls(
            instance_uid=instance_uid,
            unique_uid=unique_uid,
            full_media_pool_uid=full_media_pool_uid,
            incremental_media_pool_uid=incremental_media_pool_uid,
            is_gfs_enabled=is_gfs_enabled,
            field_embedded=field_embedded,
        )

        backup_server_backup_tape_job.additional_properties = d
        return backup_server_backup_tape_job

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
