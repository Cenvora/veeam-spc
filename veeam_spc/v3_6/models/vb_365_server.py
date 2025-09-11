from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.management_agent_status import ManagementAgentStatus
from ..models.vb_365_server_server_api_version import Vb365ServerServerApiVersion
from ..models.vb_365_server_status import Vb365ServerStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365Server")


@_attrs_define
class Vb365Server:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup for Microsoft 365 server.
        location_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup for Microsoft 365 server location.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization.
        management_agent_uid (Union[Unset, UUID]): UID assigned to a management agent installed on a Veeam Backup for
            Microsoft 365 Server.
        installation_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup for Microsoft 365 server installation.
        name (Union[Unset, str]): Host name of a Veeam Backup for Microsoft 365 server.
        version (Union[Unset, str]): Version of Veeam Backup for Microsoft 365 installed on a server.
        major_version (Union[Unset, int]): Major version of Veeam Backup for Microsoft 365 installed on a server.
        server_api_version (Union[Unset, Vb365ServerServerApiVersion]): Version of Veeam Backup for Microsoft 365 server
            API.
        status (Union[Unset, Vb365ServerStatus]): Veeam Backup for Microsoft 365 server status.
        management_agent_status (Union[Unset, ManagementAgentStatus]): Status of a management agent.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    location_uid: Union[Unset, UUID] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    management_agent_uid: Union[Unset, UUID] = UNSET
    installation_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    major_version: Union[Unset, int] = UNSET
    server_api_version: Union[Unset, Vb365ServerServerApiVersion] = UNSET
    status: Union[Unset, Vb365ServerStatus] = UNSET
    management_agent_status: Union[Unset, ManagementAgentStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        location_uid: Union[Unset, str] = UNSET
        if not isinstance(self.location_uid, Unset):
            location_uid = str(self.location_uid)

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        management_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.management_agent_uid, Unset):
            management_agent_uid = str(self.management_agent_uid)

        installation_uid: Union[Unset, str] = UNSET
        if not isinstance(self.installation_uid, Unset):
            installation_uid = str(self.installation_uid)

        name = self.name

        version = self.version

        major_version = self.major_version

        server_api_version: Union[Unset, str] = UNSET
        if not isinstance(self.server_api_version, Unset):
            server_api_version = self.server_api_version.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        management_agent_status: Union[Unset, str] = UNSET
        if not isinstance(self.management_agent_status, Unset):
            management_agent_status = self.management_agent_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if location_uid is not UNSET:
            field_dict["locationUid"] = location_uid
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if management_agent_uid is not UNSET:
            field_dict["managementAgentUid"] = management_agent_uid
        if installation_uid is not UNSET:
            field_dict["installationUid"] = installation_uid
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version
        if major_version is not UNSET:
            field_dict["majorVersion"] = major_version
        if server_api_version is not UNSET:
            field_dict["serverApiVersion"] = server_api_version
        if status is not UNSET:
            field_dict["status"] = status
        if management_agent_status is not UNSET:
            field_dict["managementAgentStatus"] = management_agent_status

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

        _location_uid = d.pop("locationUid", UNSET)
        location_uid: Union[Unset, UUID]
        if isinstance(_location_uid, Unset):
            location_uid = UNSET
        else:
            location_uid = UUID(_location_uid)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        _management_agent_uid = d.pop("managementAgentUid", UNSET)
        management_agent_uid: Union[Unset, UUID]
        if isinstance(_management_agent_uid, Unset):
            management_agent_uid = UNSET
        else:
            management_agent_uid = UUID(_management_agent_uid)

        _installation_uid = d.pop("installationUid", UNSET)
        installation_uid: Union[Unset, UUID]
        if isinstance(_installation_uid, Unset):
            installation_uid = UNSET
        else:
            installation_uid = UUID(_installation_uid)

        name = d.pop("name", UNSET)

        version = d.pop("version", UNSET)

        major_version = d.pop("majorVersion", UNSET)

        _server_api_version = d.pop("serverApiVersion", UNSET)
        server_api_version: Union[Unset, Vb365ServerServerApiVersion]
        if isinstance(_server_api_version, Unset):
            server_api_version = UNSET
        else:
            server_api_version = Vb365ServerServerApiVersion(_server_api_version)

        _status = d.pop("status", UNSET)
        status: Union[Unset, Vb365ServerStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = Vb365ServerStatus(_status)

        _management_agent_status = d.pop("managementAgentStatus", UNSET)
        management_agent_status: Union[Unset, ManagementAgentStatus]
        if isinstance(_management_agent_status, Unset):
            management_agent_status = UNSET
        else:
            management_agent_status = ManagementAgentStatus(_management_agent_status)

        vb_365_server = cls(
            instance_uid=instance_uid,
            location_uid=location_uid,
            organization_uid=organization_uid,
            management_agent_uid=management_agent_uid,
            installation_uid=installation_uid,
            name=name,
            version=version,
            major_version=major_version,
            server_api_version=server_api_version,
            status=status,
            management_agent_status=management_agent_status,
        )

        vb_365_server.additional_properties = d
        return vb_365_server

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
