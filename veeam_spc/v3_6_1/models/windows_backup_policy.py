import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.backup_job_operation_mode import BackupJobOperationMode
from ..models.backup_policy_access_mode import BackupPolicyAccessMode
from ..models.backup_policy_type_readonly import BackupPolicyTypeReadonly
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.windows_backup_job_configuration import WindowsBackupJobConfiguration


T = TypeVar("T", bound="WindowsBackupPolicy")


@_attrs_define
class WindowsBackupPolicy:
    """
    Attributes:
        name (str): Name of a backup policy.
        operation_mode (BackupJobOperationMode): Backup job operation mode.
        job_configuration (WindowsBackupJobConfiguration):
        access_mode (BackupPolicyAccessMode): Backup policy access mode.
        instance_uid (Union[Unset, UUID]): UID assigned to a backup policy.
        id (Union[Unset, int]): System ID assigned to a backup policy.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization to whose Veeam backup agents a backup
            policy is assigned.
        description (Union[None, Unset, str]): Description of a backup policy.
        create_subtenants (Union[Unset, bool]): Indicates whether a subtenant must be created for each Veeam backup
            agent. Default: True.
        create_sub_folders (Union[Unset, bool]): Indicates whether a subfolder must be created for each Veeam backup
            agent on the shared folder. Default: False.
        unlimited_subtenant_quota (Union[Unset, bool]): Indicates whether a subtenant can consume unlimited amount of
            space on a repository. Default: False.
        repository_quota_gb (Union[None, Unset, int]): Maximum amount of space that a subtenant can consume on a
            repository.
            > If a subtenant can consume unlimited amount of space, the value of this property is ignored.
             Default: 100.
        type_ (Union[Unset, BackupPolicyTypeReadonly]): Backup policy type.
        created_by (Union[Unset, str]): Name of an organization that created a backup policy.
        modified_date (Union[Unset, datetime.datetime]): Date and time when settings of a backup policy were last
            modified.
        companies (Union[Unset, list[UUID]]): Array of UIDs assigned to companies to whose Veeam backup agents a policy
            is assigned.
        agents (Union[Unset, list[UUID]]): Array of UIDs assigned to management agents installed alongside Veeam backup
            agents with assigned policy.
        locations (Union[Unset, list[UUID]]): Array of UIDs assigned to locations to which management agents with
            assigned policy belong.
    """

    name: str
    operation_mode: BackupJobOperationMode
    job_configuration: "WindowsBackupJobConfiguration"
    access_mode: BackupPolicyAccessMode
    instance_uid: Union[Unset, UUID] = UNSET
    id: Union[Unset, int] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    description: Union[None, Unset, str] = UNSET
    create_subtenants: Union[Unset, bool] = True
    create_sub_folders: Union[Unset, bool] = False
    unlimited_subtenant_quota: Union[Unset, bool] = False
    repository_quota_gb: Union[None, Unset, int] = 100
    type_: Union[Unset, BackupPolicyTypeReadonly] = UNSET
    created_by: Union[Unset, str] = UNSET
    modified_date: Union[Unset, datetime.datetime] = UNSET
    companies: Union[Unset, list[UUID]] = UNSET
    agents: Union[Unset, list[UUID]] = UNSET
    locations: Union[Unset, list[UUID]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        operation_mode = self.operation_mode.value

        job_configuration = self.job_configuration.to_dict()

        access_mode = self.access_mode.value

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        id = self.id

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        create_subtenants = self.create_subtenants

        create_sub_folders = self.create_sub_folders

        unlimited_subtenant_quota = self.unlimited_subtenant_quota

        repository_quota_gb: Union[None, Unset, int]
        if isinstance(self.repository_quota_gb, Unset):
            repository_quota_gb = UNSET
        else:
            repository_quota_gb = self.repository_quota_gb

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        created_by = self.created_by

        modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat()

        companies: Union[Unset, list[str]] = UNSET
        if not isinstance(self.companies, Unset):
            companies = []
            for companies_item_data in self.companies:
                companies_item = str(companies_item_data)
                companies.append(companies_item)

        agents: Union[Unset, list[str]] = UNSET
        if not isinstance(self.agents, Unset):
            agents = []
            for agents_item_data in self.agents:
                agents_item = str(agents_item_data)
                agents.append(agents_item)

        locations: Union[Unset, list[str]] = UNSET
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
        if create_sub_folders is not UNSET:
            field_dict["createSubFolders"] = create_sub_folders
        if unlimited_subtenant_quota is not UNSET:
            field_dict["unlimitedSubtenantQuota"] = unlimited_subtenant_quota
        if repository_quota_gb is not UNSET:
            field_dict["repositoryQuotaGb"] = repository_quota_gb
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
        from ..models.windows_backup_job_configuration import WindowsBackupJobConfiguration

        d = dict(src_dict)
        name = d.pop("name")

        operation_mode = BackupJobOperationMode(d.pop("operationMode"))

        job_configuration = WindowsBackupJobConfiguration.from_dict(d.pop("jobConfiguration"))

        access_mode = BackupPolicyAccessMode(d.pop("accessMode"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        id = d.pop("id", UNSET)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        create_subtenants = d.pop("createSubtenants", UNSET)

        create_sub_folders = d.pop("createSubFolders", UNSET)

        unlimited_subtenant_quota = d.pop("unlimitedSubtenantQuota", UNSET)

        def _parse_repository_quota_gb(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        repository_quota_gb = _parse_repository_quota_gb(d.pop("repositoryQuotaGb", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, BackupPolicyTypeReadonly]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BackupPolicyTypeReadonly(_type_)

        created_by = d.pop("createdBy", UNSET)

        _modified_date = d.pop("modifiedDate", UNSET)
        modified_date: Union[Unset, datetime.datetime]
        if isinstance(_modified_date, Unset):
            modified_date = UNSET
        else:
            modified_date = isoparse(_modified_date)

        companies = []
        _companies = d.pop("companies", UNSET)
        for companies_item_data in _companies or []:
            companies_item = UUID(companies_item_data)

            companies.append(companies_item)

        agents = []
        _agents = d.pop("agents", UNSET)
        for agents_item_data in _agents or []:
            agents_item = UUID(agents_item_data)

            agents.append(agents_item)

        locations = []
        _locations = d.pop("locations", UNSET)
        for locations_item_data in _locations or []:
            locations_item = UUID(locations_item_data)

            locations.append(locations_item)

        windows_backup_policy = cls(
            name=name,
            operation_mode=operation_mode,
            job_configuration=job_configuration,
            access_mode=access_mode,
            instance_uid=instance_uid,
            id=id,
            organization_uid=organization_uid,
            description=description,
            create_subtenants=create_subtenants,
            create_sub_folders=create_sub_folders,
            unlimited_subtenant_quota=unlimited_subtenant_quota,
            repository_quota_gb=repository_quota_gb,
            type_=type_,
            created_by=created_by,
            modified_date=modified_date,
            companies=companies,
            agents=agents,
            locations=locations,
        )

        windows_backup_policy.additional_properties = d
        return windows_backup_policy

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
