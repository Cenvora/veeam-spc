from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_full_backup_maintenance_defragment_and_compact import (
        BackupServerBackupJobFullBackupMaintenanceDefragmentAndCompact,
    )
    from ..models.backup_server_backup_job_full_backup_maintenance_remove_data import (
        BackupServerBackupJobFullBackupMaintenanceRemoveData,
    )


T = TypeVar("T", bound="BackupServerBackupJobFullBackupMaintenance")


@_attrs_define
class BackupServerBackupJobFullBackupMaintenance:
    """Maintenance settings for full backup files.

    Attributes:
        remove_data (Union[Unset, BackupServerBackupJobFullBackupMaintenanceRemoveData]): Backup data settings for
            deleted VMs.
        defragment_and_compact (Union[Unset, BackupServerBackupJobFullBackupMaintenanceDefragmentAndCompact]): Compact
            operation settings.
    """

    remove_data: Union[Unset, "BackupServerBackupJobFullBackupMaintenanceRemoveData"] = UNSET
    defragment_and_compact: Union[Unset, "BackupServerBackupJobFullBackupMaintenanceDefragmentAndCompact"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        remove_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.remove_data, Unset):
            remove_data = self.remove_data.to_dict()

        defragment_and_compact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.defragment_and_compact, Unset):
            defragment_and_compact = self.defragment_and_compact.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if remove_data is not UNSET:
            field_dict["removeData"] = remove_data
        if defragment_and_compact is not UNSET:
            field_dict["defragmentAndCompact"] = defragment_and_compact

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_backup_job_full_backup_maintenance_defragment_and_compact import (
            BackupServerBackupJobFullBackupMaintenanceDefragmentAndCompact,
        )
        from ..models.backup_server_backup_job_full_backup_maintenance_remove_data import (
            BackupServerBackupJobFullBackupMaintenanceRemoveData,
        )

        d = dict(src_dict)
        _remove_data = d.pop("removeData", UNSET)
        remove_data: Union[Unset, BackupServerBackupJobFullBackupMaintenanceRemoveData]
        if isinstance(_remove_data, Unset):
            remove_data = UNSET
        else:
            remove_data = BackupServerBackupJobFullBackupMaintenanceRemoveData.from_dict(_remove_data)

        _defragment_and_compact = d.pop("defragmentAndCompact", UNSET)
        defragment_and_compact: Union[Unset, BackupServerBackupJobFullBackupMaintenanceDefragmentAndCompact]
        if isinstance(_defragment_and_compact, Unset):
            defragment_and_compact = UNSET
        else:
            defragment_and_compact = BackupServerBackupJobFullBackupMaintenanceDefragmentAndCompact.from_dict(
                _defragment_and_compact
            )

        backup_server_backup_job_full_backup_maintenance = cls(
            remove_data=remove_data,
            defragment_and_compact=defragment_and_compact,
        )

        backup_server_backup_job_full_backup_maintenance.additional_properties = d
        return backup_server_backup_job_full_backup_maintenance

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
