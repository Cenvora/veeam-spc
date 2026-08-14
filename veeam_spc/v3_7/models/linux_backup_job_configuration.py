from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linux_backup_source import LinuxBackupSource
    from ..models.linux_backup_storage import LinuxBackupStorage
    from ..models.linux_backup_target import LinuxBackupTarget
    from ..models.linux_gfs_retention_settings import LinuxGfsRetentionSettings
    from ..models.linux_indexing_settings import LinuxIndexingSettings
    from ..models.linux_job_application_aware_processing_settings import LinuxJobApplicationAwareProcessingSettings
    from ..models.linux_job_retention_settings import LinuxJobRetentionSettings
    from ..models.linux_job_schedule_settings import LinuxJobScheduleSettings
    from ..models.linux_job_script_settings import LinuxJobScriptSettings


T = TypeVar("T", bound="LinuxBackupJobConfiguration")


@_attrs_define
class LinuxBackupJobConfiguration:
    """
    Attributes:
        backup_source (LinuxBackupSource):
        backup_target (LinuxBackupTarget):
        backup_storage (LinuxBackupStorage | Unset):
        indexing_settings (LinuxIndexingSettings | Unset):
        script_settings (LinuxJobScriptSettings | Unset):
        retention_settings (LinuxJobRetentionSettings | Unset):
        schedule_settings (LinuxJobScheduleSettings | Unset):
        application_aware_processing_settings (LinuxJobApplicationAwareProcessingSettings | Unset):
        gfs_retention_settings (LinuxGfsRetentionSettings | Unset):
    """

    backup_source: LinuxBackupSource
    backup_target: LinuxBackupTarget
    backup_storage: LinuxBackupStorage | Unset = UNSET
    indexing_settings: LinuxIndexingSettings | Unset = UNSET
    script_settings: LinuxJobScriptSettings | Unset = UNSET
    retention_settings: LinuxJobRetentionSettings | Unset = UNSET
    schedule_settings: LinuxJobScheduleSettings | Unset = UNSET
    application_aware_processing_settings: LinuxJobApplicationAwareProcessingSettings | Unset = UNSET
    gfs_retention_settings: LinuxGfsRetentionSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_source = self.backup_source.to_dict()

        backup_target = self.backup_target.to_dict()

        backup_storage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_storage, Unset):
            backup_storage = self.backup_storage.to_dict()

        indexing_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.indexing_settings, Unset):
            indexing_settings = self.indexing_settings.to_dict()

        script_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.script_settings, Unset):
            script_settings = self.script_settings.to_dict()

        retention_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retention_settings, Unset):
            retention_settings = self.retention_settings.to_dict()

        schedule_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule_settings, Unset):
            schedule_settings = self.schedule_settings.to_dict()

        application_aware_processing_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.application_aware_processing_settings, Unset):
            application_aware_processing_settings = self.application_aware_processing_settings.to_dict()

        gfs_retention_settings: dict[str, Any] | Unset = UNSET
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
        if backup_storage is not UNSET:
            field_dict["backupStorage"] = backup_storage
        if indexing_settings is not UNSET:
            field_dict["indexingSettings"] = indexing_settings
        if script_settings is not UNSET:
            field_dict["scriptSettings"] = script_settings
        if retention_settings is not UNSET:
            field_dict["retentionSettings"] = retention_settings
        if schedule_settings is not UNSET:
            field_dict["scheduleSettings"] = schedule_settings
        if application_aware_processing_settings is not UNSET:
            field_dict["applicationAwareProcessingSettings"] = application_aware_processing_settings
        if gfs_retention_settings is not UNSET:
            field_dict["gfsRetentionSettings"] = gfs_retention_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linux_backup_source import LinuxBackupSource
        from ..models.linux_backup_storage import LinuxBackupStorage
        from ..models.linux_backup_target import LinuxBackupTarget
        from ..models.linux_gfs_retention_settings import LinuxGfsRetentionSettings
        from ..models.linux_indexing_settings import LinuxIndexingSettings
        from ..models.linux_job_application_aware_processing_settings import LinuxJobApplicationAwareProcessingSettings
        from ..models.linux_job_retention_settings import LinuxJobRetentionSettings
        from ..models.linux_job_schedule_settings import LinuxJobScheduleSettings
        from ..models.linux_job_script_settings import LinuxJobScriptSettings

        d = dict(src_dict)
        backup_source = LinuxBackupSource.from_dict(d.pop("backupSource"))

        backup_target = LinuxBackupTarget.from_dict(d.pop("backupTarget"))

        _backup_storage = d.pop("backupStorage", UNSET)
        backup_storage: LinuxBackupStorage | Unset
        if isinstance(_backup_storage, Unset):
            backup_storage = UNSET
        else:
            backup_storage = LinuxBackupStorage.from_dict(_backup_storage)

        _indexing_settings = d.pop("indexingSettings", UNSET)
        indexing_settings: LinuxIndexingSettings | Unset
        if isinstance(_indexing_settings, Unset):
            indexing_settings = UNSET
        else:
            indexing_settings = LinuxIndexingSettings.from_dict(_indexing_settings)

        _script_settings = d.pop("scriptSettings", UNSET)
        script_settings: LinuxJobScriptSettings | Unset
        if isinstance(_script_settings, Unset):
            script_settings = UNSET
        else:
            script_settings = LinuxJobScriptSettings.from_dict(_script_settings)

        _retention_settings = d.pop("retentionSettings", UNSET)
        retention_settings: LinuxJobRetentionSettings | Unset
        if isinstance(_retention_settings, Unset):
            retention_settings = UNSET
        else:
            retention_settings = LinuxJobRetentionSettings.from_dict(_retention_settings)

        _schedule_settings = d.pop("scheduleSettings", UNSET)
        schedule_settings: LinuxJobScheduleSettings | Unset
        if isinstance(_schedule_settings, Unset):
            schedule_settings = UNSET
        else:
            schedule_settings = LinuxJobScheduleSettings.from_dict(_schedule_settings)

        _application_aware_processing_settings = d.pop("applicationAwareProcessingSettings", UNSET)
        application_aware_processing_settings: LinuxJobApplicationAwareProcessingSettings | Unset
        if isinstance(_application_aware_processing_settings, Unset):
            application_aware_processing_settings = UNSET
        else:
            application_aware_processing_settings = LinuxJobApplicationAwareProcessingSettings.from_dict(
                _application_aware_processing_settings
            )

        _gfs_retention_settings = d.pop("gfsRetentionSettings", UNSET)
        gfs_retention_settings: LinuxGfsRetentionSettings | Unset
        if isinstance(_gfs_retention_settings, Unset):
            gfs_retention_settings = UNSET
        else:
            gfs_retention_settings = LinuxGfsRetentionSettings.from_dict(_gfs_retention_settings)

        linux_backup_job_configuration = cls(
            backup_source=backup_source,
            backup_target=backup_target,
            backup_storage=backup_storage,
            indexing_settings=indexing_settings,
            script_settings=script_settings,
            retention_settings=retention_settings,
            schedule_settings=schedule_settings,
            application_aware_processing_settings=application_aware_processing_settings,
            gfs_retention_settings=gfs_retention_settings,
        )

        linux_backup_job_configuration.additional_properties = d
        return linux_backup_job_configuration

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
