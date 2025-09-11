from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedded_for_backup_server_job_children import EmbeddedForBackupServerJobChildren


T = TypeVar("T", bound="BackupServerVmCopyJob")


@_attrs_define
class BackupServerVmCopyJob:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Backup & Replication.
        unique_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Service Provider Console.
        target_repository_uid (Union[Unset, UUID]): UID assigned to a target repository.
        field_embedded (Union[Unset, EmbeddedForBackupServerJobChildren]): Resource representation of the related Veeam
            Backup & Replication server job entity.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    unique_uid: Union[Unset, UUID] = UNSET
    target_repository_uid: Union[Unset, UUID] = UNSET
    field_embedded: Union[Unset, "EmbeddedForBackupServerJobChildren"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        unique_uid: Union[Unset, str] = UNSET
        if not isinstance(self.unique_uid, Unset):
            unique_uid = str(self.unique_uid)

        target_repository_uid: Union[Unset, str] = UNSET
        if not isinstance(self.target_repository_uid, Unset):
            target_repository_uid = str(self.target_repository_uid)

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
        if target_repository_uid is not UNSET:
            field_dict["targetRepositoryUid"] = target_repository_uid
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

        _target_repository_uid = d.pop("targetRepositoryUid", UNSET)
        target_repository_uid: Union[Unset, UUID]
        if isinstance(_target_repository_uid, Unset):
            target_repository_uid = UNSET
        else:
            target_repository_uid = UUID(_target_repository_uid)

        _field_embedded = d.pop("_embedded", UNSET)
        field_embedded: Union[Unset, EmbeddedForBackupServerJobChildren]
        if isinstance(_field_embedded, Unset):
            field_embedded = UNSET
        else:
            field_embedded = EmbeddedForBackupServerJobChildren.from_dict(_field_embedded)

        backup_server_vm_copy_job = cls(
            instance_uid=instance_uid,
            unique_uid=unique_uid,
            target_repository_uid=target_repository_uid,
            field_embedded=field_embedded,
        )

        backup_server_vm_copy_job.additional_properties = d
        return backup_server_vm_copy_job

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
