import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.public_cloud_guest_os_credentials_role import PublicCloudGuestOsCredentialsRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudGuestOsCredentials")


@_attrs_define
class PublicCloudGuestOsCredentials:
    """
    Attributes:
        password (str): Password.
        guest_os_credentials_uid (Union[Unset, UUID]): UID assgined to guest OS credentials record.
        role (Union[Unset, PublicCloudGuestOsCredentialsRole]):
        username (Union[Unset, str]): User name.
        description (Union[Unset, str]): Description of credentials.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization to which an account belongs.
        site_uid (Union[Unset, UUID]): UID assigned to a Veeam Cloud Connect site.
        appliances (Union[Unset, list[UUID]]): Array of UIDs assigned to Veeam Backup for Public Clouds appliances that
            can be accessed using the credentials.
        last_change_timestamp (Union[Unset, datetime.datetime]): Date and time when the latest change was applied to
            credentials.
    """

    password: str
    guest_os_credentials_uid: Union[Unset, UUID] = UNSET
    role: Union[Unset, PublicCloudGuestOsCredentialsRole] = UNSET
    username: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    site_uid: Union[Unset, UUID] = UNSET
    appliances: Union[Unset, list[UUID]] = UNSET
    last_change_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        password = self.password

        guest_os_credentials_uid: Union[Unset, str] = UNSET
        if not isinstance(self.guest_os_credentials_uid, Unset):
            guest_os_credentials_uid = str(self.guest_os_credentials_uid)

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        username = self.username

        description = self.description

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        site_uid: Union[Unset, str] = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        appliances: Union[Unset, list[str]] = UNSET
        if not isinstance(self.appliances, Unset):
            appliances = []
            for appliances_item_data in self.appliances:
                appliances_item = str(appliances_item_data)
                appliances.append(appliances_item)

        last_change_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.last_change_timestamp, Unset):
            last_change_timestamp = self.last_change_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "password": password,
            }
        )
        if guest_os_credentials_uid is not UNSET:
            field_dict["guestOsCredentialsUid"] = guest_os_credentials_uid
        if role is not UNSET:
            field_dict["role"] = role
        if username is not UNSET:
            field_dict["username"] = username
        if description is not UNSET:
            field_dict["description"] = description
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid
        if appliances is not UNSET:
            field_dict["appliances"] = appliances
        if last_change_timestamp is not UNSET:
            field_dict["lastChangeTimestamp"] = last_change_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        password = d.pop("password")

        _guest_os_credentials_uid = d.pop("guestOsCredentialsUid", UNSET)
        guest_os_credentials_uid: Union[Unset, UUID]
        if isinstance(_guest_os_credentials_uid, Unset):
            guest_os_credentials_uid = UNSET
        else:
            guest_os_credentials_uid = UUID(_guest_os_credentials_uid)

        _role = d.pop("role", UNSET)
        role: Union[Unset, PublicCloudGuestOsCredentialsRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = PublicCloudGuestOsCredentialsRole(_role)

        username = d.pop("username", UNSET)

        description = d.pop("description", UNSET)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        _site_uid = d.pop("siteUid", UNSET)
        site_uid: Union[Unset, UUID]
        if isinstance(_site_uid, Unset):
            site_uid = UNSET
        else:
            site_uid = UUID(_site_uid)

        appliances = []
        _appliances = d.pop("appliances", UNSET)
        for appliances_item_data in _appliances or []:
            appliances_item = UUID(appliances_item_data)

            appliances.append(appliances_item)

        _last_change_timestamp = d.pop("lastChangeTimestamp", UNSET)
        last_change_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_last_change_timestamp, Unset):
            last_change_timestamp = UNSET
        else:
            last_change_timestamp = isoparse(_last_change_timestamp)

        public_cloud_guest_os_credentials = cls(
            password=password,
            guest_os_credentials_uid=guest_os_credentials_uid,
            role=role,
            username=username,
            description=description,
            organization_uid=organization_uid,
            site_uid=site_uid,
            appliances=appliances,
            last_change_timestamp=last_change_timestamp,
        )

        public_cloud_guest_os_credentials.additional_properties = d
        return public_cloud_guest_os_credentials

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
