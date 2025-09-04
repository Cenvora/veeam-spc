import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
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
    from ..models.backup_server_job_session_task import BackupServerJobSessionTask


T = TypeVar("T", bound="BackupServerJob")


@_attrs_define
class BackupServerJob:
    r"""
    Example:
        {'instanceUid': 'EDEB5975-B409-49B5-8ECE-FFFECB13494F', 'name': 'Web server Backup to Cloud', 'backupServerUid':
            'DF997BD3-4AE9-4841-8152-8FF5CC703EAB', 'status': 'Success', 'type': 'BackupVm', 'lastRun':
            datetime.datetime(2016, 11, 1, 18, 35, 28, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600),
            '+01:00')), 'endTime': datetime.datetime(2016, 11, 1, 18, 40, 56,
            tzinfo=datetime.timezone(datetime.timedelta(seconds=3600), '+01:00')), 'duration': 328, 'processingRate': 17,
            'avgDuration': 328, 'transferredData': 1052, 'bottleneck': 'Source', 'isEnabled': True, 'scheduleType':
            'Periodically', 'retentionLimit': 14, 'retentionLimitType': 'RestorePoints', 'isGfsOptionEnabled': True}

    Attributes:
        status (BackupServerJobStatus): Status of the latest job session.
            > Can be changed to `Running` or `Stopping` using the PATCH operation.
        is_enabled (bool): Indicates whether a job schedule is enabled.
            > Can be changed using the PATCH operation.
        instance_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Backup & Replication.
        unique_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Service Provider Console.
        name (Union[Unset, str]): Name of a job.
        description (Union[Unset, str]): Description of a job.
        created_by (Union[Unset, str]): Name of a user that created a job.
        creation_time (Union[None, Unset, datetime.datetime]): Date and time when a job was created.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup & Replication server.
        location_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup & Replication server location.
        site_uid (Union[None, UUID, Unset]): UID assigned to a Veeam Cloud Connect site.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization that owns a Veeam Backup & Replication
            server.
        mapped_organization_uid (Union[None, UUID, Unset]): UID assigned to an organization to whom the job is assigned.
        type_ (Union[Unset, BackupServerJobType]): Type of a job.
        last_run (Union[None, Unset, datetime.datetime]): Date and time when the latest job session started.
        last_end_time (Union[None, Unset, datetime.datetime]): Date and time when the latest job session ended.
        last_duration (Union[None, Unset, int]): Duration of the latest job session, in seconds.
        processing_rate (Union[None, Unset, float]): Rate at which VM data was processed during the latest job session.
        avg_duration (Union[None, Unset, int]): Average time a job session takes to complete, in seconds.
        transferred_data (Union[None, Unset, int]): Total amount of data that was transferred to target during the
            latest job session, in bytes.
        backup_chain_size (Union[None, Unset, int]): Size of all backup files created by the backup job, in bytes.
            > Available only for VMware vSphere and Microsoft HyperV VMs.
        bottleneck (Union[Unset, BackupServerJobBottleneck]): Bottleneck in the process of transferring the data from
            source to target.
        schedule_type (Union[Unset, BackupServerJobScheduleType]): Type of a schedule configured for a job.
        failure_message (Union[None, Unset, str]): Message that is displayed in case a backup job fails.
            > Every line break is represented by the `\r\n` control characters.
        target_type (Union[Unset, BackupServerJobTargetType]): Type of a target backup location.
        destination (Union[None, Unset, str]): Name of a target backup location.
        retention_limit (Union[None, Unset, int]): Number of retention policy units.
        retention_limit_type (Union[Unset, BackupServerJobRetentionLimitType]): Type of retention policy units.
        is_gfs_option_enabled (Union[Unset, bool]): Indicates whether the GFS retention is enabled.
        last_session_tasks (Union[Unset, list['BackupServerJobSessionTask']]): Latest job session tasks.
            > Available only for VM backup and replication jobs.
    """

    status: BackupServerJobStatus
    is_enabled: bool
    instance_uid: Union[Unset, UUID] = UNSET
    unique_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    creation_time: Union[None, Unset, datetime.datetime] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    location_uid: Union[Unset, UUID] = UNSET
    site_uid: Union[None, UUID, Unset] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    mapped_organization_uid: Union[None, UUID, Unset] = UNSET
    type_: Union[Unset, BackupServerJobType] = UNSET
    last_run: Union[None, Unset, datetime.datetime] = UNSET
    last_end_time: Union[None, Unset, datetime.datetime] = UNSET
    last_duration: Union[None, Unset, int] = UNSET
    processing_rate: Union[None, Unset, float] = UNSET
    avg_duration: Union[None, Unset, int] = UNSET
    transferred_data: Union[None, Unset, int] = UNSET
    backup_chain_size: Union[None, Unset, int] = UNSET
    bottleneck: Union[Unset, BackupServerJobBottleneck] = UNSET
    schedule_type: Union[Unset, BackupServerJobScheduleType] = UNSET
    failure_message: Union[None, Unset, str] = UNSET
    target_type: Union[Unset, BackupServerJobTargetType] = UNSET
    destination: Union[None, Unset, str] = UNSET
    retention_limit: Union[None, Unset, int] = UNSET
    retention_limit_type: Union[Unset, BackupServerJobRetentionLimitType] = UNSET
    is_gfs_option_enabled: Union[Unset, bool] = UNSET
    last_session_tasks: Union[Unset, list["BackupServerJobSessionTask"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        is_enabled = self.is_enabled

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        unique_uid: Union[Unset, str] = UNSET
        if not isinstance(self.unique_uid, Unset):
            unique_uid = str(self.unique_uid)

        name = self.name

        description = self.description

        created_by = self.created_by

        creation_time: Union[None, Unset, str]
        if isinstance(self.creation_time, Unset):
            creation_time = UNSET
        elif isinstance(self.creation_time, datetime.datetime):
            creation_time = self.creation_time.isoformat()
        else:
            creation_time = self.creation_time

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        location_uid: Union[Unset, str] = UNSET
        if not isinstance(self.location_uid, Unset):
            location_uid = str(self.location_uid)

        site_uid: Union[None, Unset, str]
        if isinstance(self.site_uid, Unset):
            site_uid = UNSET
        elif isinstance(self.site_uid, UUID):
            site_uid = str(self.site_uid)
        else:
            site_uid = self.site_uid

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        mapped_organization_uid: Union[None, Unset, str]
        if isinstance(self.mapped_organization_uid, Unset):
            mapped_organization_uid = UNSET
        elif isinstance(self.mapped_organization_uid, UUID):
            mapped_organization_uid = str(self.mapped_organization_uid)
        else:
            mapped_organization_uid = self.mapped_organization_uid

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

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

        processing_rate: Union[None, Unset, float]
        if isinstance(self.processing_rate, Unset):
            processing_rate = UNSET
        else:
            processing_rate = self.processing_rate

        avg_duration: Union[None, Unset, int]
        if isinstance(self.avg_duration, Unset):
            avg_duration = UNSET
        else:
            avg_duration = self.avg_duration

        transferred_data: Union[None, Unset, int]
        if isinstance(self.transferred_data, Unset):
            transferred_data = UNSET
        else:
            transferred_data = self.transferred_data

        backup_chain_size: Union[None, Unset, int]
        if isinstance(self.backup_chain_size, Unset):
            backup_chain_size = UNSET
        else:
            backup_chain_size = self.backup_chain_size

        bottleneck: Union[Unset, str] = UNSET
        if not isinstance(self.bottleneck, Unset):
            bottleneck = self.bottleneck.value

        schedule_type: Union[Unset, str] = UNSET
        if not isinstance(self.schedule_type, Unset):
            schedule_type = self.schedule_type.value

        failure_message: Union[None, Unset, str]
        if isinstance(self.failure_message, Unset):
            failure_message = UNSET
        else:
            failure_message = self.failure_message

        target_type: Union[Unset, str] = UNSET
        if not isinstance(self.target_type, Unset):
            target_type = self.target_type.value

        destination: Union[None, Unset, str]
        if isinstance(self.destination, Unset):
            destination = UNSET
        else:
            destination = self.destination

        retention_limit: Union[None, Unset, int]
        if isinstance(self.retention_limit, Unset):
            retention_limit = UNSET
        else:
            retention_limit = self.retention_limit

        retention_limit_type: Union[Unset, str] = UNSET
        if not isinstance(self.retention_limit_type, Unset):
            retention_limit_type = self.retention_limit_type.value

        is_gfs_option_enabled = self.is_gfs_option_enabled

        last_session_tasks: Union[Unset, list[dict[str, Any]]] = UNSET
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
        from ..models.backup_server_job_session_task import BackupServerJobSessionTask

        d = dict(src_dict)
        status = BackupServerJobStatus(d.pop("status"))

        is_enabled = d.pop("isEnabled")

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _unique_uid = d.pop("uniqueUid", UNSET)
        unique_uid: Union[Unset, UUID]
        if isinstance(_unique_uid, Unset):
            unique_uid = UNSET
        else:
            unique_uid = UUID(_unique_uid)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        created_by = d.pop("createdBy", UNSET)

        def _parse_creation_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                creation_time_type_0 = isoparse(data)

                return creation_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        creation_time = _parse_creation_time(d.pop("creationTime", UNSET))

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: Union[Unset, UUID]
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        _location_uid = d.pop("locationUid", UNSET)
        location_uid: Union[Unset, UUID]
        if isinstance(_location_uid, Unset):
            location_uid = UNSET
        else:
            location_uid = UUID(_location_uid)

        def _parse_site_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                site_uid_type_0 = UUID(data)

                return site_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        site_uid = _parse_site_uid(d.pop("siteUid", UNSET))

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        def _parse_mapped_organization_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mapped_organization_uid_type_0 = UUID(data)

                return mapped_organization_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        mapped_organization_uid = _parse_mapped_organization_uid(d.pop("mappedOrganizationUid", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, BackupServerJobType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BackupServerJobType(_type_)

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

        def _parse_processing_rate(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        processing_rate = _parse_processing_rate(d.pop("processingRate", UNSET))

        def _parse_avg_duration(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        avg_duration = _parse_avg_duration(d.pop("avgDuration", UNSET))

        def _parse_transferred_data(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        transferred_data = _parse_transferred_data(d.pop("transferredData", UNSET))

        def _parse_backup_chain_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        backup_chain_size = _parse_backup_chain_size(d.pop("backupChainSize", UNSET))

        _bottleneck = d.pop("bottleneck", UNSET)
        bottleneck: Union[Unset, BackupServerJobBottleneck]
        if isinstance(_bottleneck, Unset):
            bottleneck = UNSET
        else:
            bottleneck = BackupServerJobBottleneck(_bottleneck)

        _schedule_type = d.pop("scheduleType", UNSET)
        schedule_type: Union[Unset, BackupServerJobScheduleType]
        if isinstance(_schedule_type, Unset):
            schedule_type = UNSET
        else:
            schedule_type = BackupServerJobScheduleType(_schedule_type)

        def _parse_failure_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        failure_message = _parse_failure_message(d.pop("failureMessage", UNSET))

        _target_type = d.pop("targetType", UNSET)
        target_type: Union[Unset, BackupServerJobTargetType]
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = BackupServerJobTargetType(_target_type)

        def _parse_destination(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        destination = _parse_destination(d.pop("destination", UNSET))

        def _parse_retention_limit(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        retention_limit = _parse_retention_limit(d.pop("retentionLimit", UNSET))

        _retention_limit_type = d.pop("retentionLimitType", UNSET)
        retention_limit_type: Union[Unset, BackupServerJobRetentionLimitType]
        if isinstance(_retention_limit_type, Unset):
            retention_limit_type = UNSET
        else:
            retention_limit_type = BackupServerJobRetentionLimitType(_retention_limit_type)

        is_gfs_option_enabled = d.pop("isGfsOptionEnabled", UNSET)

        last_session_tasks = []
        _last_session_tasks = d.pop("lastSessionTasks", UNSET)
        for last_session_tasks_item_data in _last_session_tasks or []:
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
