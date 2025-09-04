import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedComputerManagedByConsoleRestorePoint")


@_attrs_define
class ProtectedComputerManagedByConsoleRestorePoint:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a restore point.
        backup_agent_uid (Union[Unset, UUID]): UID assigned to a Veeam backup agent.
        job_uid (Union[Unset, UUID]): UID assigned to a backup job that created the restore point.
        backedup_items (Union[Unset, str]): Protected objects.
        destination (Union[Unset, str]): Path to the protected object locations.
        size (Union[Unset, int]): Size of the restore point, in bytes.
        increment_raw_data_size (Union[Unset, int]): Size of backup increment, in bytes.
        source_size (Union[Unset, int]): Size of the protected data, in bytes.
        creation_date (Union[Unset, datetime.datetime]): Date of the restore point creation.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    backup_agent_uid: Union[Unset, UUID] = UNSET
    job_uid: Union[Unset, UUID] = UNSET
    backedup_items: Union[Unset, str] = UNSET
    destination: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    increment_raw_data_size: Union[Unset, int] = UNSET
    source_size: Union[Unset, int] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        backup_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_agent_uid, Unset):
            backup_agent_uid = str(self.backup_agent_uid)

        job_uid: Union[Unset, str] = UNSET
        if not isinstance(self.job_uid, Unset):
            job_uid = str(self.job_uid)

        backedup_items = self.backedup_items

        destination = self.destination

        size = self.size

        increment_raw_data_size = self.increment_raw_data_size

        source_size = self.source_size

        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if backup_agent_uid is not UNSET:
            field_dict["backupAgentUid"] = backup_agent_uid
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if backedup_items is not UNSET:
            field_dict["backedupItems"] = backedup_items
        if destination is not UNSET:
            field_dict["destination"] = destination
        if size is not UNSET:
            field_dict["size"] = size
        if increment_raw_data_size is not UNSET:
            field_dict["incrementRawDataSize"] = increment_raw_data_size
        if source_size is not UNSET:
            field_dict["sourceSize"] = source_size
        if creation_date is not UNSET:
            field_dict["creationDate"] = creation_date

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

        _backup_agent_uid = d.pop("backupAgentUid", UNSET)
        backup_agent_uid: Union[Unset, UUID]
        if isinstance(_backup_agent_uid, Unset):
            backup_agent_uid = UNSET
        else:
            backup_agent_uid = UUID(_backup_agent_uid)

        _job_uid = d.pop("jobUid", UNSET)
        job_uid: Union[Unset, UUID]
        if isinstance(_job_uid, Unset):
            job_uid = UNSET
        else:
            job_uid = UUID(_job_uid)

        backedup_items = d.pop("backedupItems", UNSET)

        destination = d.pop("destination", UNSET)

        size = d.pop("size", UNSET)

        increment_raw_data_size = d.pop("incrementRawDataSize", UNSET)

        source_size = d.pop("sourceSize", UNSET)

        _creation_date = d.pop("creationDate", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        protected_computer_managed_by_console_restore_point = cls(
            instance_uid=instance_uid,
            backup_agent_uid=backup_agent_uid,
            job_uid=job_uid,
            backedup_items=backedup_items,
            destination=destination,
            size=size,
            increment_raw_data_size=increment_raw_data_size,
            source_size=source_size,
            creation_date=creation_date,
        )

        protected_computer_managed_by_console_restore_point.additional_properties = d
        return protected_computer_managed_by_console_restore_point

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
