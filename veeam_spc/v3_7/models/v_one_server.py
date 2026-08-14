from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.management_agent_status import ManagementAgentStatus
from ..models.v_one_server_alarms_synchronization_status import VOneServerAlarmsSynchronizationStatus
from ..models.v_one_server_status import VOneServerStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="VOneServer")


@_attrs_define
class VOneServer:
    """
    Attributes:
        instance_uid (UUID | Unset): UID assigned to a Veeam ONE server.
        location_uid (UUID | Unset): UID assigned to a Veeam ONE server location.
        organization_uid (UUID | Unset): UID assigned to an organization.
        management_agent_uid (UUID | Unset): UID assigned to a management agent installed on a Veeam ONE server.
        installation_uid (UUID | Unset): UID assigned to a Veeam ONE installation.
        name (str | Unset): Host name of a Veeam ONE server.
        version (str | Unset): Veeam ONE version installed on a server.
        status (VOneServerStatus | Unset): Veeam ONE server status.
        management_agent_status (ManagementAgentStatus | Unset): Status of a management agent.
        alarms_synchronization_status (VOneServerAlarmsSynchronizationStatus | Unset): Veeam ONE server alarm
            synchronization status.
    """

    instance_uid: UUID | Unset = UNSET
    location_uid: UUID | Unset = UNSET
    organization_uid: UUID | Unset = UNSET
    management_agent_uid: UUID | Unset = UNSET
    installation_uid: UUID | Unset = UNSET
    name: str | Unset = UNSET
    version: str | Unset = UNSET
    status: VOneServerStatus | Unset = UNSET
    management_agent_status: ManagementAgentStatus | Unset = UNSET
    alarms_synchronization_status: VOneServerAlarmsSynchronizationStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        location_uid: str | Unset = UNSET
        if not isinstance(self.location_uid, Unset):
            location_uid = str(self.location_uid)

        organization_uid: str | Unset = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        management_agent_uid: str | Unset = UNSET
        if not isinstance(self.management_agent_uid, Unset):
            management_agent_uid = str(self.management_agent_uid)

        installation_uid: str | Unset = UNSET
        if not isinstance(self.installation_uid, Unset):
            installation_uid = str(self.installation_uid)

        name = self.name

        version = self.version

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        management_agent_status: str | Unset = UNSET
        if not isinstance(self.management_agent_status, Unset):
            management_agent_status = self.management_agent_status.value

        alarms_synchronization_status: str | Unset = UNSET
        if not isinstance(self.alarms_synchronization_status, Unset):
            alarms_synchronization_status = self.alarms_synchronization_status.value

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
        if status is not UNSET:
            field_dict["status"] = status
        if management_agent_status is not UNSET:
            field_dict["managementAgentStatus"] = management_agent_status
        if alarms_synchronization_status is not UNSET:
            field_dict["alarmsSynchronizationStatus"] = alarms_synchronization_status

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

        _location_uid = d.pop("locationUid", UNSET)
        location_uid: UUID | Unset
        if isinstance(_location_uid, Unset):
            location_uid = UNSET
        else:
            location_uid = UUID(_location_uid)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: UUID | Unset
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        _management_agent_uid = d.pop("managementAgentUid", UNSET)
        management_agent_uid: UUID | Unset
        if isinstance(_management_agent_uid, Unset):
            management_agent_uid = UNSET
        else:
            management_agent_uid = UUID(_management_agent_uid)

        _installation_uid = d.pop("installationUid", UNSET)
        installation_uid: UUID | Unset
        if isinstance(_installation_uid, Unset):
            installation_uid = UNSET
        else:
            installation_uid = UUID(_installation_uid)

        name = d.pop("name", UNSET)

        version = d.pop("version", UNSET)

        _status = d.pop("status", UNSET)
        status: VOneServerStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = VOneServerStatus(_status)

        _management_agent_status = d.pop("managementAgentStatus", UNSET)
        management_agent_status: ManagementAgentStatus | Unset
        if isinstance(_management_agent_status, Unset):
            management_agent_status = UNSET
        else:
            management_agent_status = ManagementAgentStatus(_management_agent_status)

        _alarms_synchronization_status = d.pop("alarmsSynchronizationStatus", UNSET)
        alarms_synchronization_status: VOneServerAlarmsSynchronizationStatus | Unset
        if isinstance(_alarms_synchronization_status, Unset):
            alarms_synchronization_status = UNSET
        else:
            alarms_synchronization_status = VOneServerAlarmsSynchronizationStatus(_alarms_synchronization_status)

        v_one_server = cls(
            instance_uid=instance_uid,
            location_uid=location_uid,
            organization_uid=organization_uid,
            management_agent_uid=management_agent_uid,
            installation_uid=installation_uid,
            name=name,
            version=version,
            status=status,
            management_agent_status=management_agent_status,
            alarms_synchronization_status=alarms_synchronization_status,
        )

        v_one_server.additional_properties = d
        return v_one_server

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
