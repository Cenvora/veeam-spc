from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_agent_settings import BackupAgentSettings
    from ..models.domain_credentials import DomainCredentials


T = TypeVar("T", bound="DeploymentConfiguration")


@_attrs_define
class DeploymentConfiguration:
    """
    Attributes:
        backup_policy_uid (Union[None, UUID, Unset]): UID of a backup policy that must be assigned to Veeam backup
            agent.
        allow_auto_reboot_if_needed (Union[Unset, bool]): Indicates whether system reboot is allowed. Default: False.
        set_read_only_access (Union[Unset, bool]): Indicates whether the read-only access mode is enabled for Veeam
            backup agents. Default: True.
        install_cbt_driver (Union[Unset, bool]): Indicates whether CBT driver is installed during agent deployment.
            Default: False.
        credentials (Union[Unset, DomainCredentials]):
        backup_agent_settings (Union[Unset, BackupAgentSettings]):
    """

    backup_policy_uid: Union[None, UUID, Unset] = UNSET
    allow_auto_reboot_if_needed: Union[Unset, bool] = False
    set_read_only_access: Union[Unset, bool] = True
    install_cbt_driver: Union[Unset, bool] = False
    credentials: Union[Unset, "DomainCredentials"] = UNSET
    backup_agent_settings: Union[Unset, "BackupAgentSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_policy_uid: Union[None, Unset, str]
        if isinstance(self.backup_policy_uid, Unset):
            backup_policy_uid = UNSET
        elif isinstance(self.backup_policy_uid, UUID):
            backup_policy_uid = str(self.backup_policy_uid)
        else:
            backup_policy_uid = self.backup_policy_uid

        allow_auto_reboot_if_needed = self.allow_auto_reboot_if_needed

        set_read_only_access = self.set_read_only_access

        install_cbt_driver = self.install_cbt_driver

        credentials: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        backup_agent_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.backup_agent_settings, Unset):
            backup_agent_settings = self.backup_agent_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_policy_uid is not UNSET:
            field_dict["backupPolicyUid"] = backup_policy_uid
        if allow_auto_reboot_if_needed is not UNSET:
            field_dict["allowAutoRebootIfNeeded"] = allow_auto_reboot_if_needed
        if set_read_only_access is not UNSET:
            field_dict["setReadOnlyAccess"] = set_read_only_access
        if install_cbt_driver is not UNSET:
            field_dict["installCbtDriver"] = install_cbt_driver
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if backup_agent_settings is not UNSET:
            field_dict["backupAgentSettings"] = backup_agent_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_agent_settings import BackupAgentSettings
        from ..models.domain_credentials import DomainCredentials

        d = dict(src_dict)

        def _parse_backup_policy_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_policy_uid_type_0 = UUID(data)

                return backup_policy_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        backup_policy_uid = _parse_backup_policy_uid(d.pop("backupPolicyUid", UNSET))

        allow_auto_reboot_if_needed = d.pop("allowAutoRebootIfNeeded", UNSET)

        set_read_only_access = d.pop("setReadOnlyAccess", UNSET)

        install_cbt_driver = d.pop("installCbtDriver", UNSET)

        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, DomainCredentials]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = DomainCredentials.from_dict(_credentials)

        _backup_agent_settings = d.pop("backupAgentSettings", UNSET)
        backup_agent_settings: Union[Unset, BackupAgentSettings]
        if isinstance(_backup_agent_settings, Unset):
            backup_agent_settings = UNSET
        else:
            backup_agent_settings = BackupAgentSettings.from_dict(_backup_agent_settings)

        deployment_configuration = cls(
            backup_policy_uid=backup_policy_uid,
            allow_auto_reboot_if_needed=allow_auto_reboot_if_needed,
            set_read_only_access=set_read_only_access,
            install_cbt_driver=install_cbt_driver,
            credentials=credentials,
            backup_agent_settings=backup_agent_settings,
        )

        deployment_configuration.additional_properties = d
        return deployment_configuration

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
