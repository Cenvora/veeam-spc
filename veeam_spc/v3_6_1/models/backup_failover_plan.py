from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_failover_plan_status import BackupFailoverPlanStatus
from ..models.backup_failover_plan_type import BackupFailoverPlanType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_failover_plan_last_session_type_0 import BackupFailoverPlanLastSessionType0


T = TypeVar("T", bound="BackupFailoverPlan")


@_attrs_define
class BackupFailoverPlan:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a failover plan.
        original_uid (Union[Unset, UUID]): UID assigned to a failover plan in Veeam Backup & Replication.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup & Replication server on which a failover
            plan is configured.
        name (Union[Unset, str]): Name of a failover plan.
        type_ (Union[Unset, BackupFailoverPlanType]): Type of a failover plan.
        status (Union[Unset, BackupFailoverPlanStatus]): Status of a failover plan.
        tenant_uid (Union[None, UUID, Unset]): UID assigned to a tenant for which a failover plan is configured.
        objects_count (Union[Unset, int]): Number of objects in a job.
        pre_failover_script_enabled (Union[None, Unset, bool]): Indicates whether a custom script must be executed
            before a failover plan.
        pre_failover_command (Union[None, Unset, str]): Path to a script file that is executed before a failover.
            > Property modification is performed asynchronously and cannot be tracked.
        post_failover_command (Union[None, Unset, str]): Path to a script file that is executed after a failover.
            > Property modification is performed asynchronously and cannot be tracked.
        post_failover_script_enabled (Union[None, Unset, bool]): Indicates whether a custom script must be executed
            after a failover plan.
        last_session (Union['BackupFailoverPlanLastSessionType0', None, Unset]): Information on the latest failover plan
            session.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    original_uid: Union[Unset, UUID] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    type_: Union[Unset, BackupFailoverPlanType] = UNSET
    status: Union[Unset, BackupFailoverPlanStatus] = UNSET
    tenant_uid: Union[None, UUID, Unset] = UNSET
    objects_count: Union[Unset, int] = UNSET
    pre_failover_script_enabled: Union[None, Unset, bool] = UNSET
    pre_failover_command: Union[None, Unset, str] = UNSET
    post_failover_command: Union[None, Unset, str] = UNSET
    post_failover_script_enabled: Union[None, Unset, bool] = UNSET
    last_session: Union["BackupFailoverPlanLastSessionType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.backup_failover_plan_last_session_type_0 import BackupFailoverPlanLastSessionType0

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        original_uid: Union[Unset, str] = UNSET
        if not isinstance(self.original_uid, Unset):
            original_uid = str(self.original_uid)

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        name = self.name

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        tenant_uid: Union[None, Unset, str]
        if isinstance(self.tenant_uid, Unset):
            tenant_uid = UNSET
        elif isinstance(self.tenant_uid, UUID):
            tenant_uid = str(self.tenant_uid)
        else:
            tenant_uid = self.tenant_uid

        objects_count = self.objects_count

        pre_failover_script_enabled: Union[None, Unset, bool]
        if isinstance(self.pre_failover_script_enabled, Unset):
            pre_failover_script_enabled = UNSET
        else:
            pre_failover_script_enabled = self.pre_failover_script_enabled

        pre_failover_command: Union[None, Unset, str]
        if isinstance(self.pre_failover_command, Unset):
            pre_failover_command = UNSET
        else:
            pre_failover_command = self.pre_failover_command

        post_failover_command: Union[None, Unset, str]
        if isinstance(self.post_failover_command, Unset):
            post_failover_command = UNSET
        else:
            post_failover_command = self.post_failover_command

        post_failover_script_enabled: Union[None, Unset, bool]
        if isinstance(self.post_failover_script_enabled, Unset):
            post_failover_script_enabled = UNSET
        else:
            post_failover_script_enabled = self.post_failover_script_enabled

        last_session: Union[None, Unset, dict[str, Any]]
        if isinstance(self.last_session, Unset):
            last_session = UNSET
        elif isinstance(self.last_session, BackupFailoverPlanLastSessionType0):
            last_session = self.last_session.to_dict()
        else:
            last_session = self.last_session

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if original_uid is not UNSET:
            field_dict["originalUid"] = original_uid
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if tenant_uid is not UNSET:
            field_dict["tenantUid"] = tenant_uid
        if objects_count is not UNSET:
            field_dict["objectsCount"] = objects_count
        if pre_failover_script_enabled is not UNSET:
            field_dict["preFailoverScriptEnabled"] = pre_failover_script_enabled
        if pre_failover_command is not UNSET:
            field_dict["preFailoverCommand"] = pre_failover_command
        if post_failover_command is not UNSET:
            field_dict["postFailoverCommand"] = post_failover_command
        if post_failover_script_enabled is not UNSET:
            field_dict["postFailoverScriptEnabled"] = post_failover_script_enabled
        if last_session is not UNSET:
            field_dict["lastSession"] = last_session

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_failover_plan_last_session_type_0 import BackupFailoverPlanLastSessionType0

        d = dict(src_dict)
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

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: Union[Unset, UUID]
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, BackupFailoverPlanType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BackupFailoverPlanType(_type_)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BackupFailoverPlanStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BackupFailoverPlanStatus(_status)

        def _parse_tenant_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tenant_uid_type_0 = UUID(data)

                return tenant_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        tenant_uid = _parse_tenant_uid(d.pop("tenantUid", UNSET))

        objects_count = d.pop("objectsCount", UNSET)

        def _parse_pre_failover_script_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        pre_failover_script_enabled = _parse_pre_failover_script_enabled(d.pop("preFailoverScriptEnabled", UNSET))

        def _parse_pre_failover_command(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pre_failover_command = _parse_pre_failover_command(d.pop("preFailoverCommand", UNSET))

        def _parse_post_failover_command(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        post_failover_command = _parse_post_failover_command(d.pop("postFailoverCommand", UNSET))

        def _parse_post_failover_script_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        post_failover_script_enabled = _parse_post_failover_script_enabled(d.pop("postFailoverScriptEnabled", UNSET))

        def _parse_last_session(data: object) -> Union["BackupFailoverPlanLastSessionType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_backup_failover_plan_last_session_type_0 = (
                    BackupFailoverPlanLastSessionType0.from_dict(data)
                )

                return componentsschemas_backup_failover_plan_last_session_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BackupFailoverPlanLastSessionType0", None, Unset], data)

        last_session = _parse_last_session(d.pop("lastSession", UNSET))

        backup_failover_plan = cls(
            instance_uid=instance_uid,
            original_uid=original_uid,
            backup_server_uid=backup_server_uid,
            name=name,
            type_=type_,
            status=status,
            tenant_uid=tenant_uid,
            objects_count=objects_count,
            pre_failover_script_enabled=pre_failover_script_enabled,
            pre_failover_command=pre_failover_command,
            post_failover_command=post_failover_command,
            post_failover_script_enabled=post_failover_script_enabled,
            last_session=last_session,
        )

        backup_failover_plan.additional_properties = d
        return backup_failover_plan

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
