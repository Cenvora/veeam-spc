import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.backup_job_operation_mode_readonly import BackupJobOperationModeReadonly
from ..models.backup_policy_access_mode import BackupPolicyAccessMode
from ..models.backup_policy_system_type import BackupPolicySystemType
from ..models.backup_policy_type_readonly import BackupPolicyTypeReadonly
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupPolicy")


@_attrs_define
class BackupPolicy:
    r"""
    Example:
        {'instanceUid': 'D80427DD-3F62-4AF3-A206-98ABC24C87E5', 'organizationUid':
            'A41427DD-3F62-4AF3-A206-98ABC24C87E5', 'name': 'Backup Policy X', 'configId': 'CC221975-B409-49B5-8ECE-
            FFFECB13494F', 'description': 'Backup Policy X', 'mode': 'Server', 'operationMode': 'Server', 'type':
            'Provider', 'accessMode': 'Public'}

    Attributes:
        name (str): Backup policy name. Pattern is '^[^$()%]+$' for Windows policy and '^[^~"#%&*:<>?!/\\{|}'`$]+$' for
            Linux and Mac policies.
        operation_mode (BackupJobOperationModeReadonly): Backup job operation mode.
        access_mode (BackupPolicyAccessMode): Backup policy access mode.
        instance_uid (Union[Unset, UUID]): UID assigned to a backup policy.
        id (Union[Unset, int]): System ID assigned to a backup policy.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization to whose agents a backup policy is
            assigned.
        description (Union[Unset, str]): Backup policy description.
        config_id (Union[Unset, UUID]): System ID assigned to a backup policy configuration.
        type_ (Union[Unset, BackupPolicyTypeReadonly]): Backup policy type.
        system_type (Union[Unset, BackupPolicySystemType]): Type of guest OS on a managed computer.
        created_by (Union[Unset, str]): Name of a company, reseller or service provider that created a backup policy.
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
    operation_mode: BackupJobOperationModeReadonly
    access_mode: BackupPolicyAccessMode
    instance_uid: Union[Unset, UUID] = UNSET
    id: Union[Unset, int] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    description: Union[Unset, str] = UNSET
    config_id: Union[Unset, UUID] = UNSET
    type_: Union[Unset, BackupPolicyTypeReadonly] = UNSET
    system_type: Union[Unset, BackupPolicySystemType] = UNSET
    created_by: Union[Unset, str] = UNSET
    modified_date: Union[Unset, datetime.datetime] = UNSET
    companies: Union[Unset, list[UUID]] = UNSET
    agents: Union[Unset, list[UUID]] = UNSET
    locations: Union[Unset, list[UUID]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        operation_mode = self.operation_mode.value

        access_mode = self.access_mode.value

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        id = self.id

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        description = self.description

        config_id: Union[Unset, str] = UNSET
        if not isinstance(self.config_id, Unset):
            config_id = str(self.config_id)

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        system_type: Union[Unset, str] = UNSET
        if not isinstance(self.system_type, Unset):
            system_type = self.system_type.value

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
        if config_id is not UNSET:
            field_dict["configId"] = config_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if system_type is not UNSET:
            field_dict["systemType"] = system_type
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
        d = dict(src_dict)
        name = d.pop("name")

        operation_mode = BackupJobOperationModeReadonly(d.pop("operationMode"))

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

        description = d.pop("description", UNSET)

        _config_id = d.pop("configId", UNSET)
        config_id: Union[Unset, UUID]
        if isinstance(_config_id, Unset):
            config_id = UNSET
        else:
            config_id = UUID(_config_id)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, BackupPolicyTypeReadonly]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BackupPolicyTypeReadonly(_type_)

        _system_type = d.pop("systemType", UNSET)
        system_type: Union[Unset, BackupPolicySystemType]
        if isinstance(_system_type, Unset):
            system_type = UNSET
        else:
            system_type = BackupPolicySystemType(_system_type)

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

        backup_policy = cls(
            name=name,
            operation_mode=operation_mode,
            access_mode=access_mode,
            instance_uid=instance_uid,
            id=id,
            organization_uid=organization_uid,
            description=description,
            config_id=config_id,
            type_=type_,
            system_type=system_type,
            created_by=created_by,
            modified_date=modified_date,
            companies=companies,
            agents=agents,
            locations=locations,
        )

        backup_policy.additional_properties = d
        return backup_policy

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
