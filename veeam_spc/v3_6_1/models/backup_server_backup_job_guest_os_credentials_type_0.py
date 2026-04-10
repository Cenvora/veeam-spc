from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_credentials_type import BackupServerCredentialsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_guest_os_credentials_per_machine import (
        BackupServerBackupJobGuestOsCredentialsPerMachine,
    )


T = TypeVar("T", bound="BackupServerBackupJobGuestOsCredentialsType0")


@_attrs_define
class BackupServerBackupJobGuestOsCredentialsType0:
    """VM custom credentials.

    Attributes:
        credentials_id (UUID): UID assigned to a credentials record that is used to access Microsoft Windows VMs.
        credentials_type (BackupServerCredentialsType): Credentials type.
        credentials_per_machine (Union[None, Unset, list['BackupServerBackupJobGuestOsCredentialsPerMachine']]): Array
            of individual credentials for VMs.
    """

    credentials_id: UUID
    credentials_type: BackupServerCredentialsType
    credentials_per_machine: Union[None, Unset, list["BackupServerBackupJobGuestOsCredentialsPerMachine"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credentials_id = str(self.credentials_id)

        credentials_type = self.credentials_type.value

        credentials_per_machine: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.credentials_per_machine, Unset):
            credentials_per_machine = UNSET
        elif isinstance(self.credentials_per_machine, list):
            credentials_per_machine = []
            for credentials_per_machine_type_0_item_data in self.credentials_per_machine:
                credentials_per_machine_type_0_item = credentials_per_machine_type_0_item_data.to_dict()
                credentials_per_machine.append(credentials_per_machine_type_0_item)

        else:
            credentials_per_machine = self.credentials_per_machine

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

        def _parse_credentials_per_machine(
            data: object,
        ) -> Union[None, Unset, list["BackupServerBackupJobGuestOsCredentialsPerMachine"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                credentials_per_machine_type_0 = []
                _credentials_per_machine_type_0 = data
                for credentials_per_machine_type_0_item_data in _credentials_per_machine_type_0:
                    credentials_per_machine_type_0_item = BackupServerBackupJobGuestOsCredentialsPerMachine.from_dict(
                        credentials_per_machine_type_0_item_data
                    )

                    credentials_per_machine_type_0.append(credentials_per_machine_type_0_item)

                return credentials_per_machine_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["BackupServerBackupJobGuestOsCredentialsPerMachine"]], data)

        credentials_per_machine = _parse_credentials_per_machine(d.pop("credentialsPerMachine", UNSET))

        backup_server_backup_job_guest_os_credentials_type_0 = cls(
            credentials_id=credentials_id,
            credentials_type=credentials_type,
            credentials_per_machine=credentials_per_machine,
        )

        backup_server_backup_job_guest_os_credentials_type_0.additional_properties = d
        return backup_server_backup_job_guest_os_credentials_type_0

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
