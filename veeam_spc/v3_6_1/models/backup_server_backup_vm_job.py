from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_backup_vm_job_subtype import BackupServerBackupVmJobSubtype
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedded_for_backup_server_job_children_type_0 import EmbeddedForBackupServerJobChildrenType0


T = TypeVar("T", bound="BackupServerBackupVmJob")


@_attrs_define
class BackupServerBackupVmJob:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Backup & Replication.
        unique_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Service Provider Console.
        subtype (Union[Unset, BackupServerBackupVmJobSubtype]): VM platform.
        target_repository_uid (Union[Unset, UUID]): UID assigned to a target repository.
        protected_vm_count (Union[Unset, int]): Number of VMs included in a job.
        field_embedded (Union['EmbeddedForBackupServerJobChildrenType0', None, Unset]): Resource representation of the
            related Veeam Backup & Replication server job entity.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    unique_uid: Union[Unset, UUID] = UNSET
    subtype: Union[Unset, BackupServerBackupVmJobSubtype] = UNSET
    target_repository_uid: Union[Unset, UUID] = UNSET
    protected_vm_count: Union[Unset, int] = UNSET
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

        subtype: Union[Unset, str] = UNSET
        if not isinstance(self.subtype, Unset):
            subtype = self.subtype.value

        target_repository_uid: Union[Unset, str] = UNSET
        if not isinstance(self.target_repository_uid, Unset):
            target_repository_uid = str(self.target_repository_uid)

        protected_vm_count = self.protected_vm_count

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
        if subtype is not UNSET:
            field_dict["subtype"] = subtype
        if target_repository_uid is not UNSET:
            field_dict["targetRepositoryUid"] = target_repository_uid
        if protected_vm_count is not UNSET:
            field_dict["protectedVmCount"] = protected_vm_count
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

        _subtype = d.pop("subtype", UNSET)
        subtype: Union[Unset, BackupServerBackupVmJobSubtype]
        if isinstance(_subtype, Unset):
            subtype = UNSET
        else:
            subtype = BackupServerBackupVmJobSubtype(_subtype)

        _target_repository_uid = d.pop("targetRepositoryUid", UNSET)
        target_repository_uid: Union[Unset, UUID]
        if isinstance(_target_repository_uid, Unset):
            target_repository_uid = UNSET
        else:
            target_repository_uid = UUID(_target_repository_uid)

        protected_vm_count = d.pop("protectedVmCount", UNSET)

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

        backup_server_backup_vm_job = cls(
            instance_uid=instance_uid,
            unique_uid=unique_uid,
            subtype=subtype,
            target_repository_uid=target_repository_uid,
            protected_vm_count=protected_vm_count,
            field_embedded=field_embedded,
        )

        backup_server_backup_vm_job.additional_properties = d
        return backup_server_backup_vm_job

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
