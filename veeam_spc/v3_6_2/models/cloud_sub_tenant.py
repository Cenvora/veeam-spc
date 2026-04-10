from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudSubTenant")


@_attrs_define
class CloudSubTenant:
    """
    Example:
        {'instanceUid': '1111568E-F90F-4702-8151-CBE3CE2A8C10', 'tenantUid': '0000568E-F90F-4702-8151-CBE3CE2A8C10',
            'name': 'SubTenant01', 'description': 'SubTenant X for Agent X', 'backupServerUid':
            'DF997BD3-4AE9-4841-8152-8FF5CC703EAB', 'isEnabled': True}

    Attributes:
        instance_uid (UUID | Unset): UID assigned to a subtenant account.
        tenant_uid (UUID | Unset): UID assigned to a tenant that manages a subtenant account.
        name (str | Unset): User name of a subtenant account.
        description (str | Unset): Description of a subtenant account.
        backup_server_uid (UUID | Unset): UID assigned to a Veeam Cloud Connect server.
        is_enabled (bool | Unset): Indicates whether a subtenant account is enabled.
    """

    instance_uid: UUID | Unset = UNSET
    tenant_uid: UUID | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    backup_server_uid: UUID | Unset = UNSET
    is_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        tenant_uid: str | Unset = UNSET
        if not isinstance(self.tenant_uid, Unset):
            tenant_uid = str(self.tenant_uid)

        name = self.name

        description = self.description

        backup_server_uid: str | Unset = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        is_enabled = self.is_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if tenant_uid is not UNSET:
            field_dict["tenantUid"] = tenant_uid
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _tenant_uid = d.pop("tenantUid", UNSET)
        tenant_uid: UUID | Unset
        if isinstance(_tenant_uid, Unset):
            tenant_uid = UNSET
        else:
            tenant_uid = UUID(_tenant_uid)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: UUID | Unset
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        is_enabled = d.pop("isEnabled", UNSET)

        cloud_sub_tenant = cls(
            instance_uid=instance_uid,
            tenant_uid=tenant_uid,
            name=name,
            description=description,
            backup_server_uid=backup_server_uid,
            is_enabled=is_enabled,
        )

        cloud_sub_tenant.additional_properties = d
        return cloud_sub_tenant

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
