from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedded_for_backup_server_job_children_type_0 import EmbeddedForBackupServerJobChildrenType0


T = TypeVar("T", bound="BackupServerFileTapeJob")


@_attrs_define
class BackupServerFileTapeJob:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Backup & Replication.
        unique_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Service Provider Console.
        full_media_pool_uid (Union[Unset, UUID]): UID assigned to a media pool for full backups.
        incremental_media_pool_uid (Union[Unset, UUID]): UID assigned to a media pool for increment backups.
        field_embedded (Union['EmbeddedForBackupServerJobChildrenType0', None, Unset]): Resource representation of the
            related Veeam Backup & Replication server job entity.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    unique_uid: Union[Unset, UUID] = UNSET
    full_media_pool_uid: Union[Unset, UUID] = UNSET
    incremental_media_pool_uid: Union[Unset, UUID] = UNSET
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

        full_media_pool_uid: Union[Unset, str] = UNSET
        if not isinstance(self.full_media_pool_uid, Unset):
            full_media_pool_uid = str(self.full_media_pool_uid)

        incremental_media_pool_uid: Union[Unset, str] = UNSET
        if not isinstance(self.incremental_media_pool_uid, Unset):
            incremental_media_pool_uid = str(self.incremental_media_pool_uid)

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
        if full_media_pool_uid is not UNSET:
            field_dict["fullMediaPoolUid"] = full_media_pool_uid
        if incremental_media_pool_uid is not UNSET:
            field_dict["incrementalMediaPoolUid"] = incremental_media_pool_uid
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

        backup_server_file_tape_job = cls(
            instance_uid=instance_uid,
            unique_uid=unique_uid,
            full_media_pool_uid=full_media_pool_uid,
            incremental_media_pool_uid=incremental_media_pool_uid,
            field_embedded=field_embedded,
        )

        backup_server_file_tape_job.additional_properties = d
        return backup_server_file_tape_job

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
