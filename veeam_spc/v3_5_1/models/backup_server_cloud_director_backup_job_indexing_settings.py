from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_object_indexing import BackupServerBackupJobObjectIndexing
    from ..models.backup_server_cloud_director_object import BackupServerCloudDirectorObject


T = TypeVar("T", bound="BackupServerCloudDirectorBackupJobIndexingSettings")


@_attrs_define
class BackupServerCloudDirectorBackupJobIndexingSettings:
    """VM with guest OS file indexing options.

    Attributes:
        vm_object (BackupServerCloudDirectorObject): VMware Cloud Director object.
        windows_indexing (Union[Unset, BackupServerBackupJobObjectIndexing]): Guest OS indexing options for a VM.
        linux_indexing (Union[Unset, BackupServerBackupJobObjectIndexing]): Guest OS indexing options for a VM.
    """

    vm_object: "BackupServerCloudDirectorObject"
    windows_indexing: Union[Unset, "BackupServerBackupJobObjectIndexing"] = UNSET
    linux_indexing: Union[Unset, "BackupServerBackupJobObjectIndexing"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vm_object = self.vm_object.to_dict()

        windows_indexing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.windows_indexing, Unset):
            windows_indexing = self.windows_indexing.to_dict()

        linux_indexing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.linux_indexing, Unset):
            linux_indexing = self.linux_indexing.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vmObject": vm_object,
            }
        )
        if windows_indexing is not UNSET:
            field_dict["windowsIndexing"] = windows_indexing
        if linux_indexing is not UNSET:
            field_dict["linuxIndexing"] = linux_indexing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_backup_job_object_indexing import BackupServerBackupJobObjectIndexing
        from ..models.backup_server_cloud_director_object import BackupServerCloudDirectorObject

        d = dict(src_dict)
        vm_object = BackupServerCloudDirectorObject.from_dict(d.pop("vmObject"))

        _windows_indexing = d.pop("windowsIndexing", UNSET)
        windows_indexing: Union[Unset, BackupServerBackupJobObjectIndexing]
        if isinstance(_windows_indexing, Unset):
            windows_indexing = UNSET
        else:
            windows_indexing = BackupServerBackupJobObjectIndexing.from_dict(_windows_indexing)

        _linux_indexing = d.pop("linuxIndexing", UNSET)
        linux_indexing: Union[Unset, BackupServerBackupJobObjectIndexing]
        if isinstance(_linux_indexing, Unset):
            linux_indexing = UNSET
        else:
            linux_indexing = BackupServerBackupJobObjectIndexing.from_dict(_linux_indexing)

        backup_server_cloud_director_backup_job_indexing_settings = cls(
            vm_object=vm_object,
            windows_indexing=windows_indexing,
            linux_indexing=linux_indexing,
        )

        backup_server_cloud_director_backup_job_indexing_settings.additional_properties = d
        return backup_server_cloud_director_backup_job_indexing_settings

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
