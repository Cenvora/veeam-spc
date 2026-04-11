from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.backup_server_agent_job_object_backup_status import BackupServerAgentJobObjectBackupStatus
from ..models.backup_server_agent_job_object_os_type import BackupServerAgentJobObjectOsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerAgentJobObject")


@_attrs_define
class BackupServerAgentJobObject:
    r"""
    Attributes:
        instance_uid (UUID | Unset): UID assigned to a job object in Veeam Backup & Replication.
        unique_uid (UUID | Unset): UID assigned to a job object in Veeam Service Provider Console.
        backup_server_uid (None | Unset | UUID): UID assigned to a Veeam Backup & Replication server.
        agent_uid (None | Unset | UUID): UID assigned to a Veeam backup agent.
        job_uid (UUID | Unset): UID assigned to a job in Veeam Backup & Replication.
        unique_job_uid (UUID | Unset): UID assigned to a job in Veeam Service Provider Console.
        computer (None | str | Unset): Computer name of a Veeam backup agent.
        backup_status (BackupServerAgentJobObjectBackupStatus | Unset): Status of a job.
        last_run (datetime.datetime | None | Unset): Date and time when the latest job session started.
        last_end_time (datetime.datetime | None | Unset): Date and time when the latest job session ended.
        last_duration (int | None | Unset): Duration of the latest job session, in seconds.
        restore_points_count (int | Unset): Number of restore points available in the backup chain.
        os_type (BackupServerAgentJobObjectOsType | Unset): Type of a protected computer operating system.
        failure_message (None | str | Unset): Message that is displayed in case a backup job fails.
            > Every line break is represented by the `\r\n` control characters.
    """

    instance_uid: UUID | Unset = UNSET
    unique_uid: UUID | Unset = UNSET
    backup_server_uid: None | Unset | UUID = UNSET
    agent_uid: None | Unset | UUID = UNSET
    job_uid: UUID | Unset = UNSET
    unique_job_uid: UUID | Unset = UNSET
    computer: None | str | Unset = UNSET
    backup_status: BackupServerAgentJobObjectBackupStatus | Unset = UNSET
    last_run: datetime.datetime | None | Unset = UNSET
    last_end_time: datetime.datetime | None | Unset = UNSET
    last_duration: int | None | Unset = UNSET
    restore_points_count: int | Unset = UNSET
    os_type: BackupServerAgentJobObjectOsType | Unset = UNSET
    failure_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        unique_uid: str | Unset = UNSET
        if not isinstance(self.unique_uid, Unset):
            unique_uid = str(self.unique_uid)

        backup_server_uid: None | str | Unset
        if isinstance(self.backup_server_uid, Unset):
            backup_server_uid = UNSET
        elif isinstance(self.backup_server_uid, UUID):
            backup_server_uid = str(self.backup_server_uid)
        else:
            backup_server_uid = self.backup_server_uid

        agent_uid: None | str | Unset
        if isinstance(self.agent_uid, Unset):
            agent_uid = UNSET
        elif isinstance(self.agent_uid, UUID):
            agent_uid = str(self.agent_uid)
        else:
            agent_uid = self.agent_uid

        job_uid: str | Unset = UNSET
        if not isinstance(self.job_uid, Unset):
            job_uid = str(self.job_uid)

        unique_job_uid: str | Unset = UNSET
        if not isinstance(self.unique_job_uid, Unset):
            unique_job_uid = str(self.unique_job_uid)

        computer: None | str | Unset
        if isinstance(self.computer, Unset):
            computer = UNSET
        else:
            computer = self.computer

        backup_status: str | Unset = UNSET
        if not isinstance(self.backup_status, Unset):
            backup_status = self.backup_status.value

        last_run: None | str | Unset
        if isinstance(self.last_run, Unset):
            last_run = UNSET
        elif isinstance(self.last_run, datetime.datetime):
            last_run = self.last_run.isoformat()
        else:
            last_run = self.last_run

        last_end_time: None | str | Unset
        if isinstance(self.last_end_time, Unset):
            last_end_time = UNSET
        elif isinstance(self.last_end_time, datetime.datetime):
            last_end_time = self.last_end_time.isoformat()
        else:
            last_end_time = self.last_end_time

        last_duration: int | None | Unset
        if isinstance(self.last_duration, Unset):
            last_duration = UNSET
        else:
            last_duration = self.last_duration

        restore_points_count = self.restore_points_count

        os_type: str | Unset = UNSET
        if not isinstance(self.os_type, Unset):
            os_type = self.os_type.value

        failure_message: None | str | Unset
        if isinstance(self.failure_message, Unset):
            failure_message = UNSET
        else:
            failure_message = self.failure_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if unique_uid is not UNSET:
            field_dict["uniqueUid"] = unique_uid
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if agent_uid is not UNSET:
            field_dict["agentUid"] = agent_uid
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if unique_job_uid is not UNSET:
            field_dict["uniqueJobUid"] = unique_job_uid
        if computer is not UNSET:
            field_dict["computer"] = computer
        if backup_status is not UNSET:
            field_dict["backupStatus"] = backup_status
        if last_run is not UNSET:
            field_dict["lastRun"] = last_run
        if last_end_time is not UNSET:
            field_dict["lastEndTime"] = last_end_time
        if last_duration is not UNSET:
            field_dict["lastDuration"] = last_duration
        if restore_points_count is not UNSET:
            field_dict["restorePointsCount"] = restore_points_count
        if os_type is not UNSET:
            field_dict["osType"] = os_type
        if failure_message is not UNSET:
            field_dict["failureMessage"] = failure_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _unique_uid = d.pop("uniqueUid", UNSET)
        unique_uid: UUID | Unset
        if isinstance(_unique_uid, Unset):
            unique_uid = UNSET
        else:
            unique_uid = UUID(_unique_uid)

        def _parse_backup_server_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_server_uid_type_0 = UUID(data)

                return backup_server_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        backup_server_uid = _parse_backup_server_uid(d.pop("backupServerUid", UNSET))

        def _parse_agent_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                agent_uid_type_0 = UUID(data)

                return agent_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        agent_uid = _parse_agent_uid(d.pop("agentUid", UNSET))

        _job_uid = d.pop("jobUid", UNSET)
        job_uid: UUID | Unset
        if isinstance(_job_uid, Unset):
            job_uid = UNSET
        else:
            job_uid = UUID(_job_uid)

        _unique_job_uid = d.pop("uniqueJobUid", UNSET)
        unique_job_uid: UUID | Unset
        if isinstance(_unique_job_uid, Unset):
            unique_job_uid = UNSET
        else:
            unique_job_uid = UUID(_unique_job_uid)

        def _parse_computer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        computer = _parse_computer(d.pop("computer", UNSET))

        _backup_status = d.pop("backupStatus", UNSET)
        backup_status: BackupServerAgentJobObjectBackupStatus | Unset
        if isinstance(_backup_status, Unset):
            backup_status = UNSET
        else:
            backup_status = BackupServerAgentJobObjectBackupStatus(_backup_status)

        def _parse_last_run(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_run_type_0 = isoparse(data)

                return last_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_run = _parse_last_run(d.pop("lastRun", UNSET))

        def _parse_last_end_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_end_time_type_0 = isoparse(data)

                return last_end_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_end_time = _parse_last_end_time(d.pop("lastEndTime", UNSET))

        def _parse_last_duration(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_duration = _parse_last_duration(d.pop("lastDuration", UNSET))

        restore_points_count = d.pop("restorePointsCount", UNSET)

        _os_type = d.pop("osType", UNSET)
        os_type: BackupServerAgentJobObjectOsType | Unset
        if isinstance(_os_type, Unset):
            os_type = UNSET
        else:
            os_type = BackupServerAgentJobObjectOsType(_os_type)

        def _parse_failure_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        failure_message = _parse_failure_message(d.pop("failureMessage", UNSET))

        backup_server_agent_job_object = cls(
            instance_uid=instance_uid,
            unique_uid=unique_uid,
            backup_server_uid=backup_server_uid,
            agent_uid=agent_uid,
            job_uid=job_uid,
            unique_job_uid=unique_job_uid,
            computer=computer,
            backup_status=backup_status,
            last_run=last_run,
            last_end_time=last_end_time,
            last_duration=last_duration,
            restore_points_count=restore_points_count,
            os_type=os_type,
            failure_message=failure_message,
        )

        backup_server_agent_job_object.additional_properties = d
        return backup_server_agent_job_object

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
