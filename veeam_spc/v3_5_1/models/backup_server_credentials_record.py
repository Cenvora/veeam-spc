import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.backup_server_credentials_type import BackupServerCredentialsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_credentials_record_linux_details import BackupServerCredentialsRecordLinuxDetails


T = TypeVar("T", bound="BackupServerCredentialsRecord")


@_attrs_define
class BackupServerCredentialsRecord:
    """Veeam Backup & Replication credentials.

    Attributes:
        instance_uid (UUID): UID assigned to credentials record.
        type_ (BackupServerCredentialsType): Credentials type.
        username (str): User name.
        creation_time (datetime.datetime): Date and time when credentials were created.
        description (Union[Unset, str]): Description of credentials.
        mapped_organization_uid (Union[Unset, UUID]): UID of a company to whom credentials are assigned.
        mapped_organization_name (Union[Unset, str]): Name of a company to whom credentials are assigned.
        linux_credentials_details (Union[Unset, BackupServerCredentialsRecordLinuxDetails]): Details of credentials used
            to access Linux computers.
    """

    instance_uid: UUID
    type_: BackupServerCredentialsType
    username: str
    creation_time: datetime.datetime
    description: Union[Unset, str] = UNSET
    mapped_organization_uid: Union[Unset, UUID] = UNSET
    mapped_organization_name: Union[Unset, str] = UNSET
    linux_credentials_details: Union[Unset, "BackupServerCredentialsRecordLinuxDetails"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid = str(self.instance_uid)

        type_ = self.type_.value

        username = self.username

        creation_time = self.creation_time.isoformat()

        description = self.description

        mapped_organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.mapped_organization_uid, Unset):
            mapped_organization_uid = str(self.mapped_organization_uid)

        mapped_organization_name = self.mapped_organization_name

        linux_credentials_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.linux_credentials_details, Unset):
            linux_credentials_details = self.linux_credentials_details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instanceUid": instance_uid,
                "type": type_,
                "username": username,
                "creationTime": creation_time,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if mapped_organization_uid is not UNSET:
            field_dict["mappedOrganizationUid"] = mapped_organization_uid
        if mapped_organization_name is not UNSET:
            field_dict["mappedOrganizationName"] = mapped_organization_name
        if linux_credentials_details is not UNSET:
            field_dict["linuxCredentialsDetails"] = linux_credentials_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_credentials_record_linux_details import BackupServerCredentialsRecordLinuxDetails

        d = dict(src_dict)
        instance_uid = UUID(d.pop("instanceUid"))

        type_ = BackupServerCredentialsType(d.pop("type"))

        username = d.pop("username")

        creation_time = isoparse(d.pop("creationTime"))

        description = d.pop("description", UNSET)

        _mapped_organization_uid = d.pop("mappedOrganizationUid", UNSET)
        mapped_organization_uid: Union[Unset, UUID]
        if isinstance(_mapped_organization_uid, Unset):
            mapped_organization_uid = UNSET
        else:
            mapped_organization_uid = UUID(_mapped_organization_uid)

        mapped_organization_name = d.pop("mappedOrganizationName", UNSET)

        _linux_credentials_details = d.pop("linuxCredentialsDetails", UNSET)
        linux_credentials_details: Union[Unset, BackupServerCredentialsRecordLinuxDetails]
        if isinstance(_linux_credentials_details, Unset):
            linux_credentials_details = UNSET
        else:
            linux_credentials_details = BackupServerCredentialsRecordLinuxDetails.from_dict(_linux_credentials_details)

        backup_server_credentials_record = cls(
            instance_uid=instance_uid,
            type_=type_,
            username=username,
            creation_time=creation_time,
            description=description,
            mapped_organization_uid=mapped_organization_uid,
            mapped_organization_name=mapped_organization_name,
            linux_credentials_details=linux_credentials_details,
        )

        backup_server_credentials_record.additional_properties = d
        return backup_server_credentials_record

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
