from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_exclusions import BackupServerBackupJobExclusions
    from ..models.backup_server_backup_job_vmware_object_size import BackupServerBackupJobVmwareObjectSize


T = TypeVar("T", bound="BackupServerBackupJobVirtualMachines")


@_attrs_define
class BackupServerBackupJobVirtualMachines:
    """Backup scope.

    Attributes:
        includes (list['BackupServerBackupJobVmwareObjectSize']): Array of VMs and VM containers processed by a backup
            job.
        excludes (Union[Unset, BackupServerBackupJobExclusions]): Array of objects excluded from a backup job.
    """

    includes: list["BackupServerBackupJobVmwareObjectSize"]
    excludes: Union[Unset, "BackupServerBackupJobExclusions"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        includes = []
        for includes_item_data in self.includes:
            includes_item = includes_item_data.to_dict()
            includes.append(includes_item)

        excludes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.excludes, Unset):
            excludes = self.excludes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "includes": includes,
            }
        )
        if excludes is not UNSET:
            field_dict["excludes"] = excludes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_backup_job_exclusions import BackupServerBackupJobExclusions
        from ..models.backup_server_backup_job_vmware_object_size import BackupServerBackupJobVmwareObjectSize

        d = dict(src_dict)
        includes = []
        _includes = d.pop("includes")
        for includes_item_data in _includes:
            includes_item = BackupServerBackupJobVmwareObjectSize.from_dict(includes_item_data)

            includes.append(includes_item)

        _excludes = d.pop("excludes", UNSET)
        excludes: Union[Unset, BackupServerBackupJobExclusions]
        if isinstance(_excludes, Unset):
            excludes = UNSET
        else:
            excludes = BackupServerBackupJobExclusions.from_dict(_excludes)

        backup_server_backup_job_virtual_machines = cls(
            includes=includes,
            excludes=excludes,
        )

        backup_server_backup_job_virtual_machines.additional_properties = d
        return backup_server_backup_job_virtual_machines

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
