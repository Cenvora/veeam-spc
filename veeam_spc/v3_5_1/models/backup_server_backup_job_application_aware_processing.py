from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_application_settings import BackupServerBackupJobApplicationSettings


T = TypeVar("T", bound="BackupServerBackupJobApplicationAwareProcessing")


@_attrs_define
class BackupServerBackupJobApplicationAwareProcessing:
    """Application-aware processing settings.

    Attributes:
        is_enabled (Union[Unset, bool]): Indicates whether application-aware processing is enabled. Default: False.
        app_settings (Union[Unset, list['BackupServerBackupJobApplicationSettings']]): Array of VMware vSphere objects
            and their application settings.
    """

    is_enabled: Union[Unset, bool] = False
    app_settings: Union[Unset, list["BackupServerBackupJobApplicationSettings"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        app_settings: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.app_settings, Unset):
            app_settings = []
            for app_settings_item_data in self.app_settings:
                app_settings_item = app_settings_item_data.to_dict()
                app_settings.append(app_settings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if app_settings is not UNSET:
            field_dict["appSettings"] = app_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_backup_job_application_settings import BackupServerBackupJobApplicationSettings

        d = dict(src_dict)
        is_enabled = d.pop("isEnabled", UNSET)

        app_settings = []
        _app_settings = d.pop("appSettings", UNSET)
        for app_settings_item_data in _app_settings or []:
            app_settings_item = BackupServerBackupJobApplicationSettings.from_dict(app_settings_item_data)

            app_settings.append(app_settings_item)

        backup_server_backup_job_application_aware_processing = cls(
            is_enabled=is_enabled,
            app_settings=app_settings,
        )

        backup_server_backup_job_application_aware_processing.additional_properties = d
        return backup_server_backup_job_application_aware_processing

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
