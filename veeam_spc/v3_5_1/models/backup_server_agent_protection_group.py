from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerAgentProtectionGroup")


@_attrs_define
class BackupServerAgentProtectionGroup:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a server.
        name (Union[Unset, str]): Host name of a server.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup & Replication server.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if name is not UNSET:
            field_dict["name"] = name
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        name = d.pop("name", UNSET)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: Union[Unset, UUID]
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        backup_server_agent_protection_group = cls(
            instance_uid=instance_uid,
            name=name,
            backup_server_uid=backup_server_uid,
        )

        backup_server_agent_protection_group.additional_properties = d
        return backup_server_agent_protection_group

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
