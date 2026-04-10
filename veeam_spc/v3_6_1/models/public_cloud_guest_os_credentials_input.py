from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.public_cloud_guest_os_credentials_input_role import PublicCloudGuestOsCredentialsInputRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudGuestOsCredentialsInput")


@_attrs_define
class PublicCloudGuestOsCredentialsInput:
    """Potential fail on deploying an appliance because of wrong credentials format.

    Attributes:
        role (PublicCloudGuestOsCredentialsInputRole): Role of a user.
        username (str): User name.
        password (str): Password.
        description (Union[None, Unset, str]): Description of a user.
        site_uid (Union[None, UUID, Unset]): Veeam Cloud Connect site UID.
    """

    role: PublicCloudGuestOsCredentialsInputRole
    username: str
    password: str
    description: Union[None, Unset, str] = UNSET
    site_uid: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role.value

        username = self.username

        password = self.password

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        site_uid: Union[None, Unset, str]
        if isinstance(self.site_uid, Unset):
            site_uid = UNSET
        elif isinstance(self.site_uid, UUID):
            site_uid = str(self.site_uid)
        else:
            site_uid = self.site_uid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "username": username,
                "password": password,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role = PublicCloudGuestOsCredentialsInputRole(d.pop("role"))

        username = d.pop("username")

        password = d.pop("password")

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_site_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                site_uid_type_0 = UUID(data)

                return site_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        site_uid = _parse_site_uid(d.pop("siteUid", UNSET))

        public_cloud_guest_os_credentials_input = cls(
            role=role,
            username=username,
            password=password,
            description=description,
            site_uid=site_uid,
        )

        public_cloud_guest_os_credentials_input.additional_properties = d
        return public_cloud_guest_os_credentials_input

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
