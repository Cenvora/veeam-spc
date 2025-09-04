import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.management_agent_connection_status import ManagementAgentConnectionStatus
from ..models.management_agent_role import ManagementAgentRole
from ..models.management_agent_status import ManagementAgentStatus
from ..models.management_agent_type import ManagementAgentType
from ..models.management_agent_version_status import ManagementAgentVersionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computer_info import ComputerInfo


T = TypeVar("T", bound="ManagementAgent")


@_attrs_define
class ManagementAgent:
    """
    Attributes:
        location_uid (UUID): UID assigned to a location to which a management agent belongs.
        instance_uid (Union[Unset, UUID]): UID assigned to a management agent.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization to which a management agent belongs.
        host_name (Union[None, Unset, str]): Name of a computer on which a management agent is deployed.
        friendly_name (Union[None, Unset, str]): Friendly name of a management agent.
        last_heartbeat_time (Union[Unset, datetime.datetime]): Date and time when a management agent on a computer sent
            the latest heartbeat.
        version (Union[Unset, str]): Version of a management agent deployed on a computer.
        discovery_time (Union[Unset, datetime.datetime]): Date and time when a computer was discovered.
        tag (Union[None, Unset, str]): Additional information.
        status (Union[Unset, ManagementAgentStatus]): Status of a management agent.
        type_ (Union[Unset, ManagementAgentType]): Role of a management agent.
        computer_info (Union[Unset, ComputerInfo]): Information about a computer on which a management agent is
            deployed.
        connection_status (Union[Unset, ManagementAgentConnectionStatus]): Connection status of a management agent.
        is_reboot_required (Union[Unset, bool]): Indicates whether computer reboot is required.
        connection_account (Union[None, UUID, Unset]): Company owner user name that is used to connect a management
            agent to a cloud gateway.
        version_status (Union[Unset, ManagementAgentVersionStatus]): Status of a management agent version.
        role (Union[Unset, ManagementAgentRole]): Role of a management agent.
    """

    location_uid: UUID
    instance_uid: Union[Unset, UUID] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    host_name: Union[None, Unset, str] = UNSET
    friendly_name: Union[None, Unset, str] = UNSET
    last_heartbeat_time: Union[Unset, datetime.datetime] = UNSET
    version: Union[Unset, str] = UNSET
    discovery_time: Union[Unset, datetime.datetime] = UNSET
    tag: Union[None, Unset, str] = UNSET
    status: Union[Unset, ManagementAgentStatus] = UNSET
    type_: Union[Unset, ManagementAgentType] = UNSET
    computer_info: Union[Unset, "ComputerInfo"] = UNSET
    connection_status: Union[Unset, ManagementAgentConnectionStatus] = UNSET
    is_reboot_required: Union[Unset, bool] = UNSET
    connection_account: Union[None, UUID, Unset] = UNSET
    version_status: Union[Unset, ManagementAgentVersionStatus] = UNSET
    role: Union[Unset, ManagementAgentRole] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location_uid = str(self.location_uid)

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        host_name: Union[None, Unset, str]
        if isinstance(self.host_name, Unset):
            host_name = UNSET
        else:
            host_name = self.host_name

        friendly_name: Union[None, Unset, str]
        if isinstance(self.friendly_name, Unset):
            friendly_name = UNSET
        else:
            friendly_name = self.friendly_name

        last_heartbeat_time: Union[Unset, str] = UNSET
        if not isinstance(self.last_heartbeat_time, Unset):
            last_heartbeat_time = self.last_heartbeat_time.isoformat()

        version = self.version

        discovery_time: Union[Unset, str] = UNSET
        if not isinstance(self.discovery_time, Unset):
            discovery_time = self.discovery_time.isoformat()

        tag: Union[None, Unset, str]
        if isinstance(self.tag, Unset):
            tag = UNSET
        else:
            tag = self.tag

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        computer_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.computer_info, Unset):
            computer_info = self.computer_info.to_dict()

        connection_status: Union[Unset, str] = UNSET
        if not isinstance(self.connection_status, Unset):
            connection_status = self.connection_status.value

        is_reboot_required = self.is_reboot_required

        connection_account: Union[None, Unset, str]
        if isinstance(self.connection_account, Unset):
            connection_account = UNSET
        elif isinstance(self.connection_account, UUID):
            connection_account = str(self.connection_account)
        else:
            connection_account = self.connection_account

        version_status: Union[Unset, str] = UNSET
        if not isinstance(self.version_status, Unset):
            version_status = self.version_status.value

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "locationUid": location_uid,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if friendly_name is not UNSET:
            field_dict["friendlyName"] = friendly_name
        if last_heartbeat_time is not UNSET:
            field_dict["lastHeartbeatTime"] = last_heartbeat_time
        if version is not UNSET:
            field_dict["version"] = version
        if discovery_time is not UNSET:
            field_dict["discoveryTime"] = discovery_time
        if tag is not UNSET:
            field_dict["tag"] = tag
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_
        if computer_info is not UNSET:
            field_dict["computerInfo"] = computer_info
        if connection_status is not UNSET:
            field_dict["connectionStatus"] = connection_status
        if is_reboot_required is not UNSET:
            field_dict["isRebootRequired"] = is_reboot_required
        if connection_account is not UNSET:
            field_dict["connectionAccount"] = connection_account
        if version_status is not UNSET:
            field_dict["versionStatus"] = version_status
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.computer_info import ComputerInfo

        d = dict(src_dict)
        location_uid = UUID(d.pop("locationUid"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        def _parse_host_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        host_name = _parse_host_name(d.pop("hostName", UNSET))

        def _parse_friendly_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        friendly_name = _parse_friendly_name(d.pop("friendlyName", UNSET))

        _last_heartbeat_time = d.pop("lastHeartbeatTime", UNSET)
        last_heartbeat_time: Union[Unset, datetime.datetime]
        if isinstance(_last_heartbeat_time, Unset):
            last_heartbeat_time = UNSET
        else:
            last_heartbeat_time = isoparse(_last_heartbeat_time)

        version = d.pop("version", UNSET)

        _discovery_time = d.pop("discoveryTime", UNSET)
        discovery_time: Union[Unset, datetime.datetime]
        if isinstance(_discovery_time, Unset):
            discovery_time = UNSET
        else:
            discovery_time = isoparse(_discovery_time)

        def _parse_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tag = _parse_tag(d.pop("tag", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, ManagementAgentStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ManagementAgentStatus(_status)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ManagementAgentType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ManagementAgentType(_type_)

        _computer_info = d.pop("computerInfo", UNSET)
        computer_info: Union[Unset, ComputerInfo]
        if isinstance(_computer_info, Unset):
            computer_info = UNSET
        else:
            computer_info = ComputerInfo.from_dict(_computer_info)

        _connection_status = d.pop("connectionStatus", UNSET)
        connection_status: Union[Unset, ManagementAgentConnectionStatus]
        if isinstance(_connection_status, Unset):
            connection_status = UNSET
        else:
            connection_status = ManagementAgentConnectionStatus(_connection_status)

        is_reboot_required = d.pop("isRebootRequired", UNSET)

        def _parse_connection_account(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                connection_account_type_0 = UUID(data)

                return connection_account_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        connection_account = _parse_connection_account(d.pop("connectionAccount", UNSET))

        _version_status = d.pop("versionStatus", UNSET)
        version_status: Union[Unset, ManagementAgentVersionStatus]
        if isinstance(_version_status, Unset):
            version_status = UNSET
        else:
            version_status = ManagementAgentVersionStatus(_version_status)

        _role = d.pop("role", UNSET)
        role: Union[Unset, ManagementAgentRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = ManagementAgentRole(_role)

        management_agent = cls(
            location_uid=location_uid,
            instance_uid=instance_uid,
            organization_uid=organization_uid,
            host_name=host_name,
            friendly_name=friendly_name,
            last_heartbeat_time=last_heartbeat_time,
            version=version,
            discovery_time=discovery_time,
            tag=tag,
            status=status,
            type_=type_,
            computer_info=computer_info,
            connection_status=connection_status,
            is_reboot_required=is_reboot_required,
            connection_account=connection_account,
            version_status=version_status,
            role=role,
        )

        management_agent.additional_properties = d
        return management_agent

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
