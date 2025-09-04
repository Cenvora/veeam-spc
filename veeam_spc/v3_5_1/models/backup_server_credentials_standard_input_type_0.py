from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerCredentialsStandardInputType0")


@_attrs_define
class BackupServerCredentialsStandardInputType0:
    """
    Attributes:
        username (str): User name.
        password (str): Password.
        description (Union[None, Unset, str]): Credentials description.
        mapped_organization_uid (Union[None, UUID, Unset]): UID of a company to whom credentials are assigned.
    """

    username: str
    password: str
    description: Union[None, Unset, str] = UNSET
    mapped_organization_uid: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        mapped_organization_uid: Union[None, Unset, str]
        if isinstance(self.mapped_organization_uid, Unset):
            mapped_organization_uid = UNSET
        elif isinstance(self.mapped_organization_uid, UUID):
            mapped_organization_uid = str(self.mapped_organization_uid)
        else:
            mapped_organization_uid = self.mapped_organization_uid

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

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_mapped_organization_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mapped_organization_uid_type_0 = UUID(data)

                return mapped_organization_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        mapped_organization_uid = _parse_mapped_organization_uid(d.pop("mappedOrganizationUid", UNSET))

        backup_server_credentials_standard_input_type_0 = cls(
            username=username,
            password=password,
            description=description,
            mapped_organization_uid=mapped_organization_uid,
        )

        backup_server_credentials_standard_input_type_0.additional_properties = d
        return backup_server_credentials_standard_input_type_0

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
