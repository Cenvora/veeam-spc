import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerCredentialsStandardType0")


@_attrs_define
class BackupServerCredentialsStandardType0:
    """
    Attributes:
        instance_uid (UUID): UID assigned to a credentials record.
        username (str): User name.
        description (Union[None, Unset, str]): Description of credentials.'
        creation_time (Union[Unset, datetime.datetime]): Date and time when credentials were created.
        mapped_organization_uid (Union[None, UUID, Unset]): UID of a company to whom credentials are assigned.
        mapped_organization_name (Union[None, Unset, str]): Name of a company to whom credentials are assigned.
    """

    instance_uid: UUID
    username: str
    description: Union[None, Unset, str] = UNSET
    creation_time: Union[Unset, datetime.datetime] = UNSET
    mapped_organization_uid: Union[None, UUID, Unset] = UNSET
    mapped_organization_name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid = str(self.instance_uid)

        username = self.username

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        creation_time: Union[Unset, str] = UNSET
        if not isinstance(self.creation_time, Unset):
            creation_time = self.creation_time.isoformat()

        mapped_organization_uid: Union[None, Unset, str]
        if isinstance(self.mapped_organization_uid, Unset):
            mapped_organization_uid = UNSET
        elif isinstance(self.mapped_organization_uid, UUID):
            mapped_organization_uid = str(self.mapped_organization_uid)
        else:
            mapped_organization_uid = self.mapped_organization_uid

        mapped_organization_name: Union[None, Unset, str]
        if isinstance(self.mapped_organization_name, Unset):
            mapped_organization_name = UNSET
        else:
            mapped_organization_name = self.mapped_organization_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instanceUid": instance_uid,
                "username": username,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if creation_time is not UNSET:
            field_dict["creationTime"] = creation_time
        if mapped_organization_uid is not UNSET:
            field_dict["mappedOrganizationUid"] = mapped_organization_uid
        if mapped_organization_name is not UNSET:
            field_dict["mappedOrganizationName"] = mapped_organization_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        instance_uid = UUID(d.pop("instanceUid"))

        username = d.pop("username")

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        _creation_time = d.pop("creationTime", UNSET)
        creation_time: Union[Unset, datetime.datetime]
        if isinstance(_creation_time, Unset):
            creation_time = UNSET
        else:
            creation_time = isoparse(_creation_time)

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

        def _parse_mapped_organization_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mapped_organization_name = _parse_mapped_organization_name(d.pop("mappedOrganizationName", UNSET))

        backup_server_credentials_standard_type_0 = cls(
            instance_uid=instance_uid,
            username=username,
            description=description,
            creation_time=creation_time,
            mapped_organization_uid=mapped_organization_uid,
            mapped_organization_name=mapped_organization_name,
        )

        backup_server_credentials_standard_type_0.additional_properties = d
        return backup_server_credentials_standard_type_0

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
