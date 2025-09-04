from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinuxDiscoveryRuleDeploymentSettings")


@_attrs_define
class LinuxDiscoveryRuleDeploymentSettings:
    """
    Attributes:
        is_enabled (Union[Unset, bool]): Indicates whether Veeam backup agent is automatically installed on computers as
            part of discovery. Default: False.
        backup_policy_uid (Union[Unset, UUID]): UID of a discovery rule that must be assigned after installation.
        set_read_only_access (Union[Unset, bool]): Indicates whether the read-only access mode is enabled for Veeam
            Agent for Linux. Default: True.
    """

    is_enabled: Union[Unset, bool] = False
    backup_policy_uid: Union[Unset, UUID] = UNSET
    set_read_only_access: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        backup_policy_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_policy_uid, Unset):
            backup_policy_uid = str(self.backup_policy_uid)

        set_read_only_access = self.set_read_only_access

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if backup_policy_uid is not UNSET:
            field_dict["backupPolicyUid"] = backup_policy_uid
        if set_read_only_access is not UNSET:
            field_dict["setReadOnlyAccess"] = set_read_only_access

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_enabled = d.pop("isEnabled", UNSET)

        _backup_policy_uid = d.pop("backupPolicyUid", UNSET)
        backup_policy_uid: Union[Unset, UUID]
        if isinstance(_backup_policy_uid, Unset):
            backup_policy_uid = UNSET
        else:
            backup_policy_uid = UUID(_backup_policy_uid)

        set_read_only_access = d.pop("setReadOnlyAccess", UNSET)

        linux_discovery_rule_deployment_settings = cls(
            is_enabled=is_enabled,
            backup_policy_uid=backup_policy_uid,
            set_read_only_access=set_read_only_access,
        )

        linux_discovery_rule_deployment_settings.additional_properties = d
        return linux_discovery_rule_deployment_settings

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
