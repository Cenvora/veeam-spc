from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedded_for_backup_server_job_children import EmbeddedForBackupServerJobChildren


T = TypeVar("T", bound="BackupServerReplicationVmJob")


@_attrs_define
class BackupServerReplicationVmJob:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Backup & Replication.
        unique_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Service Provider Console.
        protected_vm_count (Union[Unset, int]): Number of VMs included in a job.
        is_cloud_job (Union[Unset, bool]): Indicates whether VM replicas are created on a cloud host.
        cloud_host_uid (Union[Unset, UUID]): UID assigned to a cloud host.
        target_host_uid (Union[Unset, UUID]): UID assigned to a target host for VM replicas.
        source_wan_accelerator_uid (Union[Unset, UUID]): UID assigned to a source WAN accelerator.
        target_wan_accelerator_uid (Union[Unset, UUID]): UID assigned to a target WAN accelerator.
        through_wan_accelerators (Union[Unset, bool]): Indicates whether WAN acceleration is enabled.
        field_embedded (Union[Unset, EmbeddedForBackupServerJobChildren]): Resource representation of the related Veeam
            Backup & Replication server job entity.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    unique_uid: Union[Unset, UUID] = UNSET
    protected_vm_count: Union[Unset, int] = UNSET
    is_cloud_job: Union[Unset, bool] = UNSET
    cloud_host_uid: Union[Unset, UUID] = UNSET
    target_host_uid: Union[Unset, UUID] = UNSET
    source_wan_accelerator_uid: Union[Unset, UUID] = UNSET
    target_wan_accelerator_uid: Union[Unset, UUID] = UNSET
    through_wan_accelerators: Union[Unset, bool] = UNSET
    field_embedded: Union[Unset, "EmbeddedForBackupServerJobChildren"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        unique_uid: Union[Unset, str] = UNSET
        if not isinstance(self.unique_uid, Unset):
            unique_uid = str(self.unique_uid)

        protected_vm_count = self.protected_vm_count

        is_cloud_job = self.is_cloud_job

        cloud_host_uid: Union[Unset, str] = UNSET
        if not isinstance(self.cloud_host_uid, Unset):
            cloud_host_uid = str(self.cloud_host_uid)

        target_host_uid: Union[Unset, str] = UNSET
        if not isinstance(self.target_host_uid, Unset):
            target_host_uid = str(self.target_host_uid)

        source_wan_accelerator_uid: Union[Unset, str] = UNSET
        if not isinstance(self.source_wan_accelerator_uid, Unset):
            source_wan_accelerator_uid = str(self.source_wan_accelerator_uid)

        target_wan_accelerator_uid: Union[Unset, str] = UNSET
        if not isinstance(self.target_wan_accelerator_uid, Unset):
            target_wan_accelerator_uid = str(self.target_wan_accelerator_uid)

        through_wan_accelerators = self.through_wan_accelerators

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
        if protected_vm_count is not UNSET:
            field_dict["protectedVmCount"] = protected_vm_count
        if is_cloud_job is not UNSET:
            field_dict["isCloudJob"] = is_cloud_job
        if cloud_host_uid is not UNSET:
            field_dict["cloudHostUid"] = cloud_host_uid
        if target_host_uid is not UNSET:
            field_dict["targetHostUid"] = target_host_uid
        if source_wan_accelerator_uid is not UNSET:
            field_dict["sourceWanAcceleratorUid"] = source_wan_accelerator_uid
        if target_wan_accelerator_uid is not UNSET:
            field_dict["targetWanAcceleratorUid"] = target_wan_accelerator_uid
        if through_wan_accelerators is not UNSET:
            field_dict["throughWanAccelerators"] = through_wan_accelerators
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

        protected_vm_count = d.pop("protectedVmCount", UNSET)

        is_cloud_job = d.pop("isCloudJob", UNSET)

        _cloud_host_uid = d.pop("cloudHostUid", UNSET)
        cloud_host_uid: Union[Unset, UUID]
        if isinstance(_cloud_host_uid, Unset):
            cloud_host_uid = UNSET
        else:
            cloud_host_uid = UUID(_cloud_host_uid)

        _target_host_uid = d.pop("targetHostUid", UNSET)
        target_host_uid: Union[Unset, UUID]
        if isinstance(_target_host_uid, Unset):
            target_host_uid = UNSET
        else:
            target_host_uid = UUID(_target_host_uid)

        _source_wan_accelerator_uid = d.pop("sourceWanAcceleratorUid", UNSET)
        source_wan_accelerator_uid: Union[Unset, UUID]
        if isinstance(_source_wan_accelerator_uid, Unset):
            source_wan_accelerator_uid = UNSET
        else:
            source_wan_accelerator_uid = UUID(_source_wan_accelerator_uid)

        _target_wan_accelerator_uid = d.pop("targetWanAcceleratorUid", UNSET)
        target_wan_accelerator_uid: Union[Unset, UUID]
        if isinstance(_target_wan_accelerator_uid, Unset):
            target_wan_accelerator_uid = UNSET
        else:
            target_wan_accelerator_uid = UUID(_target_wan_accelerator_uid)

        through_wan_accelerators = d.pop("throughWanAccelerators", UNSET)

        _field_embedded = d.pop("_embedded", UNSET)
        field_embedded: Union[Unset, EmbeddedForBackupServerJobChildren]
        if isinstance(_field_embedded, Unset):
            field_embedded = UNSET
        else:
            field_embedded = EmbeddedForBackupServerJobChildren.from_dict(_field_embedded)

        backup_server_replication_vm_job = cls(
            instance_uid=instance_uid,
            unique_uid=unique_uid,
            protected_vm_count=protected_vm_count,
            is_cloud_job=is_cloud_job,
            cloud_host_uid=cloud_host_uid,
            target_host_uid=target_host_uid,
            source_wan_accelerator_uid=source_wan_accelerator_uid,
            target_wan_accelerator_uid=target_wan_accelerator_uid,
            through_wan_accelerators=through_wan_accelerators,
            field_embedded=field_embedded,
        )

        backup_server_replication_vm_job.additional_properties = d
        return backup_server_replication_vm_job

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
