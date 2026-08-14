from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
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
        instance_uid (UUID | Unset): UID assigned to a backup.
        backup_object_uid (UUID | Unset): UID assigned to a backup object included in a backup.
        name (str | Unset): Name of a backup.
        tenant_uid (UUID | Unset): UID assigned to a tenant.
        sub_tenant_uid (UUID | Unset): UID assigned to a subtenant.
        type_ (CloudBackupType | Unset): Type of a backed-up object.
        site_uid (UUID | Unset): UID assigned to a Veeam Cloud Connect site.
        repository_uid (UUID | Unset): UID assigned to a Veeam Cloud Connect repository.
        job_uid (UUID | Unset): UID assigned to a backup job that created the backup.
        source_installation_uid (UUID | Unset): Installation UID of a Veeam product that is installed on the backed up
            object.
        restore_points_count (int | Unset): Number of restore points.
    """

    instance_uid: UUID | Unset = UNSET
    backup_object_uid: UUID | Unset = UNSET
    name: str | Unset = UNSET
    tenant_uid: UUID | Unset = UNSET
    sub_tenant_uid: UUID | Unset = UNSET
    type_: CloudBackupType | Unset = UNSET
    site_uid: UUID | Unset = UNSET
    repository_uid: UUID | Unset = UNSET
    job_uid: UUID | Unset = UNSET
    source_installation_uid: UUID | Unset = UNSET
    restore_points_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        backup_object_uid: str | Unset = UNSET
        if not isinstance(self.backup_object_uid, Unset):
            backup_object_uid = str(self.backup_object_uid)

        name = self.name

        tenant_uid: str | Unset = UNSET
        if not isinstance(self.tenant_uid, Unset):
            tenant_uid = str(self.tenant_uid)

        sub_tenant_uid: str | Unset = UNSET
        if not isinstance(self.sub_tenant_uid, Unset):
            sub_tenant_uid = str(self.sub_tenant_uid)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        site_uid: str | Unset = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        repository_uid: str | Unset = UNSET
        if not isinstance(self.repository_uid, Unset):
            repository_uid = str(self.repository_uid)

        job_uid: str | Unset = UNSET
        if not isinstance(self.job_uid, Unset):
            job_uid = str(self.job_uid)

        source_installation_uid: str | Unset = UNSET
        if not isinstance(self.source_installation_uid, Unset):
            source_installation_uid = str(self.source_installation_uid)

        restore_points_count = self.restore_points_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if backup_object_uid is not UNSET:
            field_dict["backupObjectUid"] = backup_object_uid
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
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _backup_object_uid = d.pop("backupObjectUid", UNSET)
        backup_object_uid: UUID | Unset
        if isinstance(_backup_object_uid, Unset):
            backup_object_uid = UNSET
        else:
            backup_object_uid = UUID(_backup_object_uid)

        name = d.pop("name", UNSET)

        _tenant_uid = d.pop("tenantUid", UNSET)
        tenant_uid: UUID | Unset
        if isinstance(_tenant_uid, Unset):
            tenant_uid = UNSET
        else:
            tenant_uid = UUID(_tenant_uid)

        _sub_tenant_uid = d.pop("subTenantUid", UNSET)
        sub_tenant_uid: UUID | Unset
        if isinstance(_sub_tenant_uid, Unset):
            sub_tenant_uid = UNSET
        else:
            sub_tenant_uid = UUID(_sub_tenant_uid)

        _type_ = d.pop("type", UNSET)
        type_: CloudBackupType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CloudBackupType(_type_)

        _site_uid = d.pop("siteUid", UNSET)
        site_uid: UUID | Unset
        if isinstance(_site_uid, Unset):
            site_uid = UNSET
        else:
            site_uid = UUID(_site_uid)

        _repository_uid = d.pop("repositoryUid", UNSET)
        repository_uid: UUID | Unset
        if isinstance(_repository_uid, Unset):
            repository_uid = UNSET
        else:
            repository_uid = UUID(_repository_uid)

        _job_uid = d.pop("jobUid", UNSET)
        job_uid: UUID | Unset
        if isinstance(_job_uid, Unset):
            job_uid = UNSET
        else:
            job_uid = UUID(_job_uid)

        _source_installation_uid = d.pop("sourceInstallationUid", UNSET)
        source_installation_uid: UUID | Unset
        if isinstance(_source_installation_uid, Unset):
            source_installation_uid = UNSET
        else:
            source_installation_uid = UUID(_source_installation_uid)

        restore_points_count = d.pop("restorePointsCount", UNSET)

        cloud_backup = cls(
            instance_uid=instance_uid,
            backup_object_uid=backup_object_uid,
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
