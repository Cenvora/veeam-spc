import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.backup_failover_plan_restore_session_backup_status import BackupFailoverPlanRestoreSessionBackupStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupFailoverPlanRestoreSession")


@_attrs_define
class BackupFailoverPlanRestoreSession:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a protected VM.
        backup_status (Union[Unset, BackupFailoverPlanRestoreSessionBackupStatus]): Status of a failover session.
        restore_point_uid (Union[None, UUID, Unset]): UID assigned to a replication restore point.
        restore_point_date_time (Union[None, Unset, datetime.datetime]): Date and time of the replication restore point
            creation.
        start_date_time (Union[Unset, datetime.datetime]): Failover session start date and time.
        end_date_time (Union[None, Unset, datetime.datetime]): Failover session end date and time.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    backup_status: Union[Unset, BackupFailoverPlanRestoreSessionBackupStatus] = UNSET
    restore_point_uid: Union[None, UUID, Unset] = UNSET
    restore_point_date_time: Union[None, Unset, datetime.datetime] = UNSET
    start_date_time: Union[Unset, datetime.datetime] = UNSET
    end_date_time: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        backup_status: Union[Unset, str] = UNSET
        if not isinstance(self.backup_status, Unset):
            backup_status = self.backup_status.value

        restore_point_uid: Union[None, Unset, str]
        if isinstance(self.restore_point_uid, Unset):
            restore_point_uid = UNSET
        elif isinstance(self.restore_point_uid, UUID):
            restore_point_uid = str(self.restore_point_uid)
        else:
            restore_point_uid = self.restore_point_uid

        restore_point_date_time: Union[None, Unset, str]
        if isinstance(self.restore_point_date_time, Unset):
            restore_point_date_time = UNSET
        elif isinstance(self.restore_point_date_time, datetime.datetime):
            restore_point_date_time = self.restore_point_date_time.isoformat()
        else:
            restore_point_date_time = self.restore_point_date_time

        start_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_date_time, Unset):
            start_date_time = self.start_date_time.isoformat()

        end_date_time: Union[None, Unset, str]
        if isinstance(self.end_date_time, Unset):
            end_date_time = UNSET
        elif isinstance(self.end_date_time, datetime.datetime):
            end_date_time = self.end_date_time.isoformat()
        else:
            end_date_time = self.end_date_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if backup_status is not UNSET:
            field_dict["backupStatus"] = backup_status
        if restore_point_uid is not UNSET:
            field_dict["restorePointUid"] = restore_point_uid
        if restore_point_date_time is not UNSET:
            field_dict["restorePointDateTime"] = restore_point_date_time
        if start_date_time is not UNSET:
            field_dict["startDateTime"] = start_date_time
        if end_date_time is not UNSET:
            field_dict["endDateTime"] = end_date_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _backup_status = d.pop("backupStatus", UNSET)
        backup_status: Union[Unset, BackupFailoverPlanRestoreSessionBackupStatus]
        if isinstance(_backup_status, Unset):
            backup_status = UNSET
        else:
            backup_status = BackupFailoverPlanRestoreSessionBackupStatus(_backup_status)

        def _parse_restore_point_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                restore_point_uid_type_0 = UUID(data)

                return restore_point_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        restore_point_uid = _parse_restore_point_uid(d.pop("restorePointUid", UNSET))

        def _parse_restore_point_date_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                restore_point_date_time_type_0 = isoparse(data)

                return restore_point_date_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        restore_point_date_time = _parse_restore_point_date_time(d.pop("restorePointDateTime", UNSET))

        _start_date_time = d.pop("startDateTime", UNSET)
        start_date_time: Union[Unset, datetime.datetime]
        if isinstance(_start_date_time, Unset):
            start_date_time = UNSET
        else:
            start_date_time = isoparse(_start_date_time)

        def _parse_end_date_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_time_type_0 = isoparse(data)

                return end_date_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        end_date_time = _parse_end_date_time(d.pop("endDateTime", UNSET))

        backup_failover_plan_restore_session = cls(
            instance_uid=instance_uid,
            backup_status=backup_status,
            restore_point_uid=restore_point_uid,
            restore_point_date_time=restore_point_date_time,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
        )

        backup_failover_plan_restore_session.additional_properties = d
        return backup_failover_plan_restore_session

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
