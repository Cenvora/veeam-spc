from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_job_operation_mode import BackupJobOperationMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cloud_repository_connection_settings_type_0 import CloudRepositoryConnectionSettingsType0
    from ..models.linux_backup_job_configuration import LinuxBackupJobConfiguration


T = TypeVar("T", bound="LinuxCustomJobConfiguration")


@_attrs_define
class LinuxCustomJobConfiguration:
    """
    Attributes:
        name (str): Job name.
        operation_mode (BackupJobOperationMode): Backup job operation mode.
        job_configuration (LinuxBackupJobConfiguration):
        description (Union[None, Unset, str]): Job description.
        cloud_repository_connection_settings (Union['CloudRepositoryConnectionSettingsType0', None, Unset]): Settings
            required to connect a cloud repository that is used as a target location for backups.
    """

    name: str
    operation_mode: BackupJobOperationMode
    job_configuration: "LinuxBackupJobConfiguration"
    description: Union[None, Unset, str] = UNSET
    cloud_repository_connection_settings: Union["CloudRepositoryConnectionSettingsType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cloud_repository_connection_settings_type_0 import CloudRepositoryConnectionSettingsType0

        name = self.name

        operation_mode = self.operation_mode.value

        job_configuration = self.job_configuration.to_dict()

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        cloud_repository_connection_settings: Union[None, Unset, dict[str, Any]]
        if isinstance(self.cloud_repository_connection_settings, Unset):
            cloud_repository_connection_settings = UNSET
        elif isinstance(self.cloud_repository_connection_settings, CloudRepositoryConnectionSettingsType0):
            cloud_repository_connection_settings = self.cloud_repository_connection_settings.to_dict()
        else:
            cloud_repository_connection_settings = self.cloud_repository_connection_settings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "operationMode": operation_mode,
                "jobConfiguration": job_configuration,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if cloud_repository_connection_settings is not UNSET:
            field_dict["cloudRepositoryConnectionSettings"] = cloud_repository_connection_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cloud_repository_connection_settings_type_0 import CloudRepositoryConnectionSettingsType0
        from ..models.linux_backup_job_configuration import LinuxBackupJobConfiguration

        d = dict(src_dict)
        name = d.pop("name")

        operation_mode = BackupJobOperationMode(d.pop("operationMode"))

        job_configuration = LinuxBackupJobConfiguration.from_dict(d.pop("jobConfiguration"))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_cloud_repository_connection_settings(
            data: object,
        ) -> Union["CloudRepositoryConnectionSettingsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_cloud_repository_connection_settings_type_0 = (
                    CloudRepositoryConnectionSettingsType0.from_dict(data)
                )

                return componentsschemas_cloud_repository_connection_settings_type_0
            except:  # noqa: E722
                pass
            return cast(Union["CloudRepositoryConnectionSettingsType0", None, Unset], data)

        cloud_repository_connection_settings = _parse_cloud_repository_connection_settings(
            d.pop("cloudRepositoryConnectionSettings", UNSET)
        )

        linux_custom_job_configuration = cls(
            name=name,
            operation_mode=operation_mode,
            job_configuration=job_configuration,
            description=description,
            cloud_repository_connection_settings=cloud_repository_connection_settings,
        )

        linux_custom_job_configuration.additional_properties = d
        return linux_custom_job_configuration

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
