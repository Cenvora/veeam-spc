import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
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
        job_uid (Union[None, UUID, Unset]): UID assigned to a backup job that created the restore point.
        backedup_items (Union[Unset, str]): Protected objects.
        destination (Union[Unset, str]): Path to the protected object locations.
        size (Union[None, Unset, int]): Size of the restore point, in bytes.
        increment_raw_data_size (Union[None, Unset, int]): Size of backup increment, in bytes.
        source_size (Union[None, Unset, int]): Size of the protected data, in bytes.
        creation_date (Union[None, Unset, datetime.datetime]): Date of the restore point creation.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    backup_agent_uid: Union[Unset, UUID] = UNSET
    job_uid: Union[None, UUID, Unset] = UNSET
    backedup_items: Union[Unset, str] = UNSET
    destination: Union[Unset, str] = UNSET
    size: Union[None, Unset, int] = UNSET
    increment_raw_data_size: Union[None, Unset, int] = UNSET
    source_size: Union[None, Unset, int] = UNSET
    creation_date: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        backup_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_agent_uid, Unset):
            backup_agent_uid = str(self.backup_agent_uid)

        job_uid: Union[None, Unset, str]
        if isinstance(self.job_uid, Unset):
            job_uid = UNSET
        elif isinstance(self.job_uid, UUID):
            job_uid = str(self.job_uid)
        else:
            job_uid = self.job_uid

        backedup_items = self.backedup_items

        destination = self.destination

        size: Union[None, Unset, int]
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        increment_raw_data_size: Union[None, Unset, int]
        if isinstance(self.increment_raw_data_size, Unset):
            increment_raw_data_size = UNSET
        else:
            increment_raw_data_size = self.increment_raw_data_size

        source_size: Union[None, Unset, int]
        if isinstance(self.source_size, Unset):
            source_size = UNSET
        else:
            source_size = self.source_size

        creation_date: Union[None, Unset, str]
        if isinstance(self.creation_date, Unset):
            creation_date = UNSET
        elif isinstance(self.creation_date, datetime.datetime):
            creation_date = self.creation_date.isoformat()
        else:
            creation_date = self.creation_date

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

        def _parse_job_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_uid_type_0 = UUID(data)

                return job_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        job_uid = _parse_job_uid(d.pop("jobUid", UNSET))

        backedup_items = d.pop("backedupItems", UNSET)

        destination = d.pop("destination", UNSET)

        def _parse_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        size = _parse_size(d.pop("size", UNSET))

        def _parse_increment_raw_data_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        increment_raw_data_size = _parse_increment_raw_data_size(d.pop("incrementRawDataSize", UNSET))

        def _parse_source_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        source_size = _parse_source_size(d.pop("sourceSize", UNSET))

        def _parse_creation_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                creation_date_type_0 = isoparse(data)

                return creation_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        creation_date = _parse_creation_date(d.pop("creationDate", UNSET))

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
