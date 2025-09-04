import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.vb_365_copy_job_last_status import Vb365CopyJobLastStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vb_365_copy_job_schedule_policy import Vb365CopyJobSchedulePolicy
    from ..models.vb_365_job_session_log import Vb365JobSessionLog


T = TypeVar("T", bound="Vb365CopyJob")


@_attrs_define
class Vb365CopyJob:
    """
    Attributes:
        source_backup_job_uid (UUID): UID assigned to a source Veeam Backup for Microsoft 365 job.
        repository_uid (UUID): UID assigned to a backup repository.
        instance_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup for Microsoft 365 backup copy job.
        name (Union[Unset, str]): Name of a Veeam Backup for Microsoft 365 backup copy job.
        repository_name (Union[Unset, str]): Name of a backup repository.
        vb_365_organization_uid (Union[Unset, UUID]): UID assigned to a Microsoft organization.
        vspc_organization_uid (Union[Unset, UUID]): UID assigned to a Veeam Service Provider Console organization.
        vspc_organization_name (Union[Unset, str]): Name of a Veeam Service Provider Console organization.
        vb_365_server_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup for Microsoft 365 server.
        vb_365_server_name (Union[Unset, str]): Name of a Veeam Backup for Microsoft 365 server.
        last_run (Union[Unset, datetime.datetime]): Date and time of the latest job run.
        next_run (Union[Unset, datetime.datetime]): Date and time of the next scheduled job run.
        is_enabled (Union[Unset, bool]): Indicates whether a Veeam Backup for Microsoft 365 backup copy job is enabled.
            Default: True.
        last_status (Union[Unset, Vb365CopyJobLastStatus]): Status of the latest job run.
        last_status_details (Union[Unset, str]): Details on the latest job run.
        last_error_log_records (Union[Unset, list['Vb365JobSessionLog']]): The list of last job session logs.
        schedule_policy (Union[Unset, Vb365CopyJobSchedulePolicy]):
    """

    source_backup_job_uid: UUID
    repository_uid: UUID
    instance_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    repository_name: Union[Unset, str] = UNSET
    vb_365_organization_uid: Union[Unset, UUID] = UNSET
    vspc_organization_uid: Union[Unset, UUID] = UNSET
    vspc_organization_name: Union[Unset, str] = UNSET
    vb_365_server_uid: Union[Unset, UUID] = UNSET
    vb_365_server_name: Union[Unset, str] = UNSET
    last_run: Union[Unset, datetime.datetime] = UNSET
    next_run: Union[Unset, datetime.datetime] = UNSET
    is_enabled: Union[Unset, bool] = True
    last_status: Union[Unset, Vb365CopyJobLastStatus] = UNSET
    last_status_details: Union[Unset, str] = UNSET
    last_error_log_records: Union[Unset, list["Vb365JobSessionLog"]] = UNSET
    schedule_policy: Union[Unset, "Vb365CopyJobSchedulePolicy"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_backup_job_uid = str(self.source_backup_job_uid)

        repository_uid = str(self.repository_uid)

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        repository_name = self.repository_name

        vb_365_organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.vb_365_organization_uid, Unset):
            vb_365_organization_uid = str(self.vb_365_organization_uid)

        vspc_organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.vspc_organization_uid, Unset):
            vspc_organization_uid = str(self.vspc_organization_uid)

        vspc_organization_name = self.vspc_organization_name

        vb_365_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.vb_365_server_uid, Unset):
            vb_365_server_uid = str(self.vb_365_server_uid)

        vb_365_server_name = self.vb_365_server_name

        last_run: Union[Unset, str] = UNSET
        if not isinstance(self.last_run, Unset):
            last_run = self.last_run.isoformat()

        next_run: Union[Unset, str] = UNSET
        if not isinstance(self.next_run, Unset):
            next_run = self.next_run.isoformat()

        is_enabled = self.is_enabled

        last_status: Union[Unset, str] = UNSET
        if not isinstance(self.last_status, Unset):
            last_status = self.last_status.value

        last_status_details = self.last_status_details

        last_error_log_records: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.last_error_log_records, Unset):
            last_error_log_records = []
            for last_error_log_records_item_data in self.last_error_log_records:
                last_error_log_records_item = last_error_log_records_item_data.to_dict()
                last_error_log_records.append(last_error_log_records_item)

        schedule_policy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schedule_policy, Unset):
            schedule_policy = self.schedule_policy.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sourceBackupJobUid": source_backup_job_uid,
                "repositoryUid": repository_uid,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if name is not UNSET:
            field_dict["name"] = name
        if repository_name is not UNSET:
            field_dict["repositoryName"] = repository_name
        if vb_365_organization_uid is not UNSET:
            field_dict["vb365OrganizationUid"] = vb_365_organization_uid
        if vspc_organization_uid is not UNSET:
            field_dict["vspcOrganizationUid"] = vspc_organization_uid
        if vspc_organization_name is not UNSET:
            field_dict["vspcOrganizationName"] = vspc_organization_name
        if vb_365_server_uid is not UNSET:
            field_dict["vb365ServerUid"] = vb_365_server_uid
        if vb_365_server_name is not UNSET:
            field_dict["vb365ServerName"] = vb_365_server_name
        if last_run is not UNSET:
            field_dict["lastRun"] = last_run
        if next_run is not UNSET:
            field_dict["nextRun"] = next_run
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if last_status is not UNSET:
            field_dict["lastStatus"] = last_status
        if last_status_details is not UNSET:
            field_dict["lastStatusDetails"] = last_status_details
        if last_error_log_records is not UNSET:
            field_dict["lastErrorLogRecords"] = last_error_log_records
        if schedule_policy is not UNSET:
            field_dict["schedulePolicy"] = schedule_policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vb_365_copy_job_schedule_policy import Vb365CopyJobSchedulePolicy
        from ..models.vb_365_job_session_log import Vb365JobSessionLog

        d = dict(src_dict)
        source_backup_job_uid = UUID(d.pop("sourceBackupJobUid"))

        repository_uid = UUID(d.pop("repositoryUid"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        name = d.pop("name", UNSET)

        repository_name = d.pop("repositoryName", UNSET)

        _vb_365_organization_uid = d.pop("vb365OrganizationUid", UNSET)
        vb_365_organization_uid: Union[Unset, UUID]
        if isinstance(_vb_365_organization_uid, Unset):
            vb_365_organization_uid = UNSET
        else:
            vb_365_organization_uid = UUID(_vb_365_organization_uid)

        _vspc_organization_uid = d.pop("vspcOrganizationUid", UNSET)
        vspc_organization_uid: Union[Unset, UUID]
        if isinstance(_vspc_organization_uid, Unset):
            vspc_organization_uid = UNSET
        else:
            vspc_organization_uid = UUID(_vspc_organization_uid)

        vspc_organization_name = d.pop("vspcOrganizationName", UNSET)

        _vb_365_server_uid = d.pop("vb365ServerUid", UNSET)
        vb_365_server_uid: Union[Unset, UUID]
        if isinstance(_vb_365_server_uid, Unset):
            vb_365_server_uid = UNSET
        else:
            vb_365_server_uid = UUID(_vb_365_server_uid)

        vb_365_server_name = d.pop("vb365ServerName", UNSET)

        _last_run = d.pop("lastRun", UNSET)
        last_run: Union[Unset, datetime.datetime]
        if isinstance(_last_run, Unset):
            last_run = UNSET
        else:
            last_run = isoparse(_last_run)

        _next_run = d.pop("nextRun", UNSET)
        next_run: Union[Unset, datetime.datetime]
        if isinstance(_next_run, Unset):
            next_run = UNSET
        else:
            next_run = isoparse(_next_run)

        is_enabled = d.pop("isEnabled", UNSET)

        _last_status = d.pop("lastStatus", UNSET)
        last_status: Union[Unset, Vb365CopyJobLastStatus]
        if isinstance(_last_status, Unset):
            last_status = UNSET
        else:
            last_status = Vb365CopyJobLastStatus(_last_status)

        last_status_details = d.pop("lastStatusDetails", UNSET)

        last_error_log_records = []
        _last_error_log_records = d.pop("lastErrorLogRecords", UNSET)
        for last_error_log_records_item_data in _last_error_log_records or []:
            last_error_log_records_item = Vb365JobSessionLog.from_dict(last_error_log_records_item_data)

            last_error_log_records.append(last_error_log_records_item)

        _schedule_policy = d.pop("schedulePolicy", UNSET)
        schedule_policy: Union[Unset, Vb365CopyJobSchedulePolicy]
        if isinstance(_schedule_policy, Unset):
            schedule_policy = UNSET
        else:
            schedule_policy = Vb365CopyJobSchedulePolicy.from_dict(_schedule_policy)

        vb_365_copy_job = cls(
            source_backup_job_uid=source_backup_job_uid,
            repository_uid=repository_uid,
            instance_uid=instance_uid,
            name=name,
            repository_name=repository_name,
            vb_365_organization_uid=vb_365_organization_uid,
            vspc_organization_uid=vspc_organization_uid,
            vspc_organization_name=vspc_organization_name,
            vb_365_server_uid=vb_365_server_uid,
            vb_365_server_name=vb_365_server_name,
            last_run=last_run,
            next_run=next_run,
            is_enabled=is_enabled,
            last_status=last_status,
            last_status_details=last_status_details,
            last_error_log_records=last_error_log_records,
            schedule_policy=schedule_policy,
        )

        vb_365_copy_job.additional_properties = d
        return vb_365_copy_job

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
