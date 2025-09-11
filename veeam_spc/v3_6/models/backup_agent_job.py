import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.backup_agent_job_backup_mode import BackupAgentJobBackupMode
from ..models.backup_agent_job_schedule_type import BackupAgentJobScheduleType
from ..models.backup_agent_job_status import BackupAgentJobStatus
from ..models.backup_agent_job_system_type import BackupAgentJobSystemType
from ..models.backup_agent_job_target_type_detailed import BackupAgentJobTargetTypeDetailed
from ..models.backup_agent_operation_mode import BackupAgentOperationMode
from ..models.backup_policy_assign_status import BackupPolicyAssignStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupAgentJob")


@_attrs_define
class BackupAgentJob:
    r"""
    Attributes:
        status (BackupAgentJobStatus): Status of the latest job session.
            > Can be changed to `Running` or `Stopping` using the PATCH endpoint.
        instance_uid (Union[Unset, UUID]): UID assigned to a Veeam backup agent job.
        original_uid (Union[Unset, UUID]): UID assigned to a job on Veeam backup agent side.
        backup_agent_uid (Union[Unset, UUID]): UID assigned to a Veeam backup agent.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization.
        name (Union[Unset, str]): Name of a Veeam backup agent job.
        description (Union[Unset, str]): Description of a Veeam backup agent job.
        config_uid (Union[Unset, UUID]): UID assigned to a backup job configuration.
        system_type (Union[Unset, BackupAgentJobSystemType]): Type of guest OS on a managed computer.
        backup_policy_uid (Union[Unset, UUID]): UID of a backup policy assigned to a Veeam backup agent.
        backup_policy_name (Union[Unset, str]): Name of a backup policy assigned to a Veeam backup agent.
        backup_policy_assign_status (Union[Unset, BackupPolicyAssignStatus]):
        backup_policy_failure_message (Union[Unset, str]): Message that is displayed in case a backup policy job fails.
            > Every line break is represented by the `\r\n` control characters.
        operation_mode (Union[Unset, BackupAgentOperationMode]): Backup job operation mode.
        destination (Union[Unset, str]): Location where backup files for a Veeam backup agent reside.
        restore_points (Union[Unset, int]): Number of restore points.
        last_run (Union[Unset, datetime.datetime]): Date and time when the latest job session started.
        last_end_time (Union[Unset, datetime.datetime]): Date and time when the latest job session finished.
        last_duration (Union[Unset, int]): Duration of the latest backup job session, in seconds.
        next_run (Union[Unset, datetime.datetime]): Date and time of the next scheduled backup job session.
        avg_duration (Union[Unset, int]): Average duration of a backup job session, in seconds.
        backup_mode (Union[Unset, BackupAgentJobBackupMode]): Type of backup operation mode.
        target_type (Union[Unset, BackupAgentJobTargetTypeDetailed]): Type of a location where backup files for a Veeam
            backup agent reside.
        is_enabled (Union[Unset, bool]): Indicates whether a job schedule is enabled.
            > Can be changed using the PATCH endpoint.
        schedule_type (Union[Unset, BackupAgentJobScheduleType]): Type of schedule configured for the job.
        schedule_display_name (Union[Unset, str]): Name of a backup job schedule.
        last_modified_date (Union[Unset, datetime.datetime]): Date and time when settings of a backup job were last
            modified.
        last_modified_by (Union[Unset, str]): Name of a user who last modified job settings.
        failure_message (Union[Unset, str]): Message that is displayed in case a backup job fails.
        backed_up_size (Union[Unset, int]): Total size of all restore points, in bytes.
        free_space (Union[Unset, int]): Amount of free space available on the target repository.
            > If the job has never been run, the property value is `null`.
    """

    status: BackupAgentJobStatus
    instance_uid: Union[Unset, UUID] = UNSET
    original_uid: Union[Unset, UUID] = UNSET
    backup_agent_uid: Union[Unset, UUID] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    config_uid: Union[Unset, UUID] = UNSET
    system_type: Union[Unset, BackupAgentJobSystemType] = UNSET
    backup_policy_uid: Union[Unset, UUID] = UNSET
    backup_policy_name: Union[Unset, str] = UNSET
    backup_policy_assign_status: Union[Unset, BackupPolicyAssignStatus] = UNSET
    backup_policy_failure_message: Union[Unset, str] = UNSET
    operation_mode: Union[Unset, BackupAgentOperationMode] = UNSET
    destination: Union[Unset, str] = UNSET
    restore_points: Union[Unset, int] = UNSET
    last_run: Union[Unset, datetime.datetime] = UNSET
    last_end_time: Union[Unset, datetime.datetime] = UNSET
    last_duration: Union[Unset, int] = UNSET
    next_run: Union[Unset, datetime.datetime] = UNSET
    avg_duration: Union[Unset, int] = UNSET
    backup_mode: Union[Unset, BackupAgentJobBackupMode] = UNSET
    target_type: Union[Unset, BackupAgentJobTargetTypeDetailed] = UNSET
    is_enabled: Union[Unset, bool] = UNSET
    schedule_type: Union[Unset, BackupAgentJobScheduleType] = UNSET
    schedule_display_name: Union[Unset, str] = UNSET
    last_modified_date: Union[Unset, datetime.datetime] = UNSET
    last_modified_by: Union[Unset, str] = UNSET
    failure_message: Union[Unset, str] = UNSET
    backed_up_size: Union[Unset, int] = UNSET
    free_space: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        original_uid: Union[Unset, str] = UNSET
        if not isinstance(self.original_uid, Unset):
            original_uid = str(self.original_uid)

        backup_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_agent_uid, Unset):
            backup_agent_uid = str(self.backup_agent_uid)

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        name = self.name

        description = self.description

        config_uid: Union[Unset, str] = UNSET
        if not isinstance(self.config_uid, Unset):
            config_uid = str(self.config_uid)

        system_type: Union[Unset, str] = UNSET
        if not isinstance(self.system_type, Unset):
            system_type = self.system_type.value

        backup_policy_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_policy_uid, Unset):
            backup_policy_uid = str(self.backup_policy_uid)

        backup_policy_name = self.backup_policy_name

        backup_policy_assign_status: Union[Unset, str] = UNSET
        if not isinstance(self.backup_policy_assign_status, Unset):
            backup_policy_assign_status = self.backup_policy_assign_status.value

        backup_policy_failure_message = self.backup_policy_failure_message

        operation_mode: Union[Unset, str] = UNSET
        if not isinstance(self.operation_mode, Unset):
            operation_mode = self.operation_mode.value

        destination = self.destination

        restore_points = self.restore_points

        last_run: Union[Unset, str] = UNSET
        if not isinstance(self.last_run, Unset):
            last_run = self.last_run.isoformat()

        last_end_time: Union[Unset, str] = UNSET
        if not isinstance(self.last_end_time, Unset):
            last_end_time = self.last_end_time.isoformat()

        last_duration = self.last_duration

        next_run: Union[Unset, str] = UNSET
        if not isinstance(self.next_run, Unset):
            next_run = self.next_run.isoformat()

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

        schedule_display_name = self.schedule_display_name

        last_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_modified_date, Unset):
            last_modified_date = self.last_modified_date.isoformat()

        last_modified_by = self.last_modified_by

        failure_message = self.failure_message

        backed_up_size = self.backed_up_size

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
        if original_uid is not UNSET:
            field_dict["originalUid"] = original_uid
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
        if backup_policy_name is not UNSET:
            field_dict["backupPolicyName"] = backup_policy_name
        if backup_policy_assign_status is not UNSET:
            field_dict["backupPolicyAssignStatus"] = backup_policy_assign_status
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
        if schedule_display_name is not UNSET:
            field_dict["scheduleDisplayName"] = schedule_display_name
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
        status = BackupAgentJobStatus(d.pop("status"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _original_uid = d.pop("originalUid", UNSET)
        original_uid: Union[Unset, UUID]
        if isinstance(_original_uid, Unset):
            original_uid = UNSET
        else:
            original_uid = UUID(_original_uid)

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

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

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

        _backup_policy_uid = d.pop("backupPolicyUid", UNSET)
        backup_policy_uid: Union[Unset, UUID]
        if isinstance(_backup_policy_uid, Unset):
            backup_policy_uid = UNSET
        else:
            backup_policy_uid = UUID(_backup_policy_uid)

        backup_policy_name = d.pop("backupPolicyName", UNSET)

        _backup_policy_assign_status = d.pop("backupPolicyAssignStatus", UNSET)
        backup_policy_assign_status: Union[Unset, BackupPolicyAssignStatus]
        if isinstance(_backup_policy_assign_status, Unset):
            backup_policy_assign_status = UNSET
        else:
            backup_policy_assign_status = BackupPolicyAssignStatus(_backup_policy_assign_status)

        backup_policy_failure_message = d.pop("backupPolicyFailureMessage", UNSET)

        _operation_mode = d.pop("operationMode", UNSET)
        operation_mode: Union[Unset, BackupAgentOperationMode]
        if isinstance(_operation_mode, Unset):
            operation_mode = UNSET
        else:
            operation_mode = BackupAgentOperationMode(_operation_mode)

        destination = d.pop("destination", UNSET)

        restore_points = d.pop("restorePoints", UNSET)

        _last_run = d.pop("lastRun", UNSET)
        last_run: Union[Unset, datetime.datetime]
        if isinstance(_last_run, Unset):
            last_run = UNSET
        else:
            last_run = isoparse(_last_run)

        _last_end_time = d.pop("lastEndTime", UNSET)
        last_end_time: Union[Unset, datetime.datetime]
        if isinstance(_last_end_time, Unset):
            last_end_time = UNSET
        else:
            last_end_time = isoparse(_last_end_time)

        last_duration = d.pop("lastDuration", UNSET)

        _next_run = d.pop("nextRun", UNSET)
        next_run: Union[Unset, datetime.datetime]
        if isinstance(_next_run, Unset):
            next_run = UNSET
        else:
            next_run = isoparse(_next_run)

        avg_duration = d.pop("avgDuration", UNSET)

        _backup_mode = d.pop("backupMode", UNSET)
        backup_mode: Union[Unset, BackupAgentJobBackupMode]
        if isinstance(_backup_mode, Unset):
            backup_mode = UNSET
        else:
            backup_mode = BackupAgentJobBackupMode(_backup_mode)

        _target_type = d.pop("targetType", UNSET)
        target_type: Union[Unset, BackupAgentJobTargetTypeDetailed]
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = BackupAgentJobTargetTypeDetailed(_target_type)

        is_enabled = d.pop("isEnabled", UNSET)

        _schedule_type = d.pop("scheduleType", UNSET)
        schedule_type: Union[Unset, BackupAgentJobScheduleType]
        if isinstance(_schedule_type, Unset):
            schedule_type = UNSET
        else:
            schedule_type = BackupAgentJobScheduleType(_schedule_type)

        schedule_display_name = d.pop("scheduleDisplayName", UNSET)

        _last_modified_date = d.pop("lastModifiedDate", UNSET)
        last_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_last_modified_date, Unset):
            last_modified_date = UNSET
        else:
            last_modified_date = isoparse(_last_modified_date)

        last_modified_by = d.pop("lastModifiedBy", UNSET)

        failure_message = d.pop("failureMessage", UNSET)

        backed_up_size = d.pop("backedUpSize", UNSET)

        free_space = d.pop("freeSpace", UNSET)

        backup_agent_job = cls(
            status=status,
            instance_uid=instance_uid,
            original_uid=original_uid,
            backup_agent_uid=backup_agent_uid,
            organization_uid=organization_uid,
            name=name,
            description=description,
            config_uid=config_uid,
            system_type=system_type,
            backup_policy_uid=backup_policy_uid,
            backup_policy_name=backup_policy_name,
            backup_policy_assign_status=backup_policy_assign_status,
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
            schedule_display_name=schedule_display_name,
            last_modified_date=last_modified_date,
            last_modified_by=last_modified_by,
            failure_message=failure_message,
            backed_up_size=backed_up_size,
            free_space=free_space,
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
