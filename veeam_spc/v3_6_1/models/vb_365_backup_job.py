import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.vb_365_backup_job_backup_type import Vb365BackupJobBackupType
from ..models.vb_365_backup_job_last_status import Vb365BackupJobLastStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vb_365_backup_job_schedule_policy import Vb365BackupJobSchedulePolicy
    from ..models.vb_365_job_item_composed import Vb365JobItemComposed
    from ..models.vb_365_job_session_log import Vb365JobSessionLog


T = TypeVar("T", bound="Vb365BackupJob")


@_attrs_define
class Vb365BackupJob:
    """
    Attributes:
        name (str): Name of a Veeam Backup for Microsoft 365 backup job.
        repository_uid (UUID): UID assigned to a backup repository.
            >When patching job target repository, you can use the `GetVb365BackupJobAvailableBackupRepositories` operation
            to retrieve a list of available repositories.
        instance_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup for Microsoft 365 backup job.
        description (Union[None, Unset, str]): Description of a Veeam Backup for Microsoft 365 backup job.
        repository_name (Union[Unset, str]): Name of a backup repository.
        vb_365_organization_uid (Union[Unset, UUID]): UID assigned to a Microsoft organization.
        vspc_organization_uid (Union[None, UUID, Unset]): UID assigned to a Veeam Service Provider Console organization.
        vspc_organization_name (Union[None, Unset, str]): Name of a Veeam Service Provider Console organization.
        vb_365_server_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup for Microsoft 365 server.
        vb_365_server_name (Union[Unset, str]): Name Of a Veeam Backup for Microsoft 365 server.
        last_run (Union[None, Unset, datetime.datetime]): Date and time of the latest job run.
        next_run (Union[None, Unset, datetime.datetime]): Date and time of the next scheduled job run.
        is_enabled (Union[Unset, bool]): Indicates whether a Veeam Backup for Microsoft backup job is enabled. Default:
            False.
        is_copy_job_available (Union[Unset, bool]): Indicates whether a backup copy job can be created for the Veeam
            Backup for Microsoft 365 backup job.
        backup_type (Union[Unset, Vb365BackupJobBackupType]): Type of a Veeam Backup for Microsoft 365 backup job.
        last_status (Union[Unset, Vb365BackupJobLastStatus]): Status of the latest job run.
        last_status_details (Union[Unset, str]): Details on the latest job run.
        last_error_log_records (Union[Unset, list['Vb365JobSessionLog']]): The list of last job session logs.
        selected_items (Union[Unset, list['Vb365JobItemComposed']]): Array of backup job items.
        excluded_items (Union[Unset, list['Vb365JobItemComposed']]): Array of items excluded from the backup job.
        schedule_policy (Union[Unset, Vb365BackupJobSchedulePolicy]):
    """

    name: str
    repository_uid: UUID
    instance_uid: Union[Unset, UUID] = UNSET
    description: Union[None, Unset, str] = UNSET
    repository_name: Union[Unset, str] = UNSET
    vb_365_organization_uid: Union[Unset, UUID] = UNSET
    vspc_organization_uid: Union[None, UUID, Unset] = UNSET
    vspc_organization_name: Union[None, Unset, str] = UNSET
    vb_365_server_uid: Union[Unset, UUID] = UNSET
    vb_365_server_name: Union[Unset, str] = UNSET
    last_run: Union[None, Unset, datetime.datetime] = UNSET
    next_run: Union[None, Unset, datetime.datetime] = UNSET
    is_enabled: Union[Unset, bool] = False
    is_copy_job_available: Union[Unset, bool] = UNSET
    backup_type: Union[Unset, Vb365BackupJobBackupType] = UNSET
    last_status: Union[Unset, Vb365BackupJobLastStatus] = UNSET
    last_status_details: Union[Unset, str] = UNSET
    last_error_log_records: Union[Unset, list["Vb365JobSessionLog"]] = UNSET
    selected_items: Union[Unset, list["Vb365JobItemComposed"]] = UNSET
    excluded_items: Union[Unset, list["Vb365JobItemComposed"]] = UNSET
    schedule_policy: Union[Unset, "Vb365BackupJobSchedulePolicy"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        repository_uid = str(self.repository_uid)

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

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

        vb_365_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.vb_365_server_uid, Unset):
            vb_365_server_uid = str(self.vb_365_server_uid)

        vb_365_server_name = self.vb_365_server_name

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

        backup_type: Union[Unset, str] = UNSET
        if not isinstance(self.backup_type, Unset):
            backup_type = self.backup_type.value

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

        selected_items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.selected_items, Unset):
            selected_items = []
            for selected_items_item_data in self.selected_items:
                selected_items_item = selected_items_item_data.to_dict()
                selected_items.append(selected_items_item)

        excluded_items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.excluded_items, Unset):
            excluded_items = []
            for excluded_items_item_data in self.excluded_items:
                excluded_items_item = excluded_items_item_data.to_dict()
                excluded_items.append(excluded_items_item)

        schedule_policy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schedule_policy, Unset):
            schedule_policy = self.schedule_policy.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "repositoryUid": repository_uid,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if description is not UNSET:
            field_dict["description"] = description
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
        if is_copy_job_available is not UNSET:
            field_dict["isCopyJobAvailable"] = is_copy_job_available
        if backup_type is not UNSET:
            field_dict["backupType"] = backup_type
        if last_status is not UNSET:
            field_dict["lastStatus"] = last_status
        if last_status_details is not UNSET:
            field_dict["lastStatusDetails"] = last_status_details
        if last_error_log_records is not UNSET:
            field_dict["lastErrorLogRecords"] = last_error_log_records
        if selected_items is not UNSET:
            field_dict["selectedItems"] = selected_items
        if excluded_items is not UNSET:
            field_dict["excludedItems"] = excluded_items
        if schedule_policy is not UNSET:
            field_dict["schedulePolicy"] = schedule_policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vb_365_backup_job_schedule_policy import Vb365BackupJobSchedulePolicy
        from ..models.vb_365_job_item_composed import Vb365JobItemComposed
        from ..models.vb_365_job_session_log import Vb365JobSessionLog

        d = dict(src_dict)
        name = d.pop("name")

        repository_uid = UUID(d.pop("repositoryUid"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

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

        _vb_365_server_uid = d.pop("vb365ServerUid", UNSET)
        vb_365_server_uid: Union[Unset, UUID]
        if isinstance(_vb_365_server_uid, Unset):
            vb_365_server_uid = UNSET
        else:
            vb_365_server_uid = UUID(_vb_365_server_uid)

        vb_365_server_name = d.pop("vb365ServerName", UNSET)

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

        _backup_type = d.pop("backupType", UNSET)
        backup_type: Union[Unset, Vb365BackupJobBackupType]
        if isinstance(_backup_type, Unset):
            backup_type = UNSET
        else:
            backup_type = Vb365BackupJobBackupType(_backup_type)

        _last_status = d.pop("lastStatus", UNSET)
        last_status: Union[Unset, Vb365BackupJobLastStatus]
        if isinstance(_last_status, Unset):
            last_status = UNSET
        else:
            last_status = Vb365BackupJobLastStatus(_last_status)

        last_status_details = d.pop("lastStatusDetails", UNSET)

        last_error_log_records = []
        _last_error_log_records = d.pop("lastErrorLogRecords", UNSET)
        for last_error_log_records_item_data in _last_error_log_records or []:
            last_error_log_records_item = Vb365JobSessionLog.from_dict(last_error_log_records_item_data)

            last_error_log_records.append(last_error_log_records_item)

        selected_items = []
        _selected_items = d.pop("selectedItems", UNSET)
        for selected_items_item_data in _selected_items or []:
            selected_items_item = Vb365JobItemComposed.from_dict(selected_items_item_data)

            selected_items.append(selected_items_item)

        excluded_items = []
        _excluded_items = d.pop("excludedItems", UNSET)
        for excluded_items_item_data in _excluded_items or []:
            excluded_items_item = Vb365JobItemComposed.from_dict(excluded_items_item_data)

            excluded_items.append(excluded_items_item)

        _schedule_policy = d.pop("schedulePolicy", UNSET)
        schedule_policy: Union[Unset, Vb365BackupJobSchedulePolicy]
        if isinstance(_schedule_policy, Unset):
            schedule_policy = UNSET
        else:
            schedule_policy = Vb365BackupJobSchedulePolicy.from_dict(_schedule_policy)

        vb_365_backup_job = cls(
            name=name,
            repository_uid=repository_uid,
            instance_uid=instance_uid,
            description=description,
            repository_name=repository_name,
            vb_365_organization_uid=vb_365_organization_uid,
            vspc_organization_uid=vspc_organization_uid,
            vspc_organization_name=vspc_organization_name,
            vb_365_server_uid=vb_365_server_uid,
            vb_365_server_name=vb_365_server_name,
            last_run=last_run,
            next_run=next_run,
            is_enabled=is_enabled,
            is_copy_job_available=is_copy_job_available,
            backup_type=backup_type,
            last_status=last_status,
            last_status_details=last_status_details,
            last_error_log_records=last_error_log_records,
            selected_items=selected_items,
            excluded_items=excluded_items,
            schedule_policy=schedule_policy,
        )

        vb_365_backup_job.additional_properties = d
        return vb_365_backup_job

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
