from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_vmware_object import BackupServerVmwareObject


T = TypeVar("T", bound="BackupServerBackupJobGuestOsCredentialsPerMachine")


@_attrs_define
class BackupServerBackupJobGuestOsCredentialsPerMachine:
    """Individual VM credentials.

    Attributes:
        vm_object (BackupServerVmwareObject): VMware vSphere object.
        windows_credentials_id (Union[Unset, UUID]): UID assigned to a credentials record that is used to access
            Microsoft Windows VM.
        linux_credentials_id (Union[Unset, UUID]): UID assigned to a credentials record that is used to access Linux VM.
    """

    vm_object: "BackupServerVmwareObject"
    windows_credentials_id: Union[Unset, UUID] = UNSET
    linux_credentials_id: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vm_object = self.vm_object.to_dict()

        windows_credentials_id: Union[Unset, str] = UNSET
        if not isinstance(self.windows_credentials_id, Unset):
            windows_credentials_id = str(self.windows_credentials_id)

        linux_credentials_id: Union[Unset, str] = UNSET
        if not isinstance(self.linux_credentials_id, Unset):
            linux_credentials_id = str(self.linux_credentials_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vmObject": vm_object,
            }
        )
        if windows_credentials_id is not UNSET:
            field_dict["windowsCredentialsId"] = windows_credentials_id
        if linux_credentials_id is not UNSET:
            field_dict["linuxCredentialsId"] = linux_credentials_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_vmware_object import BackupServerVmwareObject

        d = dict(src_dict)
        vm_object = BackupServerVmwareObject.from_dict(d.pop("vmObject"))

        _windows_credentials_id = d.pop("windowsCredentialsId", UNSET)
        windows_credentials_id: Union[Unset, UUID]
        if isinstance(_windows_credentials_id, Unset):
            windows_credentials_id = UNSET
        else:
            windows_credentials_id = UUID(_windows_credentials_id)

        _linux_credentials_id = d.pop("linuxCredentialsId", UNSET)
        linux_credentials_id: Union[Unset, UUID]
        if isinstance(_linux_credentials_id, Unset):
            linux_credentials_id = UNSET
        else:
            linux_credentials_id = UUID(_linux_credentials_id)

        backup_server_backup_job_guest_os_credentials_per_machine = cls(
            vm_object=vm_object,
            windows_credentials_id=windows_credentials_id,
            linux_credentials_id=linux_credentials_id,
        )

        backup_server_backup_job_guest_os_credentials_per_machine.additional_properties = d
        return backup_server_backup_job_guest_os_credentials_per_machine

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
