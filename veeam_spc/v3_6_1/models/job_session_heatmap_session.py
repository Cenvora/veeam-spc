import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.job_session_heatmap_job_result import JobSessionHeatmapJobResult
from ..models.job_session_heatmap_job_type import JobSessionHeatmapJobType
from ..models.job_session_heatmap_platform_type import JobSessionHeatmapPlatformType
from ..models.job_session_heatmap_workload_type import JobSessionHeatmapWorkloadType
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobSessionHeatmapSession")


@_attrs_define
class JobSessionHeatmapSession:
    """
    Attributes:
        job_name (Union[Unset, str]): Name of a job.
        server_name (Union[Unset, str]): Name of a server on which a job is configured.
        management_agent_uid (Union[Unset, UUID]): UID assigned to a management agent.
        location_name (Union[Unset, str]): Name of a location to which a job belongs.
        location_uid (Union[Unset, UUID]): UID assigned to a location to which a job belongs.
        organization_name (Union[Unset, str]): Name of an organization to which a job belongs.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization to which a job belongs.
        start_time (Union[Unset, datetime.datetime]): Date and time when a job session started.
        end_time (Union[Unset, datetime.datetime]): Date and time when a job session ended.
        duration (Union[Unset, int]): Time taken to complete a job session, in seconds.
        session_uid (Union[Unset, UUID]): UID assigned to a job session.
        failure_message (Union[None, Unset, str]): Information on job sessions that finished with errors and warnings.
        time_shift_minutes (Union[Unset, int]): Offset from the local time of a job session, in minutes.
        result (Union[Unset, JobSessionHeatmapJobResult]): Result of a job session.
        job_type (Union[Unset, JobSessionHeatmapJobType]): Type of a job.
        workload_type (Union[Unset, JobSessionHeatmapWorkloadType]): Type of workloads processed by a job session.
        platform_type (Union[Unset, JobSessionHeatmapPlatformType]): Platform of processed workloads.
    """

    job_name: Union[Unset, str] = UNSET
    server_name: Union[Unset, str] = UNSET
    management_agent_uid: Union[Unset, UUID] = UNSET
    location_name: Union[Unset, str] = UNSET
    location_uid: Union[Unset, UUID] = UNSET
    organization_name: Union[Unset, str] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    end_time: Union[Unset, datetime.datetime] = UNSET
    duration: Union[Unset, int] = UNSET
    session_uid: Union[Unset, UUID] = UNSET
    failure_message: Union[None, Unset, str] = UNSET
    time_shift_minutes: Union[Unset, int] = UNSET
    result: Union[Unset, JobSessionHeatmapJobResult] = UNSET
    job_type: Union[Unset, JobSessionHeatmapJobType] = UNSET
    workload_type: Union[Unset, JobSessionHeatmapWorkloadType] = UNSET
    platform_type: Union[Unset, JobSessionHeatmapPlatformType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_name = self.job_name

        server_name = self.server_name

        management_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.management_agent_uid, Unset):
            management_agent_uid = str(self.management_agent_uid)

        location_name = self.location_name

        location_uid: Union[Unset, str] = UNSET
        if not isinstance(self.location_uid, Unset):
            location_uid = str(self.location_uid)

        organization_name = self.organization_name

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        end_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        duration = self.duration

        session_uid: Union[Unset, str] = UNSET
        if not isinstance(self.session_uid, Unset):
            session_uid = str(self.session_uid)

        failure_message: Union[None, Unset, str]
        if isinstance(self.failure_message, Unset):
            failure_message = UNSET
        else:
            failure_message = self.failure_message

        time_shift_minutes = self.time_shift_minutes

        result: Union[Unset, str] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.value

        job_type: Union[Unset, str] = UNSET
        if not isinstance(self.job_type, Unset):
            job_type = self.job_type.value

        workload_type: Union[Unset, str] = UNSET
        if not isinstance(self.workload_type, Unset):
            workload_type = self.workload_type.value

        platform_type: Union[Unset, str] = UNSET
        if not isinstance(self.platform_type, Unset):
            platform_type = self.platform_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_name is not UNSET:
            field_dict["jobName"] = job_name
        if server_name is not UNSET:
            field_dict["serverName"] = server_name
        if management_agent_uid is not UNSET:
            field_dict["managementAgentUid"] = management_agent_uid
        if location_name is not UNSET:
            field_dict["locationName"] = location_name
        if location_uid is not UNSET:
            field_dict["locationUid"] = location_uid
        if organization_name is not UNSET:
            field_dict["organizationName"] = organization_name
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if duration is not UNSET:
            field_dict["duration"] = duration
        if session_uid is not UNSET:
            field_dict["sessionUid"] = session_uid
        if failure_message is not UNSET:
            field_dict["failureMessage"] = failure_message
        if time_shift_minutes is not UNSET:
            field_dict["timeShiftMinutes"] = time_shift_minutes
        if result is not UNSET:
            field_dict["result"] = result
        if job_type is not UNSET:
            field_dict["jobType"] = job_type
        if workload_type is not UNSET:
            field_dict["workloadType"] = workload_type
        if platform_type is not UNSET:
            field_dict["platformType"] = platform_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_name = d.pop("jobName", UNSET)

        server_name = d.pop("serverName", UNSET)

        _management_agent_uid = d.pop("managementAgentUid", UNSET)
        management_agent_uid: Union[Unset, UUID]
        if isinstance(_management_agent_uid, Unset):
            management_agent_uid = UNSET
        else:
            management_agent_uid = UUID(_management_agent_uid)

        location_name = d.pop("locationName", UNSET)

        _location_uid = d.pop("locationUid", UNSET)
        location_uid: Union[Unset, UUID]
        if isinstance(_location_uid, Unset):
            location_uid = UNSET
        else:
            location_uid = UUID(_location_uid)

        organization_name = d.pop("organizationName", UNSET)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _end_time = d.pop("endTime", UNSET)
        end_time: Union[Unset, datetime.datetime]
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        duration = d.pop("duration", UNSET)

        _session_uid = d.pop("sessionUid", UNSET)
        session_uid: Union[Unset, UUID]
        if isinstance(_session_uid, Unset):
            session_uid = UNSET
        else:
            session_uid = UUID(_session_uid)

        def _parse_failure_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        failure_message = _parse_failure_message(d.pop("failureMessage", UNSET))

        time_shift_minutes = d.pop("timeShiftMinutes", UNSET)

        _result = d.pop("result", UNSET)
        result: Union[Unset, JobSessionHeatmapJobResult]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = JobSessionHeatmapJobResult(_result)

        _job_type = d.pop("jobType", UNSET)
        job_type: Union[Unset, JobSessionHeatmapJobType]
        if isinstance(_job_type, Unset):
            job_type = UNSET
        else:
            job_type = JobSessionHeatmapJobType(_job_type)

        _workload_type = d.pop("workloadType", UNSET)
        workload_type: Union[Unset, JobSessionHeatmapWorkloadType]
        if isinstance(_workload_type, Unset):
            workload_type = UNSET
        else:
            workload_type = JobSessionHeatmapWorkloadType(_workload_type)

        _platform_type = d.pop("platformType", UNSET)
        platform_type: Union[Unset, JobSessionHeatmapPlatformType]
        if isinstance(_platform_type, Unset):
            platform_type = UNSET
        else:
            platform_type = JobSessionHeatmapPlatformType(_platform_type)

        job_session_heatmap_session = cls(
            job_name=job_name,
            server_name=server_name,
            management_agent_uid=management_agent_uid,
            location_name=location_name,
            location_uid=location_uid,
            organization_name=organization_name,
            organization_uid=organization_uid,
            start_time=start_time,
            end_time=end_time,
            duration=duration,
            session_uid=session_uid,
            failure_message=failure_message,
            time_shift_minutes=time_shift_minutes,
            result=result,
            job_type=job_type,
            workload_type=workload_type,
            platform_type=platform_type,
        )

        job_session_heatmap_session.additional_properties = d
        return job_session_heatmap_session

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
