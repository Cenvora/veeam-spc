from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_backup_job_application_aware_processing import (
        BackupServerBackupJobApplicationAwareProcessing,
    )
    from ..models.backup_server_backup_job_guest_file_system_indexing import (
        BackupServerBackupJobGuestFileSystemIndexing,
    )
    from ..models.backup_server_backup_job_guest_interaction_proxies_settings import (
        BackupServerBackupJobGuestInteractionProxiesSettings,
    )
    from ..models.backup_server_backup_job_guest_os_credentials import BackupServerBackupJobGuestOsCredentials


T = TypeVar("T", bound="BackupServerBackupJobGuestProcessing")


@_attrs_define
class BackupServerBackupJobGuestProcessing:
    """Guest processing settings.

    Attributes:
        app_aware_processing (BackupServerBackupJobApplicationAwareProcessing | Unset): Application-aware processing
            settings.
        guest_fs_indexing (BackupServerBackupJobGuestFileSystemIndexing | Unset): Guest OS file indexing.
        guest_interaction_proxies (BackupServerBackupJobGuestInteractionProxiesSettings | Unset): Interaction proxy
            settings.
        guest_credentials (BackupServerBackupJobGuestOsCredentials | Unset): VM custom credentials.
    """

    app_aware_processing: BackupServerBackupJobApplicationAwareProcessing | Unset = UNSET
    guest_fs_indexing: BackupServerBackupJobGuestFileSystemIndexing | Unset = UNSET
    guest_interaction_proxies: BackupServerBackupJobGuestInteractionProxiesSettings | Unset = UNSET
    guest_credentials: BackupServerBackupJobGuestOsCredentials | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_aware_processing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.app_aware_processing, Unset):
            app_aware_processing = self.app_aware_processing.to_dict()

        guest_fs_indexing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.guest_fs_indexing, Unset):
            guest_fs_indexing = self.guest_fs_indexing.to_dict()

        guest_interaction_proxies: dict[str, Any] | Unset = UNSET
        if not isinstance(self.guest_interaction_proxies, Unset):
            guest_interaction_proxies = self.guest_interaction_proxies.to_dict()

        guest_credentials: dict[str, Any] | Unset = UNSET
        if not isinstance(self.guest_credentials, Unset):
            guest_credentials = self.guest_credentials.to_dict()

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
        from ..models.backup_server_backup_job_application_aware_processing import (
            BackupServerBackupJobApplicationAwareProcessing,
        )
        from ..models.backup_server_backup_job_guest_file_system_indexing import (
            BackupServerBackupJobGuestFileSystemIndexing,
        )
        from ..models.backup_server_backup_job_guest_interaction_proxies_settings import (
            BackupServerBackupJobGuestInteractionProxiesSettings,
        )
        from ..models.backup_server_backup_job_guest_os_credentials import BackupServerBackupJobGuestOsCredentials

        d = dict(src_dict)
        _app_aware_processing = d.pop("appAwareProcessing", UNSET)
        app_aware_processing: BackupServerBackupJobApplicationAwareProcessing | Unset
        if isinstance(_app_aware_processing, Unset):
            app_aware_processing = UNSET
        else:
            app_aware_processing = BackupServerBackupJobApplicationAwareProcessing.from_dict(_app_aware_processing)

        _guest_fs_indexing = d.pop("guestFSIndexing", UNSET)
        guest_fs_indexing: BackupServerBackupJobGuestFileSystemIndexing | Unset
        if isinstance(_guest_fs_indexing, Unset):
            guest_fs_indexing = UNSET
        else:
            guest_fs_indexing = BackupServerBackupJobGuestFileSystemIndexing.from_dict(_guest_fs_indexing)

        _guest_interaction_proxies = d.pop("guestInteractionProxies", UNSET)
        guest_interaction_proxies: BackupServerBackupJobGuestInteractionProxiesSettings | Unset
        if isinstance(_guest_interaction_proxies, Unset):
            guest_interaction_proxies = UNSET
        else:
            guest_interaction_proxies = BackupServerBackupJobGuestInteractionProxiesSettings.from_dict(
                _guest_interaction_proxies
            )

        _guest_credentials = d.pop("guestCredentials", UNSET)
        guest_credentials: BackupServerBackupJobGuestOsCredentials | Unset
        if isinstance(_guest_credentials, Unset):
            guest_credentials = UNSET
        else:
            guest_credentials = BackupServerBackupJobGuestOsCredentials.from_dict(_guest_credentials)

        backup_server_backup_job_guest_processing = cls(
            app_aware_processing=app_aware_processing,
            guest_fs_indexing=guest_fs_indexing,
            guest_interaction_proxies=guest_interaction_proxies,
            guest_credentials=guest_credentials,
        )

        backup_server_backup_job_guest_processing.additional_properties = d
        return backup_server_backup_job_guest_processing

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
