import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.protected_computer_managed_by_console_job_target_type import (
    ProtectedComputerManagedByConsoleJobTargetType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedComputerManagedByConsoleJob")


@_attrs_define
class ProtectedComputerManagedByConsoleJob:
    """
    Attributes:
        backup_agent_uid (Union[Unset, UUID]): UID assigned to a Veeam backup agent.
        job_uid (Union[Unset, UUID]): UID assigned to a job that protects the computer.
        job_name (Union[Unset, str]): Name of a job that protects the computer.
        source_size (Union[Unset, int]): Size of protected data, in bytes.
        total_restore_point_size (Union[Unset, int]): Total size of all restore points, in bytes.
        latest_restore_point_size (Union[Unset, int]): Size of the latest restore point, in bytes.
        restore_points (Union[Unset, int]): Number of restore points.
        latest_restore_point_date (Union[Unset, datetime.datetime]): Date and time of the latest restore point creation.
        target_type (Union[Unset, ProtectedComputerManagedByConsoleJobTargetType]): Type of a target repository.
    """

    backup_agent_uid: Union[Unset, UUID] = UNSET
    job_uid: Union[Unset, UUID] = UNSET
    job_name: Union[Unset, str] = UNSET
    source_size: Union[Unset, int] = UNSET
    total_restore_point_size: Union[Unset, int] = UNSET
    latest_restore_point_size: Union[Unset, int] = UNSET
    restore_points: Union[Unset, int] = UNSET
    latest_restore_point_date: Union[Unset, datetime.datetime] = UNSET
    target_type: Union[Unset, ProtectedComputerManagedByConsoleJobTargetType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_agent_uid, Unset):
            backup_agent_uid = str(self.backup_agent_uid)

        job_uid: Union[Unset, str] = UNSET
        if not isinstance(self.job_uid, Unset):
            job_uid = str(self.job_uid)

        job_name = self.job_name

        source_size = self.source_size

        total_restore_point_size = self.total_restore_point_size

        latest_restore_point_size = self.latest_restore_point_size

        restore_points = self.restore_points

        latest_restore_point_date: Union[Unset, str] = UNSET
        if not isinstance(self.latest_restore_point_date, Unset):
            latest_restore_point_date = self.latest_restore_point_date.isoformat()

        target_type: Union[Unset, str] = UNSET
        if not isinstance(self.target_type, Unset):
            target_type = self.target_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_agent_uid is not UNSET:
            field_dict["backupAgentUid"] = backup_agent_uid
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if job_name is not UNSET:
            field_dict["jobName"] = job_name
        if source_size is not UNSET:
            field_dict["sourceSize"] = source_size
        if total_restore_point_size is not UNSET:
            field_dict["totalRestorePointSize"] = total_restore_point_size
        if latest_restore_point_size is not UNSET:
            field_dict["latestRestorePointSize"] = latest_restore_point_size
        if restore_points is not UNSET:
            field_dict["restorePoints"] = restore_points
        if latest_restore_point_date is not UNSET:
            field_dict["latestRestorePointDate"] = latest_restore_point_date
        if target_type is not UNSET:
            field_dict["targetType"] = target_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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

        job_name = d.pop("jobName", UNSET)

        source_size = d.pop("sourceSize", UNSET)

        total_restore_point_size = d.pop("totalRestorePointSize", UNSET)

        latest_restore_point_size = d.pop("latestRestorePointSize", UNSET)

        restore_points = d.pop("restorePoints", UNSET)

        _latest_restore_point_date = d.pop("latestRestorePointDate", UNSET)
        latest_restore_point_date: Union[Unset, datetime.datetime]
        if isinstance(_latest_restore_point_date, Unset):
            latest_restore_point_date = UNSET
        else:
            latest_restore_point_date = isoparse(_latest_restore_point_date)

        _target_type = d.pop("targetType", UNSET)
        target_type: Union[Unset, ProtectedComputerManagedByConsoleJobTargetType]
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = ProtectedComputerManagedByConsoleJobTargetType(_target_type)

        protected_computer_managed_by_console_job = cls(
            backup_agent_uid=backup_agent_uid,
            job_uid=job_uid,
            job_name=job_name,
            source_size=source_size,
            total_restore_point_size=total_restore_point_size,
            latest_restore_point_size=latest_restore_point_size,
            restore_points=restore_points,
            latest_restore_point_date=latest_restore_point_date,
            target_type=target_type,
        )

        protected_computer_managed_by_console_job.additional_properties = d
        return protected_computer_managed_by_console_job

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
