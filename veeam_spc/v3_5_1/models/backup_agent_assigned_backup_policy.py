import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.backup_agent_assigned_backup_policy_status import BackupAgentAssignedBackupPolicyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupAgentAssignedBackupPolicy")


@_attrs_define
class BackupAgentAssignedBackupPolicy:
    """
    Attributes:
        config_uid (Union[Unset, UUID]): UID assigned to a backup policy configuration.
        backup_agent_uid (Union[Unset, UUID]): UID assigned to a Veeam backup agent.
        backup_policy_uid (Union[Unset, UUID]): UID assigned to a backup policy.
        status (Union[Unset, BackupAgentAssignedBackupPolicyStatus]): Status of the policy assignment.
        is_custom (Union[Unset, bool]): Indicates whether a backup policy is custom.
        is_out_of_date (Union[Unset, bool]): Indicates whether a newer revision of a backup policy exists that has not
            been assigned to an agent.
        backup_policy_failure_message (Union[Unset, str]): Message that is displayed in case backup policy assignment
            fails.
        backup_policy_revision (Union[Unset, int]): Revision of a backup policy.
        assigned_date (Union[Unset, datetime.datetime]): Date of the policy assignment.
            > If the backup policy is assigned to a Linux or Mac computer, the value of this property is `null`.
        assigned_by (Union[Unset, str]): Organization or user who assigned a backup policy.
            > If the backup policy is assigned to a Linux or Mac computer, the value of this property is `null`.
    """

    config_uid: Union[Unset, UUID] = UNSET
    backup_agent_uid: Union[Unset, UUID] = UNSET
    backup_policy_uid: Union[Unset, UUID] = UNSET
    status: Union[Unset, BackupAgentAssignedBackupPolicyStatus] = UNSET
    is_custom: Union[Unset, bool] = UNSET
    is_out_of_date: Union[Unset, bool] = UNSET
    backup_policy_failure_message: Union[Unset, str] = UNSET
    backup_policy_revision: Union[Unset, int] = UNSET
    assigned_date: Union[Unset, datetime.datetime] = UNSET
    assigned_by: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config_uid: Union[Unset, str] = UNSET
        if not isinstance(self.config_uid, Unset):
            config_uid = str(self.config_uid)

        backup_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_agent_uid, Unset):
            backup_agent_uid = str(self.backup_agent_uid)

        backup_policy_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_policy_uid, Unset):
            backup_policy_uid = str(self.backup_policy_uid)

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        is_custom = self.is_custom

        is_out_of_date = self.is_out_of_date

        backup_policy_failure_message = self.backup_policy_failure_message

        backup_policy_revision = self.backup_policy_revision

        assigned_date: Union[Unset, str] = UNSET
        if not isinstance(self.assigned_date, Unset):
            assigned_date = self.assigned_date.isoformat()

        assigned_by = self.assigned_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config_uid is not UNSET:
            field_dict["configUid"] = config_uid
        if backup_agent_uid is not UNSET:
            field_dict["backupAgentUid"] = backup_agent_uid
        if backup_policy_uid is not UNSET:
            field_dict["backupPolicyUid"] = backup_policy_uid
        if status is not UNSET:
            field_dict["status"] = status
        if is_custom is not UNSET:
            field_dict["isCustom"] = is_custom
        if is_out_of_date is not UNSET:
            field_dict["isOutOfDate"] = is_out_of_date
        if backup_policy_failure_message is not UNSET:
            field_dict["backupPolicyFailureMessage"] = backup_policy_failure_message
        if backup_policy_revision is not UNSET:
            field_dict["backupPolicyRevision"] = backup_policy_revision
        if assigned_date is not UNSET:
            field_dict["assignedDate"] = assigned_date
        if assigned_by is not UNSET:
            field_dict["assignedBy"] = assigned_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _config_uid = d.pop("configUid", UNSET)
        config_uid: Union[Unset, UUID]
        if isinstance(_config_uid, Unset):
            config_uid = UNSET
        else:
            config_uid = UUID(_config_uid)

        _backup_agent_uid = d.pop("backupAgentUid", UNSET)
        backup_agent_uid: Union[Unset, UUID]
        if isinstance(_backup_agent_uid, Unset):
            backup_agent_uid = UNSET
        else:
            backup_agent_uid = UUID(_backup_agent_uid)

        _backup_policy_uid = d.pop("backupPolicyUid", UNSET)
        backup_policy_uid: Union[Unset, UUID]
        if isinstance(_backup_policy_uid, Unset):
            backup_policy_uid = UNSET
        else:
            backup_policy_uid = UUID(_backup_policy_uid)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BackupAgentAssignedBackupPolicyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BackupAgentAssignedBackupPolicyStatus(_status)

        is_custom = d.pop("isCustom", UNSET)

        is_out_of_date = d.pop("isOutOfDate", UNSET)

        backup_policy_failure_message = d.pop("backupPolicyFailureMessage", UNSET)

        backup_policy_revision = d.pop("backupPolicyRevision", UNSET)

        _assigned_date = d.pop("assignedDate", UNSET)
        assigned_date: Union[Unset, datetime.datetime]
        if isinstance(_assigned_date, Unset):
            assigned_date = UNSET
        else:
            assigned_date = isoparse(_assigned_date)

        assigned_by = d.pop("assignedBy", UNSET)

        backup_agent_assigned_backup_policy = cls(
            config_uid=config_uid,
            backup_agent_uid=backup_agent_uid,
            backup_policy_uid=backup_policy_uid,
            status=status,
            is_custom=is_custom,
            is_out_of_date=is_out_of_date,
            backup_policy_failure_message=backup_policy_failure_message,
            backup_policy_revision=backup_policy_revision,
            assigned_date=assigned_date,
            assigned_by=assigned_by,
        )

        backup_agent_assigned_backup_policy.additional_properties = d
        return backup_agent_assigned_backup_policy

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
