from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.windows_advanced_job_settings import WindowsAdvancedJobSettings
    from ..models.windows_backup_source import WindowsBackupSource
    from ..models.windows_backup_target import WindowsBackupTarget
    from ..models.windows_gfs_retention_settings import WindowsGfsRetentionSettings
    from ..models.windows_server_mode_job_settings import WindowsServerModeJobSettings
    from ..models.windows_workstation_mode_job_settings import WindowsWorkstationModeJobSettings


T = TypeVar("T", bound="WindowsBackupJobConfiguration")


@_attrs_define
class WindowsBackupJobConfiguration:
    """
    Attributes:
        backup_source (WindowsBackupSource):
        backup_target (WindowsBackupTarget):
        server_mode_settings (Union[Unset, WindowsServerModeJobSettings]):
        workstation_mode_settings (Union[Unset, WindowsWorkstationModeJobSettings]):
        advanced_settings (Union[Unset, WindowsAdvancedJobSettings]):
        gfs_retention_settings (Union[Unset, WindowsGfsRetentionSettings]):
    """

    backup_source: "WindowsBackupSource"
    backup_target: "WindowsBackupTarget"
    server_mode_settings: Union[Unset, "WindowsServerModeJobSettings"] = UNSET
    workstation_mode_settings: Union[Unset, "WindowsWorkstationModeJobSettings"] = UNSET
    advanced_settings: Union[Unset, "WindowsAdvancedJobSettings"] = UNSET
    gfs_retention_settings: Union[Unset, "WindowsGfsRetentionSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_source = self.backup_source.to_dict()

        backup_target = self.backup_target.to_dict()

        server_mode_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.server_mode_settings, Unset):
            server_mode_settings = self.server_mode_settings.to_dict()

        workstation_mode_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.workstation_mode_settings, Unset):
            workstation_mode_settings = self.workstation_mode_settings.to_dict()

        advanced_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.advanced_settings, Unset):
            advanced_settings = self.advanced_settings.to_dict()

        gfs_retention_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.gfs_retention_settings, Unset):
            gfs_retention_settings = self.gfs_retention_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backupSource": backup_source,
                "backupTarget": backup_target,
            }
        )
        if server_mode_settings is not UNSET:
            field_dict["serverModeSettings"] = server_mode_settings
        if workstation_mode_settings is not UNSET:
            field_dict["workstationModeSettings"] = workstation_mode_settings
        if advanced_settings is not UNSET:
            field_dict["advancedSettings"] = advanced_settings
        if gfs_retention_settings is not UNSET:
            field_dict["gfsRetentionSettings"] = gfs_retention_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.windows_advanced_job_settings import WindowsAdvancedJobSettings
        from ..models.windows_backup_source import WindowsBackupSource
        from ..models.windows_backup_target import WindowsBackupTarget
        from ..models.windows_gfs_retention_settings import WindowsGfsRetentionSettings
        from ..models.windows_server_mode_job_settings import WindowsServerModeJobSettings
        from ..models.windows_workstation_mode_job_settings import WindowsWorkstationModeJobSettings

        d = dict(src_dict)
        backup_source = WindowsBackupSource.from_dict(d.pop("backupSource"))

        backup_target = WindowsBackupTarget.from_dict(d.pop("backupTarget"))

        _server_mode_settings = d.pop("serverModeSettings", UNSET)
        server_mode_settings: Union[Unset, WindowsServerModeJobSettings]
        if isinstance(_server_mode_settings, Unset):
            server_mode_settings = UNSET
        else:
            server_mode_settings = WindowsServerModeJobSettings.from_dict(_server_mode_settings)

        _workstation_mode_settings = d.pop("workstationModeSettings", UNSET)
        workstation_mode_settings: Union[Unset, WindowsWorkstationModeJobSettings]
        if isinstance(_workstation_mode_settings, Unset):
            workstation_mode_settings = UNSET
        else:
            workstation_mode_settings = WindowsWorkstationModeJobSettings.from_dict(_workstation_mode_settings)

        _advanced_settings = d.pop("advancedSettings", UNSET)
        advanced_settings: Union[Unset, WindowsAdvancedJobSettings]
        if isinstance(_advanced_settings, Unset):
            advanced_settings = UNSET
        else:
            advanced_settings = WindowsAdvancedJobSettings.from_dict(_advanced_settings)

        _gfs_retention_settings = d.pop("gfsRetentionSettings", UNSET)
        gfs_retention_settings: Union[Unset, WindowsGfsRetentionSettings]
        if isinstance(_gfs_retention_settings, Unset):
            gfs_retention_settings = UNSET
        else:
            gfs_retention_settings = WindowsGfsRetentionSettings.from_dict(_gfs_retention_settings)

        windows_backup_job_configuration = cls(
            backup_source=backup_source,
            backup_target=backup_target,
            server_mode_settings=server_mode_settings,
            workstation_mode_settings=workstation_mode_settings,
            advanced_settings=advanced_settings,
            gfs_retention_settings=gfs_retention_settings,
        )

        windows_backup_job_configuration.additional_properties = d
        return windows_backup_job_configuration

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
