from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_backup_server_role_type import BackupServerBackupServerRoleType
from ..models.backup_server_status import BackupServerStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServer")


@_attrs_define
class BackupServer:
    """
    Example:
        {'instanceUid': 'DF997BD3-4AE9-4841-8152-8FF5CC703EAB', 'name': 'VBR', 'managementAgentUid':
            '8BDD0D87-D160-40B5-88D3-E77A6F912AF6', 'version': '9.5.4.1000', 'installationUid':
            'C42C94E9-DB8A-4CF4-AF57-911EFA7FEE87'}

    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup & Replication server.
        name (Union[Unset, str]): Name of a Veeam Backup & Replication server.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization to which a management agent belongs.
        location_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup & Replication server location.
        management_agent_uid (Union[Unset, UUID]): UID assigned to a management agent installed on a Veeam Backup &
            Replication server.
        version (Union[Unset, str]): Version of Veeam Backup & Replication installed on a server.
        display_version (Union[Unset, str]): Version of Veeam Backup & Replication with additional information on
            installed patch version.
        installation_uid (Union[Unset, str]): UID assigned to Veeam Backup & Replication installation.
        backup_server_role_type (Union[Unset, BackupServerBackupServerRoleType]): Role of a Veeam Backup & Replication
            server.
        status (Union[Unset, BackupServerStatus]): Backup server status.
        in_high_availability_cluster (Union[Unset, bool]): Indicates whether a Veeam Backup & Replication server is a
            part of a High Availability cluster.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    location_uid: Union[Unset, UUID] = UNSET
    management_agent_uid: Union[Unset, UUID] = UNSET
    version: Union[Unset, str] = UNSET
    display_version: Union[Unset, str] = UNSET
    installation_uid: Union[Unset, str] = UNSET
    backup_server_role_type: Union[Unset, BackupServerBackupServerRoleType] = UNSET
    status: Union[Unset, BackupServerStatus] = UNSET
    in_high_availability_cluster: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        location_uid: Union[Unset, str] = UNSET
        if not isinstance(self.location_uid, Unset):
            location_uid = str(self.location_uid)

        management_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.management_agent_uid, Unset):
            management_agent_uid = str(self.management_agent_uid)

        version = self.version

        display_version = self.display_version

        installation_uid = self.installation_uid

        backup_server_role_type: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_role_type, Unset):
            backup_server_role_type = self.backup_server_role_type.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        in_high_availability_cluster = self.in_high_availability_cluster

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if name is not UNSET:
            field_dict["name"] = name
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if location_uid is not UNSET:
            field_dict["locationUid"] = location_uid
        if management_agent_uid is not UNSET:
            field_dict["managementAgentUid"] = management_agent_uid
        if version is not UNSET:
            field_dict["version"] = version
        if display_version is not UNSET:
            field_dict["displayVersion"] = display_version
        if installation_uid is not UNSET:
            field_dict["installationUid"] = installation_uid
        if backup_server_role_type is not UNSET:
            field_dict["backupServerRoleType"] = backup_server_role_type
        if status is not UNSET:
            field_dict["status"] = status
        if in_high_availability_cluster is not UNSET:
            field_dict["inHighAvailabilityCluster"] = in_high_availability_cluster

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

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        _location_uid = d.pop("locationUid", UNSET)
        location_uid: Union[Unset, UUID]
        if isinstance(_location_uid, Unset):
            location_uid = UNSET
        else:
            location_uid = UUID(_location_uid)

        _management_agent_uid = d.pop("managementAgentUid", UNSET)
        management_agent_uid: Union[Unset, UUID]
        if isinstance(_management_agent_uid, Unset):
            management_agent_uid = UNSET
        else:
            management_agent_uid = UUID(_management_agent_uid)

        version = d.pop("version", UNSET)

        display_version = d.pop("displayVersion", UNSET)

        installation_uid = d.pop("installationUid", UNSET)

        _backup_server_role_type = d.pop("backupServerRoleType", UNSET)
        backup_server_role_type: Union[Unset, BackupServerBackupServerRoleType]
        if isinstance(_backup_server_role_type, Unset):
            backup_server_role_type = UNSET
        else:
            backup_server_role_type = BackupServerBackupServerRoleType(_backup_server_role_type)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BackupServerStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BackupServerStatus(_status)

        in_high_availability_cluster = d.pop("inHighAvailabilityCluster", UNSET)

        backup_server = cls(
            instance_uid=instance_uid,
            name=name,
            organization_uid=organization_uid,
            location_uid=location_uid,
            management_agent_uid=management_agent_uid,
            version=version,
            display_version=display_version,
            installation_uid=installation_uid,
            backup_server_role_type=backup_server_role_type,
            status=status,
            in_high_availability_cluster=in_high_availability_cluster,
        )

        backup_server.additional_properties = d
        return backup_server

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
