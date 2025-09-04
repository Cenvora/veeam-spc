from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_agent_installation_status import BackupServerAgentInstallationStatus
from ..models.backup_server_agent_license import BackupServerAgentLicense
from ..models.backup_server_agent_license_status import BackupServerAgentLicenseStatus
from ..models.backup_server_agent_os_type import BackupServerAgentOsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerAgent")


@_attrs_define
class BackupServerAgent:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a Veeam backup agent.
        name (Union[Unset, str]): Name of a Veeam backup agent.
        machine_name (Union[Unset, str]): DNS name of a machine on which a Veeam backup agent is installed.
        guest_os (Union[Unset, str]): Operating system installed on a computer.
        version (Union[Unset, str]): Version of a Veeam backup agent.
        bios_uid (Union[Unset, UUID]): UUID in Win32_ComputerSystem WMI class.
        ip_addresses (Union[Unset, list[str]]): Computer IP addresses.
        protection_groups (Union[Unset, list[UUID]]): Protection group UIDs.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup & Replication server that manages a Veeam
            backup agent.
        is_unmanaged (Union[Unset, bool]): Indicates whether a Veeam backup agent is unmanaged.
        installation_status (Union[Unset, BackupServerAgentInstallationStatus]): Status of Veeam backup agent
            installation.
        license_ (Union[Unset, BackupServerAgentLicense]): Type of a Veeam backup agent license.
        license_status (Union[Unset, BackupServerAgentLicenseStatus]): Status of a Veeam backup agent license.
        os_type (Union[Unset, BackupServerAgentOsType]): Type of a Veeam backup agent operating system.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    machine_name: Union[Unset, str] = UNSET
    guest_os: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    bios_uid: Union[Unset, UUID] = UNSET
    ip_addresses: Union[Unset, list[str]] = UNSET
    protection_groups: Union[Unset, list[UUID]] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    is_unmanaged: Union[Unset, bool] = UNSET
    installation_status: Union[Unset, BackupServerAgentInstallationStatus] = UNSET
    license_: Union[Unset, BackupServerAgentLicense] = UNSET
    license_status: Union[Unset, BackupServerAgentLicenseStatus] = UNSET
    os_type: Union[Unset, BackupServerAgentOsType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        machine_name = self.machine_name

        guest_os = self.guest_os

        version = self.version

        bios_uid: Union[Unset, str] = UNSET
        if not isinstance(self.bios_uid, Unset):
            bios_uid = str(self.bios_uid)

        ip_addresses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ip_addresses, Unset):
            ip_addresses = self.ip_addresses

        protection_groups: Union[Unset, list[str]] = UNSET
        if not isinstance(self.protection_groups, Unset):
            protection_groups = []
            for protection_groups_item_data in self.protection_groups:
                protection_groups_item = str(protection_groups_item_data)
                protection_groups.append(protection_groups_item)

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        is_unmanaged = self.is_unmanaged

        installation_status: Union[Unset, str] = UNSET
        if not isinstance(self.installation_status, Unset):
            installation_status = self.installation_status.value

        license_: Union[Unset, str] = UNSET
        if not isinstance(self.license_, Unset):
            license_ = self.license_.value

        license_status: Union[Unset, str] = UNSET
        if not isinstance(self.license_status, Unset):
            license_status = self.license_status.value

        os_type: Union[Unset, str] = UNSET
        if not isinstance(self.os_type, Unset):
            os_type = self.os_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if name is not UNSET:
            field_dict["name"] = name
        if machine_name is not UNSET:
            field_dict["machineName"] = machine_name
        if guest_os is not UNSET:
            field_dict["guestOs"] = guest_os
        if version is not UNSET:
            field_dict["version"] = version
        if bios_uid is not UNSET:
            field_dict["biosUid"] = bios_uid
        if ip_addresses is not UNSET:
            field_dict["ipAddresses"] = ip_addresses
        if protection_groups is not UNSET:
            field_dict["protectionGroups"] = protection_groups
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if is_unmanaged is not UNSET:
            field_dict["isUnmanaged"] = is_unmanaged
        if installation_status is not UNSET:
            field_dict["installationStatus"] = installation_status
        if license_ is not UNSET:
            field_dict["license"] = license_
        if license_status is not UNSET:
            field_dict["licenseStatus"] = license_status
        if os_type is not UNSET:
            field_dict["osType"] = os_type

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

        machine_name = d.pop("machineName", UNSET)

        guest_os = d.pop("guestOs", UNSET)

        version = d.pop("version", UNSET)

        _bios_uid = d.pop("biosUid", UNSET)
        bios_uid: Union[Unset, UUID]
        if isinstance(_bios_uid, Unset):
            bios_uid = UNSET
        else:
            bios_uid = UUID(_bios_uid)

        ip_addresses = cast(list[str], d.pop("ipAddresses", UNSET))

        protection_groups = []
        _protection_groups = d.pop("protectionGroups", UNSET)
        for protection_groups_item_data in _protection_groups or []:
            protection_groups_item = UUID(protection_groups_item_data)

            protection_groups.append(protection_groups_item)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: Union[Unset, UUID]
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        is_unmanaged = d.pop("isUnmanaged", UNSET)

        _installation_status = d.pop("installationStatus", UNSET)
        installation_status: Union[Unset, BackupServerAgentInstallationStatus]
        if isinstance(_installation_status, Unset):
            installation_status = UNSET
        else:
            installation_status = BackupServerAgentInstallationStatus(_installation_status)

        _license_ = d.pop("license", UNSET)
        license_: Union[Unset, BackupServerAgentLicense]
        if isinstance(_license_, Unset):
            license_ = UNSET
        else:
            license_ = BackupServerAgentLicense(_license_)

        _license_status = d.pop("licenseStatus", UNSET)
        license_status: Union[Unset, BackupServerAgentLicenseStatus]
        if isinstance(_license_status, Unset):
            license_status = UNSET
        else:
            license_status = BackupServerAgentLicenseStatus(_license_status)

        _os_type = d.pop("osType", UNSET)
        os_type: Union[Unset, BackupServerAgentOsType]
        if isinstance(_os_type, Unset):
            os_type = UNSET
        else:
            os_type = BackupServerAgentOsType(_os_type)

        backup_server_agent = cls(
            instance_uid=instance_uid,
            name=name,
            machine_name=machine_name,
            guest_os=guest_os,
            version=version,
            bios_uid=bios_uid,
            ip_addresses=ip_addresses,
            protection_groups=protection_groups,
            backup_server_uid=backup_server_uid,
            is_unmanaged=is_unmanaged,
            installation_status=installation_status,
            license_=license_,
            license_status=license_status,
            os_type=os_type,
        )

        backup_server_agent.additional_properties = d
        return backup_server_agent

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
