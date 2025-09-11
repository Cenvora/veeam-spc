from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_job_operation_mode import BackupJobOperationMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cloud_repository_connection_settings import CloudRepositoryConnectionSettings
    from ..models.mac_backup_job_configuration import MacBackupJobConfiguration


T = TypeVar("T", bound="MacCustomJobConfiguration")


@_attrs_define
class MacCustomJobConfiguration:
    """
    Attributes:
        name (str): Name of a backup policy.
        operation_mode (BackupJobOperationMode): Backup job operation mode.
        job_configuration (MacBackupJobConfiguration):
        description (Union[Unset, str]): Description of a backup policy.
        cloud_repository_connection_settings (Union[Unset, CloudRepositoryConnectionSettings]): Settings required to
            connect a cloud repository that is used as a target location for backups.
    """

    name: str
    operation_mode: BackupJobOperationMode
    job_configuration: "MacBackupJobConfiguration"
    description: Union[Unset, str] = UNSET
    cloud_repository_connection_settings: Union[Unset, "CloudRepositoryConnectionSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        operation_mode = self.operation_mode.value

        job_configuration = self.job_configuration.to_dict()

        description = self.description

        cloud_repository_connection_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cloud_repository_connection_settings, Unset):
            cloud_repository_connection_settings = self.cloud_repository_connection_settings.to_dict()

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
        from ..models.cloud_repository_connection_settings import CloudRepositoryConnectionSettings
        from ..models.mac_backup_job_configuration import MacBackupJobConfiguration

        d = dict(src_dict)
        name = d.pop("name")

        operation_mode = BackupJobOperationMode(d.pop("operationMode"))

        job_configuration = MacBackupJobConfiguration.from_dict(d.pop("jobConfiguration"))

        description = d.pop("description", UNSET)

        _cloud_repository_connection_settings = d.pop("cloudRepositoryConnectionSettings", UNSET)
        cloud_repository_connection_settings: Union[Unset, CloudRepositoryConnectionSettings]
        if isinstance(_cloud_repository_connection_settings, Unset):
            cloud_repository_connection_settings = UNSET
        else:
            cloud_repository_connection_settings = CloudRepositoryConnectionSettings.from_dict(
                _cloud_repository_connection_settings
            )

        mac_custom_job_configuration = cls(
            name=name,
            operation_mode=operation_mode,
            job_configuration=job_configuration,
            description=description,
            cloud_repository_connection_settings=cloud_repository_connection_settings,
        )

        mac_custom_job_configuration.additional_properties = d
        return mac_custom_job_configuration

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
