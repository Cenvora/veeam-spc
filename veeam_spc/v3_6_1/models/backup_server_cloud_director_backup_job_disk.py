from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_backup_job_vmware_disks_type_to_process import BackupServerBackupJobVmwareDisksTypeToProcess
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_cloud_director_object import BackupServerCloudDirectorObject


T = TypeVar("T", bound="BackupServerCloudDirectorBackupJobDisk")


@_attrs_define
class BackupServerCloudDirectorBackupJobDisk:
    """
    Attributes:
        vm_object (BackupServerCloudDirectorObject): VMware Cloud Director object.
        disks_to_process (BackupServerBackupJobVmwareDisksTypeToProcess): Type of a disk.
        disks (list[str]): Array of IDs assigned to VM disks.
        remove_from_vm_configuration (Union[None, Unset, bool]): Indicates whether the disk is removed from the VM
            configuration.
    """

    vm_object: "BackupServerCloudDirectorObject"
    disks_to_process: BackupServerBackupJobVmwareDisksTypeToProcess
    disks: list[str]
    remove_from_vm_configuration: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vm_object = self.vm_object.to_dict()

        disks_to_process = self.disks_to_process.value

        disks = self.disks

        remove_from_vm_configuration: Union[None, Unset, bool]
        if isinstance(self.remove_from_vm_configuration, Unset):
            remove_from_vm_configuration = UNSET
        else:
            remove_from_vm_configuration = self.remove_from_vm_configuration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vmObject": vm_object,
                "disksToProcess": disks_to_process,
                "disks": disks,
            }
        )
        if remove_from_vm_configuration is not UNSET:
            field_dict["removeFromVMConfiguration"] = remove_from_vm_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_cloud_director_object import BackupServerCloudDirectorObject

        d = dict(src_dict)
        vm_object = BackupServerCloudDirectorObject.from_dict(d.pop("vmObject"))

        disks_to_process = BackupServerBackupJobVmwareDisksTypeToProcess(d.pop("disksToProcess"))

        disks = cast(list[str], d.pop("disks"))

        def _parse_remove_from_vm_configuration(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        remove_from_vm_configuration = _parse_remove_from_vm_configuration(d.pop("removeFromVMConfiguration", UNSET))

        backup_server_cloud_director_backup_job_disk = cls(
            vm_object=vm_object,
            disks_to_process=disks_to_process,
            disks=disks,
            remove_from_vm_configuration=remove_from_vm_configuration,
        )

        backup_server_cloud_director_backup_job_disk.additional_properties = d
        return backup_server_cloud_director_backup_job_disk

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
