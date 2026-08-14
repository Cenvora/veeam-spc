from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linux_discovery_credentials import LinuxDiscoveryCredentials


T = TypeVar("T", bound="LinuxDeploymentConfiguration")


@_attrs_define
class LinuxDeploymentConfiguration:
    """
    Example:
        {'backupPolicyUid': None, 'setReadOnlyAccess': True, 'credentials': None}

    Attributes:
        backup_policy_uid (UUID | Unset): UID of a backup policy that is assigned to Veeam Agent for Linux.
        set_read_only_access (bool | Unset): Indicates whether the read-only access mode is enabled for Veeam Agent for
            Linux. Default: True.
        credentials (list[LinuxDiscoveryCredentials] | Unset): Credentials required to access discovered computers.
    """

    backup_policy_uid: UUID | Unset = UNSET
    set_read_only_access: bool | Unset = True
    credentials: list[LinuxDiscoveryCredentials] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_policy_uid: str | Unset = UNSET
        if not isinstance(self.backup_policy_uid, Unset):
            backup_policy_uid = str(self.backup_policy_uid)

        set_read_only_access = self.set_read_only_access

        credentials: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = []
            for credentials_item_data in self.credentials:
                credentials_item = credentials_item_data.to_dict()
                credentials.append(credentials_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_policy_uid is not UNSET:
            field_dict["backupPolicyUid"] = backup_policy_uid
        if set_read_only_access is not UNSET:
            field_dict["setReadOnlyAccess"] = set_read_only_access
        if credentials is not UNSET:
            field_dict["credentials"] = credentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linux_discovery_credentials import LinuxDiscoveryCredentials

        d = dict(src_dict)
        _backup_policy_uid = d.pop("backupPolicyUid", UNSET)
        backup_policy_uid: UUID | Unset
        if isinstance(_backup_policy_uid, Unset):
            backup_policy_uid = UNSET
        else:
            backup_policy_uid = UUID(_backup_policy_uid)

        set_read_only_access = d.pop("setReadOnlyAccess", UNSET)

        _credentials = d.pop("credentials", UNSET)
        credentials: list[LinuxDiscoveryCredentials] | Unset = UNSET
        if _credentials is not UNSET:
            credentials = []
            for credentials_item_data in _credentials:
                credentials_item = LinuxDiscoveryCredentials.from_dict(credentials_item_data)

                credentials.append(credentials_item)

        linux_deployment_configuration = cls(
            backup_policy_uid=backup_policy_uid,
            set_read_only_access=set_read_only_access,
            credentials=credentials,
        )

        linux_deployment_configuration.additional_properties = d
        return linux_deployment_configuration

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
