from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.backup_server_public_cloud_appliance_management_type import BackupServerPublicCloudApplianceManagementType
from ..models.backup_server_public_cloud_appliance_platform import BackupServerPublicCloudAppliancePlatform
from ..models.public_cloud_policy_state import PublicCloudPolicyState
from ..models.public_cloud_policy_status import PublicCloudPolicyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudDatabasePolicy")


@_attrs_define
class PublicCloudDatabasePolicy:
    """
    Attributes:
        instance_uid (UUID | Unset): UID assigned to a cloud database policy.
        name (str | Unset): Name of cloud database policy.
        appliance_uid (UUID | Unset): UID assigned to a Veeam Backup for Public Clouds appliance.
        status (PublicCloudPolicyStatus | Unset): Status of a Veeam Backup for Public Clouds policy.
        state (PublicCloudPolicyState | Unset): State of a Veeam Backup for Public Clouds policy.
        appliance_management_type (BackupServerPublicCloudApplianceManagementType | Unset): Management type of a Veeam
            Backup for Public Clouds appliance.
        management_agent_uid (UUID | Unset): UID assigned to a management agent.
        backup_server_uid (UUID | Unset): UID assigned to a Veeam Backup & Replication server.
        organization_uid (UUID | Unset): UID assigned to a mapped organization.
        location_uid (UUID | Unset): UID assigned to a cloud database policy location.
        instances_count (int | Unset): Number of cloud databases included in a policy.
        next_run (datetime.datetime | Unset): Date and time of the next scheduled policy run.
        platform_type (BackupServerPublicCloudAppliancePlatform | Unset): Platform of a Veeam Backup for Public Clouds
            appliance.
    """

    instance_uid: UUID | Unset = UNSET
    name: str | Unset = UNSET
    appliance_uid: UUID | Unset = UNSET
    status: PublicCloudPolicyStatus | Unset = UNSET
    state: PublicCloudPolicyState | Unset = UNSET
    appliance_management_type: BackupServerPublicCloudApplianceManagementType | Unset = UNSET
    management_agent_uid: UUID | Unset = UNSET
    backup_server_uid: UUID | Unset = UNSET
    organization_uid: UUID | Unset = UNSET
    location_uid: UUID | Unset = UNSET
    instances_count: int | Unset = UNSET
    next_run: datetime.datetime | Unset = UNSET
    platform_type: BackupServerPublicCloudAppliancePlatform | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        appliance_uid: str | Unset = UNSET
        if not isinstance(self.appliance_uid, Unset):
            appliance_uid = str(self.appliance_uid)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        appliance_management_type: str | Unset = UNSET
        if not isinstance(self.appliance_management_type, Unset):
            appliance_management_type = self.appliance_management_type.value

        management_agent_uid: str | Unset = UNSET
        if not isinstance(self.management_agent_uid, Unset):
            management_agent_uid = str(self.management_agent_uid)

        backup_server_uid: str | Unset = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        organization_uid: str | Unset = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        location_uid: str | Unset = UNSET
        if not isinstance(self.location_uid, Unset):
            location_uid = str(self.location_uid)

        instances_count = self.instances_count

        next_run: str | Unset = UNSET
        if not isinstance(self.next_run, Unset):
            next_run = self.next_run.isoformat()

        platform_type: str | Unset = UNSET
        if not isinstance(self.platform_type, Unset):
            platform_type = self.platform_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if name is not UNSET:
            field_dict["name"] = name
        if appliance_uid is not UNSET:
            field_dict["applianceUid"] = appliance_uid
        if status is not UNSET:
            field_dict["status"] = status
        if state is not UNSET:
            field_dict["state"] = state
        if appliance_management_type is not UNSET:
            field_dict["applianceManagementType"] = appliance_management_type
        if management_agent_uid is not UNSET:
            field_dict["managementAgentUid"] = management_agent_uid
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if location_uid is not UNSET:
            field_dict["locationUid"] = location_uid
        if instances_count is not UNSET:
            field_dict["instancesCount"] = instances_count
        if next_run is not UNSET:
            field_dict["nextRun"] = next_run
        if platform_type is not UNSET:
            field_dict["platformType"] = platform_type

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

        name = d.pop("name", UNSET)

        _appliance_uid = d.pop("applianceUid", UNSET)
        appliance_uid: UUID | Unset
        if isinstance(_appliance_uid, Unset):
            appliance_uid = UNSET
        else:
            appliance_uid = UUID(_appliance_uid)

        _status = d.pop("status", UNSET)
        status: PublicCloudPolicyStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PublicCloudPolicyStatus(_status)

        _state = d.pop("state", UNSET)
        state: PublicCloudPolicyState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PublicCloudPolicyState(_state)

        _appliance_management_type = d.pop("applianceManagementType", UNSET)
        appliance_management_type: BackupServerPublicCloudApplianceManagementType | Unset
        if isinstance(_appliance_management_type, Unset):
            appliance_management_type = UNSET
        else:
            appliance_management_type = BackupServerPublicCloudApplianceManagementType(_appliance_management_type)

        _management_agent_uid = d.pop("managementAgentUid", UNSET)
        management_agent_uid: UUID | Unset
        if isinstance(_management_agent_uid, Unset):
            management_agent_uid = UNSET
        else:
            management_agent_uid = UUID(_management_agent_uid)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: UUID | Unset
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: UUID | Unset
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        _location_uid = d.pop("locationUid", UNSET)
        location_uid: UUID | Unset
        if isinstance(_location_uid, Unset):
            location_uid = UNSET
        else:
            location_uid = UUID(_location_uid)

        instances_count = d.pop("instancesCount", UNSET)

        _next_run = d.pop("nextRun", UNSET)
        next_run: datetime.datetime | Unset
        if isinstance(_next_run, Unset):
            next_run = UNSET
        else:
            next_run = isoparse(_next_run)

        _platform_type = d.pop("platformType", UNSET)
        platform_type: BackupServerPublicCloudAppliancePlatform | Unset
        if isinstance(_platform_type, Unset):
            platform_type = UNSET
        else:
            platform_type = BackupServerPublicCloudAppliancePlatform(_platform_type)

        public_cloud_database_policy = cls(
            instance_uid=instance_uid,
            name=name,
            appliance_uid=appliance_uid,
            status=status,
            state=state,
            appliance_management_type=appliance_management_type,
            management_agent_uid=management_agent_uid,
            backup_server_uid=backup_server_uid,
            organization_uid=organization_uid,
            location_uid=location_uid,
            instances_count=instances_count,
            next_run=next_run,
            platform_type=platform_type,
        )

        public_cloud_database_policy.additional_properties = d
        return public_cloud_database_policy

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
