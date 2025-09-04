import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.vb_365_job_job_type import Vb365JobJobType
from ..models.vb_365_job_last_status import Vb365JobLastStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vb_365_job_session_log import Vb365JobSessionLog


T = TypeVar("T", bound="Vb365Job")


@_attrs_define
class Vb365Job:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup for Microsoft 365 job.
        name (Union[Unset, str]): Name of a Veeam Backup for Microsoft 365 job.
        job_type (Union[Unset, Vb365JobJobType]): Type of a Veeam Backup for Microsoft 365 job.
        repository_uid (Union[Unset, UUID]): UID assigned to a backup repository.
        repository_name (Union[Unset, str]): Name of a backup repository.
        vb_365_organization_uid (Union[Unset, UUID]): UID assigned to a Microsoft organization.
        vspc_organization_uid (Union[None, UUID, Unset]): UID assigned to a Veeam Service Provider Console organization.
        vspc_organization_name (Union[None, Unset, str]): Name of a Veeam Service Provider Console organization.
        schedule_editing_available (Union[Unset, bool]): Indicates whether job schedule editing is available to a
            current user.
        vb_365_server_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup for Microsoft 365 server.
        vb_365_server_name (Union[Unset, str]): Name of a Veeam Backup for Microsoft 365 server.
        management_agent_uid (Union[Unset, UUID]): UID assigned to a management agent installed on a Veeam Backup for
            Microsoft 365 Server.
        last_run (Union[None, Unset, datetime.datetime]): Date and time of the latest job run.
        next_run (Union[None, Unset, datetime.datetime]): Date and time of the next scheduled job run.
        is_enabled (Union[Unset, bool]): Indicates whether a Veeam Backup for Microsoft 365 job is enabled. Default:
            False.
        is_copy_job_available (Union[Unset, bool]): Indicates whether a backup copy job can be created for the Veeam
            Backup for Microsoft 365 job.
        last_status (Union[Unset, Vb365JobLastStatus]): Status of the latest job run.
        last_status_details (Union[Unset, str]): Details on the latest job run.
        last_error_log_records (Union[Unset, list['Vb365JobSessionLog']]): The list of last job session logs.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    job_type: Union[Unset, Vb365JobJobType] = UNSET
    repository_uid: Union[Unset, UUID] = UNSET
    repository_name: Union[Unset, str] = UNSET
    vb_365_organization_uid: Union[Unset, UUID] = UNSET
    vspc_organization_uid: Union[None, UUID, Unset] = UNSET
    vspc_organization_name: Union[None, Unset, str] = UNSET
    schedule_editing_available: Union[Unset, bool] = UNSET
    vb_365_server_uid: Union[Unset, UUID] = UNSET
    vb_365_server_name: Union[Unset, str] = UNSET
    management_agent_uid: Union[Unset, UUID] = UNSET
    last_run: Union[None, Unset, datetime.datetime] = UNSET
    next_run: Union[None, Unset, datetime.datetime] = UNSET
    is_enabled: Union[Unset, bool] = False
    is_copy_job_available: Union[Unset, bool] = UNSET
    last_status: Union[Unset, Vb365JobLastStatus] = UNSET
    last_status_details: Union[Unset, str] = UNSET
    last_error_log_records: Union[Unset, list["Vb365JobSessionLog"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        job_type: Union[Unset, str] = UNSET
        if not isinstance(self.job_type, Unset):
            job_type = self.job_type.value

        repository_uid: Union[Unset, str] = UNSET
        if not isinstance(self.repository_uid, Unset):
            repository_uid = str(self.repository_uid)

        repository_name = self.repository_name

        vb_365_organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.vb_365_organization_uid, Unset):
            vb_365_organization_uid = str(self.vb_365_organization_uid)

        vspc_organization_uid: Union[None, Unset, str]
        if isinstance(self.vspc_organization_uid, Unset):
            vspc_organization_uid = UNSET
        elif isinstance(self.vspc_organization_uid, UUID):
            vspc_organization_uid = str(self.vspc_organization_uid)
        else:
            vspc_organization_uid = self.vspc_organization_uid

        vspc_organization_name: Union[None, Unset, str]
        if isinstance(self.vspc_organization_name, Unset):
            vspc_organization_name = UNSET
        else:
            vspc_organization_name = self.vspc_organization_name

        schedule_editing_available = self.schedule_editing_available

        vb_365_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.vb_365_server_uid, Unset):
            vb_365_server_uid = str(self.vb_365_server_uid)

        vb_365_server_name = self.vb_365_server_name

        management_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.management_agent_uid, Unset):
            management_agent_uid = str(self.management_agent_uid)

        last_run: Union[None, Unset, str]
        if isinstance(self.last_run, Unset):
            last_run = UNSET
        elif isinstance(self.last_run, datetime.datetime):
            last_run = self.last_run.isoformat()
        else:
            last_run = self.last_run

        next_run: Union[None, Unset, str]
        if isinstance(self.next_run, Unset):
            next_run = UNSET
        elif isinstance(self.next_run, datetime.datetime):
            next_run = self.next_run.isoformat()
        else:
            next_run = self.next_run

        is_enabled = self.is_enabled

        is_copy_job_available = self.is_copy_job_available

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if name is not UNSET:
            field_dict["name"] = name
        if job_type is not UNSET:
            field_dict["jobType"] = job_type
        if repository_uid is not UNSET:
            field_dict["repositoryUid"] = repository_uid
        if repository_name is not UNSET:
            field_dict["repositoryName"] = repository_name
        if vb_365_organization_uid is not UNSET:
            field_dict["vb365OrganizationUid"] = vb_365_organization_uid
        if vspc_organization_uid is not UNSET:
            field_dict["vspcOrganizationUid"] = vspc_organization_uid
        if vspc_organization_name is not UNSET:
            field_dict["vspcOrganizationName"] = vspc_organization_name
        if schedule_editing_available is not UNSET:
            field_dict["scheduleEditingAvailable"] = schedule_editing_available
        if vb_365_server_uid is not UNSET:
            field_dict["vb365ServerUid"] = vb_365_server_uid
        if vb_365_server_name is not UNSET:
            field_dict["vb365ServerName"] = vb_365_server_name
        if management_agent_uid is not UNSET:
            field_dict["managementAgentUid"] = management_agent_uid
        if last_run is not UNSET:
            field_dict["lastRun"] = last_run
        if next_run is not UNSET:
            field_dict["nextRun"] = next_run
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if is_copy_job_available is not UNSET:
            field_dict["isCopyJobAvailable"] = is_copy_job_available
        if last_status is not UNSET:
            field_dict["lastStatus"] = last_status
        if last_status_details is not UNSET:
            field_dict["lastStatusDetails"] = last_status_details
        if last_error_log_records is not UNSET:
            field_dict["lastErrorLogRecords"] = last_error_log_records

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vb_365_job_session_log import Vb365JobSessionLog

        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        name = d.pop("name", UNSET)

        _job_type = d.pop("jobType", UNSET)
        job_type: Union[Unset, Vb365JobJobType]
        if isinstance(_job_type, Unset):
            job_type = UNSET
        else:
            job_type = Vb365JobJobType(_job_type)

        _repository_uid = d.pop("repositoryUid", UNSET)
        repository_uid: Union[Unset, UUID]
        if isinstance(_repository_uid, Unset):
            repository_uid = UNSET
        else:
            repository_uid = UUID(_repository_uid)

        repository_name = d.pop("repositoryName", UNSET)

        _vb_365_organization_uid = d.pop("vb365OrganizationUid", UNSET)
        vb_365_organization_uid: Union[Unset, UUID]
        if isinstance(_vb_365_organization_uid, Unset):
            vb_365_organization_uid = UNSET
        else:
            vb_365_organization_uid = UUID(_vb_365_organization_uid)

        def _parse_vspc_organization_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                vspc_organization_uid_type_0 = UUID(data)

                return vspc_organization_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        vspc_organization_uid = _parse_vspc_organization_uid(d.pop("vspcOrganizationUid", UNSET))

        def _parse_vspc_organization_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        vspc_organization_name = _parse_vspc_organization_name(d.pop("vspcOrganizationName", UNSET))

        schedule_editing_available = d.pop("scheduleEditingAvailable", UNSET)

        _vb_365_server_uid = d.pop("vb365ServerUid", UNSET)
        vb_365_server_uid: Union[Unset, UUID]
        if isinstance(_vb_365_server_uid, Unset):
            vb_365_server_uid = UNSET
        else:
            vb_365_server_uid = UUID(_vb_365_server_uid)

        vb_365_server_name = d.pop("vb365ServerName", UNSET)

        _management_agent_uid = d.pop("managementAgentUid", UNSET)
        management_agent_uid: Union[Unset, UUID]
        if isinstance(_management_agent_uid, Unset):
            management_agent_uid = UNSET
        else:
            management_agent_uid = UUID(_management_agent_uid)

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

        is_enabled = d.pop("isEnabled", UNSET)

        is_copy_job_available = d.pop("isCopyJobAvailable", UNSET)

        _last_status = d.pop("lastStatus", UNSET)
        last_status: Union[Unset, Vb365JobLastStatus]
        if isinstance(_last_status, Unset):
            last_status = UNSET
        else:
            last_status = Vb365JobLastStatus(_last_status)

        last_status_details = d.pop("lastStatusDetails", UNSET)

        last_error_log_records = []
        _last_error_log_records = d.pop("lastErrorLogRecords", UNSET)
        for last_error_log_records_item_data in _last_error_log_records or []:
            last_error_log_records_item = Vb365JobSessionLog.from_dict(last_error_log_records_item_data)

            last_error_log_records.append(last_error_log_records_item)

        vb_365_job = cls(
            instance_uid=instance_uid,
            name=name,
            job_type=job_type,
            repository_uid=repository_uid,
            repository_name=repository_name,
            vb_365_organization_uid=vb_365_organization_uid,
            vspc_organization_uid=vspc_organization_uid,
            vspc_organization_name=vspc_organization_name,
            schedule_editing_available=schedule_editing_available,
            vb_365_server_uid=vb_365_server_uid,
            vb_365_server_name=vb_365_server_name,
            management_agent_uid=management_agent_uid,
            last_run=last_run,
            next_run=next_run,
            is_enabled=is_enabled,
            is_copy_job_available=is_copy_job_available,
            last_status=last_status,
            last_status_details=last_status_details,
            last_error_log_records=last_error_log_records,
        )

        vb_365_job.additional_properties = d
        return vb_365_job

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
