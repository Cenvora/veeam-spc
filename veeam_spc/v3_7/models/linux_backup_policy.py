from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.backup_job_operation_mode import BackupJobOperationMode
from ..models.backup_policy_access_mode import BackupPolicyAccessMode
from ..models.backup_policy_type_readonly import BackupPolicyTypeReadonly
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linux_backup_job_configuration import LinuxBackupJobConfiguration


T = TypeVar("T", bound="LinuxBackupPolicy")


@_attrs_define
class LinuxBackupPolicy:
    """
    Attributes:
        name (str): Name of a backup policy.
        operation_mode (BackupJobOperationMode): Backup job operation mode.
        job_configuration (LinuxBackupJobConfiguration):
        access_mode (BackupPolicyAccessMode): Backup policy access mode.
        instance_uid (UUID | Unset): UID assigned to a backup policy.
        id (int | Unset): System ID assigned to a backup policy.
        organization_uid (UUID | Unset): UID assigned to an organization to whose agents a backup policy is assigned.
        description (str | Unset): Description of a backup policy.
        create_subtenants (bool | Unset): Indicates whether a subtenant must be created for each Veeam backup agent.
            Default: True.
        unlimited_subtenant_quota (bool | Unset): Indicates whether a subtenant can consume unlimited amount of space on
            a repository. Default: False.
        repository_quota_gb (int | Unset): Maximum amount of space that a subtenant can consume on a repository.
            > If a subtenant can consume unlimited amount of space, the value of this property is ignored.'
             Default: 100.
        type_ (BackupPolicyTypeReadonly | Unset): Backup policy type.
        created_by (str | Unset): Name of an organization that created a backup policy.
        modified_date (datetime.datetime | Unset): Date and time when settings of a backup policy were last modified.
        companies (list[UUID] | Unset): Array of UIDs assigned to companies to whose Veeam backup agents a policy is
            assigned.
        agents (list[UUID] | Unset): Array of UIDs assigned to management agents installed alongside Veeam backup agents
            with assigned policy.
        locations (list[UUID] | Unset): Array of UIDs assigned to locations to which management agents with assigned
            policy belong.
    """

    name: str
    operation_mode: BackupJobOperationMode
    job_configuration: LinuxBackupJobConfiguration
    access_mode: BackupPolicyAccessMode
    instance_uid: UUID | Unset = UNSET
    id: int | Unset = UNSET
    organization_uid: UUID | Unset = UNSET
    description: str | Unset = UNSET
    create_subtenants: bool | Unset = True
    unlimited_subtenant_quota: bool | Unset = False
    repository_quota_gb: int | Unset = 100
    type_: BackupPolicyTypeReadonly | Unset = UNSET
    created_by: str | Unset = UNSET
    modified_date: datetime.datetime | Unset = UNSET
    companies: list[UUID] | Unset = UNSET
    agents: list[UUID] | Unset = UNSET
    locations: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        operation_mode = self.operation_mode.value

        job_configuration = self.job_configuration.to_dict()

        access_mode = self.access_mode.value

        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        id = self.id

        organization_uid: str | Unset = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        description = self.description

        create_subtenants = self.create_subtenants

        unlimited_subtenant_quota = self.unlimited_subtenant_quota

        repository_quota_gb = self.repository_quota_gb

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        created_by = self.created_by

        modified_date: str | Unset = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat()

        companies: list[str] | Unset = UNSET
        if not isinstance(self.companies, Unset):
            companies = []
            for companies_item_data in self.companies:
                companies_item = str(companies_item_data)
                companies.append(companies_item)

        agents: list[str] | Unset = UNSET
        if not isinstance(self.agents, Unset):
            agents = []
            for agents_item_data in self.agents:
                agents_item = str(agents_item_data)
                agents.append(agents_item)

        locations: list[str] | Unset = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for locations_item_data in self.locations:
                locations_item = str(locations_item_data)
                locations.append(locations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "operationMode": operation_mode,
                "jobConfiguration": job_configuration,
                "accessMode": access_mode,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if id is not UNSET:
            field_dict["id"] = id
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if description is not UNSET:
            field_dict["description"] = description
        if create_subtenants is not UNSET:
            field_dict["createSubtenants"] = create_subtenants
        if unlimited_subtenant_quota is not UNSET:
            field_dict["unlimitedSubtenantQuota"] = unlimited_subtenant_quota
        if repository_quota_gb is not UNSET:
            field_dict["repositoryQuotaGB"] = repository_quota_gb
        if type_ is not UNSET:
            field_dict["type"] = type_
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if companies is not UNSET:
            field_dict["companies"] = companies
        if agents is not UNSET:
            field_dict["agents"] = agents
        if locations is not UNSET:
            field_dict["locations"] = locations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linux_backup_job_configuration import LinuxBackupJobConfiguration

        d = dict(src_dict)
        name = d.pop("name")

        operation_mode = BackupJobOperationMode(d.pop("operationMode"))

        job_configuration = LinuxBackupJobConfiguration.from_dict(d.pop("jobConfiguration"))

        access_mode = BackupPolicyAccessMode(d.pop("accessMode"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        id = d.pop("id", UNSET)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: UUID | Unset
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        description = d.pop("description", UNSET)

        create_subtenants = d.pop("createSubtenants", UNSET)

        unlimited_subtenant_quota = d.pop("unlimitedSubtenantQuota", UNSET)

        repository_quota_gb = d.pop("repositoryQuotaGB", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: BackupPolicyTypeReadonly | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BackupPolicyTypeReadonly(_type_)

        created_by = d.pop("createdBy", UNSET)

        _modified_date = d.pop("modifiedDate", UNSET)
        modified_date: datetime.datetime | Unset
        if isinstance(_modified_date, Unset):
            modified_date = UNSET
        else:
            modified_date = isoparse(_modified_date)

        _companies = d.pop("companies", UNSET)
        companies: list[UUID] | Unset = UNSET
        if _companies is not UNSET:
            companies = []
            for companies_item_data in _companies:
                companies_item = UUID(companies_item_data)

                companies.append(companies_item)

        _agents = d.pop("agents", UNSET)
        agents: list[UUID] | Unset = UNSET
        if _agents is not UNSET:
            agents = []
            for agents_item_data in _agents:
                agents_item = UUID(agents_item_data)

                agents.append(agents_item)

        _locations = d.pop("locations", UNSET)
        locations: list[UUID] | Unset = UNSET
        if _locations is not UNSET:
            locations = []
            for locations_item_data in _locations:
                locations_item = UUID(locations_item_data)

                locations.append(locations_item)

        linux_backup_policy = cls(
            name=name,
            operation_mode=operation_mode,
            job_configuration=job_configuration,
            access_mode=access_mode,
            instance_uid=instance_uid,
            id=id,
            organization_uid=organization_uid,
            description=description,
            create_subtenants=create_subtenants,
            unlimited_subtenant_quota=unlimited_subtenant_quota,
            repository_quota_gb=repository_quota_gb,
            type_=type_,
            created_by=created_by,
            modified_date=modified_date,
            companies=companies,
            agents=agents,
            locations=locations,
        )

        linux_backup_policy.additional_properties = d
        return linux_backup_policy

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
