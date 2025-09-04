import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.windows_backup_agent_job_backup_mode import WindowsBackupAgentJobBackupMode
from ..models.windows_backup_agent_job_operation_mode import WindowsBackupAgentJobOperationMode
from ..models.windows_backup_agent_job_schedule_events_item import WindowsBackupAgentJobScheduleEventsItem
from ..models.windows_backup_agent_job_schedule_type import WindowsBackupAgentJobScheduleType
from ..models.windows_backup_agent_job_status import WindowsBackupAgentJobStatus
from ..models.windows_backup_agent_job_target_type import WindowsBackupAgentJobTargetType
from ..types import UNSET, Unset

T = TypeVar("T", bound="WindowsBackupAgentJob")


@_attrs_define
class WindowsBackupAgentJob:
    r"""
    Example:
        {'backupAgentUid': 'CCEB5975-B409-49B5-8ECE-FFFECB13494F', 'name': 'VAW job 2 Cloud', 'configUid':
            'AF097BD3-4AE9-4841-8152-8FF5CC703EAB', 'status': 'Success', 'operationMode': 'Server', 'backupMode': 'File',
            'destination': '\\\\share\\backup\\test', 'restorePoints': 4, 'lastRun': datetime.datetime(2018, 11, 1, 11, 35,
            tzinfo=datetime.timezone(datetime.timedelta(seconds=3600), '+01:00')), 'lastEndTime': datetime.datetime(2018,
            11, 1, 11, 45, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600), '+01:00')), 'lastDuration': 600,
            'nextRun': datetime.datetime(2018, 12, 1, 11, 35, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600),
            '+01:00')), 'avgDuration': 575, 'targetType': 'Local', 'isEnabled': True, 'schedulingType': 'Periodically',
            'failureMessage': '', 'lastModifiedDate': datetime.datetime(2018, 11, 1, 11, 45,
            tzinfo=datetime.timezone(datetime.timedelta(seconds=3600), '+01:00')), 'lastModifiedBy': 'someuser',
            'backedUpSize': 12550788}

    Attributes:
        status (WindowsBackupAgentJobStatus): Status of the latest job session.
            > Can be changed to `Running` or `Stopping` using the PATCH endpoint.
        instance_uid (Union[Unset, UUID]): UID assigned to a Veeam Agent for Microsoft Windows job.
        backup_agent_uid (Union[Unset, UUID]): UID assigned to a Veeam Agent for Microsoft Windows.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization.
        name (Union[None, Unset, str]): Name of a Veeam Agent for Microsoft Windows job.
        config_uid (Union[Unset, UUID]): UID assigned to a backup job configuration.
        backup_policy_uid (Union[None, UUID, Unset]): UID of a backup policy assigned to a Veeam Agent for Microsoft
            Windows.
        backup_policy_failure_message (Union[None, Unset, str]): Message that is displayed in case a backup policy job
            fails.
        operation_mode (Union[Unset, WindowsBackupAgentJobOperationMode]): Operation mode of a Veeam Agent for Microsoft
            Windows.
        destination (Union[None, Unset, str]): Location where backup files for a Veeam Agent for Microsoft Windows
            reside.
        restore_points (Union[None, Unset, int]): Number of restore points.
        last_run (Union[None, Unset, datetime.datetime]): Date and time when the latest job session started.
        last_end_time (Union[None, Unset, datetime.datetime]): Date and time when the latest job session finished.
        last_duration (Union[None, Unset, int]): Duration of the latest backup job session, in seconds.
        next_run (Union[None, Unset, datetime.datetime]): Date and time of the next scheduled backup job session.
        avg_duration (Union[None, Unset, int]): Average duration of a backup job session, in seconds.
        backup_mode (Union[Unset, WindowsBackupAgentJobBackupMode]): Type of backup operation mode.
        target_type (Union[Unset, WindowsBackupAgentJobTargetType]): Type of a location where backup files for a Veeam
            Agent for Microsoft Windows reside.
        is_enabled (Union[Unset, bool]): Indicates whether a job schedule is enabled.
            > Can be changed using the PATCH endpoint.
        schedule_type (Union[Unset, WindowsBackupAgentJobScheduleType]): Type of schedule configured for the job.
        schedule_events (Union[Unset, list[WindowsBackupAgentJobScheduleEventsItem]]): Events that trigger the backup
            job launch.
        last_modified_date (Union[None, Unset, datetime.datetime]): Date and time when settings of the backup job were
            last modified.
        last_modified_by (Union[None, Unset, str]): Name of the user who last modified job settings.
        failure_message (Union[None, Unset, str]): Message that is displayed in case a backup job fails.
        backed_up_size (Union[None, Unset, int]): Total size of all restore points, in bytes.
        free_space (Union[None, Unset, int]): Amount of free space available on the target repository.
            > If the job has never been run, the property value is `null`.
    """

    status: WindowsBackupAgentJobStatus
    instance_uid: Union[Unset, UUID] = UNSET
    backup_agent_uid: Union[Unset, UUID] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    name: Union[None, Unset, str] = UNSET
    config_uid: Union[Unset, UUID] = UNSET
    backup_policy_uid: Union[None, UUID, Unset] = UNSET
    backup_policy_failure_message: Union[None, Unset, str] = UNSET
    operation_mode: Union[Unset, WindowsBackupAgentJobOperationMode] = UNSET
    destination: Union[None, Unset, str] = UNSET
    restore_points: Union[None, Unset, int] = UNSET
    last_run: Union[None, Unset, datetime.datetime] = UNSET
    last_end_time: Union[None, Unset, datetime.datetime] = UNSET
    last_duration: Union[None, Unset, int] = UNSET
    next_run: Union[None, Unset, datetime.datetime] = UNSET
    avg_duration: Union[None, Unset, int] = UNSET
    backup_mode: Union[Unset, WindowsBackupAgentJobBackupMode] = UNSET
    target_type: Union[Unset, WindowsBackupAgentJobTargetType] = UNSET
    is_enabled: Union[Unset, bool] = UNSET
    schedule_type: Union[Unset, WindowsBackupAgentJobScheduleType] = UNSET
    schedule_events: Union[Unset, list[WindowsBackupAgentJobScheduleEventsItem]] = UNSET
    last_modified_date: Union[None, Unset, datetime.datetime] = UNSET
    last_modified_by: Union[None, Unset, str] = UNSET
    failure_message: Union[None, Unset, str] = UNSET
    backed_up_size: Union[None, Unset, int] = UNSET
    free_space: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        backup_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_agent_uid, Unset):
            backup_agent_uid = str(self.backup_agent_uid)

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        config_uid: Union[Unset, str] = UNSET
        if not isinstance(self.config_uid, Unset):
            config_uid = str(self.config_uid)

        backup_policy_uid: Union[None, Unset, str]
        if isinstance(self.backup_policy_uid, Unset):
            backup_policy_uid = UNSET
        elif isinstance(self.backup_policy_uid, UUID):
            backup_policy_uid = str(self.backup_policy_uid)
        else:
            backup_policy_uid = self.backup_policy_uid

        backup_policy_failure_message: Union[None, Unset, str]
        if isinstance(self.backup_policy_failure_message, Unset):
            backup_policy_failure_message = UNSET
        else:
            backup_policy_failure_message = self.backup_policy_failure_message

        operation_mode: Union[Unset, str] = UNSET
        if not isinstance(self.operation_mode, Unset):
            operation_mode = self.operation_mode.value

        destination: Union[None, Unset, str]
        if isinstance(self.destination, Unset):
            destination = UNSET
        else:
            destination = self.destination

        restore_points: Union[None, Unset, int]
        if isinstance(self.restore_points, Unset):
            restore_points = UNSET
        else:
            restore_points = self.restore_points

        last_run: Union[None, Unset, str]
        if isinstance(self.last_run, Unset):
            last_run = UNSET
        elif isinstance(self.last_run, datetime.datetime):
            last_run = self.last_run.isoformat()
        else:
            last_run = self.last_run

        last_end_time: Union[None, Unset, str]
        if isinstance(self.last_end_time, Unset):
            last_end_time = UNSET
        elif isinstance(self.last_end_time, datetime.datetime):
            last_end_time = self.last_end_time.isoformat()
        else:
            last_end_time = self.last_end_time

        last_duration: Union[None, Unset, int]
        if isinstance(self.last_duration, Unset):
            last_duration = UNSET
        else:
            last_duration = self.last_duration

        next_run: Union[None, Unset, str]
        if isinstance(self.next_run, Unset):
            next_run = UNSET
        elif isinstance(self.next_run, datetime.datetime):
            next_run = self.next_run.isoformat()
        else:
            next_run = self.next_run

        avg_duration: Union[None, Unset, int]
        if isinstance(self.avg_duration, Unset):
            avg_duration = UNSET
        else:
            avg_duration = self.avg_duration

        backup_mode: Union[Unset, str] = UNSET
        if not isinstance(self.backup_mode, Unset):
            backup_mode = self.backup_mode.value

        target_type: Union[Unset, str] = UNSET
        if not isinstance(self.target_type, Unset):
            target_type = self.target_type.value

        is_enabled = self.is_enabled

        schedule_type: Union[Unset, str] = UNSET
        if not isinstance(self.schedule_type, Unset):
            schedule_type = self.schedule_type.value

        schedule_events: Union[Unset, list[str]] = UNSET
        if not isinstance(self.schedule_events, Unset):
            schedule_events = []
            for schedule_events_item_data in self.schedule_events:
                schedule_events_item = schedule_events_item_data.value
                schedule_events.append(schedule_events_item)

        last_modified_date: Union[None, Unset, str]
        if isinstance(self.last_modified_date, Unset):
            last_modified_date = UNSET
        elif isinstance(self.last_modified_date, datetime.datetime):
            last_modified_date = self.last_modified_date.isoformat()
        else:
            last_modified_date = self.last_modified_date

        last_modified_by: Union[None, Unset, str]
        if isinstance(self.last_modified_by, Unset):
            last_modified_by = UNSET
        else:
            last_modified_by = self.last_modified_by

        failure_message: Union[None, Unset, str]
        if isinstance(self.failure_message, Unset):
            failure_message = UNSET
        else:
            failure_message = self.failure_message

        backed_up_size: Union[None, Unset, int]
        if isinstance(self.backed_up_size, Unset):
            backed_up_size = UNSET
        else:
            backed_up_size = self.backed_up_size

        free_space: Union[None, Unset, int]
        if isinstance(self.free_space, Unset):
            free_space = UNSET
        else:
            free_space = self.free_space

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if backup_agent_uid is not UNSET:
            field_dict["backupAgentUid"] = backup_agent_uid
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if name is not UNSET:
            field_dict["name"] = name
        if config_uid is not UNSET:
            field_dict["configUid"] = config_uid
        if backup_policy_uid is not UNSET:
            field_dict["backupPolicyUid"] = backup_policy_uid
        if backup_policy_failure_message is not UNSET:
            field_dict["backupPolicyFailureMessage"] = backup_policy_failure_message
        if operation_mode is not UNSET:
            field_dict["operationMode"] = operation_mode
        if destination is not UNSET:
            field_dict["destination"] = destination
        if restore_points is not UNSET:
            field_dict["restorePoints"] = restore_points
        if last_run is not UNSET:
            field_dict["lastRun"] = last_run
        if last_end_time is not UNSET:
            field_dict["lastEndTime"] = last_end_time
        if last_duration is not UNSET:
            field_dict["lastDuration"] = last_duration
        if next_run is not UNSET:
            field_dict["nextRun"] = next_run
        if avg_duration is not UNSET:
            field_dict["avgDuration"] = avg_duration
        if backup_mode is not UNSET:
            field_dict["backupMode"] = backup_mode
        if target_type is not UNSET:
            field_dict["targetType"] = target_type
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if schedule_type is not UNSET:
            field_dict["scheduleType"] = schedule_type
        if schedule_events is not UNSET:
            field_dict["scheduleEvents"] = schedule_events
        if last_modified_date is not UNSET:
            field_dict["lastModifiedDate"] = last_modified_date
        if last_modified_by is not UNSET:
            field_dict["lastModifiedBy"] = last_modified_by
        if failure_message is not UNSET:
            field_dict["failureMessage"] = failure_message
        if backed_up_size is not UNSET:
            field_dict["backedUpSize"] = backed_up_size
        if free_space is not UNSET:
            field_dict["freeSpace"] = free_space

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = WindowsBackupAgentJobStatus(d.pop("status"))

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

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        _config_uid = d.pop("configUid", UNSET)
        config_uid: Union[Unset, UUID]
        if isinstance(_config_uid, Unset):
            config_uid = UNSET
        else:
            config_uid = UUID(_config_uid)

        def _parse_backup_policy_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_policy_uid_type_0 = UUID(data)

                return backup_policy_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        backup_policy_uid = _parse_backup_policy_uid(d.pop("backupPolicyUid", UNSET))

        def _parse_backup_policy_failure_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        backup_policy_failure_message = _parse_backup_policy_failure_message(d.pop("backupPolicyFailureMessage", UNSET))

        _operation_mode = d.pop("operationMode", UNSET)
        operation_mode: Union[Unset, WindowsBackupAgentJobOperationMode]
        if isinstance(_operation_mode, Unset):
            operation_mode = UNSET
        else:
            operation_mode = WindowsBackupAgentJobOperationMode(_operation_mode)

        def _parse_destination(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        destination = _parse_destination(d.pop("destination", UNSET))

        def _parse_restore_points(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        restore_points = _parse_restore_points(d.pop("restorePoints", UNSET))

        def _parse_last_run(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_run_type_0 = isoparse(data)

                return last_run_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_run = _parse_last_run(d.pop("lastRun", UNSET))

        def _parse_last_end_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_end_time_type_0 = isoparse(data)

                return last_end_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_end_time = _parse_last_end_time(d.pop("lastEndTime", UNSET))

        def _parse_last_duration(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        last_duration = _parse_last_duration(d.pop("lastDuration", UNSET))

        def _parse_next_run(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_run_type_0 = isoparse(data)

                return next_run_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        next_run = _parse_next_run(d.pop("nextRun", UNSET))

        def _parse_avg_duration(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        avg_duration = _parse_avg_duration(d.pop("avgDuration", UNSET))

        _backup_mode = d.pop("backupMode", UNSET)
        backup_mode: Union[Unset, WindowsBackupAgentJobBackupMode]
        if isinstance(_backup_mode, Unset):
            backup_mode = UNSET
        else:
            backup_mode = WindowsBackupAgentJobBackupMode(_backup_mode)

        _target_type = d.pop("targetType", UNSET)
        target_type: Union[Unset, WindowsBackupAgentJobTargetType]
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = WindowsBackupAgentJobTargetType(_target_type)

        is_enabled = d.pop("isEnabled", UNSET)

        _schedule_type = d.pop("scheduleType", UNSET)
        schedule_type: Union[Unset, WindowsBackupAgentJobScheduleType]
        if isinstance(_schedule_type, Unset):
            schedule_type = UNSET
        else:
            schedule_type = WindowsBackupAgentJobScheduleType(_schedule_type)

        schedule_events = []
        _schedule_events = d.pop("scheduleEvents", UNSET)
        for schedule_events_item_data in _schedule_events or []:
            schedule_events_item = WindowsBackupAgentJobScheduleEventsItem(schedule_events_item_data)

            schedule_events.append(schedule_events_item)

        def _parse_last_modified_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_modified_date_type_0 = isoparse(data)

                return last_modified_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_modified_date = _parse_last_modified_date(d.pop("lastModifiedDate", UNSET))

        def _parse_last_modified_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_modified_by = _parse_last_modified_by(d.pop("lastModifiedBy", UNSET))

        def _parse_failure_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        failure_message = _parse_failure_message(d.pop("failureMessage", UNSET))

        def _parse_backed_up_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        backed_up_size = _parse_backed_up_size(d.pop("backedUpSize", UNSET))

        def _parse_free_space(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        free_space = _parse_free_space(d.pop("freeSpace", UNSET))

        windows_backup_agent_job = cls(
            status=status,
            instance_uid=instance_uid,
            backup_agent_uid=backup_agent_uid,
            organization_uid=organization_uid,
            name=name,
            config_uid=config_uid,
            backup_policy_uid=backup_policy_uid,
            backup_policy_failure_message=backup_policy_failure_message,
            operation_mode=operation_mode,
            destination=destination,
            restore_points=restore_points,
            last_run=last_run,
            last_end_time=last_end_time,
            last_duration=last_duration,
            next_run=next_run,
            avg_duration=avg_duration,
            backup_mode=backup_mode,
            target_type=target_type,
            is_enabled=is_enabled,
            schedule_type=schedule_type,
            schedule_events=schedule_events,
            last_modified_date=last_modified_date,
            last_modified_by=last_modified_by,
            failure_message=failure_message,
            backed_up_size=backed_up_size,
            free_space=free_space,
        )

        windows_backup_agent_job.additional_properties = d
        return windows_backup_agent_job

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
