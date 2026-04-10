from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_cloud_director_backup_job_application_settings_type_0 import (
        BackupServerCloudDirectorBackupJobApplicationSettingsType0,
    )


T = TypeVar("T", bound="BackupServerCloudDirectorBackupJobApplicationAwareProcessing")


@_attrs_define
class BackupServerCloudDirectorBackupJobApplicationAwareProcessing:
    """Application-aware processing settings.

    Attributes:
        is_enabled (Union[Unset, bool]): Indicates whether application-aware processing is enabled. Default: False.
        app_settings (Union[None, Unset, list[Union['BackupServerCloudDirectorBackupJobApplicationSettingsType0',
            None]]]): Array of VMware Cloud Director objects and their application settings.
    """

    is_enabled: Union[Unset, bool] = False
    app_settings: Union[
        None, Unset, list[Union["BackupServerCloudDirectorBackupJobApplicationSettingsType0", None]]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.backup_server_cloud_director_backup_job_application_settings_type_0 import (
            BackupServerCloudDirectorBackupJobApplicationSettingsType0,
        )

        is_enabled = self.is_enabled

        app_settings: Union[None, Unset, list[Union[None, dict[str, Any]]]]
        if isinstance(self.app_settings, Unset):
            app_settings = UNSET
        elif isinstance(self.app_settings, list):
            app_settings = []
            for app_settings_type_0_item_data in self.app_settings:
                app_settings_type_0_item: Union[None, dict[str, Any]]
                if isinstance(
                    app_settings_type_0_item_data, BackupServerCloudDirectorBackupJobApplicationSettingsType0
                ):
                    app_settings_type_0_item = app_settings_type_0_item_data.to_dict()
                else:
                    app_settings_type_0_item = app_settings_type_0_item_data
                app_settings.append(app_settings_type_0_item)

        else:
            app_settings = self.app_settings

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
        from ..models.backup_server_cloud_director_backup_job_application_settings_type_0 import (
            BackupServerCloudDirectorBackupJobApplicationSettingsType0,
        )

        d = dict(src_dict)
        is_enabled = d.pop("isEnabled", UNSET)

        def _parse_app_settings(
            data: object,
        ) -> Union[None, Unset, list[Union["BackupServerCloudDirectorBackupJobApplicationSettingsType0", None]]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                app_settings_type_0 = []
                _app_settings_type_0 = data
                for app_settings_type_0_item_data in _app_settings_type_0:

                    def _parse_app_settings_type_0_item(
                        data: object,
                    ) -> Union["BackupServerCloudDirectorBackupJobApplicationSettingsType0", None]:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_backup_server_cloud_director_backup_job_application_settings_type_0 = (
                                BackupServerCloudDirectorBackupJobApplicationSettingsType0.from_dict(data)
                            )

                            return componentsschemas_backup_server_cloud_director_backup_job_application_settings_type_0
                        except:  # noqa: E722
                            pass
                        return cast(Union["BackupServerCloudDirectorBackupJobApplicationSettingsType0", None], data)

                    app_settings_type_0_item = _parse_app_settings_type_0_item(app_settings_type_0_item_data)

                    app_settings_type_0.append(app_settings_type_0_item)

                return app_settings_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[None, Unset, list[Union["BackupServerCloudDirectorBackupJobApplicationSettingsType0", None]]],
                data,
            )

        app_settings = _parse_app_settings(d.pop("appSettings", UNSET))

        backup_server_cloud_director_backup_job_application_aware_processing = cls(
            is_enabled=is_enabled,
            app_settings=app_settings,
        )

        backup_server_cloud_director_backup_job_application_aware_processing.additional_properties = d
        return backup_server_cloud_director_backup_job_application_aware_processing

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
