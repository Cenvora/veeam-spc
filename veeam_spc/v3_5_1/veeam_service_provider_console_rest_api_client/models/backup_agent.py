import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.backup_agent_agent_platform import BackupAgentAgentPlatform
from ..models.backup_agent_gui_mode import BackupAgentGuiMode
from ..models.backup_agent_installation_type import BackupAgentInstallationType
from ..models.backup_agent_management_agent_status import BackupAgentManagementAgentStatus
from ..models.backup_agent_management_mode import BackupAgentManagementMode
from ..models.backup_agent_operation_mode import BackupAgentOperationMode
from ..models.backup_agent_platform import BackupAgentPlatform
from ..models.backup_agent_status import BackupAgentStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupAgent")


@_attrs_define
class BackupAgent:
    """
    Example:
        {'managementAgentUid': 'BB111975-B409-49B5-8ECE-FFFECB13494F', 'name': 'VAW AgentX', 'operationMode': 'Server',
            'guiMode': 'ReadOnly', 'platform': 'Cloud'}

    Attributes:
        gui_mode (BackupAgentGuiMode): Indicates the UI access mode for the Veeam backup agent.
        instance_uid (Union[Unset, UUID]): UID assigned to a Veeam backup agent.
        agent_platform (Union[Unset, BackupAgentAgentPlatform]): Name of a platform on which Veeam backup agent is
            deployed.
        status (Union[Unset, BackupAgentStatus]): Status of a Veeam backup agent.
        management_agent_status (Union[Unset, BackupAgentManagementAgentStatus]): Status of a management agent.
        management_agent_uid (Union[Unset, UUID]): UID assigned to a management agent that is deployed along with Veeam
            backup agent.
        site_uid (Union[None, UUID, Unset]): UID assigned to a Veeam Cloud Connect site on which an organization that
            owns Veeam backup agents is registered.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization to which Veeam backup agents belong.
        name (Union[Unset, str]): Name of a managed computer on which Veeam backup agent is deployed.
        operation_mode (Union[Unset, BackupAgentOperationMode]): Backup job operation mode.
        platform (Union[Unset, BackupAgentPlatform]): Computer platform on which Veeam backup agent is deployed.
        version (Union[Unset, str]): Version of Veeam backup agent deployed on a managed computer.
        activation_time (Union[None, Unset, datetime.datetime]): Date and time when Veeam backup agent was activated.
        management_mode (Union[Unset, BackupAgentManagementMode]): Management mode of Veeam backup agent.
            > You can change management mode to `ManagedByConsole` or `UnManaged` using the PATCH endpoint.
        installation_type (Union[Unset, BackupAgentInstallationType]): Type of Veeam backup agent installation
            procedure.
        total_jobs_count (Union[Unset, int]): Number of all jobs.
        running_jobs_count (Union[Unset, int]): Number of running jobs.
        success_jobs_count (Union[Unset, int]): Number of successful jobs.
    """

    gui_mode: BackupAgentGuiMode
    instance_uid: Union[Unset, UUID] = UNSET
    agent_platform: Union[Unset, BackupAgentAgentPlatform] = UNSET
    status: Union[Unset, BackupAgentStatus] = UNSET
    management_agent_status: Union[Unset, BackupAgentManagementAgentStatus] = UNSET
    management_agent_uid: Union[Unset, UUID] = UNSET
    site_uid: Union[None, UUID, Unset] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    operation_mode: Union[Unset, BackupAgentOperationMode] = UNSET
    platform: Union[Unset, BackupAgentPlatform] = UNSET
    version: Union[Unset, str] = UNSET
    activation_time: Union[None, Unset, datetime.datetime] = UNSET
    management_mode: Union[Unset, BackupAgentManagementMode] = UNSET
    installation_type: Union[Unset, BackupAgentInstallationType] = UNSET
    total_jobs_count: Union[Unset, int] = UNSET
    running_jobs_count: Union[Unset, int] = UNSET
    success_jobs_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gui_mode = self.gui_mode.value

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        agent_platform: Union[Unset, str] = UNSET
        if not isinstance(self.agent_platform, Unset):
            agent_platform = self.agent_platform.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        management_agent_status: Union[Unset, str] = UNSET
        if not isinstance(self.management_agent_status, Unset):
            management_agent_status = self.management_agent_status.value

        management_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.management_agent_uid, Unset):
            management_agent_uid = str(self.management_agent_uid)

        site_uid: Union[None, Unset, str]
        if isinstance(self.site_uid, Unset):
            site_uid = UNSET
        elif isinstance(self.site_uid, UUID):
            site_uid = str(self.site_uid)
        else:
            site_uid = self.site_uid

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        name = self.name

        operation_mode: Union[Unset, str] = UNSET
        if not isinstance(self.operation_mode, Unset):
            operation_mode = self.operation_mode.value

        platform: Union[Unset, str] = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        version = self.version

        activation_time: Union[None, Unset, str]
        if isinstance(self.activation_time, Unset):
            activation_time = UNSET
        elif isinstance(self.activation_time, datetime.datetime):
            activation_time = self.activation_time.isoformat()
        else:
            activation_time = self.activation_time

        management_mode: Union[Unset, str] = UNSET
        if not isinstance(self.management_mode, Unset):
            management_mode = self.management_mode.value

        installation_type: Union[Unset, str] = UNSET
        if not isinstance(self.installation_type, Unset):
            installation_type = self.installation_type.value

        total_jobs_count = self.total_jobs_count

        running_jobs_count = self.running_jobs_count

        success_jobs_count = self.success_jobs_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "guiMode": gui_mode,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if agent_platform is not UNSET:
            field_dict["agentPlatform"] = agent_platform
        if status is not UNSET:
            field_dict["status"] = status
        if management_agent_status is not UNSET:
            field_dict["managementAgentStatus"] = management_agent_status
        if management_agent_uid is not UNSET:
            field_dict["managementAgentUid"] = management_agent_uid
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if name is not UNSET:
            field_dict["name"] = name
        if operation_mode is not UNSET:
            field_dict["operationMode"] = operation_mode
        if platform is not UNSET:
            field_dict["platform"] = platform
        if version is not UNSET:
            field_dict["version"] = version
        if activation_time is not UNSET:
            field_dict["activationTime"] = activation_time
        if management_mode is not UNSET:
            field_dict["managementMode"] = management_mode
        if installation_type is not UNSET:
            field_dict["installationType"] = installation_type
        if total_jobs_count is not UNSET:
            field_dict["totalJobsCount"] = total_jobs_count
        if running_jobs_count is not UNSET:
            field_dict["runningJobsCount"] = running_jobs_count
        if success_jobs_count is not UNSET:
            field_dict["successJobsCount"] = success_jobs_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gui_mode = BackupAgentGuiMode(d.pop("guiMode"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _agent_platform = d.pop("agentPlatform", UNSET)
        agent_platform: Union[Unset, BackupAgentAgentPlatform]
        if isinstance(_agent_platform, Unset):
            agent_platform = UNSET
        else:
            agent_platform = BackupAgentAgentPlatform(_agent_platform)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BackupAgentStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BackupAgentStatus(_status)

        _management_agent_status = d.pop("managementAgentStatus", UNSET)
        management_agent_status: Union[Unset, BackupAgentManagementAgentStatus]
        if isinstance(_management_agent_status, Unset):
            management_agent_status = UNSET
        else:
            management_agent_status = BackupAgentManagementAgentStatus(_management_agent_status)

        _management_agent_uid = d.pop("managementAgentUid", UNSET)
        management_agent_uid: Union[Unset, UUID]
        if isinstance(_management_agent_uid, Unset):
            management_agent_uid = UNSET
        else:
            management_agent_uid = UUID(_management_agent_uid)

        def _parse_site_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                site_uid_type_0 = UUID(data)

                return site_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        site_uid = _parse_site_uid(d.pop("siteUid", UNSET))

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        name = d.pop("name", UNSET)

        _operation_mode = d.pop("operationMode", UNSET)
        operation_mode: Union[Unset, BackupAgentOperationMode]
        if isinstance(_operation_mode, Unset):
            operation_mode = UNSET
        else:
            operation_mode = BackupAgentOperationMode(_operation_mode)

        _platform = d.pop("platform", UNSET)
        platform: Union[Unset, BackupAgentPlatform]
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = BackupAgentPlatform(_platform)

        version = d.pop("version", UNSET)

        def _parse_activation_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                activation_time_type_0 = isoparse(data)

                return activation_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        activation_time = _parse_activation_time(d.pop("activationTime", UNSET))

        _management_mode = d.pop("managementMode", UNSET)
        management_mode: Union[Unset, BackupAgentManagementMode]
        if isinstance(_management_mode, Unset):
            management_mode = UNSET
        else:
            management_mode = BackupAgentManagementMode(_management_mode)

        _installation_type = d.pop("installationType", UNSET)
        installation_type: Union[Unset, BackupAgentInstallationType]
        if isinstance(_installation_type, Unset):
            installation_type = UNSET
        else:
            installation_type = BackupAgentInstallationType(_installation_type)

        total_jobs_count = d.pop("totalJobsCount", UNSET)

        running_jobs_count = d.pop("runningJobsCount", UNSET)

        success_jobs_count = d.pop("successJobsCount", UNSET)

        backup_agent = cls(
            gui_mode=gui_mode,
            instance_uid=instance_uid,
            agent_platform=agent_platform,
            status=status,
            management_agent_status=management_agent_status,
            management_agent_uid=management_agent_uid,
            site_uid=site_uid,
            organization_uid=organization_uid,
            name=name,
            operation_mode=operation_mode,
            platform=platform,
            version=version,
            activation_time=activation_time,
            management_mode=management_mode,
            installation_type=installation_type,
            total_jobs_count=total_jobs_count,
            running_jobs_count=running_jobs_count,
            success_jobs_count=success_jobs_count,
        )

        backup_agent.additional_properties = d
        return backup_agent

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
