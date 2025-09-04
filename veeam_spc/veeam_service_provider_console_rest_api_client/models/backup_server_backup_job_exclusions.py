from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_exclusions_templates import BackupServerBackupJobExclusionsTemplates
    from ..models.backup_server_backup_job_vmware_object_disk import BackupServerBackupJobVmwareObjectDisk
    from ..models.backup_server_backup_job_vmware_object_size import BackupServerBackupJobVmwareObjectSize


T = TypeVar("T", bound="BackupServerBackupJobExclusions")


@_attrs_define
class BackupServerBackupJobExclusions:
    """Array of objects excluded from a backup job.

    Attributes:
        vms (Union[Unset, list['BackupServerBackupJobVmwareObjectSize']]): Array of VMs excluded from a backup job.
        disks (Union[Unset, list['BackupServerBackupJobVmwareObjectDisk']]): Array of VM disks excluded from a backup
            job.
        templates (Union[Unset, BackupServerBackupJobExclusionsTemplates]): Excluded VM templates.
    """

    vms: Union[Unset, list["BackupServerBackupJobVmwareObjectSize"]] = UNSET
    disks: Union[Unset, list["BackupServerBackupJobVmwareObjectDisk"]] = UNSET
    templates: Union[Unset, "BackupServerBackupJobExclusionsTemplates"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vms: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vms, Unset):
            vms = []
            for vms_item_data in self.vms:
                vms_item = vms_item_data.to_dict()
                vms.append(vms_item)

        disks: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.disks, Unset):
            disks = []
            for disks_item_data in self.disks:
                disks_item = disks_item_data.to_dict()
                disks.append(disks_item)

        templates: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.templates, Unset):
            templates = self.templates.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vms is not UNSET:
            field_dict["vms"] = vms
        if disks is not UNSET:
            field_dict["disks"] = disks
        if templates is not UNSET:
            field_dict["templates"] = templates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_backup_job_exclusions_templates import BackupServerBackupJobExclusionsTemplates
        from ..models.backup_server_backup_job_vmware_object_disk import BackupServerBackupJobVmwareObjectDisk
        from ..models.backup_server_backup_job_vmware_object_size import BackupServerBackupJobVmwareObjectSize

        d = dict(src_dict)
        vms = []
        _vms = d.pop("vms", UNSET)
        for vms_item_data in _vms or []:
            vms_item = BackupServerBackupJobVmwareObjectSize.from_dict(vms_item_data)

            vms.append(vms_item)

        disks = []
        _disks = d.pop("disks", UNSET)
        for disks_item_data in _disks or []:
            disks_item = BackupServerBackupJobVmwareObjectDisk.from_dict(disks_item_data)

            disks.append(disks_item)

        _templates = d.pop("templates", UNSET)
        templates: Union[Unset, BackupServerBackupJobExclusionsTemplates]
        if isinstance(_templates, Unset):
            templates = UNSET
        else:
            templates = BackupServerBackupJobExclusionsTemplates.from_dict(_templates)

        backup_server_backup_job_exclusions = cls(
            vms=vms,
            disks=disks,
            templates=templates,
        )

        backup_server_backup_job_exclusions.additional_properties = d
        return backup_server_backup_job_exclusions

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
