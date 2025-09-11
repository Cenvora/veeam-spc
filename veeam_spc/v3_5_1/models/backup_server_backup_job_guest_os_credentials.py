from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_credentials_type import BackupServerCredentialsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_guest_os_credentials_per_machine import (
        BackupServerBackupJobGuestOsCredentialsPerMachine,
    )


T = TypeVar("T", bound="BackupServerBackupJobGuestOsCredentials")


@_attrs_define
class BackupServerBackupJobGuestOsCredentials:
    """VM custom credentials.

    Attributes:
        credentials_id (UUID): UID assigned to a credentials record that is used to access Microsoft Windows VMs.
        credentials_type (BackupServerCredentialsType): Credentials type.
        credentials_per_machine (Union[Unset, list['BackupServerBackupJobGuestOsCredentialsPerMachine']]): Array of
            individual credentials for VMs.
    """

    credentials_id: UUID
    credentials_type: BackupServerCredentialsType
    credentials_per_machine: Union[Unset, list["BackupServerBackupJobGuestOsCredentialsPerMachine"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credentials_id = str(self.credentials_id)

        credentials_type = self.credentials_type.value

        credentials_per_machine: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.credentials_per_machine, Unset):
            credentials_per_machine = []
            for credentials_per_machine_item_data in self.credentials_per_machine:
                credentials_per_machine_item = credentials_per_machine_item_data.to_dict()
                credentials_per_machine.append(credentials_per_machine_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentialsId": credentials_id,
                "credentialsType": credentials_type,
            }
        )
        if credentials_per_machine is not UNSET:
            field_dict["credentialsPerMachine"] = credentials_per_machine

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_backup_job_guest_os_credentials_per_machine import (
            BackupServerBackupJobGuestOsCredentialsPerMachine,
        )

        d = dict(src_dict)
        credentials_id = UUID(d.pop("credentialsId"))

        credentials_type = BackupServerCredentialsType(d.pop("credentialsType"))

        credentials_per_machine = []
        _credentials_per_machine = d.pop("credentialsPerMachine", UNSET)
        for credentials_per_machine_item_data in _credentials_per_machine or []:
            credentials_per_machine_item = BackupServerBackupJobGuestOsCredentialsPerMachine.from_dict(
                credentials_per_machine_item_data
            )

            credentials_per_machine.append(credentials_per_machine_item)

        backup_server_backup_job_guest_os_credentials = cls(
            credentials_id=credentials_id,
            credentials_type=credentials_type,
            credentials_per_machine=credentials_per_machine,
        )

        backup_server_backup_job_guest_os_credentials.additional_properties = d
        return backup_server_backup_job_guest_os_credentials

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
