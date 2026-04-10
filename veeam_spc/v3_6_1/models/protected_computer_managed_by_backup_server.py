import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.malware_state import MalwareState
from ..models.protected_computer_managed_by_backup_server_operation_mode import (
    ProtectedComputerManagedByBackupServerOperationMode,
)
from ..models.protected_computer_managed_by_backup_server_platform_type import (
    ProtectedComputerManagedByBackupServerPlatformType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedComputerManagedByBackupServer")


@_attrs_define
class ProtectedComputerManagedByBackupServer:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a protected computer.
        source_instance_uid (Union[Unset, UUID]): Protected computer UID assigned in Veeam Backup & Replication.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a backup server.
        protection_groups (Union[Unset, list[UUID]]): Protection group UIDs.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization.
        name (Union[Unset, str]): Hostname of a protected computer.
        ip_addresses (Union[Unset, list[str]]): Computer IP addresses.
        guest_os (Union[Unset, str]): Operating system installed on a protected computer.
        platform_type (Union[Unset, ProtectedComputerManagedByBackupServerPlatformType]): Platform type of a protected
            computer.
        operation_mode (Union[Unset, ProtectedComputerManagedByBackupServerOperationMode]): Operation mode.
        latest_restore_point_date (Union[None, Unset, datetime.datetime]): Date and time of the latest restore point
            creation.
        malware_state (Union[Unset, MalwareState]): Malware status.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    source_instance_uid: Union[Unset, UUID] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    protection_groups: Union[Unset, list[UUID]] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    ip_addresses: Union[Unset, list[str]] = UNSET
    guest_os: Union[Unset, str] = UNSET
    platform_type: Union[Unset, ProtectedComputerManagedByBackupServerPlatformType] = UNSET
    operation_mode: Union[Unset, ProtectedComputerManagedByBackupServerOperationMode] = UNSET
    latest_restore_point_date: Union[None, Unset, datetime.datetime] = UNSET
    malware_state: Union[Unset, MalwareState] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        source_instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.source_instance_uid, Unset):
            source_instance_uid = str(self.source_instance_uid)

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        protection_groups: Union[Unset, list[str]] = UNSET
        if not isinstance(self.protection_groups, Unset):
            protection_groups = []
            for protection_groups_item_data in self.protection_groups:
                protection_groups_item = str(protection_groups_item_data)
                protection_groups.append(protection_groups_item)

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        name = self.name

        ip_addresses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ip_addresses, Unset):
            ip_addresses = self.ip_addresses

        guest_os = self.guest_os

        platform_type: Union[Unset, str] = UNSET
        if not isinstance(self.platform_type, Unset):
            platform_type = self.platform_type.value

        operation_mode: Union[Unset, str] = UNSET
        if not isinstance(self.operation_mode, Unset):
            operation_mode = self.operation_mode.value

        latest_restore_point_date: Union[None, Unset, str]
        if isinstance(self.latest_restore_point_date, Unset):
            latest_restore_point_date = UNSET
        elif isinstance(self.latest_restore_point_date, datetime.datetime):
            latest_restore_point_date = self.latest_restore_point_date.isoformat()
        else:
            latest_restore_point_date = self.latest_restore_point_date

        malware_state: Union[Unset, str] = UNSET
        if not isinstance(self.malware_state, Unset):
            malware_state = self.malware_state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if source_instance_uid is not UNSET:
            field_dict["sourceInstanceUid"] = source_instance_uid
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if protection_groups is not UNSET:
            field_dict["protectionGroups"] = protection_groups
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if name is not UNSET:
            field_dict["name"] = name
        if ip_addresses is not UNSET:
            field_dict["ipAddresses"] = ip_addresses
        if guest_os is not UNSET:
            field_dict["guestOs"] = guest_os
        if platform_type is not UNSET:
            field_dict["platformType"] = platform_type
        if operation_mode is not UNSET:
            field_dict["operationMode"] = operation_mode
        if latest_restore_point_date is not UNSET:
            field_dict["latestRestorePointDate"] = latest_restore_point_date
        if malware_state is not UNSET:
            field_dict["malwareState"] = malware_state

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

        _source_instance_uid = d.pop("sourceInstanceUid", UNSET)
        source_instance_uid: Union[Unset, UUID]
        if isinstance(_source_instance_uid, Unset):
            source_instance_uid = UNSET
        else:
            source_instance_uid = UUID(_source_instance_uid)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: Union[Unset, UUID]
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        protection_groups = []
        _protection_groups = d.pop("protectionGroups", UNSET)
        for protection_groups_item_data in _protection_groups or []:
            protection_groups_item = UUID(protection_groups_item_data)

            protection_groups.append(protection_groups_item)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        name = d.pop("name", UNSET)

        ip_addresses = cast(list[str], d.pop("ipAddresses", UNSET))

        guest_os = d.pop("guestOs", UNSET)

        _platform_type = d.pop("platformType", UNSET)
        platform_type: Union[Unset, ProtectedComputerManagedByBackupServerPlatformType]
        if isinstance(_platform_type, Unset):
            platform_type = UNSET
        else:
            platform_type = ProtectedComputerManagedByBackupServerPlatformType(_platform_type)

        _operation_mode = d.pop("operationMode", UNSET)
        operation_mode: Union[Unset, ProtectedComputerManagedByBackupServerOperationMode]
        if isinstance(_operation_mode, Unset):
            operation_mode = UNSET
        else:
            operation_mode = ProtectedComputerManagedByBackupServerOperationMode(_operation_mode)

        def _parse_latest_restore_point_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                latest_restore_point_date_type_0 = isoparse(data)

                return latest_restore_point_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        latest_restore_point_date = _parse_latest_restore_point_date(d.pop("latestRestorePointDate", UNSET))

        _malware_state = d.pop("malwareState", UNSET)
        malware_state: Union[Unset, MalwareState]
        if isinstance(_malware_state, Unset):
            malware_state = UNSET
        else:
            malware_state = MalwareState(_malware_state)

        protected_computer_managed_by_backup_server = cls(
            instance_uid=instance_uid,
            source_instance_uid=source_instance_uid,
            backup_server_uid=backup_server_uid,
            protection_groups=protection_groups,
            organization_uid=organization_uid,
            name=name,
            ip_addresses=ip_addresses,
            guest_os=guest_os,
            platform_type=platform_type,
            operation_mode=operation_mode,
            latest_restore_point_date=latest_restore_point_date,
            malware_state=malware_state,
        )

        protected_computer_managed_by_backup_server.additional_properties = d
        return protected_computer_managed_by_backup_server

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
