from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_vm_job_object_platform import BackupServerVmJobObjectPlatform
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_job_object_last_session import BackupServerJobObjectLastSession


T = TypeVar("T", bound="BackupServerVmJobObject")


@_attrs_define
class BackupServerVmJobObject:
    """
    Attributes:
        job_uid (UUID | Unset): UID assigned to a job in Veeam Backup & Replication.
        unique_job_uid (UUID | Unset): UID assigned to a job in Veeam Service Provider Console.
        instance_uid (UUID | Unset): UID assigned to a protected VM.
        name (str | Unset): Name of a VM.
        platform (BackupServerVmJobObjectPlatform | Unset): VM platform.
        hierarchy_ref (str | Unset): Reference ID of a VM.
        is_excluded (bool | Unset): Indicates whether the VM is excluded from a job.
        last_session (BackupServerJobObjectLastSession | Unset):
    """

    job_uid: UUID | Unset = UNSET
    unique_job_uid: UUID | Unset = UNSET
    instance_uid: UUID | Unset = UNSET
    name: str | Unset = UNSET
    platform: BackupServerVmJobObjectPlatform | Unset = UNSET
    hierarchy_ref: str | Unset = UNSET
    is_excluded: bool | Unset = UNSET
    last_session: BackupServerJobObjectLastSession | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_uid: str | Unset = UNSET
        if not isinstance(self.job_uid, Unset):
            job_uid = str(self.job_uid)

        unique_job_uid: str | Unset = UNSET
        if not isinstance(self.unique_job_uid, Unset):
            unique_job_uid = str(self.unique_job_uid)

        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        hierarchy_ref = self.hierarchy_ref

        is_excluded = self.is_excluded

        last_session: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_session, Unset):
            last_session = self.last_session.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if unique_job_uid is not UNSET:
            field_dict["uniqueJobUid"] = unique_job_uid
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if name is not UNSET:
            field_dict["name"] = name
        if platform is not UNSET:
            field_dict["platform"] = platform
        if hierarchy_ref is not UNSET:
            field_dict["hierarchyRef"] = hierarchy_ref
        if is_excluded is not UNSET:
            field_dict["isExcluded"] = is_excluded
        if last_session is not UNSET:
            field_dict["lastSession"] = last_session

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_job_object_last_session import BackupServerJobObjectLastSession

        d = dict(src_dict)
        _job_uid = d.pop("jobUid", UNSET)
        job_uid: UUID | Unset
        if isinstance(_job_uid, Unset):
            job_uid = UNSET
        else:
            job_uid = UUID(_job_uid)

        _unique_job_uid = d.pop("uniqueJobUid", UNSET)
        unique_job_uid: UUID | Unset
        if isinstance(_unique_job_uid, Unset):
            unique_job_uid = UNSET
        else:
            unique_job_uid = UUID(_unique_job_uid)

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        name = d.pop("name", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: BackupServerVmJobObjectPlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = BackupServerVmJobObjectPlatform(_platform)

        hierarchy_ref = d.pop("hierarchyRef", UNSET)

        is_excluded = d.pop("isExcluded", UNSET)

        _last_session = d.pop("lastSession", UNSET)
        last_session: BackupServerJobObjectLastSession | Unset
        if isinstance(_last_session, Unset):
            last_session = UNSET
        else:
            last_session = BackupServerJobObjectLastSession.from_dict(_last_session)

        backup_server_vm_job_object = cls(
            job_uid=job_uid,
            unique_job_uid=unique_job_uid,
            instance_uid=instance_uid,
            name=name,
            platform=platform,
            hierarchy_ref=hierarchy_ref,
            is_excluded=is_excluded,
            last_session=last_session,
        )

        backup_server_vm_job_object.additional_properties = d
        return backup_server_vm_job_object

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
