from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_object_indexing_type_0 import BackupServerBackupJobObjectIndexingType0
    from ..models.backup_server_cloud_director_object import BackupServerCloudDirectorObject


T = TypeVar("T", bound="BackupServerCloudDirectorBackupJobIndexingSettings")


@_attrs_define
class BackupServerCloudDirectorBackupJobIndexingSettings:
    """VM with guest OS file indexing options.

    Attributes:
        vm_object (BackupServerCloudDirectorObject): VMware Cloud Director object.
        windows_indexing (Union['BackupServerBackupJobObjectIndexingType0', None, Unset]): Guest OS indexing options for
            a VM.
        linux_indexing (Union['BackupServerBackupJobObjectIndexingType0', None, Unset]): Guest OS indexing options for a
            VM.
    """

    vm_object: "BackupServerCloudDirectorObject"
    windows_indexing: Union["BackupServerBackupJobObjectIndexingType0", None, Unset] = UNSET
    linux_indexing: Union["BackupServerBackupJobObjectIndexingType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.backup_server_backup_job_object_indexing_type_0 import BackupServerBackupJobObjectIndexingType0

        vm_object = self.vm_object.to_dict()

        windows_indexing: Union[None, Unset, dict[str, Any]]
        if isinstance(self.windows_indexing, Unset):
            windows_indexing = UNSET
        elif isinstance(self.windows_indexing, BackupServerBackupJobObjectIndexingType0):
            windows_indexing = self.windows_indexing.to_dict()
        else:
            windows_indexing = self.windows_indexing

        linux_indexing: Union[None, Unset, dict[str, Any]]
        if isinstance(self.linux_indexing, Unset):
            linux_indexing = UNSET
        elif isinstance(self.linux_indexing, BackupServerBackupJobObjectIndexingType0):
            linux_indexing = self.linux_indexing.to_dict()
        else:
            linux_indexing = self.linux_indexing

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
        from ..models.backup_server_backup_job_object_indexing_type_0 import BackupServerBackupJobObjectIndexingType0
        from ..models.backup_server_cloud_director_object import BackupServerCloudDirectorObject

        d = dict(src_dict)
        vm_object = BackupServerCloudDirectorObject.from_dict(d.pop("vmObject"))

        def _parse_windows_indexing(data: object) -> Union["BackupServerBackupJobObjectIndexingType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_object_indexing_type_0 = (
                    BackupServerBackupJobObjectIndexingType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_object_indexing_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobObjectIndexingType0", None, Unset], data)

        windows_indexing = _parse_windows_indexing(d.pop("windowsIndexing", UNSET))

        def _parse_linux_indexing(data: object) -> Union["BackupServerBackupJobObjectIndexingType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_object_indexing_type_0 = (
                    BackupServerBackupJobObjectIndexingType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_object_indexing_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobObjectIndexingType0", None, Unset], data)

        linux_indexing = _parse_linux_indexing(d.pop("linuxIndexing", UNSET))

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
