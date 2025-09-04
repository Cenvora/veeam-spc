import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
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
        job_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Backup & Replication.
        unique_job_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Service Provider Console.
        instance_uid (Union[Unset, UUID]): UID assigned to a VM.
        name (Union[Unset, str]): Name of a VM.
        status (Union[Unset, BackupServerCdpReplicationJobObjectStatus]): Task session status.
        failure_message (Union[Unset, str]): Message that is displayed in case a task session fails.
        last_session_end_time (Union[None, Unset, datetime.date]): Date and time when the latest session finished.
        sla (Union[Unset, int]): Percentage of sessions completed within the configured RPO.
        bottleneck (Union[Unset, BackupServerCdpReplicationJobObjectBottleneck]): Bottleneck in the data transmission
            process.
        max_delay_sec (Union[Unset, int]): Difference between the configured RPO and time required to transfer and save
            data, in seconds.
        avg_duration_sec (Union[None, Unset, int]): Average duration of a syncronization session, in seconds.
        max_duration_sec (Union[None, Unset, int]): Maximum duration of a syncronization session, in seconds.
        interval_sec (Union[Unset, int]): Duration of a synchronization session configured in the policy, in seconds.
        successful_sessions_count (Union[Unset, int]): Number of task sessions completed with the `Success` status.
        failed_sessions_count (Union[Unset, int]): Number of task sessions completed with the `Failed` status.
        warnings_count (Union[Unset, int]): Number of task sessions completed with the `Warning` status.
        avg_transferred_data_kb (Union[None, Unset, int]): Avarage amount of data processed during the synchronization
            session, in kilobytes.
        max_transferred_data_kb (Union[None, Unset, int]): Maximum amount of data processed during the synchronization
            session, in kilobytes.
        total_transferred_data_kb (Union[None, Unset, int]): Total size of data processed during the synchronization
            session, in kilobytes.
    """

    job_uid: Union[Unset, UUID] = UNSET
    unique_job_uid: Union[Unset, UUID] = UNSET
    instance_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    status: Union[Unset, BackupServerCdpReplicationJobObjectStatus] = UNSET
    failure_message: Union[Unset, str] = UNSET
    last_session_end_time: Union[None, Unset, datetime.date] = UNSET
    sla: Union[Unset, int] = UNSET
    bottleneck: Union[Unset, BackupServerCdpReplicationJobObjectBottleneck] = UNSET
    max_delay_sec: Union[Unset, int] = UNSET
    avg_duration_sec: Union[None, Unset, int] = UNSET
    max_duration_sec: Union[None, Unset, int] = UNSET
    interval_sec: Union[Unset, int] = UNSET
    successful_sessions_count: Union[Unset, int] = UNSET
    failed_sessions_count: Union[Unset, int] = UNSET
    warnings_count: Union[Unset, int] = UNSET
    avg_transferred_data_kb: Union[None, Unset, int] = UNSET
    max_transferred_data_kb: Union[None, Unset, int] = UNSET
    total_transferred_data_kb: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_uid: Union[Unset, str] = UNSET
        if not isinstance(self.job_uid, Unset):
            job_uid = str(self.job_uid)

        unique_job_uid: Union[Unset, str] = UNSET
        if not isinstance(self.unique_job_uid, Unset):
            unique_job_uid = str(self.unique_job_uid)

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        failure_message = self.failure_message

        last_session_end_time: Union[None, Unset, str]
        if isinstance(self.last_session_end_time, Unset):
            last_session_end_time = UNSET
        elif isinstance(self.last_session_end_time, datetime.date):
            last_session_end_time = self.last_session_end_time.isoformat()
        else:
            last_session_end_time = self.last_session_end_time

        sla = self.sla

        bottleneck: Union[Unset, str] = UNSET
        if not isinstance(self.bottleneck, Unset):
            bottleneck = self.bottleneck.value

        max_delay_sec = self.max_delay_sec

        avg_duration_sec: Union[None, Unset, int]
        if isinstance(self.avg_duration_sec, Unset):
            avg_duration_sec = UNSET
        else:
            avg_duration_sec = self.avg_duration_sec

        max_duration_sec: Union[None, Unset, int]
        if isinstance(self.max_duration_sec, Unset):
            max_duration_sec = UNSET
        else:
            max_duration_sec = self.max_duration_sec

        interval_sec = self.interval_sec

        successful_sessions_count = self.successful_sessions_count

        failed_sessions_count = self.failed_sessions_count

        warnings_count = self.warnings_count

        avg_transferred_data_kb: Union[None, Unset, int]
        if isinstance(self.avg_transferred_data_kb, Unset):
            avg_transferred_data_kb = UNSET
        else:
            avg_transferred_data_kb = self.avg_transferred_data_kb

        max_transferred_data_kb: Union[None, Unset, int]
        if isinstance(self.max_transferred_data_kb, Unset):
            max_transferred_data_kb = UNSET
        else:
            max_transferred_data_kb = self.max_transferred_data_kb

        total_transferred_data_kb: Union[None, Unset, int]
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

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BackupServerCdpReplicationJobObjectStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BackupServerCdpReplicationJobObjectStatus(_status)

        failure_message = d.pop("failureMessage", UNSET)

        def _parse_last_session_end_time(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_session_end_time_type_0 = isoparse(data).date()

                return last_session_end_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        last_session_end_time = _parse_last_session_end_time(d.pop("lastSessionEndTime", UNSET))

        sla = d.pop("sla", UNSET)

        _bottleneck = d.pop("bottleneck", UNSET)
        bottleneck: Union[Unset, BackupServerCdpReplicationJobObjectBottleneck]
        if isinstance(_bottleneck, Unset):
            bottleneck = UNSET
        else:
            bottleneck = BackupServerCdpReplicationJobObjectBottleneck(_bottleneck)

        max_delay_sec = d.pop("maxDelaySec", UNSET)

        def _parse_avg_duration_sec(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        avg_duration_sec = _parse_avg_duration_sec(d.pop("avgDurationSec", UNSET))

        def _parse_max_duration_sec(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_duration_sec = _parse_max_duration_sec(d.pop("maxDurationSec", UNSET))

        interval_sec = d.pop("intervalSec", UNSET)

        successful_sessions_count = d.pop("successfulSessionsCount", UNSET)

        failed_sessions_count = d.pop("failedSessionsCount", UNSET)

        warnings_count = d.pop("warningsCount", UNSET)

        def _parse_avg_transferred_data_kb(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        avg_transferred_data_kb = _parse_avg_transferred_data_kb(d.pop("avgTransferredDataKb", UNSET))

        def _parse_max_transferred_data_kb(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_transferred_data_kb = _parse_max_transferred_data_kb(d.pop("maxTransferredDataKb", UNSET))

        def _parse_total_transferred_data_kb(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

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
