from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudRepositoryConnectionSettingsType0")


@_attrs_define
class CloudRepositoryConnectionSettingsType0:
    """Settings required to connect a cloud repository that is used as a target location for backups.

    Attributes:
        backup_resource_uid (UUID): UID assigned to a cloud repository.'
        username (str): User name.
        password (Union[None, Unset, str]): Password.
    """

    backup_resource_uid: UUID
    username: str
    password: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_resource_uid = str(self.backup_resource_uid)

        username = self.username

        password: Union[None, Unset, str]
        if isinstance(self.password, Unset):
            password = UNSET
        else:
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

        def _parse_password(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        password = _parse_password(d.pop("password", UNSET))

        cloud_repository_connection_settings_type_0 = cls(
            backup_resource_uid=backup_resource_uid,
            username=username,
            password=password,
        )

        cloud_repository_connection_settings_type_0.additional_properties = d
        return cloud_repository_connection_settings_type_0

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
