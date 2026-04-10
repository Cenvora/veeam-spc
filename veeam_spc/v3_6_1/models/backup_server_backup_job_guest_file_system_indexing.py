from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_indexing_settings import BackupServerBackupJobIndexingSettings


T = TypeVar("T", bound="BackupServerBackupJobGuestFileSystemIndexing")


@_attrs_define
class BackupServerBackupJobGuestFileSystemIndexing:
    """Guest OS file indexing.

    Attributes:
        is_enabled (Union[Unset, bool]): Indicates whether file indexing is enabled. Default: False.
        indexing_settings (Union[None, Unset, list['BackupServerBackupJobIndexingSettings']]): Array of VMs with guest
            OS file indexing options.
    """

    is_enabled: Union[Unset, bool] = False
    indexing_settings: Union[None, Unset, list["BackupServerBackupJobIndexingSettings"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        indexing_settings: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.indexing_settings, Unset):
            indexing_settings = UNSET
        elif isinstance(self.indexing_settings, list):
            indexing_settings = []
            for indexing_settings_type_0_item_data in self.indexing_settings:
                indexing_settings_type_0_item = indexing_settings_type_0_item_data.to_dict()
                indexing_settings.append(indexing_settings_type_0_item)

        else:
            indexing_settings = self.indexing_settings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if indexing_settings is not UNSET:
            field_dict["indexingSettings"] = indexing_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_backup_job_indexing_settings import BackupServerBackupJobIndexingSettings

        d = dict(src_dict)
        is_enabled = d.pop("isEnabled", UNSET)

        def _parse_indexing_settings(data: object) -> Union[None, Unset, list["BackupServerBackupJobIndexingSettings"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                indexing_settings_type_0 = []
                _indexing_settings_type_0 = data
                for indexing_settings_type_0_item_data in _indexing_settings_type_0:
                    indexing_settings_type_0_item = BackupServerBackupJobIndexingSettings.from_dict(
                        indexing_settings_type_0_item_data
                    )

                    indexing_settings_type_0.append(indexing_settings_type_0_item)

                return indexing_settings_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["BackupServerBackupJobIndexingSettings"]], data)

        indexing_settings = _parse_indexing_settings(d.pop("indexingSettings", UNSET))

        backup_server_backup_job_guest_file_system_indexing = cls(
            is_enabled=is_enabled,
            indexing_settings=indexing_settings,
        )

        backup_server_backup_job_guest_file_system_indexing.additional_properties = d
        return backup_server_backup_job_guest_file_system_indexing

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
