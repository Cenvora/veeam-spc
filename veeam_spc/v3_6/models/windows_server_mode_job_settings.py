from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.windows_application_aware_processing_settings import WindowsApplicationAwareProcessingSettings
    from ..models.windows_indexing_settings import WindowsIndexingSettings
    from ..models.windows_server_job_retention_settings import WindowsServerJobRetentionSettings
    from ..models.windows_server_job_schedule_settings import WindowsServerJobScheduleSettings


T = TypeVar("T", bound="WindowsServerModeJobSettings")


@_attrs_define
class WindowsServerModeJobSettings:
    """
    Attributes:
        retention_settings (Union[Unset, WindowsServerJobRetentionSettings]):
        schedule_setting (Union[Unset, WindowsServerJobScheduleSettings]):
        indexing_settings (Union[Unset, WindowsIndexingSettings]):
        application_aware_processing_settings (Union[Unset, WindowsApplicationAwareProcessingSettings]):
    """

    retention_settings: Union[Unset, "WindowsServerJobRetentionSettings"] = UNSET
    schedule_setting: Union[Unset, "WindowsServerJobScheduleSettings"] = UNSET
    indexing_settings: Union[Unset, "WindowsIndexingSettings"] = UNSET
    application_aware_processing_settings: Union[Unset, "WindowsApplicationAwareProcessingSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        retention_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.retention_settings, Unset):
            retention_settings = self.retention_settings.to_dict()

        schedule_setting: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schedule_setting, Unset):
            schedule_setting = self.schedule_setting.to_dict()

        indexing_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.indexing_settings, Unset):
            indexing_settings = self.indexing_settings.to_dict()

        application_aware_processing_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.application_aware_processing_settings, Unset):
            application_aware_processing_settings = self.application_aware_processing_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if retention_settings is not UNSET:
            field_dict["retentionSettings"] = retention_settings
        if schedule_setting is not UNSET:
            field_dict["scheduleSetting"] = schedule_setting
        if indexing_settings is not UNSET:
            field_dict["indexingSettings"] = indexing_settings
        if application_aware_processing_settings is not UNSET:
            field_dict["applicationAwareProcessingSettings"] = application_aware_processing_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.windows_application_aware_processing_settings import WindowsApplicationAwareProcessingSettings
        from ..models.windows_indexing_settings import WindowsIndexingSettings
        from ..models.windows_server_job_retention_settings import WindowsServerJobRetentionSettings
        from ..models.windows_server_job_schedule_settings import WindowsServerJobScheduleSettings

        d = dict(src_dict)
        _retention_settings = d.pop("retentionSettings", UNSET)
        retention_settings: Union[Unset, WindowsServerJobRetentionSettings]
        if isinstance(_retention_settings, Unset):
            retention_settings = UNSET
        else:
            retention_settings = WindowsServerJobRetentionSettings.from_dict(_retention_settings)

        _schedule_setting = d.pop("scheduleSetting", UNSET)
        schedule_setting: Union[Unset, WindowsServerJobScheduleSettings]
        if isinstance(_schedule_setting, Unset):
            schedule_setting = UNSET
        else:
            schedule_setting = WindowsServerJobScheduleSettings.from_dict(_schedule_setting)

        _indexing_settings = d.pop("indexingSettings", UNSET)
        indexing_settings: Union[Unset, WindowsIndexingSettings]
        if isinstance(_indexing_settings, Unset):
            indexing_settings = UNSET
        else:
            indexing_settings = WindowsIndexingSettings.from_dict(_indexing_settings)

        _application_aware_processing_settings = d.pop("applicationAwareProcessingSettings", UNSET)
        application_aware_processing_settings: Union[Unset, WindowsApplicationAwareProcessingSettings]
        if isinstance(_application_aware_processing_settings, Unset):
            application_aware_processing_settings = UNSET
        else:
            application_aware_processing_settings = WindowsApplicationAwareProcessingSettings.from_dict(
                _application_aware_processing_settings
            )

        windows_server_mode_job_settings = cls(
            retention_settings=retention_settings,
            schedule_setting=schedule_setting,
            indexing_settings=indexing_settings,
            application_aware_processing_settings=application_aware_processing_settings,
        )

        windows_server_mode_job_settings.additional_properties = d
        return windows_server_mode_job_settings

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
