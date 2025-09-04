from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.computer_info_applications_type_0_item import ComputerInfoApplicationsType0Item
from ..models.computer_info_guest_os_type import ComputerInfoGuestOsType
from ..models.computer_info_platform_type import ComputerInfoPlatformType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComputerInfo")


@_attrs_define
class ComputerInfo:
    """Information about a computer on which a management agent is deployed.

    Attributes:
        unique_uid (Union[Unset, UUID]): UID assigned to a computer.
        bios_uuid (Union[Unset, UUID]): UUID in Win32_ComputerSystem WMI class.
        host_name (Union[Unset, str]): Name of a computer.
        fqdn (Union[Unset, str]): FQDN of a computer.
        guest_os (Union[Unset, str]): Operating system installed on a computer.
        guest_os_type (Union[Unset, ComputerInfoGuestOsType]): Type of a computer operating system.
        guest_os_version (Union[Unset, str]): Version of a computer operating system.
        guest_os_sku (Union[None, Unset, int]): SKU of a computer operating system.
        platform_type (Union[Unset, ComputerInfoPlatformType]): Type of a computer platform.
        ip_addresses (Union[Unset, list[str]]): Computer IP addresses.
        mac_addresses (Union[Unset, list[str]]): Computer MAC addresses.
        applications (Union[None, Unset, list[ComputerInfoApplicationsType0Item]]): Array of applications installed on a
            computer.
    """

    unique_uid: Union[Unset, UUID] = UNSET
    bios_uuid: Union[Unset, UUID] = UNSET
    host_name: Union[Unset, str] = UNSET
    fqdn: Union[Unset, str] = UNSET
    guest_os: Union[Unset, str] = UNSET
    guest_os_type: Union[Unset, ComputerInfoGuestOsType] = UNSET
    guest_os_version: Union[Unset, str] = UNSET
    guest_os_sku: Union[None, Unset, int] = UNSET
    platform_type: Union[Unset, ComputerInfoPlatformType] = UNSET
    ip_addresses: Union[Unset, list[str]] = UNSET
    mac_addresses: Union[Unset, list[str]] = UNSET
    applications: Union[None, Unset, list[ComputerInfoApplicationsType0Item]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unique_uid: Union[Unset, str] = UNSET
        if not isinstance(self.unique_uid, Unset):
            unique_uid = str(self.unique_uid)

        bios_uuid: Union[Unset, str] = UNSET
        if not isinstance(self.bios_uuid, Unset):
            bios_uuid = str(self.bios_uuid)

        host_name = self.host_name

        fqdn = self.fqdn

        guest_os = self.guest_os

        guest_os_type: Union[Unset, str] = UNSET
        if not isinstance(self.guest_os_type, Unset):
            guest_os_type = self.guest_os_type.value

        guest_os_version = self.guest_os_version

        guest_os_sku: Union[None, Unset, int]
        if isinstance(self.guest_os_sku, Unset):
            guest_os_sku = UNSET
        else:
            guest_os_sku = self.guest_os_sku

        platform_type: Union[Unset, str] = UNSET
        if not isinstance(self.platform_type, Unset):
            platform_type = self.platform_type.value

        ip_addresses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ip_addresses, Unset):
            ip_addresses = self.ip_addresses

        mac_addresses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.mac_addresses, Unset):
            mac_addresses = self.mac_addresses

        applications: Union[None, Unset, list[str]]
        if isinstance(self.applications, Unset):
            applications = UNSET
        elif isinstance(self.applications, list):
            applications = []
            for applications_type_0_item_data in self.applications:
                applications_type_0_item = applications_type_0_item_data.value
                applications.append(applications_type_0_item)

        else:
            applications = self.applications

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unique_uid is not UNSET:
            field_dict["uniqueUid"] = unique_uid
        if bios_uuid is not UNSET:
            field_dict["biosUuid"] = bios_uuid
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if fqdn is not UNSET:
            field_dict["fqdn"] = fqdn
        if guest_os is not UNSET:
            field_dict["guestOs"] = guest_os
        if guest_os_type is not UNSET:
            field_dict["guestOsType"] = guest_os_type
        if guest_os_version is not UNSET:
            field_dict["guestOsVersion"] = guest_os_version
        if guest_os_sku is not UNSET:
            field_dict["guestOsSku"] = guest_os_sku
        if platform_type is not UNSET:
            field_dict["platformType"] = platform_type
        if ip_addresses is not UNSET:
            field_dict["ipAddresses"] = ip_addresses
        if mac_addresses is not UNSET:
            field_dict["macAddresses"] = mac_addresses
        if applications is not UNSET:
            field_dict["applications"] = applications

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _unique_uid = d.pop("uniqueUid", UNSET)
        unique_uid: Union[Unset, UUID]
        if isinstance(_unique_uid, Unset):
            unique_uid = UNSET
        else:
            unique_uid = UUID(_unique_uid)

        _bios_uuid = d.pop("biosUuid", UNSET)
        bios_uuid: Union[Unset, UUID]
        if isinstance(_bios_uuid, Unset):
            bios_uuid = UNSET
        else:
            bios_uuid = UUID(_bios_uuid)

        host_name = d.pop("hostName", UNSET)

        fqdn = d.pop("fqdn", UNSET)

        guest_os = d.pop("guestOs", UNSET)

        _guest_os_type = d.pop("guestOsType", UNSET)
        guest_os_type: Union[Unset, ComputerInfoGuestOsType]
        if isinstance(_guest_os_type, Unset):
            guest_os_type = UNSET
        else:
            guest_os_type = ComputerInfoGuestOsType(_guest_os_type)

        guest_os_version = d.pop("guestOsVersion", UNSET)

        def _parse_guest_os_sku(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        guest_os_sku = _parse_guest_os_sku(d.pop("guestOsSku", UNSET))

        _platform_type = d.pop("platformType", UNSET)
        platform_type: Union[Unset, ComputerInfoPlatformType]
        if isinstance(_platform_type, Unset):
            platform_type = UNSET
        else:
            platform_type = ComputerInfoPlatformType(_platform_type)

        ip_addresses = cast(list[str], d.pop("ipAddresses", UNSET))

        mac_addresses = cast(list[str], d.pop("macAddresses", UNSET))

        def _parse_applications(data: object) -> Union[None, Unset, list[ComputerInfoApplicationsType0Item]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                applications_type_0 = []
                _applications_type_0 = data
                for applications_type_0_item_data in _applications_type_0:
                    applications_type_0_item = ComputerInfoApplicationsType0Item(applications_type_0_item_data)

                    applications_type_0.append(applications_type_0_item)

                return applications_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[ComputerInfoApplicationsType0Item]], data)

        applications = _parse_applications(d.pop("applications", UNSET))

        computer_info = cls(
            unique_uid=unique_uid,
            bios_uuid=bios_uuid,
            host_name=host_name,
            fqdn=fqdn,
            guest_os=guest_os,
            guest_os_type=guest_os_type,
            guest_os_version=guest_os_version,
            guest_os_sku=guest_os_sku,
            platform_type=platform_type,
            ip_addresses=ip_addresses,
            mac_addresses=mac_addresses,
            applications=applications,
        )

        computer_info.additional_properties = d
        return computer_info

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
