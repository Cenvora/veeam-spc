import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.vb_365_restore_point_processed_object_types_item import Vb365RestorePointProcessedObjectTypesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365RestorePoint")


@_attrs_define
class Vb365RestorePoint:
    """
    Attributes:
        id (Union[Unset, UUID]): ID assigned to a restore point.
        protected_object_id (Union[Unset, UUID]): ID assigned to an object protected by Veeam Backup for Microsoft 365.
        vb_365_job_uid (Union[Unset, UUID]): UID assigned to a backup job.
        repository_uid (Union[Unset, UUID]): UID assigned to a backup repository.
        repository_name (Union[Unset, str]): Name of a backup repository.
        backup_time (Union[Unset, datetime.datetime]): Date and time when a restore point was created.
        is_archive (Union[Unset, bool]): Indicates whether restore point is archive.
        processed_object_types (Union[Unset, list[Vb365RestorePointProcessedObjectTypesItem]]): Array of protected
            object types.
        processed_object_types_str (Union[Unset, str]): String representation of protected object type array.
    """

    id: Union[Unset, UUID] = UNSET
    protected_object_id: Union[Unset, UUID] = UNSET
    vb_365_job_uid: Union[Unset, UUID] = UNSET
    repository_uid: Union[Unset, UUID] = UNSET
    repository_name: Union[Unset, str] = UNSET
    backup_time: Union[Unset, datetime.datetime] = UNSET
    is_archive: Union[Unset, bool] = UNSET
    processed_object_types: Union[Unset, list[Vb365RestorePointProcessedObjectTypesItem]] = UNSET
    processed_object_types_str: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        protected_object_id: Union[Unset, str] = UNSET
        if not isinstance(self.protected_object_id, Unset):
            protected_object_id = str(self.protected_object_id)

        vb_365_job_uid: Union[Unset, str] = UNSET
        if not isinstance(self.vb_365_job_uid, Unset):
            vb_365_job_uid = str(self.vb_365_job_uid)

        repository_uid: Union[Unset, str] = UNSET
        if not isinstance(self.repository_uid, Unset):
            repository_uid = str(self.repository_uid)

        repository_name = self.repository_name

        backup_time: Union[Unset, str] = UNSET
        if not isinstance(self.backup_time, Unset):
            backup_time = self.backup_time.isoformat()

        is_archive = self.is_archive

        processed_object_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.processed_object_types, Unset):
            processed_object_types = []
            for processed_object_types_item_data in self.processed_object_types:
                processed_object_types_item = processed_object_types_item_data.value
                processed_object_types.append(processed_object_types_item)

        processed_object_types_str = self.processed_object_types_str

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if protected_object_id is not UNSET:
            field_dict["protectedObjectId"] = protected_object_id
        if vb_365_job_uid is not UNSET:
            field_dict["vb365JobUid"] = vb_365_job_uid
        if repository_uid is not UNSET:
            field_dict["repositoryUid"] = repository_uid
        if repository_name is not UNSET:
            field_dict["repositoryName"] = repository_name
        if backup_time is not UNSET:
            field_dict["backupTime"] = backup_time
        if is_archive is not UNSET:
            field_dict["isArchive"] = is_archive
        if processed_object_types is not UNSET:
            field_dict["processedObjectTypes"] = processed_object_types
        if processed_object_types_str is not UNSET:
            field_dict["processedObjectTypesStr"] = processed_object_types_str

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _protected_object_id = d.pop("protectedObjectId", UNSET)
        protected_object_id: Union[Unset, UUID]
        if isinstance(_protected_object_id, Unset):
            protected_object_id = UNSET
        else:
            protected_object_id = UUID(_protected_object_id)

        _vb_365_job_uid = d.pop("vb365JobUid", UNSET)
        vb_365_job_uid: Union[Unset, UUID]
        if isinstance(_vb_365_job_uid, Unset):
            vb_365_job_uid = UNSET
        else:
            vb_365_job_uid = UUID(_vb_365_job_uid)

        _repository_uid = d.pop("repositoryUid", UNSET)
        repository_uid: Union[Unset, UUID]
        if isinstance(_repository_uid, Unset):
            repository_uid = UNSET
        else:
            repository_uid = UUID(_repository_uid)

        repository_name = d.pop("repositoryName", UNSET)

        _backup_time = d.pop("backupTime", UNSET)
        backup_time: Union[Unset, datetime.datetime]
        if isinstance(_backup_time, Unset):
            backup_time = UNSET
        else:
            backup_time = isoparse(_backup_time)

        is_archive = d.pop("isArchive", UNSET)

        processed_object_types = []
        _processed_object_types = d.pop("processedObjectTypes", UNSET)
        for processed_object_types_item_data in _processed_object_types or []:
            processed_object_types_item = Vb365RestorePointProcessedObjectTypesItem(processed_object_types_item_data)

            processed_object_types.append(processed_object_types_item)

        processed_object_types_str = d.pop("processedObjectTypesStr", UNSET)

        vb_365_restore_point = cls(
            id=id,
            protected_object_id=protected_object_id,
            vb_365_job_uid=vb_365_job_uid,
            repository_uid=repository_uid,
            repository_name=repository_name,
            backup_time=backup_time,
            is_archive=is_archive,
            processed_object_types=processed_object_types,
            processed_object_types_str=processed_object_types_str,
        )

        vb_365_restore_point.additional_properties = d
        return vb_365_restore_point

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
