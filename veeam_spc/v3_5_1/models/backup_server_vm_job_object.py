from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
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
        job_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Backup & Replication.
        unique_job_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Service Provider Console.
        instance_uid (Union[Unset, UUID]): UID assigned to a protected VM.
        name (Union[Unset, str]): Name of a VM.
        platform (Union[Unset, BackupServerVmJobObjectPlatform]): VM platform.
        hierarchy_ref (Union[Unset, str]): Reference ID of a VM.
        is_excluded (Union[Unset, bool]): Indicates whether the VM is excluded from a job.
        last_session (Union[Unset, BackupServerJobObjectLastSession]):
    """

    job_uid: Union[Unset, UUID] = UNSET
    unique_job_uid: Union[Unset, UUID] = UNSET
    instance_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    platform: Union[Unset, BackupServerVmJobObjectPlatform] = UNSET
    hierarchy_ref: Union[Unset, str] = UNSET
    is_excluded: Union[Unset, bool] = UNSET
    last_session: Union[Unset, "BackupServerJobObjectLastSession"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_uid: Union[Unset, str] = UNSET
        if not isinstance(self.job_uid, Unset):
            job_uid = str(self.job_uid)

        unique_job_uid: Union[Unset, str] = UNSET
        if not isinstance(self.unique_job_uid, Unset):
            unique_job_uid = str(self.unique_job_uid)

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        platform: Union[Unset, str] = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        hierarchy_ref = self.hierarchy_ref

        is_excluded = self.is_excluded

        last_session: Union[Unset, dict[str, Any]] = UNSET
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
        job_uid: Union[Unset, UUID]
        if isinstance(_job_uid, Unset):
            job_uid = UNSET
        else:
            job_uid = UUID(_job_uid)

        _unique_job_uid = d.pop("uniqueJobUid", UNSET)
        unique_job_uid: Union[Unset, UUID]
        if isinstance(_unique_job_uid, Unset):
            unique_job_uid = UNSET
        else:
            unique_job_uid = UUID(_unique_job_uid)

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        name = d.pop("name", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: Union[Unset, BackupServerVmJobObjectPlatform]
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = BackupServerVmJobObjectPlatform(_platform)

        hierarchy_ref = d.pop("hierarchyRef", UNSET)

        is_excluded = d.pop("isExcluded", UNSET)

        _last_session = d.pop("lastSession", UNSET)
        last_session: Union[Unset, BackupServerJobObjectLastSession]
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
