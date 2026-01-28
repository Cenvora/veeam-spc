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
        instance_uid (Union[None, UUID, Unset]): UID assigned to a Veeam backup agent.
        name (Union[None, Unset, str]): Name of a Veeam backup agent.
        machine_name (Union[None, Unset, str]): DNS name of a machine on which a Veeam backup agent is installed.
        guest_os (Union[None, Unset, str]): Operating system installed on a computer.
        version (Union[None, Unset, str]): Version of a Veeam backup agent.
        bios_uid (Union[None, UUID, Unset]): UUID in Win32_ComputerSystem WMI class.
        ip_addresses (Union[None, Unset, list[str]]): Computer IP addresses.
        protection_groups (Union[None, Unset, list[UUID]]): Protection group UIDs.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup & Replication server that manages a Veeam
            backup agent.
        is_unmanaged (Union[None, Unset, bool]): Indicates whether a Veeam backup agent is unmanaged.
        installation_status (Union[Unset, BackupServerAgentInstallationStatus]): Status of Veeam backup agent
            installation.
        license_ (Union[Unset, BackupServerAgentLicense]): Type of a Veeam backup agent license.
        license_status (Union[Unset, BackupServerAgentLicenseStatus]): Status of a Veeam backup agent license.
        os_type (Union[Unset, BackupServerAgentOsType]): Type of a Veeam backup agent operating system.
    """

    instance_uid: Union[None, UUID, Unset] = UNSET
    name: Union[None, Unset, str] = UNSET
    machine_name: Union[None, Unset, str] = UNSET
    guest_os: Union[None, Unset, str] = UNSET
    version: Union[None, Unset, str] = UNSET
    bios_uid: Union[None, UUID, Unset] = UNSET
    ip_addresses: Union[None, Unset, list[str]] = UNSET
    protection_groups: Union[None, Unset, list[UUID]] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    is_unmanaged: Union[None, Unset, bool] = UNSET
    installation_status: Union[Unset, BackupServerAgentInstallationStatus] = UNSET
    license_: Union[Unset, BackupServerAgentLicense] = UNSET
    license_status: Union[Unset, BackupServerAgentLicenseStatus] = UNSET
    os_type: Union[Unset, BackupServerAgentOsType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[None, Unset, str]
        if isinstance(self.instance_uid, Unset):
            instance_uid = UNSET
        elif isinstance(self.instance_uid, UUID):
            instance_uid = str(self.instance_uid)
        else:
            instance_uid = self.instance_uid

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        machine_name: Union[None, Unset, str]
        if isinstance(self.machine_name, Unset):
            machine_name = UNSET
        else:
            machine_name = self.machine_name

        guest_os: Union[None, Unset, str]
        if isinstance(self.guest_os, Unset):
            guest_os = UNSET
        else:
            guest_os = self.guest_os

        version: Union[None, Unset, str]
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        bios_uid: Union[None, Unset, str]
        if isinstance(self.bios_uid, Unset):
            bios_uid = UNSET
        elif isinstance(self.bios_uid, UUID):
            bios_uid = str(self.bios_uid)
        else:
            bios_uid = self.bios_uid

        ip_addresses: Union[None, Unset, list[str]]
        if isinstance(self.ip_addresses, Unset):
            ip_addresses = UNSET
        elif isinstance(self.ip_addresses, list):
            ip_addresses = self.ip_addresses

        else:
            ip_addresses = self.ip_addresses

        protection_groups: Union[None, Unset, list[str]]
        if isinstance(self.protection_groups, Unset):
            protection_groups = UNSET
        elif isinstance(self.protection_groups, list):
            protection_groups = []
            for protection_groups_type_0_item_data in self.protection_groups:
                protection_groups_type_0_item = str(protection_groups_type_0_item_data)
                protection_groups.append(protection_groups_type_0_item)

        else:
            protection_groups = self.protection_groups

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        is_unmanaged: Union[None, Unset, bool]
        if isinstance(self.is_unmanaged, Unset):
            is_unmanaged = UNSET
        else:
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

        def _parse_instance_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                instance_uid_type_0 = UUID(data)

                return instance_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        instance_uid = _parse_instance_uid(d.pop("instanceUid", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_machine_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        machine_name = _parse_machine_name(d.pop("machineName", UNSET))

        def _parse_guest_os(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        guest_os = _parse_guest_os(d.pop("guestOs", UNSET))

        def _parse_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_bios_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                bios_uid_type_0 = UUID(data)

                return bios_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        bios_uid = _parse_bios_uid(d.pop("biosUid", UNSET))

        def _parse_ip_addresses(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ip_addresses_type_0 = cast(list[str], data)

                return ip_addresses_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        ip_addresses = _parse_ip_addresses(d.pop("ipAddresses", UNSET))

        def _parse_protection_groups(data: object) -> Union[None, Unset, list[UUID]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                protection_groups_type_0 = []
                _protection_groups_type_0 = data
                for protection_groups_type_0_item_data in _protection_groups_type_0:
                    protection_groups_type_0_item = UUID(protection_groups_type_0_item_data)

                    protection_groups_type_0.append(protection_groups_type_0_item)

                return protection_groups_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[UUID]], data)

        protection_groups = _parse_protection_groups(d.pop("protectionGroups", UNSET))

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: Union[Unset, UUID]
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        def _parse_is_unmanaged(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_unmanaged = _parse_is_unmanaged(d.pop("isUnmanaged", UNSET))

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
