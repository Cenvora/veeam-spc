from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_guest_interaction_proxies_settings_type_0 import (
        BackupServerBackupJobGuestInteractionProxiesSettingsType0,
    )
    from ..models.backup_server_backup_job_guest_os_credentials_type_0 import (
        BackupServerBackupJobGuestOsCredentialsType0,
    )
    from ..models.backup_server_cloud_director_backup_job_application_aware_processing import (
        BackupServerCloudDirectorBackupJobApplicationAwareProcessing,
    )
    from ..models.backup_server_cloud_director_backup_job_guest_file_system_indexing import (
        BackupServerCloudDirectorBackupJobGuestFileSystemIndexing,
    )


T = TypeVar("T", bound="BackupServerCloudDirectorBackupJobGuestProcessing")


@_attrs_define
class BackupServerCloudDirectorBackupJobGuestProcessing:
    """Guest processing settings.

    Attributes:
        app_aware_processing (Union[Unset, BackupServerCloudDirectorBackupJobApplicationAwareProcessing]): Application-
            aware processing settings.
        guest_fs_indexing (Union[Unset, BackupServerCloudDirectorBackupJobGuestFileSystemIndexing]): Guest OS file
            indexing.
        guest_interaction_proxies (Union['BackupServerBackupJobGuestInteractionProxiesSettingsType0', None, Unset]):
            Interaction proxy settings.
        guest_credentials (Union['BackupServerBackupJobGuestOsCredentialsType0', None, Unset]): VM custom credentials.
    """

    app_aware_processing: Union[Unset, "BackupServerCloudDirectorBackupJobApplicationAwareProcessing"] = UNSET
    guest_fs_indexing: Union[Unset, "BackupServerCloudDirectorBackupJobGuestFileSystemIndexing"] = UNSET
    guest_interaction_proxies: Union["BackupServerBackupJobGuestInteractionProxiesSettingsType0", None, Unset] = UNSET
    guest_credentials: Union["BackupServerBackupJobGuestOsCredentialsType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.backup_server_backup_job_guest_interaction_proxies_settings_type_0 import (
            BackupServerBackupJobGuestInteractionProxiesSettingsType0,
        )
        from ..models.backup_server_backup_job_guest_os_credentials_type_0 import (
            BackupServerBackupJobGuestOsCredentialsType0,
        )

        app_aware_processing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.app_aware_processing, Unset):
            app_aware_processing = self.app_aware_processing.to_dict()

        guest_fs_indexing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.guest_fs_indexing, Unset):
            guest_fs_indexing = self.guest_fs_indexing.to_dict()

        guest_interaction_proxies: Union[None, Unset, dict[str, Any]]
        if isinstance(self.guest_interaction_proxies, Unset):
            guest_interaction_proxies = UNSET
        elif isinstance(self.guest_interaction_proxies, BackupServerBackupJobGuestInteractionProxiesSettingsType0):
            guest_interaction_proxies = self.guest_interaction_proxies.to_dict()
        else:
            guest_interaction_proxies = self.guest_interaction_proxies

        guest_credentials: Union[None, Unset, dict[str, Any]]
        if isinstance(self.guest_credentials, Unset):
            guest_credentials = UNSET
        elif isinstance(self.guest_credentials, BackupServerBackupJobGuestOsCredentialsType0):
            guest_credentials = self.guest_credentials.to_dict()
        else:
            guest_credentials = self.guest_credentials

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_aware_processing is not UNSET:
            field_dict["appAwareProcessing"] = app_aware_processing
        if guest_fs_indexing is not UNSET:
            field_dict["guestFSIndexing"] = guest_fs_indexing
        if guest_interaction_proxies is not UNSET:
            field_dict["guestInteractionProxies"] = guest_interaction_proxies
        if guest_credentials is not UNSET:
            field_dict["guestCredentials"] = guest_credentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_backup_job_guest_interaction_proxies_settings_type_0 import (
            BackupServerBackupJobGuestInteractionProxiesSettingsType0,
        )
        from ..models.backup_server_backup_job_guest_os_credentials_type_0 import (
            BackupServerBackupJobGuestOsCredentialsType0,
        )
        from ..models.backup_server_cloud_director_backup_job_application_aware_processing import (
            BackupServerCloudDirectorBackupJobApplicationAwareProcessing,
        )
        from ..models.backup_server_cloud_director_backup_job_guest_file_system_indexing import (
            BackupServerCloudDirectorBackupJobGuestFileSystemIndexing,
        )

        d = dict(src_dict)
        _app_aware_processing = d.pop("appAwareProcessing", UNSET)
        app_aware_processing: Union[Unset, BackupServerCloudDirectorBackupJobApplicationAwareProcessing]
        if isinstance(_app_aware_processing, Unset):
            app_aware_processing = UNSET
        else:
            app_aware_processing = BackupServerCloudDirectorBackupJobApplicationAwareProcessing.from_dict(
                _app_aware_processing
            )

        _guest_fs_indexing = d.pop("guestFSIndexing", UNSET)
        guest_fs_indexing: Union[Unset, BackupServerCloudDirectorBackupJobGuestFileSystemIndexing]
        if isinstance(_guest_fs_indexing, Unset):
            guest_fs_indexing = UNSET
        else:
            guest_fs_indexing = BackupServerCloudDirectorBackupJobGuestFileSystemIndexing.from_dict(_guest_fs_indexing)

        def _parse_guest_interaction_proxies(
            data: object,
        ) -> Union["BackupServerBackupJobGuestInteractionProxiesSettingsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_guest_interaction_proxies_settings_type_0 = (
                    BackupServerBackupJobGuestInteractionProxiesSettingsType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_guest_interaction_proxies_settings_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobGuestInteractionProxiesSettingsType0", None, Unset], data)

        guest_interaction_proxies = _parse_guest_interaction_proxies(d.pop("guestInteractionProxies", UNSET))

        def _parse_guest_credentials(
            data: object,
        ) -> Union["BackupServerBackupJobGuestOsCredentialsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_server_backup_job_guest_os_credentials_type_0 = (
                    BackupServerBackupJobGuestOsCredentialsType0.from_dict(data)
                )

                return componentsschemas_backup_server_backup_job_guest_os_credentials_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupServerBackupJobGuestOsCredentialsType0", None, Unset], data)

        guest_credentials = _parse_guest_credentials(d.pop("guestCredentials", UNSET))

        backup_server_cloud_director_backup_job_guest_processing = cls(
            app_aware_processing=app_aware_processing,
            guest_fs_indexing=guest_fs_indexing,
            guest_interaction_proxies=guest_interaction_proxies,
            guest_credentials=guest_credentials,
        )

        backup_server_cloud_director_backup_job_guest_processing.additional_properties = d
        return backup_server_cloud_director_backup_job_guest_processing

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
