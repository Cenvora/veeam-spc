from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_full_backup_maintenance_defragment_and_compact_type_0 import (
        BackupServerBackupJobFullBackupMaintenanceDefragmentAndCompactType0,
    )
    from ..models.backup_server_backup_job_full_backup_maintenance_remove_data_type_0 import (
        BackupServerBackupJobFullBackupMaintenanceRemoveDataType0,
    )


T = TypeVar("T", bound="BackupServerBackupJobFullBackupMaintenanceType0")


@_attrs_define
class BackupServerBackupJobFullBackupMaintenanceType0:
    """Maintenance settings for full backup files.

    Attributes:
        remove_data (Union['BackupServerBackupJobFullBackupMaintenanceRemoveDataType0', None, Unset]): Backup data
            settings for deleted VMs.
        defragment_and_compact (Union['BackupServerBackupJobFullBackupMaintenanceDefragmentAndCompactType0', None,
            Unset]): Compact operation settings.
    """

    remove_data: Union["BackupServerBackupJobFullBackupMaintenanceRemoveDataType0", None, Unset] = UNSET
    defragment_and_compact: Union[
        "BackupServerBackupJobFullBackupMaintenanceDefragmentAndCompactType0", None, Unset
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.backup_server_backup_job_full_backup_maintenance_defragment_and_compact_type_0 import (
            BackupServerBackupJobFullBackupMaintenanceDefragmentAndCompactType0,
        )
        from ..models.backup_server_backup_job_full_backup_maintenance_remove_data_type_0 import (
            BackupServerBackupJobFullBackupMaintenanceRemoveDataType0,
        )

        remove_data: Union[None, Unset, dict[str, Any]]
        if isinstance(self.remove_data, Unset):
            remove_data = UNSET
        elif isinstance(self.remove_data, BackupServerBackupJobFullBackupMaintenanceRemoveDataType0):
            remove_data = self.remove_data.to_dict()
        else:
            remove_data = self.remove_data

        defragment_and_compact: Union[None, Unset, dict[str, Any]]
        if isinstance(self.defragment_and_compact, Unset):
            defragment_and_compact = UNSET
        elif isinstance(
            self.defragment_and_compact, BackupServerBackupJobFullBackupMaintenanceDefragmentAndCompactType0
        ):
            defragment_and_compact = self.defragment_and_compact.to_dict()
        else:
            defragment_and_compact = self.defragment_and_compact

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
        from ..models.backup_server_backup_job_full_backup_maintenance_defragment_and_compact_type_0 import (
            BackupServerBackupJobFullBackupMaintenanceDefragmentAndCompactType0,
        )
        from ..models.backup_server_backup_job_full_backup_maintenance_remove_data_type_0 import (
            BackupServerBackupJobFullBackupMaintenanceRemoveDataType0,
        )

        d = dict(src_dict)

        def _parse_remove_data(
            data: object,
        ) -> Union["BackupServerBackupJobFullBackupMaintenanceRemoveDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_full_backup_maintenance_remove_data_type_0 = (
                    BackupServerBackupJobFullBackupMaintenanceRemoveDataType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_full_backup_maintenance_remove_data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobFullBackupMaintenanceRemoveDataType0", None, Unset], data)

        remove_data = _parse_remove_data(d.pop("removeData", UNSET))

        def _parse_defragment_and_compact(
            data: object,
        ) -> Union["BackupServerBackupJobFullBackupMaintenanceDefragmentAndCompactType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_full_backup_maintenance_defragment_and_compact_type_0 = (
                    BackupServerBackupJobFullBackupMaintenanceDefragmentAndCompactType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_full_backup_maintenance_defragment_and_compact_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobFullBackupMaintenanceDefragmentAndCompactType0", None, Unset], data)

        defragment_and_compact = _parse_defragment_and_compact(d.pop("defragmentAndCompact", UNSET))

        backup_server_backup_job_full_backup_maintenance_type_0 = cls(
            remove_data=remove_data,
            defragment_and_compact=defragment_and_compact,
        )

        backup_server_backup_job_full_backup_maintenance_type_0.additional_properties = d
        return backup_server_backup_job_full_backup_maintenance_type_0

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
