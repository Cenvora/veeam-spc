from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
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
    Attributes:
        backup_policy_uid (None | Unset | UUID): UID of a backup policy that is assigned to Veeam Agent for Linux.
        set_read_only_access (bool | Unset): Indicates whether the read-only access mode is enabled for Veeam Agent for
            Linux. Default: True.
        credentials (list[LinuxDiscoveryCredentials] | None | Unset): Credentials required to access discovered
            computers.
    """

    backup_policy_uid: None | Unset | UUID = UNSET
    set_read_only_access: bool | Unset = True
    credentials: list[LinuxDiscoveryCredentials] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_policy_uid: None | str | Unset
        if isinstance(self.backup_policy_uid, Unset):
            backup_policy_uid = UNSET
        elif isinstance(self.backup_policy_uid, UUID):
            backup_policy_uid = str(self.backup_policy_uid)
        else:
            backup_policy_uid = self.backup_policy_uid

        set_read_only_access = self.set_read_only_access

        credentials: list[dict[str, Any]] | None | Unset
        if isinstance(self.credentials, Unset):
            credentials = UNSET
        elif isinstance(self.credentials, list):
            credentials = []
            for credentials_type_0_item_data in self.credentials:
                credentials_type_0_item = credentials_type_0_item_data.to_dict()
                credentials.append(credentials_type_0_item)

        else:
            credentials = self.credentials

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

        def _parse_backup_policy_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_policy_uid_type_0 = UUID(data)

                return backup_policy_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        backup_policy_uid = _parse_backup_policy_uid(d.pop("backupPolicyUid", UNSET))

        set_read_only_access = d.pop("setReadOnlyAccess", UNSET)

        def _parse_credentials(data: object) -> list[LinuxDiscoveryCredentials] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                credentials_type_0 = []
                _credentials_type_0 = data
                for credentials_type_0_item_data in _credentials_type_0:
                    credentials_type_0_item = LinuxDiscoveryCredentials.from_dict(credentials_type_0_item_data)

                    credentials_type_0.append(credentials_type_0_item)

                return credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LinuxDiscoveryCredentials] | None | Unset, data)

        credentials = _parse_credentials(d.pop("credentials", UNSET))

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
