import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.protected_computer_managed_by_console_operation_mode import ProtectedComputerManagedByConsoleOperationMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedComputerManagedByConsole")


@_attrs_define
class ProtectedComputerManagedByConsole:
    """
    Attributes:
        backup_agent_uid (Union[Unset, UUID]): UID assigned to a backup agent installed on a computer.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization.
        name (Union[Unset, str]): Hostname of a protected computer.
        number_of_jobs (Union[Unset, int]): Number of jobs.
        operation_mode (Union[Unset, ProtectedComputerManagedByConsoleOperationMode]): Operation mode.
        latest_restore_point_date (Union[Unset, datetime.datetime]): Date and time of the latest restore point creation.
    """

    backup_agent_uid: Union[Unset, UUID] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    number_of_jobs: Union[Unset, int] = UNSET
    operation_mode: Union[Unset, ProtectedComputerManagedByConsoleOperationMode] = UNSET
    latest_restore_point_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_agent_uid, Unset):
            backup_agent_uid = str(self.backup_agent_uid)

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        name = self.name

        number_of_jobs = self.number_of_jobs

        operation_mode: Union[Unset, str] = UNSET
        if not isinstance(self.operation_mode, Unset):
            operation_mode = self.operation_mode.value

        latest_restore_point_date: Union[Unset, str] = UNSET
        if not isinstance(self.latest_restore_point_date, Unset):
            latest_restore_point_date = self.latest_restore_point_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_agent_uid is not UNSET:
            field_dict["backupAgentUid"] = backup_agent_uid
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if name is not UNSET:
            field_dict["name"] = name
        if number_of_jobs is not UNSET:
            field_dict["numberOfJobs"] = number_of_jobs
        if operation_mode is not UNSET:
            field_dict["operationMode"] = operation_mode
        if latest_restore_point_date is not UNSET:
            field_dict["latestRestorePointDate"] = latest_restore_point_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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

        number_of_jobs = d.pop("numberOfJobs", UNSET)

        _operation_mode = d.pop("operationMode", UNSET)
        operation_mode: Union[Unset, ProtectedComputerManagedByConsoleOperationMode]
        if isinstance(_operation_mode, Unset):
            operation_mode = UNSET
        else:
            operation_mode = ProtectedComputerManagedByConsoleOperationMode(_operation_mode)

        _latest_restore_point_date = d.pop("latestRestorePointDate", UNSET)
        latest_restore_point_date: Union[Unset, datetime.datetime]
        if isinstance(_latest_restore_point_date, Unset):
            latest_restore_point_date = UNSET
        else:
            latest_restore_point_date = isoparse(_latest_restore_point_date)

        protected_computer_managed_by_console = cls(
            backup_agent_uid=backup_agent_uid,
            organization_uid=organization_uid,
            name=name,
            number_of_jobs=number_of_jobs,
            operation_mode=operation_mode,
            latest_restore_point_date=latest_restore_point_date,
        )

        protected_computer_managed_by_console.additional_properties = d
        return protected_computer_managed_by_console

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
