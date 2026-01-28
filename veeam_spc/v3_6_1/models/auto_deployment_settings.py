from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_agent_settings import BackupAgentSettings


T = TypeVar("T", bound="AutoDeploymentSettings")


@_attrs_define
class AutoDeploymentSettings:
    """
    Attributes:
        organization_uid (Union[Unset, UUID]): UID assigned to an organization that manages Veeam backup agent auto
            deployment.
        is_enabled (Union[Unset, bool]): Indicates whether auto deployment is enabled. Default: False.
        windows_backup_policy_uid (Union[None, UUID, Unset]): UID of a backup policy that must be assigned to a Veeam
            Agent for Microsoft Windows.
        linux_backup_policy_uid (Union[None, UUID, Unset]): UID of a backup policy that must be assigned to a Veeam
            Agent for Linux.
        mac_backup_policy_uid (Union[None, UUID, Unset]): UID of a backup policy that must be assigned to a Veeam Agent
            for Mac.
        is_retry_enabled (Union[Unset, bool]): Indicates whether retry is enabled in case deployment session fails.
            Default: False.
        retry_count (Union[Unset, int]): Number of allowed retries. Default: 3.
        retry_interval (Union[Unset, int]): Time interval in minutes after which the next deployment attempt starts.
            Default: 7.
        accept_new_connections (Union[Unset, bool]): Indicates whether Veeam Service Provider Console accepts
            connections from new management agents. Default: True.
        install_driver (Union[Unset, bool]): Indicates whether CBT driver is installed during auto deployment. Default:
            False.
        set_read_only_access (Union[Unset, bool]): Indicates whether the read-only access mode is enabled for Veeam
            backup agent. Default: True.
        backup_agent_settings (Union[Unset, BackupAgentSettings]):
    """

    organization_uid: Union[Unset, UUID] = UNSET
    is_enabled: Union[Unset, bool] = False
    windows_backup_policy_uid: Union[None, UUID, Unset] = UNSET
    linux_backup_policy_uid: Union[None, UUID, Unset] = UNSET
    mac_backup_policy_uid: Union[None, UUID, Unset] = UNSET
    is_retry_enabled: Union[Unset, bool] = False
    retry_count: Union[Unset, int] = 3
    retry_interval: Union[Unset, int] = 7
    accept_new_connections: Union[Unset, bool] = True
    install_driver: Union[Unset, bool] = False
    set_read_only_access: Union[Unset, bool] = True
    backup_agent_settings: Union[Unset, "BackupAgentSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        is_enabled = self.is_enabled

        windows_backup_policy_uid: Union[None, Unset, str]
        if isinstance(self.windows_backup_policy_uid, Unset):
            windows_backup_policy_uid = UNSET
        elif isinstance(self.windows_backup_policy_uid, UUID):
            windows_backup_policy_uid = str(self.windows_backup_policy_uid)
        else:
            windows_backup_policy_uid = self.windows_backup_policy_uid

        linux_backup_policy_uid: Union[None, Unset, str]
        if isinstance(self.linux_backup_policy_uid, Unset):
            linux_backup_policy_uid = UNSET
        elif isinstance(self.linux_backup_policy_uid, UUID):
            linux_backup_policy_uid = str(self.linux_backup_policy_uid)
        else:
            linux_backup_policy_uid = self.linux_backup_policy_uid

        mac_backup_policy_uid: Union[None, Unset, str]
        if isinstance(self.mac_backup_policy_uid, Unset):
            mac_backup_policy_uid = UNSET
        elif isinstance(self.mac_backup_policy_uid, UUID):
            mac_backup_policy_uid = str(self.mac_backup_policy_uid)
        else:
            mac_backup_policy_uid = self.mac_backup_policy_uid

        is_retry_enabled = self.is_retry_enabled

        retry_count = self.retry_count

        retry_interval = self.retry_interval

        accept_new_connections = self.accept_new_connections

        install_driver = self.install_driver

        set_read_only_access = self.set_read_only_access

        backup_agent_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.backup_agent_settings, Unset):
            backup_agent_settings = self.backup_agent_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if windows_backup_policy_uid is not UNSET:
            field_dict["windowsBackupPolicyUid"] = windows_backup_policy_uid
        if linux_backup_policy_uid is not UNSET:
            field_dict["linuxBackupPolicyUid"] = linux_backup_policy_uid
        if mac_backup_policy_uid is not UNSET:
            field_dict["macBackupPolicyUid"] = mac_backup_policy_uid
        if is_retry_enabled is not UNSET:
            field_dict["isRetryEnabled"] = is_retry_enabled
        if retry_count is not UNSET:
            field_dict["retryCount"] = retry_count
        if retry_interval is not UNSET:
            field_dict["retryInterval"] = retry_interval
        if accept_new_connections is not UNSET:
            field_dict["acceptNewConnections"] = accept_new_connections
        if install_driver is not UNSET:
            field_dict["installDriver"] = install_driver
        if set_read_only_access is not UNSET:
            field_dict["setReadOnlyAccess"] = set_read_only_access
        if backup_agent_settings is not UNSET:
            field_dict["backupAgentSettings"] = backup_agent_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_agent_settings import BackupAgentSettings

        d = dict(src_dict)
        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        is_enabled = d.pop("isEnabled", UNSET)

        def _parse_windows_backup_policy_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                windows_backup_policy_uid_type_0 = UUID(data)

                return windows_backup_policy_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        windows_backup_policy_uid = _parse_windows_backup_policy_uid(d.pop("windowsBackupPolicyUid", UNSET))

        def _parse_linux_backup_policy_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                linux_backup_policy_uid_type_0 = UUID(data)

                return linux_backup_policy_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        linux_backup_policy_uid = _parse_linux_backup_policy_uid(d.pop("linuxBackupPolicyUid", UNSET))

        def _parse_mac_backup_policy_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mac_backup_policy_uid_type_0 = UUID(data)

                return mac_backup_policy_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        mac_backup_policy_uid = _parse_mac_backup_policy_uid(d.pop("macBackupPolicyUid", UNSET))

        is_retry_enabled = d.pop("isRetryEnabled", UNSET)

        retry_count = d.pop("retryCount", UNSET)

        retry_interval = d.pop("retryInterval", UNSET)

        accept_new_connections = d.pop("acceptNewConnections", UNSET)

        install_driver = d.pop("installDriver", UNSET)

        set_read_only_access = d.pop("setReadOnlyAccess", UNSET)

        _backup_agent_settings = d.pop("backupAgentSettings", UNSET)
        backup_agent_settings: Union[Unset, BackupAgentSettings]
        if isinstance(_backup_agent_settings, Unset):
            backup_agent_settings = UNSET
        else:
            backup_agent_settings = BackupAgentSettings.from_dict(_backup_agent_settings)

        auto_deployment_settings = cls(
            organization_uid=organization_uid,
            is_enabled=is_enabled,
            windows_backup_policy_uid=windows_backup_policy_uid,
            linux_backup_policy_uid=linux_backup_policy_uid,
            mac_backup_policy_uid=mac_backup_policy_uid,
            is_retry_enabled=is_retry_enabled,
            retry_count=retry_count,
            retry_interval=retry_interval,
            accept_new_connections=accept_new_connections,
            install_driver=install_driver,
            set_read_only_access=set_read_only_access,
            backup_agent_settings=backup_agent_settings,
        )

        auto_deployment_settings.additional_properties = d
        return auto_deployment_settings

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
