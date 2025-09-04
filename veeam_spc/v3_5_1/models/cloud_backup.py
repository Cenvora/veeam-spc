from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cloud_backup_type import CloudBackupType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudBackup")


@_attrs_define
class CloudBackup:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a backup.
        name (Union[Unset, str]): Name of a backup.
        tenant_uid (Union[Unset, UUID]): UID assigned to a tenant.
        sub_tenant_uid (Union[Unset, UUID]): UID assigned to a subtenant.
        type_ (Union[Unset, CloudBackupType]): Type of a backed up object.
        site_uid (Union[Unset, UUID]): UID assigned to a Veeam Cloud Connect site.
        repository_uid (Union[Unset, UUID]): UID assigned to a Veeam Cloud Connect repository.
        job_uid (Union[Unset, UUID]): UID assigned to a backup job that created the backup.
        source_installation_uid (Union[Unset, UUID]): Installation UID of a Veeam product that is installed on the
            backed up object.
        restore_points_count (Union[Unset, int]): Number of restore points.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    tenant_uid: Union[Unset, UUID] = UNSET
    sub_tenant_uid: Union[Unset, UUID] = UNSET
    type_: Union[Unset, CloudBackupType] = UNSET
    site_uid: Union[Unset, UUID] = UNSET
    repository_uid: Union[Unset, UUID] = UNSET
    job_uid: Union[Unset, UUID] = UNSET
    source_installation_uid: Union[Unset, UUID] = UNSET
    restore_points_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        tenant_uid: Union[Unset, str] = UNSET
        if not isinstance(self.tenant_uid, Unset):
            tenant_uid = str(self.tenant_uid)

        sub_tenant_uid: Union[Unset, str] = UNSET
        if not isinstance(self.sub_tenant_uid, Unset):
            sub_tenant_uid = str(self.sub_tenant_uid)

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        site_uid: Union[Unset, str] = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        repository_uid: Union[Unset, str] = UNSET
        if not isinstance(self.repository_uid, Unset):
            repository_uid = str(self.repository_uid)

        job_uid: Union[Unset, str] = UNSET
        if not isinstance(self.job_uid, Unset):
            job_uid = str(self.job_uid)

        source_installation_uid: Union[Unset, str] = UNSET
        if not isinstance(self.source_installation_uid, Unset):
            source_installation_uid = str(self.source_installation_uid)

        restore_points_count = self.restore_points_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if name is not UNSET:
            field_dict["name"] = name
        if tenant_uid is not UNSET:
            field_dict["tenantUid"] = tenant_uid
        if sub_tenant_uid is not UNSET:
            field_dict["subTenantUid"] = sub_tenant_uid
        if type_ is not UNSET:
            field_dict["type"] = type_
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid
        if repository_uid is not UNSET:
            field_dict["repositoryUid"] = repository_uid
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if source_installation_uid is not UNSET:
            field_dict["sourceInstallationUid"] = source_installation_uid
        if restore_points_count is not UNSET:
            field_dict["restorePointsCount"] = restore_points_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        name = d.pop("name", UNSET)

        _tenant_uid = d.pop("tenantUid", UNSET)
        tenant_uid: Union[Unset, UUID]
        if isinstance(_tenant_uid, Unset):
            tenant_uid = UNSET
        else:
            tenant_uid = UUID(_tenant_uid)

        _sub_tenant_uid = d.pop("subTenantUid", UNSET)
        sub_tenant_uid: Union[Unset, UUID]
        if isinstance(_sub_tenant_uid, Unset):
            sub_tenant_uid = UNSET
        else:
            sub_tenant_uid = UUID(_sub_tenant_uid)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, CloudBackupType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CloudBackupType(_type_)

        _site_uid = d.pop("siteUid", UNSET)
        site_uid: Union[Unset, UUID]
        if isinstance(_site_uid, Unset):
            site_uid = UNSET
        else:
            site_uid = UUID(_site_uid)

        _repository_uid = d.pop("repositoryUid", UNSET)
        repository_uid: Union[Unset, UUID]
        if isinstance(_repository_uid, Unset):
            repository_uid = UNSET
        else:
            repository_uid = UUID(_repository_uid)

        _job_uid = d.pop("jobUid", UNSET)
        job_uid: Union[Unset, UUID]
        if isinstance(_job_uid, Unset):
            job_uid = UNSET
        else:
            job_uid = UUID(_job_uid)

        _source_installation_uid = d.pop("sourceInstallationUid", UNSET)
        source_installation_uid: Union[Unset, UUID]
        if isinstance(_source_installation_uid, Unset):
            source_installation_uid = UNSET
        else:
            source_installation_uid = UUID(_source_installation_uid)

        restore_points_count = d.pop("restorePointsCount", UNSET)

        cloud_backup = cls(
            instance_uid=instance_uid,
            name=name,
            tenant_uid=tenant_uid,
            sub_tenant_uid=sub_tenant_uid,
            type_=type_,
            site_uid=site_uid,
            repository_uid=repository_uid,
            job_uid=job_uid,
            source_installation_uid=source_installation_uid,
            restore_points_count=restore_points_count,
        )

        cloud_backup.additional_properties = d
        return cloud_backup

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
