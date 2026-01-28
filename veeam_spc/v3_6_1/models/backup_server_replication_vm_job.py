from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedded_for_backup_server_job_children_type_0 import EmbeddedForBackupServerJobChildrenType0


T = TypeVar("T", bound="BackupServerReplicationVmJob")


@_attrs_define
class BackupServerReplicationVmJob:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Backup & Replication.
        unique_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Service Provider Console.
        protected_vm_count (Union[Unset, int]): Number of VMs included in a job.
        is_cloud_job (Union[Unset, bool]): Indicates whether VM replicas are created on a cloud host.
        cloud_host_uid (Union[None, UUID, Unset]): UID assigned to a cloud host.
        target_host_uid (Union[Unset, UUID]): UID assigned to a target host for VM replicas.
        source_wan_accelerator_uid (Union[None, UUID, Unset]): UID assigned to a source WAN accelerator.
        target_wan_accelerator_uid (Union[None, UUID, Unset]): UID assigned to a target WAN accelerator.
        through_wan_accelerators (Union[Unset, bool]): Indicates whether WAN acceleration is enabled.
        field_embedded (Union['EmbeddedForBackupServerJobChildrenType0', None, Unset]): Resource representation of the
            related Veeam Backup & Replication server job entity.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    unique_uid: Union[Unset, UUID] = UNSET
    protected_vm_count: Union[Unset, int] = UNSET
    is_cloud_job: Union[Unset, bool] = UNSET
    cloud_host_uid: Union[None, UUID, Unset] = UNSET
    target_host_uid: Union[Unset, UUID] = UNSET
    source_wan_accelerator_uid: Union[None, UUID, Unset] = UNSET
    target_wan_accelerator_uid: Union[None, UUID, Unset] = UNSET
    through_wan_accelerators: Union[Unset, bool] = UNSET
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

        protected_vm_count = self.protected_vm_count

        is_cloud_job = self.is_cloud_job

        cloud_host_uid: Union[None, Unset, str]
        if isinstance(self.cloud_host_uid, Unset):
            cloud_host_uid = UNSET
        elif isinstance(self.cloud_host_uid, UUID):
            cloud_host_uid = str(self.cloud_host_uid)
        else:
            cloud_host_uid = self.cloud_host_uid

        target_host_uid: Union[Unset, str] = UNSET
        if not isinstance(self.target_host_uid, Unset):
            target_host_uid = str(self.target_host_uid)

        source_wan_accelerator_uid: Union[None, Unset, str]
        if isinstance(self.source_wan_accelerator_uid, Unset):
            source_wan_accelerator_uid = UNSET
        elif isinstance(self.source_wan_accelerator_uid, UUID):
            source_wan_accelerator_uid = str(self.source_wan_accelerator_uid)
        else:
            source_wan_accelerator_uid = self.source_wan_accelerator_uid

        target_wan_accelerator_uid: Union[None, Unset, str]
        if isinstance(self.target_wan_accelerator_uid, Unset):
            target_wan_accelerator_uid = UNSET
        elif isinstance(self.target_wan_accelerator_uid, UUID):
            target_wan_accelerator_uid = str(self.target_wan_accelerator_uid)
        else:
            target_wan_accelerator_uid = self.target_wan_accelerator_uid

        through_wan_accelerators = self.through_wan_accelerators

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

        protected_vm_count = d.pop("protectedVmCount", UNSET)

        is_cloud_job = d.pop("isCloudJob", UNSET)

        def _parse_cloud_host_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cloud_host_uid_type_0 = UUID(data)

                return cloud_host_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        cloud_host_uid = _parse_cloud_host_uid(d.pop("cloudHostUid", UNSET))

        _target_host_uid = d.pop("targetHostUid", UNSET)
        target_host_uid: Union[Unset, UUID]
        if isinstance(_target_host_uid, Unset):
            target_host_uid = UNSET
        else:
            target_host_uid = UUID(_target_host_uid)

        def _parse_source_wan_accelerator_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_wan_accelerator_uid_type_0 = UUID(data)

                return source_wan_accelerator_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        source_wan_accelerator_uid = _parse_source_wan_accelerator_uid(d.pop("sourceWanAcceleratorUid", UNSET))

        def _parse_target_wan_accelerator_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                target_wan_accelerator_uid_type_0 = UUID(data)

                return target_wan_accelerator_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        target_wan_accelerator_uid = _parse_target_wan_accelerator_uid(d.pop("targetWanAcceleratorUid", UNSET))

        through_wan_accelerators = d.pop("throughWanAccelerators", UNSET)

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
