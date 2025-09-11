from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudRepositoryConnectionSettings")


@_attrs_define
class CloudRepositoryConnectionSettings:
    """Settings required to connect a cloud repository that is used as a target location for backups.

    Attributes:
        backup_resource_uid (UUID): UID assigned to a cloud repository.'
        username (str): User name.
        password (Union[Unset, str]): Password.
    """

    backup_resource_uid: UUID
    username: str
    password: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_resource_uid = str(self.backup_resource_uid)

        username = self.username

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backupResourceUid": backup_resource_uid,
                "username": username,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backup_resource_uid = UUID(d.pop("backupResourceUid"))

        username = d.pop("username")

        password = d.pop("password", UNSET)

        cloud_repository_connection_settings = cls(
            backup_resource_uid=backup_resource_uid,
            username=username,
            password=password,
        )

        cloud_repository_connection_settings.additional_properties = d
        return cloud_repository_connection_settings

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
