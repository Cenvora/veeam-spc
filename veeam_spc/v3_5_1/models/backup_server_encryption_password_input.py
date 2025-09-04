from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerEncryptionPasswordInput")


@_attrs_define
class BackupServerEncryptionPasswordInput:
    """
    Attributes:
        password (str): Veeam Backup & Replication encryption password.
        hint (str): Hint for a Veeam Backup & Replication server encryption password.
        unique_id (Union[Unset, str]): Unique ID assigned to a Veeam Backup & Replication server encryption password.
        mapped_organization_uid (Union[Unset, UUID]): UID of a company to whom a Veeam Backup & Replication server
            encryption password is assigned.
        mapped_organization_name (Union[Unset, str]): Name of a company to whom a Veeam Backup & Replication server
            encryption password is assigned.
    """

    password: str
    hint: str
    unique_id: Union[Unset, str] = UNSET
    mapped_organization_uid: Union[Unset, UUID] = UNSET
    mapped_organization_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        password = self.password

        hint = self.hint

        unique_id = self.unique_id

        mapped_organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.mapped_organization_uid, Unset):
            mapped_organization_uid = str(self.mapped_organization_uid)

        mapped_organization_name = self.mapped_organization_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "password": password,
                "hint": hint,
            }
        )
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id
        if mapped_organization_uid is not UNSET:
            field_dict["mappedOrganizationUid"] = mapped_organization_uid
        if mapped_organization_name is not UNSET:
            field_dict["mappedOrganizationName"] = mapped_organization_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        password = d.pop("password")

        hint = d.pop("hint")

        unique_id = d.pop("uniqueId", UNSET)

        _mapped_organization_uid = d.pop("mappedOrganizationUid", UNSET)
        mapped_organization_uid: Union[Unset, UUID]
        if isinstance(_mapped_organization_uid, Unset):
            mapped_organization_uid = UNSET
        else:
            mapped_organization_uid = UUID(_mapped_organization_uid)

        mapped_organization_name = d.pop("mappedOrganizationName", UNSET)

        backup_server_encryption_password_input = cls(
            password=password,
            hint=hint,
            unique_id=unique_id,
            mapped_organization_uid=mapped_organization_uid,
            mapped_organization_name=mapped_organization_name,
        )

        backup_server_encryption_password_input.additional_properties = d
        return backup_server_encryption_password_input

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
