from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_exclusions_templates_type_0 import (
        BackupServerBackupJobExclusionsTemplatesType0,
    )
    from ..models.backup_server_cloud_director_backup_job_disk import BackupServerCloudDirectorBackupJobDisk
    from ..models.backup_server_cloud_director_object import BackupServerCloudDirectorObject


T = TypeVar("T", bound="BackupServerCloudDirectorBackupJobExclusionsType0")


@_attrs_define
class BackupServerCloudDirectorBackupJobExclusionsType0:
    """Array of objects excluded from a backup job.

    Attributes:
        vms (Union[None, Unset, list['BackupServerCloudDirectorObject']]): Array of VMs excluded from a backup job.'
        disks (Union[None, Unset, list['BackupServerCloudDirectorBackupJobDisk']]): Array of VM disks excluded from a
            backup job.
        templates (Union['BackupServerBackupJobExclusionsTemplatesType0', None, Unset]): Excluded VM templates.
    """

    vms: Union[None, Unset, list["BackupServerCloudDirectorObject"]] = UNSET
    disks: Union[None, Unset, list["BackupServerCloudDirectorBackupJobDisk"]] = UNSET
    templates: Union["BackupServerBackupJobExclusionsTemplatesType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.backup_server_backup_job_exclusions_templates_type_0 import (
            BackupServerBackupJobExclusionsTemplatesType0,
        )

        vms: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.vms, Unset):
            vms = UNSET
        elif isinstance(self.vms, list):
            vms = []
            for vms_type_0_item_data in self.vms:
                vms_type_0_item = vms_type_0_item_data.to_dict()
                vms.append(vms_type_0_item)

        else:
            vms = self.vms

        disks: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.disks, Unset):
            disks = UNSET
        elif isinstance(self.disks, list):
            disks = []
            for disks_type_0_item_data in self.disks:
                disks_type_0_item = disks_type_0_item_data.to_dict()
                disks.append(disks_type_0_item)

        else:
            disks = self.disks

        templates: Union[None, Unset, dict[str, Any]]
        if isinstance(self.templates, Unset):
            templates = UNSET
        elif isinstance(self.templates, BackupServerBackupJobExclusionsTemplatesType0):
            templates = self.templates.to_dict()
        else:
            templates = self.templates

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
        from ..models.backup_server_backup_job_exclusions_templates_type_0 import (
            BackupServerBackupJobExclusionsTemplatesType0,
        )
        from ..models.backup_server_cloud_director_backup_job_disk import BackupServerCloudDirectorBackupJobDisk
        from ..models.backup_server_cloud_director_object import BackupServerCloudDirectorObject

        d = dict(src_dict)

        def _parse_vms(data: object) -> Union[None, Unset, list["BackupServerCloudDirectorObject"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                vms_type_0 = []
                _vms_type_0 = data
                for vms_type_0_item_data in _vms_type_0:
                    vms_type_0_item = BackupServerCloudDirectorObject.from_dict(vms_type_0_item_data)

                    vms_type_0.append(vms_type_0_item)

                return vms_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["BackupServerCloudDirectorObject"]], data)

        vms = _parse_vms(d.pop("vms", UNSET))

        def _parse_disks(data: object) -> Union[None, Unset, list["BackupServerCloudDirectorBackupJobDisk"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                disks_type_0 = []
                _disks_type_0 = data
                for disks_type_0_item_data in _disks_type_0:
                    disks_type_0_item = BackupServerCloudDirectorBackupJobDisk.from_dict(disks_type_0_item_data)

                    disks_type_0.append(disks_type_0_item)

                return disks_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["BackupServerCloudDirectorBackupJobDisk"]], data)

        disks = _parse_disks(d.pop("disks", UNSET))

        def _parse_templates(data: object) -> Union["BackupServerBackupJobExclusionsTemplatesType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_exclusions_templates_type_0 = (
                    BackupServerBackupJobExclusionsTemplatesType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_exclusions_templates_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobExclusionsTemplatesType0", None, Unset], data)

        templates = _parse_templates(d.pop("templates", UNSET))

        backup_server_cloud_director_backup_job_exclusions_type_0 = cls(
            vms=vms,
            disks=disks,
            templates=templates,
        )

        backup_server_cloud_director_backup_job_exclusions_type_0.additional_properties = d
        return backup_server_cloud_director_backup_job_exclusions_type_0

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
