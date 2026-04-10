from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
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
        name (Union[None, Unset, str]): Name of a backup.
        tenant_uid (Union[Unset, UUID]): UID assigned to a tenant.
        sub_tenant_uid (Union[None, UUID, Unset]): UID assigned to a subtenant.
        type_ (Union[Unset, CloudBackupType]): Type of a backed up object.
        site_uid (Union[Unset, UUID]): UID assigned to a Veeam Cloud Connect site.
        repository_uid (Union[Unset, UUID]): UID assigned to a Veeam Cloud Connect repository.
        job_uid (Union[None, UUID, Unset]): UID assigned to a backup job that created the backup.
        source_installation_uid (Union[None, UUID, Unset]): Installation UID of a Veeam product that is installed on the
            backed up object.
        restore_points_count (Union[Unset, int]): Number of restore points.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    name: Union[None, Unset, str] = UNSET
    tenant_uid: Union[Unset, UUID] = UNSET
    sub_tenant_uid: Union[None, UUID, Unset] = UNSET
    type_: Union[Unset, CloudBackupType] = UNSET
    site_uid: Union[Unset, UUID] = UNSET
    repository_uid: Union[Unset, UUID] = UNSET
    job_uid: Union[None, UUID, Unset] = UNSET
    source_installation_uid: Union[None, UUID, Unset] = UNSET
    restore_points_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        tenant_uid: Union[Unset, str] = UNSET
        if not isinstance(self.tenant_uid, Unset):
            tenant_uid = str(self.tenant_uid)

        sub_tenant_uid: Union[None, Unset, str]
        if isinstance(self.sub_tenant_uid, Unset):
            sub_tenant_uid = UNSET
        elif isinstance(self.sub_tenant_uid, UUID):
            sub_tenant_uid = str(self.sub_tenant_uid)
        else:
            sub_tenant_uid = self.sub_tenant_uid

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        site_uid: Union[Unset, str] = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        repository_uid: Union[Unset, str] = UNSET
        if not isinstance(self.repository_uid, Unset):
            repository_uid = str(self.repository_uid)

        job_uid: Union[None, Unset, str]
        if isinstance(self.job_uid, Unset):
            job_uid = UNSET
        elif isinstance(self.job_uid, UUID):
            job_uid = str(self.job_uid)
        else:
            job_uid = self.job_uid

        source_installation_uid: Union[None, Unset, str]
        if isinstance(self.source_installation_uid, Unset):
            source_installation_uid = UNSET
        elif isinstance(self.source_installation_uid, UUID):
            source_installation_uid = str(self.source_installation_uid)
        else:
            source_installation_uid = self.source_installation_uid

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

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        _tenant_uid = d.pop("tenantUid", UNSET)
        tenant_uid: Union[Unset, UUID]
        if isinstance(_tenant_uid, Unset):
            tenant_uid = UNSET
        else:
            tenant_uid = UUID(_tenant_uid)

        def _parse_sub_tenant_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sub_tenant_uid_type_0 = UUID(data)

                return sub_tenant_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        sub_tenant_uid = _parse_sub_tenant_uid(d.pop("subTenantUid", UNSET))

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

        def _parse_job_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_uid_type_0 = UUID(data)

                return job_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        job_uid = _parse_job_uid(d.pop("jobUid", UNSET))

        def _parse_source_installation_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_installation_uid_type_0 = UUID(data)

                return source_installation_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        source_installation_uid = _parse_source_installation_uid(d.pop("sourceInstallationUid", UNSET))

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
