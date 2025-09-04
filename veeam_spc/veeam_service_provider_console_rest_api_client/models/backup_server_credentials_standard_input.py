from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerCredentialsStandardInput")


@_attrs_define
class BackupServerCredentialsStandardInput:
    """
    Attributes:
        username (str): User name.
        password (str): Password.
        description (Union[Unset, str]): Credentials description.
        mapped_organization_uid (Union[Unset, UUID]): UID of a company to whom credentials are assigned.
    """

    username: str
    password: str
    description: Union[Unset, str] = UNSET
    mapped_organization_uid: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        description = self.description

        mapped_organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.mapped_organization_uid, Unset):
            mapped_organization_uid = str(self.mapped_organization_uid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "password": password,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if mapped_organization_uid is not UNSET:
            field_dict["mappedOrganizationUid"] = mapped_organization_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        password = d.pop("password")

        description = d.pop("description", UNSET)

        _mapped_organization_uid = d.pop("mappedOrganizationUid", UNSET)
        mapped_organization_uid: Union[Unset, UUID]
        if isinstance(_mapped_organization_uid, Unset):
            mapped_organization_uid = UNSET
        else:
            mapped_organization_uid = UUID(_mapped_organization_uid)

        backup_server_credentials_standard_input = cls(
            username=username,
            password=password,
            description=description,
            mapped_organization_uid=mapped_organization_uid,
        )

        backup_server_credentials_standard_input.additional_properties = d
        return backup_server_credentials_standard_input

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
