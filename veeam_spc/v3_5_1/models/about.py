import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="About")


@_attrs_define
class About:
    """
    Attributes:
        installation_id (Union[Unset, UUID]): UID assigned to a Veeam Service Provider Console unique installation type.
        installation_date (Union[Unset, datetime.datetime]): Date of Veeam Service Provider Console installation.
        actual_vaw_version (Union[Unset, str]): Current version of Veeam Agent for Windows.
        actual_val_version (Union[Unset, str]): Current version of Veeam Agent for Linux.
        actual_vam_version (Union[Unset, str]): Current version of Veeam Agent for Mac.
        server_version (Union[Unset, str]): Veeam Service Provider Console Server version.
        windows_management_agent_version (Union[Unset, str]): Version of management agents for Microsoft Windows
            computers.
        linux_management_agent_version (Union[Unset, str]): Version of management agents for Linux computers.
        mac_management_agent_version (Union[Unset, str]): Version of management agents for macOS computers.
    """

    installation_id: Union[Unset, UUID] = UNSET
    installation_date: Union[Unset, datetime.datetime] = UNSET
    actual_vaw_version: Union[Unset, str] = UNSET
    actual_val_version: Union[Unset, str] = UNSET
    actual_vam_version: Union[Unset, str] = UNSET
    server_version: Union[Unset, str] = UNSET
    windows_management_agent_version: Union[Unset, str] = UNSET
    linux_management_agent_version: Union[Unset, str] = UNSET
    mac_management_agent_version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        installation_id: Union[Unset, str] = UNSET
        if not isinstance(self.installation_id, Unset):
            installation_id = str(self.installation_id)

        installation_date: Union[Unset, str] = UNSET
        if not isinstance(self.installation_date, Unset):
            installation_date = self.installation_date.isoformat()

        actual_vaw_version = self.actual_vaw_version

        actual_val_version = self.actual_val_version

        actual_vam_version = self.actual_vam_version

        server_version = self.server_version

        windows_management_agent_version = self.windows_management_agent_version

        linux_management_agent_version = self.linux_management_agent_version

        mac_management_agent_version = self.mac_management_agent_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if installation_id is not UNSET:
            field_dict["installationId"] = installation_id
        if installation_date is not UNSET:
            field_dict["installationDate"] = installation_date
        if actual_vaw_version is not UNSET:
            field_dict["actualVawVersion"] = actual_vaw_version
        if actual_val_version is not UNSET:
            field_dict["actualValVersion"] = actual_val_version
        if actual_vam_version is not UNSET:
            field_dict["actualVamVersion"] = actual_vam_version
        if server_version is not UNSET:
            field_dict["serverVersion"] = server_version
        if windows_management_agent_version is not UNSET:
            field_dict["windowsManagementAgentVersion"] = windows_management_agent_version
        if linux_management_agent_version is not UNSET:
            field_dict["linuxManagementAgentVersion"] = linux_management_agent_version
        if mac_management_agent_version is not UNSET:
            field_dict["macManagementAgentVersion"] = mac_management_agent_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _installation_id = d.pop("installationId", UNSET)
        installation_id: Union[Unset, UUID]
        if isinstance(_installation_id, Unset):
            installation_id = UNSET
        else:
            installation_id = UUID(_installation_id)

        _installation_date = d.pop("installationDate", UNSET)
        installation_date: Union[Unset, datetime.datetime]
        if isinstance(_installation_date, Unset):
            installation_date = UNSET
        else:
            installation_date = isoparse(_installation_date)

        actual_vaw_version = d.pop("actualVawVersion", UNSET)

        actual_val_version = d.pop("actualValVersion", UNSET)

        actual_vam_version = d.pop("actualVamVersion", UNSET)

        server_version = d.pop("serverVersion", UNSET)

        windows_management_agent_version = d.pop("windowsManagementAgentVersion", UNSET)

        linux_management_agent_version = d.pop("linuxManagementAgentVersion", UNSET)

        mac_management_agent_version = d.pop("macManagementAgentVersion", UNSET)

        about = cls(
            installation_id=installation_id,
            installation_date=installation_date,
            actual_vaw_version=actual_vaw_version,
            actual_val_version=actual_val_version,
            actual_vam_version=actual_vam_version,
            server_version=server_version,
            windows_management_agent_version=windows_management_agent_version,
            linux_management_agent_version=linux_management_agent_version,
            mac_management_agent_version=mac_management_agent_version,
        )

        about.additional_properties = d
        return about

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
