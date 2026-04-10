from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.backup_server_job_bottleneck import BackupServerJobBottleneck
from ..models.backup_server_job_retention_limit_type import BackupServerJobRetentionLimitType
from ..models.backup_server_job_schedule_type import BackupServerJobScheduleType
from ..models.backup_server_job_status import BackupServerJobStatus
from ..models.backup_server_job_target_type import BackupServerJobTargetType
from ..models.backup_server_job_type import BackupServerJobType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_job_schedule import BackupServerJobSchedule
    from ..models.backup_server_job_session_task import BackupServerJobSessionTask


T = TypeVar("T", bound="BackupServerJob")


@_attrs_define
class BackupServerJob:
    r"""
    Example:
        {'instanceUid': 'EDEB5975-B409-49B5-8ECE-FFFECB13494F', 'name': 'Web server Backup to Cloud', 'backupServerUid':
            'DF997BD3-4AE9-4841-8152-8FF5CC703EAB', 'status': 'Success', 'type': 'BackupVm', 'lastRun':
            '2016-11-01T10:35:28.0000000-07:00', 'endTime': '2016-11-01T10:40:56.0000000-07:00', 'duration': 328,
            'processingRate': 17, 'avgDuration': 328, 'transferredData': 1052, 'bottleneck': 'Source', 'isEnabled': True,
            'scheduleType': 'Periodically', 'retentionLimit': 14, 'retentionLimitType': 'RestorePoints',
            'isGfsOptionEnabled': True}

    Attributes:
        status (BackupServerJobStatus): Status of the latest job session.
            > Can be changed to `Running` or `Stopping` using the PATCH operation.
        is_enabled (bool): Indicates whether a job schedule is enabled.
            > Can be changed using the PATCH operation.
        instance_uid (UUID | Unset): UID assigned to a job in Veeam Backup & Replication.
        unique_uid (UUID | Unset): UID assigned to a job in Veeam Service Provider Console.
        name (str | Unset): Name of a job.
        description (str | Unset): Description of a job.
        created_by (str | Unset): Name of a user that created a job.
        creation_time (datetime.datetime | Unset): Date and time when a job was created.
        backup_server_uid (UUID | Unset): UID assigned to a Veeam Backup & Replication server.
        location_uid (UUID | Unset): UID assigned to a Veeam Backup & Replication server location.
        site_uid (UUID | Unset): UID assigned to a Veeam Cloud Connect site.
        organization_uid (UUID | Unset): UID assigned to an organization that owns a Veeam Backup & Replication server.
        mapped_organization_uid (UUID | Unset): UID assigned to an organization to whom the job is assigned.
        type_ (BackupServerJobType | Unset): Type of a job.
        last_run (datetime.datetime | Unset): Date and time when the latest job session started.
        last_end_time (datetime.datetime | Unset): Date and time when the latest job session ended.
        last_duration (int | Unset): Duration of the latest job session, in seconds.
        processing_rate (float | Unset): Rate at which VM data was processed during the latest job session.
        avg_duration (int | Unset): Average time a job session takes to complete, in seconds.
        transferred_data (int | Unset): Total amount of data that was transferred to target during the latest job
            session, in bytes.
        backup_chain_size (int | Unset): Size of all backup files created by the backup job, in bytes.
            > Available only for VMware vSphere and Microsoft HyperV VMs.
        bottleneck (BackupServerJobBottleneck | Unset): Bottleneck in the process of transferring the data from source
            to target.
        schedule_type (BackupServerJobScheduleType | Unset): Type of a schedule configured for a job.
        schedule (BackupServerJobSchedule | Unset):
        failure_message (str | Unset): Message that is displayed in case a backup job fails.
            > Every line break is represented by the `\r\n` control characters.
        target_type (BackupServerJobTargetType | Unset): Type of a target backup location.
        destination (str | Unset): Name of a target backup location.
        retention_limit (int | Unset): Number of retention policy units.
        retention_limit_type (BackupServerJobRetentionLimitType | Unset): Type of retention policy units.
        is_gfs_option_enabled (bool | Unset): Indicates whether the GFS retention is enabled.
        last_session_tasks (list[BackupServerJobSessionTask] | Unset): Latest job session tasks.
            > Available only for VM backup and replication jobs.
    """

    status: BackupServerJobStatus
    is_enabled: bool
    instance_uid: UUID | Unset = UNSET
    unique_uid: UUID | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    created_by: str | Unset = UNSET
    creation_time: datetime.datetime | Unset = UNSET
    backup_server_uid: UUID | Unset = UNSET
    location_uid: UUID | Unset = UNSET
    site_uid: UUID | Unset = UNSET
    organization_uid: UUID | Unset = UNSET
    mapped_organization_uid: UUID | Unset = UNSET
    type_: BackupServerJobType | Unset = UNSET
    last_run: datetime.datetime | Unset = UNSET
    last_end_time: datetime.datetime | Unset = UNSET
    last_duration: int | Unset = UNSET
    processing_rate: float | Unset = UNSET
    avg_duration: int | Unset = UNSET
    transferred_data: int | Unset = UNSET
    backup_chain_size: int | Unset = UNSET
    bottleneck: BackupServerJobBottleneck | Unset = UNSET
    schedule_type: BackupServerJobScheduleType | Unset = UNSET
    schedule: BackupServerJobSchedule | Unset = UNSET
    failure_message: str | Unset = UNSET
    target_type: BackupServerJobTargetType | Unset = UNSET
    destination: str | Unset = UNSET
    retention_limit: int | Unset = UNSET
    retention_limit_type: BackupServerJobRetentionLimitType | Unset = UNSET
    is_gfs_option_enabled: bool | Unset = UNSET
    last_session_tasks: list[BackupServerJobSessionTask] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        is_enabled = self.is_enabled

        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        unique_uid: str | Unset = UNSET
        if not isinstance(self.unique_uid, Unset):
            unique_uid = str(self.unique_uid)

        name = self.name

        description = self.description

        created_by = self.created_by

        creation_time: str | Unset = UNSET
        if not isinstance(self.creation_time, Unset):
            creation_time = self.creation_time.isoformat()

        backup_server_uid: str | Unset = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        location_uid: str | Unset = UNSET
        if not isinstance(self.location_uid, Unset):
            location_uid = str(self.location_uid)

        site_uid: str | Unset = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        organization_uid: str | Unset = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        mapped_organization_uid: str | Unset = UNSET
        if not isinstance(self.mapped_organization_uid, Unset):
            mapped_organization_uid = str(self.mapped_organization_uid)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        last_run: str | Unset = UNSET
        if not isinstance(self.last_run, Unset):
            last_run = self.last_run.isoformat()

        last_end_time: str | Unset = UNSET
        if not isinstance(self.last_end_time, Unset):
            last_end_time = self.last_end_time.isoformat()

        last_duration = self.last_duration

        processing_rate = self.processing_rate

        avg_duration = self.avg_duration

        transferred_data = self.transferred_data

        backup_chain_size = self.backup_chain_size

        bottleneck: str | Unset = UNSET
        if not isinstance(self.bottleneck, Unset):
            bottleneck = self.bottleneck.value

        schedule_type: str | Unset = UNSET
        if not isinstance(self.schedule_type, Unset):
            schedule_type = self.schedule_type.value

        schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        failure_message = self.failure_message

        target_type: str | Unset = UNSET
        if not isinstance(self.target_type, Unset):
            target_type = self.target_type.value

        destination = self.destination

        retention_limit = self.retention_limit

        retention_limit_type: str | Unset = UNSET
        if not isinstance(self.retention_limit_type, Unset):
            retention_limit_type = self.retention_limit_type.value

        is_gfs_option_enabled = self.is_gfs_option_enabled

        last_session_tasks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.last_session_tasks, Unset):
            last_session_tasks = []
            for last_session_tasks_item_data in self.last_session_tasks:
                last_session_tasks_item = last_session_tasks_item_data.to_dict()
                last_session_tasks.append(last_session_tasks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "isEnabled": is_enabled,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if unique_uid is not UNSET:
            field_dict["uniqueUid"] = unique_uid
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if creation_time is not UNSET:
            field_dict["creationTime"] = creation_time
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if location_uid is not UNSET:
            field_dict["locationUid"] = location_uid
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if mapped_organization_uid is not UNSET:
            field_dict["mappedOrganizationUid"] = mapped_organization_uid
        if type_ is not UNSET:
            field_dict["type"] = type_
        if last_run is not UNSET:
            field_dict["lastRun"] = last_run
        if last_end_time is not UNSET:
            field_dict["lastEndTime"] = last_end_time
        if last_duration is not UNSET:
            field_dict["lastDuration"] = last_duration
        if processing_rate is not UNSET:
            field_dict["processingRate"] = processing_rate
        if avg_duration is not UNSET:
            field_dict["avgDuration"] = avg_duration
        if transferred_data is not UNSET:
            field_dict["transferredData"] = transferred_data
        if backup_chain_size is not UNSET:
            field_dict["backupChainSize"] = backup_chain_size
        if bottleneck is not UNSET:
            field_dict["bottleneck"] = bottleneck
        if schedule_type is not UNSET:
            field_dict["scheduleType"] = schedule_type
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if failure_message is not UNSET:
            field_dict["failureMessage"] = failure_message
        if target_type is not UNSET:
            field_dict["targetType"] = target_type
        if destination is not UNSET:
            field_dict["destination"] = destination
        if retention_limit is not UNSET:
            field_dict["retentionLimit"] = retention_limit
        if retention_limit_type is not UNSET:
            field_dict["retentionLimitType"] = retention_limit_type
        if is_gfs_option_enabled is not UNSET:
            field_dict["isGfsOptionEnabled"] = is_gfs_option_enabled
        if last_session_tasks is not UNSET:
            field_dict["lastSessionTasks"] = last_session_tasks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_job_schedule import BackupServerJobSchedule
        from ..models.backup_server_job_session_task import BackupServerJobSessionTask

        d = dict(src_dict)
        status = BackupServerJobStatus(d.pop("status"))

        is_enabled = d.pop("isEnabled")

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

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        created_by = d.pop("createdBy", UNSET)

        _creation_time = d.pop("creationTime", UNSET)
        creation_time: datetime.datetime | Unset
        if isinstance(_creation_time, Unset):
            creation_time = UNSET
        else:
            creation_time = isoparse(_creation_time)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: UUID | Unset
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        _location_uid = d.pop("locationUid", UNSET)
        location_uid: UUID | Unset
        if isinstance(_location_uid, Unset):
            location_uid = UNSET
        else:
            location_uid = UUID(_location_uid)

        _site_uid = d.pop("siteUid", UNSET)
        site_uid: UUID | Unset
        if isinstance(_site_uid, Unset):
            site_uid = UNSET
        else:
            site_uid = UUID(_site_uid)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: UUID | Unset
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        _mapped_organization_uid = d.pop("mappedOrganizationUid", UNSET)
        mapped_organization_uid: UUID | Unset
        if isinstance(_mapped_organization_uid, Unset):
            mapped_organization_uid = UNSET
        else:
            mapped_organization_uid = UUID(_mapped_organization_uid)

        _type_ = d.pop("type", UNSET)
        type_: BackupServerJobType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BackupServerJobType(_type_)

        _last_run = d.pop("lastRun", UNSET)
        last_run: datetime.datetime | Unset
        if isinstance(_last_run, Unset):
            last_run = UNSET
        else:
            last_run = isoparse(_last_run)

        _last_end_time = d.pop("lastEndTime", UNSET)
        last_end_time: datetime.datetime | Unset
        if isinstance(_last_end_time, Unset):
            last_end_time = UNSET
        else:
            last_end_time = isoparse(_last_end_time)

        last_duration = d.pop("lastDuration", UNSET)

        processing_rate = d.pop("processingRate", UNSET)

        avg_duration = d.pop("avgDuration", UNSET)

        transferred_data = d.pop("transferredData", UNSET)

        backup_chain_size = d.pop("backupChainSize", UNSET)

        _bottleneck = d.pop("bottleneck", UNSET)
        bottleneck: BackupServerJobBottleneck | Unset
        if isinstance(_bottleneck, Unset):
            bottleneck = UNSET
        else:
            bottleneck = BackupServerJobBottleneck(_bottleneck)

        _schedule_type = d.pop("scheduleType", UNSET)
        schedule_type: BackupServerJobScheduleType | Unset
        if isinstance(_schedule_type, Unset):
            schedule_type = UNSET
        else:
            schedule_type = BackupServerJobScheduleType(_schedule_type)

        _schedule = d.pop("schedule", UNSET)
        schedule: BackupServerJobSchedule | Unset
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = BackupServerJobSchedule.from_dict(_schedule)

        failure_message = d.pop("failureMessage", UNSET)

        _target_type = d.pop("targetType", UNSET)
        target_type: BackupServerJobTargetType | Unset
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = BackupServerJobTargetType(_target_type)

        destination = d.pop("destination", UNSET)

        retention_limit = d.pop("retentionLimit", UNSET)

        _retention_limit_type = d.pop("retentionLimitType", UNSET)
        retention_limit_type: BackupServerJobRetentionLimitType | Unset
        if isinstance(_retention_limit_type, Unset):
            retention_limit_type = UNSET
        else:
            retention_limit_type = BackupServerJobRetentionLimitType(_retention_limit_type)

        is_gfs_option_enabled = d.pop("isGfsOptionEnabled", UNSET)

        _last_session_tasks = d.pop("lastSessionTasks", UNSET)
        last_session_tasks: list[BackupServerJobSessionTask] | Unset = UNSET
        if _last_session_tasks is not UNSET:
            last_session_tasks = []
            for last_session_tasks_item_data in _last_session_tasks:
                last_session_tasks_item = BackupServerJobSessionTask.from_dict(last_session_tasks_item_data)

                last_session_tasks.append(last_session_tasks_item)

        backup_server_job = cls(
            status=status,
            is_enabled=is_enabled,
            instance_uid=instance_uid,
            unique_uid=unique_uid,
            name=name,
            description=description,
            created_by=created_by,
            creation_time=creation_time,
            backup_server_uid=backup_server_uid,
            location_uid=location_uid,
            site_uid=site_uid,
            organization_uid=organization_uid,
            mapped_organization_uid=mapped_organization_uid,
            type_=type_,
            last_run=last_run,
            last_end_time=last_end_time,
            last_duration=last_duration,
            processing_rate=processing_rate,
            avg_duration=avg_duration,
            transferred_data=transferred_data,
            backup_chain_size=backup_chain_size,
            bottleneck=bottleneck,
            schedule_type=schedule_type,
            schedule=schedule,
            failure_message=failure_message,
            target_type=target_type,
            destination=destination,
            retention_limit=retention_limit,
            retention_limit_type=retention_limit_type,
            is_gfs_option_enabled=is_gfs_option_enabled,
            last_session_tasks=last_session_tasks,
        )

        backup_server_job.additional_properties = d
        return backup_server_job

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
