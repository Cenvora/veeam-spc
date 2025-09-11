from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedded_for_backup_server_job_children import EmbeddedForBackupServerJobChildren


T = TypeVar("T", bound="BackupServerFileCopyJob")


@_attrs_define
class BackupServerFileCopyJob:
    """
    Attributes:
        instance_uid (UUID): UID assigned to a job in Veeam Backup & Replication.
        unique_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Service Provider Console.
        target_host_uid (Union[Unset, UUID]): UID assigned to a target host.
        target_path (Union[Unset, str]): Path to a location on a target repository where copied files reside.
        source_size (Union[Unset, int]): Size of a job source, in bytes.
        field_embedded (Union[Unset, EmbeddedForBackupServerJobChildren]): Resource representation of the related Veeam
            Backup & Replication server job entity.
    """

    instance_uid: UUID
    unique_uid: Union[Unset, UUID] = UNSET
    target_host_uid: Union[Unset, UUID] = UNSET
    target_path: Union[Unset, str] = UNSET
    source_size: Union[Unset, int] = UNSET
    field_embedded: Union[Unset, "EmbeddedForBackupServerJobChildren"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid = str(self.instance_uid)

        unique_uid: Union[Unset, str] = UNSET
        if not isinstance(self.unique_uid, Unset):
            unique_uid = str(self.unique_uid)

        target_host_uid: Union[Unset, str] = UNSET
        if not isinstance(self.target_host_uid, Unset):
            target_host_uid = str(self.target_host_uid)

        target_path = self.target_path

        source_size = self.source_size

        field_embedded: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_embedded, Unset):
            field_embedded = self.field_embedded.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instanceUid": instance_uid,
            }
        )
        if unique_uid is not UNSET:
            field_dict["uniqueUid"] = unique_uid
        if target_host_uid is not UNSET:
            field_dict["targetHostUid"] = target_host_uid
        if target_path is not UNSET:
            field_dict["targetPath"] = target_path
        if source_size is not UNSET:
            field_dict["sourceSize"] = source_size
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedded_for_backup_server_job_children import EmbeddedForBackupServerJobChildren

        d = dict(src_dict)
        instance_uid = UUID(d.pop("instanceUid"))

        _unique_uid = d.pop("uniqueUid", UNSET)
        unique_uid: Union[Unset, UUID]
        if isinstance(_unique_uid, Unset):
            unique_uid = UNSET
        else:
            unique_uid = UUID(_unique_uid)

        _target_host_uid = d.pop("targetHostUid", UNSET)
        target_host_uid: Union[Unset, UUID]
        if isinstance(_target_host_uid, Unset):
            target_host_uid = UNSET
        else:
            target_host_uid = UUID(_target_host_uid)

        target_path = d.pop("targetPath", UNSET)

        source_size = d.pop("sourceSize", UNSET)

        _field_embedded = d.pop("_embedded", UNSET)
        field_embedded: Union[Unset, EmbeddedForBackupServerJobChildren]
        if isinstance(_field_embedded, Unset):
            field_embedded = UNSET
        else:
            field_embedded = EmbeddedForBackupServerJobChildren.from_dict(_field_embedded)

        backup_server_file_copy_job = cls(
            instance_uid=instance_uid,
            unique_uid=unique_uid,
            target_host_uid=target_host_uid,
            target_path=target_path,
            source_size=source_size,
            field_embedded=field_embedded,
        )

        backup_server_file_copy_job.additional_properties = d
        return backup_server_file_copy_job

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
