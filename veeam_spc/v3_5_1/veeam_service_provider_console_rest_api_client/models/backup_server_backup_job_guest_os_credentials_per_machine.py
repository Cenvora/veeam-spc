from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
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
        windows_credentials_id (Union[None, UUID, Unset]): UID assigned to a credentials record that is used to access
            Microsoft Windows VM.
        linux_credentials_id (Union[None, UUID, Unset]): UID assigned to a credentials record that is used to access
            Linux VM.
    """

    vm_object: "BackupServerVmwareObject"
    windows_credentials_id: Union[None, UUID, Unset] = UNSET
    linux_credentials_id: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vm_object = self.vm_object.to_dict()

        windows_credentials_id: Union[None, Unset, str]
        if isinstance(self.windows_credentials_id, Unset):
            windows_credentials_id = UNSET
        elif isinstance(self.windows_credentials_id, UUID):
            windows_credentials_id = str(self.windows_credentials_id)
        else:
            windows_credentials_id = self.windows_credentials_id

        linux_credentials_id: Union[None, Unset, str]
        if isinstance(self.linux_credentials_id, Unset):
            linux_credentials_id = UNSET
        elif isinstance(self.linux_credentials_id, UUID):
            linux_credentials_id = str(self.linux_credentials_id)
        else:
            linux_credentials_id = self.linux_credentials_id

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

        def _parse_windows_credentials_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                windows_credentials_id_type_0 = UUID(data)

                return windows_credentials_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        windows_credentials_id = _parse_windows_credentials_id(d.pop("windowsCredentialsId", UNSET))

        def _parse_linux_credentials_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                linux_credentials_id_type_0 = UUID(data)

                return linux_credentials_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        linux_credentials_id = _parse_linux_credentials_id(d.pop("linuxCredentialsId", UNSET))

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
