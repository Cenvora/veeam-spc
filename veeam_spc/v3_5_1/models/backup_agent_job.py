import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.backup_agent_job_backup_mode import BackupAgentJobBackupMode
from ..models.backup_agent_job_operation_mode import BackupAgentJobOperationMode
from ..models.backup_agent_job_schedule_type import BackupAgentJobScheduleType
from ..models.backup_agent_job_status import BackupAgentJobStatus
from ..models.backup_agent_job_system_type import BackupAgentJobSystemType
from ..models.backup_agent_job_target_type import BackupAgentJobTargetType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupAgentJob")


@_attrs_define
class BackupAgentJob:
    r"""
    Attributes:
        status (BackupAgentJobStatus): Status of the latest job session.
            > Can be changed to `Running` or `Stopping` using the PATCH endpoint.
        instance_uid (Union[Unset, UUID]): UID assigned to a Veeam backup agent job.
        backup_agent_uid (Union[Unset, UUID]): UID assigned to a Veeam backup agent.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization.
        name (Union[None, Unset, str]): Name of a Veeam backup agent job.
        description (Union[None, Unset, str]): Description of a Veeam backup agent job.
        config_uid (Union[Unset, UUID]): UID assigned to a backup job configuration.
        system_type (Union[Unset, BackupAgentJobSystemType]): Type of guest OS on a managed computer.
        backup_policy_uid (Union[None, UUID, Unset]): UID of a backup policy assigned to a Veeam backup agent.
        backup_policy_failure_message (Union[None, Unset, str]): Message that is displayed in case a backup policy job
            fails.
            > Every line break is represented by the `\r\n` control characters.
        operation_mode (Union[Unset, BackupAgentJobOperationMode]): Operation mode of a Veeam backup agent.
        destination (Union[None, Unset, str]): Location where backup files for a Veeam backup agent reside.
        restore_points (Union[None, Unset, int]): Number of restore points.
        last_run (Union[None, Unset, datetime.datetime]): Date and time when the latest job session started.
        last_end_time (Union[None, Unset, datetime.datetime]): Date and time when the latest job session finished.
        last_duration (Union[None, Unset, int]): Duration of the latest backup job session, in seconds.
        next_run (Union[None, Unset, datetime.datetime]): Date and time of the next scheduled backup job session.
        avg_duration (Union[None, Unset, int]): Average duration of a backup job session, in seconds.
        backup_mode (Union[Unset, BackupAgentJobBackupMode]): Type of backup operation mode.
        target_type (Union[Unset, BackupAgentJobTargetType]): Type of a location where backup files for a Veeam backup
            agent reside.
        is_enabled (Union[Unset, bool]): Indicates whether a job schedule is enabled.
            > Can be changed using the PATCH endpoint.
        schedule_type (Union[Unset, BackupAgentJobScheduleType]): Type of schedule configured for the job.
        failure_message (Union[None, Unset, str]): Message that is displayed in case a backup job fails.
        backed_up_size (Union[None, Unset, int]): Total size of all restore points, in bytes.
    """

    status: BackupAgentJobStatus
    instance_uid: Union[Unset, UUID] = UNSET
    backup_agent_uid: Union[Unset, UUID] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    name: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    config_uid: Union[Unset, UUID] = UNSET
    system_type: Union[Unset, BackupAgentJobSystemType] = UNSET
    backup_policy_uid: Union[None, UUID, Unset] = UNSET
    backup_policy_failure_message: Union[None, Unset, str] = UNSET
    operation_mode: Union[Unset, BackupAgentJobOperationMode] = UNSET
    destination: Union[None, Unset, str] = UNSET
    restore_points: Union[None, Unset, int] = UNSET
    last_run: Union[None, Unset, datetime.datetime] = UNSET
    last_end_time: Union[None, Unset, datetime.datetime] = UNSET
    last_duration: Union[None, Unset, int] = UNSET
    next_run: Union[None, Unset, datetime.datetime] = UNSET
    avg_duration: Union[None, Unset, int] = UNSET
    backup_mode: Union[Unset, BackupAgentJobBackupMode] = UNSET
    target_type: Union[Unset, BackupAgentJobTargetType] = UNSET
    is_enabled: Union[Unset, bool] = UNSET
    schedule_type: Union[Unset, BackupAgentJobScheduleType] = UNSET
    failure_message: Union[None, Unset, str] = UNSET
    backed_up_size: Union[None, Unset, int] = UNSET
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

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        config_uid: Union[Unset, str] = UNSET
        if not isinstance(self.config_uid, Unset):
            config_uid = str(self.config_uid)

        system_type: Union[Unset, str] = UNSET
        if not isinstance(self.system_type, Unset):
            system_type = self.system_type.value

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
        if description is not UNSET:
            field_dict["description"] = description
        if config_uid is not UNSET:
            field_dict["configUid"] = config_uid
        if system_type is not UNSET:
            field_dict["systemType"] = system_type
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
        if failure_message is not UNSET:
            field_dict["failureMessage"] = failure_message
        if backed_up_size is not UNSET:
            field_dict["backedUpSize"] = backed_up_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = BackupAgentJobStatus(d.pop("status"))

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

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        _config_uid = d.pop("configUid", UNSET)
        config_uid: Union[Unset, UUID]
        if isinstance(_config_uid, Unset):
            config_uid = UNSET
        else:
            config_uid = UUID(_config_uid)

        _system_type = d.pop("systemType", UNSET)
        system_type: Union[Unset, BackupAgentJobSystemType]
        if isinstance(_system_type, Unset):
            system_type = UNSET
        else:
            system_type = BackupAgentJobSystemType(_system_type)

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
        operation_mode: Union[Unset, BackupAgentJobOperationMode]
        if isinstance(_operation_mode, Unset):
            operation_mode = UNSET
        else:
            operation_mode = BackupAgentJobOperationMode(_operation_mode)

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
        backup_mode: Union[Unset, BackupAgentJobBackupMode]
        if isinstance(_backup_mode, Unset):
            backup_mode = UNSET
        else:
            backup_mode = BackupAgentJobBackupMode(_backup_mode)

        _target_type = d.pop("targetType", UNSET)
        target_type: Union[Unset, BackupAgentJobTargetType]
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = BackupAgentJobTargetType(_target_type)

        is_enabled = d.pop("isEnabled", UNSET)

        _schedule_type = d.pop("scheduleType", UNSET)
        schedule_type: Union[Unset, BackupAgentJobScheduleType]
        if isinstance(_schedule_type, Unset):
            schedule_type = UNSET
        else:
            schedule_type = BackupAgentJobScheduleType(_schedule_type)

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

        backup_agent_job = cls(
            status=status,
            instance_uid=instance_uid,
            backup_agent_uid=backup_agent_uid,
            organization_uid=organization_uid,
            name=name,
            description=description,
            config_uid=config_uid,
            system_type=system_type,
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
            failure_message=failure_message,
            backed_up_size=backed_up_size,
        )

        backup_agent_job.additional_properties = d
        return backup_agent_job

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
