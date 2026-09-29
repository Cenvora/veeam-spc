from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.backup_server_cdp_replication_job_object_bottleneck import BackupServerCdpReplicationJobObjectBottleneck
from ..models.backup_server_cdp_replication_job_object_status import BackupServerCdpReplicationJobObjectStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerCdpReplicationJobObject")


@_attrs_define
class BackupServerCdpReplicationJobObject:
    """
    Attributes:
        job_uid (UUID | Unset): UID assigned to a job in Veeam Backup & Replication.
        unique_job_uid (UUID | Unset): UID assigned to a job in Veeam Service Provider Console.
        instance_uid (UUID | Unset): UID assigned to a VM.
        name (str | Unset): Name of a VM.
        status (BackupServerCdpReplicationJobObjectStatus | Unset): Task session status.
        failure_message (str | Unset): Message that is displayed in case a task session fails.
        last_session_end_time (datetime.date | None | Unset): Date and time when the latest session finished.
        sla (int | Unset): Percentage of sessions completed within the configured RPO.
        bottleneck (BackupServerCdpReplicationJobObjectBottleneck | Unset): Bottleneck in the data transmission process.
        max_delay_sec (int | Unset): Difference between the configured RPO and time required to transfer and save data,
            in seconds.
        avg_duration_sec (int | None | Unset): Average duration of a syncronization session, in seconds.
        max_duration_sec (int | None | Unset): Maximum duration of a syncronization session, in seconds.
        interval_sec (int | Unset): Duration of a synchronization session configured in the policy, in seconds.
        successful_sessions_count (int | Unset): Number of task sessions completed with the `Success` status.
        failed_sessions_count (int | Unset): Number of task sessions completed with the `Failed` status.
        warnings_count (int | Unset): Number of task sessions completed with the `Warning` status.
        avg_transferred_data_kb (int | None | Unset): Avarage amount of data processed during the synchronization
            session, in kilobytes.
        max_transferred_data_kb (int | None | Unset): Maximum amount of data processed during the synchronization
            session, in kilobytes.
        total_transferred_data_kb (int | None | Unset): Total size of data processed during the synchronization session,
            in kilobytes.
    """

    job_uid: UUID | Unset = UNSET
    unique_job_uid: UUID | Unset = UNSET
    instance_uid: UUID | Unset = UNSET
    name: str | Unset = UNSET
    status: BackupServerCdpReplicationJobObjectStatus | Unset = UNSET
    failure_message: str | Unset = UNSET
    last_session_end_time: datetime.date | None | Unset = UNSET
    sla: int | Unset = UNSET
    bottleneck: BackupServerCdpReplicationJobObjectBottleneck | Unset = UNSET
    max_delay_sec: int | Unset = UNSET
    avg_duration_sec: int | None | Unset = UNSET
    max_duration_sec: int | None | Unset = UNSET
    interval_sec: int | Unset = UNSET
    successful_sessions_count: int | Unset = UNSET
    failed_sessions_count: int | Unset = UNSET
    warnings_count: int | Unset = UNSET
    avg_transferred_data_kb: int | None | Unset = UNSET
    max_transferred_data_kb: int | None | Unset = UNSET
    total_transferred_data_kb: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_uid: str | Unset = UNSET
        if not isinstance(self.job_uid, Unset):
            job_uid = str(self.job_uid)

        unique_job_uid: str | Unset = UNSET
        if not isinstance(self.unique_job_uid, Unset):
            unique_job_uid = str(self.unique_job_uid)

        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        failure_message = self.failure_message

        last_session_end_time: None | str | Unset
        if isinstance(self.last_session_end_time, Unset):
            last_session_end_time = UNSET
        elif isinstance(self.last_session_end_time, datetime.date):
            last_session_end_time = self.last_session_end_time.isoformat()
        else:
            last_session_end_time = self.last_session_end_time

        sla = self.sla

        bottleneck: str | Unset = UNSET
        if not isinstance(self.bottleneck, Unset):
            bottleneck = self.bottleneck.value

        max_delay_sec = self.max_delay_sec

        avg_duration_sec: int | None | Unset
        if isinstance(self.avg_duration_sec, Unset):
            avg_duration_sec = UNSET
        else:
            avg_duration_sec = self.avg_duration_sec

        max_duration_sec: int | None | Unset
        if isinstance(self.max_duration_sec, Unset):
            max_duration_sec = UNSET
        else:
            max_duration_sec = self.max_duration_sec

        interval_sec = self.interval_sec

        successful_sessions_count = self.successful_sessions_count

        failed_sessions_count = self.failed_sessions_count

        warnings_count = self.warnings_count

        avg_transferred_data_kb: int | None | Unset
        if isinstance(self.avg_transferred_data_kb, Unset):
            avg_transferred_data_kb = UNSET
        else:
            avg_transferred_data_kb = self.avg_transferred_data_kb

        max_transferred_data_kb: int | None | Unset
        if isinstance(self.max_transferred_data_kb, Unset):
            max_transferred_data_kb = UNSET
        else:
            max_transferred_data_kb = self.max_transferred_data_kb

        total_transferred_data_kb: int | None | Unset
        if isinstance(self.total_transferred_data_kb, Unset):
            total_transferred_data_kb = UNSET
        else:
            total_transferred_data_kb = self.total_transferred_data_kb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if unique_job_uid is not UNSET:
            field_dict["uniqueJobUid"] = unique_job_uid
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if failure_message is not UNSET:
            field_dict["failureMessage"] = failure_message
        if last_session_end_time is not UNSET:
            field_dict["lastSessionEndTime"] = last_session_end_time
        if sla is not UNSET:
            field_dict["sla"] = sla
        if bottleneck is not UNSET:
            field_dict["bottleneck"] = bottleneck
        if max_delay_sec is not UNSET:
            field_dict["maxDelaySec"] = max_delay_sec
        if avg_duration_sec is not UNSET:
            field_dict["avgDurationSec"] = avg_duration_sec
        if max_duration_sec is not UNSET:
            field_dict["maxDurationSec"] = max_duration_sec
        if interval_sec is not UNSET:
            field_dict["intervalSec"] = interval_sec
        if successful_sessions_count is not UNSET:
            field_dict["successfulSessionsCount"] = successful_sessions_count
        if failed_sessions_count is not UNSET:
            field_dict["failedSessionsCount"] = failed_sessions_count
        if warnings_count is not UNSET:
            field_dict["warningsCount"] = warnings_count
        if avg_transferred_data_kb is not UNSET:
            field_dict["avgTransferredDataKb"] = avg_transferred_data_kb
        if max_transferred_data_kb is not UNSET:
            field_dict["maxTransferredDataKb"] = max_transferred_data_kb
        if total_transferred_data_kb is not UNSET:
            field_dict["totalTransferredDataKb"] = total_transferred_data_kb

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: BackupServerCdpReplicationJobObjectStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BackupServerCdpReplicationJobObjectStatus(_status)

        failure_message = d.pop("failureMessage", UNSET)

        def _parse_last_session_end_time(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_session_end_time_type_0 = isoparse(data).date()

                return last_session_end_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        last_session_end_time = _parse_last_session_end_time(d.pop("lastSessionEndTime", UNSET))

        sla = d.pop("sla", UNSET)

        _bottleneck = d.pop("bottleneck", UNSET)
        bottleneck: BackupServerCdpReplicationJobObjectBottleneck | Unset
        if isinstance(_bottleneck, Unset):
            bottleneck = UNSET
        else:
            bottleneck = BackupServerCdpReplicationJobObjectBottleneck(_bottleneck)

        max_delay_sec = d.pop("maxDelaySec", UNSET)

        def _parse_avg_duration_sec(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        avg_duration_sec = _parse_avg_duration_sec(d.pop("avgDurationSec", UNSET))

        def _parse_max_duration_sec(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_duration_sec = _parse_max_duration_sec(d.pop("maxDurationSec", UNSET))

        interval_sec = d.pop("intervalSec", UNSET)

        successful_sessions_count = d.pop("successfulSessionsCount", UNSET)

        failed_sessions_count = d.pop("failedSessionsCount", UNSET)

        warnings_count = d.pop("warningsCount", UNSET)

        def _parse_avg_transferred_data_kb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        avg_transferred_data_kb = _parse_avg_transferred_data_kb(d.pop("avgTransferredDataKb", UNSET))

        def _parse_max_transferred_data_kb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_transferred_data_kb = _parse_max_transferred_data_kb(d.pop("maxTransferredDataKb", UNSET))

        def _parse_total_transferred_data_kb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_transferred_data_kb = _parse_total_transferred_data_kb(d.pop("totalTransferredDataKb", UNSET))

        backup_server_cdp_replication_job_object = cls(
            job_uid=job_uid,
            unique_job_uid=unique_job_uid,
            instance_uid=instance_uid,
            name=name,
            status=status,
            failure_message=failure_message,
            last_session_end_time=last_session_end_time,
            sla=sla,
            bottleneck=bottleneck,
            max_delay_sec=max_delay_sec,
            avg_duration_sec=avg_duration_sec,
            max_duration_sec=max_duration_sec,
            interval_sec=interval_sec,
            successful_sessions_count=successful_sessions_count,
            failed_sessions_count=failed_sessions_count,
            warnings_count=warnings_count,
            avg_transferred_data_kb=avg_transferred_data_kb,
            max_transferred_data_kb=max_transferred_data_kb,
            total_transferred_data_kb=total_transferred_data_kb,
        )

        backup_server_cdp_replication_job_object.additional_properties = d
        return backup_server_cdp_replication_job_object

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
