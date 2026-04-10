from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerJobLinkedJobObject")


@_attrs_define
class BackupServerJobLinkedJobObject:
    """
    Attributes:
        job_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Backup & Replication.
        unique_job_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Service Provider Console.
        linked_job_uid (Union[Unset, UUID]): UID assigned to a linked backup job.
    """

    job_uid: Union[Unset, UUID] = UNSET
    unique_job_uid: Union[Unset, UUID] = UNSET
    linked_job_uid: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_uid: Union[Unset, str] = UNSET
        if not isinstance(self.job_uid, Unset):
            job_uid = str(self.job_uid)

        unique_job_uid: Union[Unset, str] = UNSET
        if not isinstance(self.unique_job_uid, Unset):
            unique_job_uid = str(self.unique_job_uid)

        linked_job_uid: Union[Unset, str] = UNSET
        if not isinstance(self.linked_job_uid, Unset):
            linked_job_uid = str(self.linked_job_uid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if unique_job_uid is not UNSET:
            field_dict["uniqueJobUid"] = unique_job_uid
        if linked_job_uid is not UNSET:
            field_dict["linkedJobUid"] = linked_job_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _job_uid = d.pop("jobUid", UNSET)
        job_uid: Union[Unset, UUID]
        if isinstance(_job_uid, Unset):
            job_uid = UNSET
        else:
            job_uid = UUID(_job_uid)

        _unique_job_uid = d.pop("uniqueJobUid", UNSET)
        unique_job_uid: Union[Unset, UUID]
        if isinstance(_unique_job_uid, Unset):
            unique_job_uid = UNSET
        else:
            unique_job_uid = UUID(_unique_job_uid)

        _linked_job_uid = d.pop("linkedJobUid", UNSET)
        linked_job_uid: Union[Unset, UUID]
        if isinstance(_linked_job_uid, Unset):
            linked_job_uid = UNSET
        else:
            linked_job_uid = UUID(_linked_job_uid)

        backup_server_job_linked_job_object = cls(
            job_uid=job_uid,
            unique_job_uid=unique_job_uid,
            linked_job_uid=linked_job_uid,
        )

        backup_server_job_linked_job_object.additional_properties = d
        return backup_server_job_linked_job_object

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
