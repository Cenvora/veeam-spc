import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.discovered_computer_backup_agent_installation_status import (
    DiscoveredComputerBackupAgentInstallationStatus,
)
from ..models.discovered_computer_backup_agent_management_status import DiscoveredComputerBackupAgentManagementStatus
from ..models.discovered_computer_status import DiscoveredComputerStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.computer_info import ComputerInfo


T = TypeVar("T", bound="DiscoveredComputer")


@_attrs_define
class DiscoveredComputer:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a discovered computer.
        rule_uid (Union[Unset, UUID]): UID assigned to a rule used to discover a computer.
        management_agent_uid (Union[Unset, UUID]): UID assigned to a management agent installed on a discovered
            computer.
        discovered_time (Union[Unset, datetime.datetime]): Date and time when a computer was discovered.
        backup_agent_installation_status (Union[Unset, DiscoveredComputerBackupAgentInstallationStatus]): Status of
            Veeam backup agent installation on a discovered computer.
        status (Union[Unset, DiscoveredComputerStatus]): Computer connection status.
            > If management agent is not installed on the computer, the connection status does not change after discovery.'
        backup_agent_version (Union[Unset, str]): Veeam backup agent version.
        backup_agent_management_status (Union[Unset, DiscoveredComputerBackupAgentManagementStatus]): Veeam backup agent
            management status.
        info (Union[Unset, ComputerInfo]): Information about a computer on which a management agent is deployed.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    rule_uid: Union[Unset, UUID] = UNSET
    management_agent_uid: Union[Unset, UUID] = UNSET
    discovered_time: Union[Unset, datetime.datetime] = UNSET
    backup_agent_installation_status: Union[Unset, DiscoveredComputerBackupAgentInstallationStatus] = UNSET
    status: Union[Unset, DiscoveredComputerStatus] = UNSET
    backup_agent_version: Union[Unset, str] = UNSET
    backup_agent_management_status: Union[Unset, DiscoveredComputerBackupAgentManagementStatus] = UNSET
    info: Union[Unset, "ComputerInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        rule_uid: Union[Unset, str] = UNSET
        if not isinstance(self.rule_uid, Unset):
            rule_uid = str(self.rule_uid)

        management_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.management_agent_uid, Unset):
            management_agent_uid = str(self.management_agent_uid)

        discovered_time: Union[Unset, str] = UNSET
        if not isinstance(self.discovered_time, Unset):
            discovered_time = self.discovered_time.isoformat()

        backup_agent_installation_status: Union[Unset, str] = UNSET
        if not isinstance(self.backup_agent_installation_status, Unset):
            backup_agent_installation_status = self.backup_agent_installation_status.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        backup_agent_version = self.backup_agent_version

        backup_agent_management_status: Union[Unset, str] = UNSET
        if not isinstance(self.backup_agent_management_status, Unset):
            backup_agent_management_status = self.backup_agent_management_status.value

        info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.info, Unset):
            info = self.info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if rule_uid is not UNSET:
            field_dict["ruleUid"] = rule_uid
        if management_agent_uid is not UNSET:
            field_dict["managementAgentUid"] = management_agent_uid
        if discovered_time is not UNSET:
            field_dict["discoveredTime"] = discovered_time
        if backup_agent_installation_status is not UNSET:
            field_dict["backupAgentInstallationStatus"] = backup_agent_installation_status
        if status is not UNSET:
            field_dict["status"] = status
        if backup_agent_version is not UNSET:
            field_dict["backupAgentVersion"] = backup_agent_version
        if backup_agent_management_status is not UNSET:
            field_dict["backupAgentManagementStatus"] = backup_agent_management_status
        if info is not UNSET:
            field_dict["info"] = info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.computer_info import ComputerInfo

        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _rule_uid = d.pop("ruleUid", UNSET)
        rule_uid: Union[Unset, UUID]
        if isinstance(_rule_uid, Unset):
            rule_uid = UNSET
        else:
            rule_uid = UUID(_rule_uid)

        _management_agent_uid = d.pop("managementAgentUid", UNSET)
        management_agent_uid: Union[Unset, UUID]
        if isinstance(_management_agent_uid, Unset):
            management_agent_uid = UNSET
        else:
            management_agent_uid = UUID(_management_agent_uid)

        _discovered_time = d.pop("discoveredTime", UNSET)
        discovered_time: Union[Unset, datetime.datetime]
        if isinstance(_discovered_time, Unset):
            discovered_time = UNSET
        else:
            discovered_time = isoparse(_discovered_time)

        _backup_agent_installation_status = d.pop("backupAgentInstallationStatus", UNSET)
        backup_agent_installation_status: Union[Unset, DiscoveredComputerBackupAgentInstallationStatus]
        if isinstance(_backup_agent_installation_status, Unset):
            backup_agent_installation_status = UNSET
        else:
            backup_agent_installation_status = DiscoveredComputerBackupAgentInstallationStatus(
                _backup_agent_installation_status
            )

        _status = d.pop("status", UNSET)
        status: Union[Unset, DiscoveredComputerStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DiscoveredComputerStatus(_status)

        backup_agent_version = d.pop("backupAgentVersion", UNSET)

        _backup_agent_management_status = d.pop("backupAgentManagementStatus", UNSET)
        backup_agent_management_status: Union[Unset, DiscoveredComputerBackupAgentManagementStatus]
        if isinstance(_backup_agent_management_status, Unset):
            backup_agent_management_status = UNSET
        else:
            backup_agent_management_status = DiscoveredComputerBackupAgentManagementStatus(
                _backup_agent_management_status
            )

        _info = d.pop("info", UNSET)
        info: Union[Unset, ComputerInfo]
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = ComputerInfo.from_dict(_info)

        discovered_computer = cls(
            instance_uid=instance_uid,
            rule_uid=rule_uid,
            management_agent_uid=management_agent_uid,
            discovered_time=discovered_time,
            backup_agent_installation_status=backup_agent_installation_status,
            status=status,
            backup_agent_version=backup_agent_version,
            backup_agent_management_status=backup_agent_management_status,
            info=info,
        )

        discovered_computer.additional_properties = d
        return discovered_computer

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
