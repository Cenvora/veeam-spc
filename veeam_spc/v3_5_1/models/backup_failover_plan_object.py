from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_failover_plan_restore_session import BackupFailoverPlanRestoreSession


T = TypeVar("T", bound="BackupFailoverPlanObject")


@_attrs_define
class BackupFailoverPlanObject:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a VM included in a failover plan.
        plan_uid (Union[Unset, UUID]): UID assigned to a failover plan.
        name (Union[Unset, str]): Name of a VM included in a failover plan.
        host_name (Union[Unset, str]): Name of a host running the VM.
        folder_name (Union[Unset, str]): Name of a folder that contains replicas.
        path (Union[Unset, str]): Path to a folder that contains replicas.
        backup_server_uid (Union[Unset, UUID]): Veeam Backup & Replication server on which a failover plan is
            configured.
        restore_session (Union[Unset, BackupFailoverPlanRestoreSession]):
    """

    instance_uid: Union[Unset, UUID] = UNSET
    plan_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    host_name: Union[Unset, str] = UNSET
    folder_name: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    restore_session: Union[Unset, "BackupFailoverPlanRestoreSession"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        plan_uid: Union[Unset, str] = UNSET
        if not isinstance(self.plan_uid, Unset):
            plan_uid = str(self.plan_uid)

        name = self.name

        host_name = self.host_name

        folder_name = self.folder_name

        path = self.path

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        restore_session: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.restore_session, Unset):
            restore_session = self.restore_session.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if plan_uid is not UNSET:
            field_dict["planUid"] = plan_uid
        if name is not UNSET:
            field_dict["name"] = name
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if folder_name is not UNSET:
            field_dict["folderName"] = folder_name
        if path is not UNSET:
            field_dict["path"] = path
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if restore_session is not UNSET:
            field_dict["restoreSession"] = restore_session

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_failover_plan_restore_session import BackupFailoverPlanRestoreSession

        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _plan_uid = d.pop("planUid", UNSET)
        plan_uid: Union[Unset, UUID]
        if isinstance(_plan_uid, Unset):
            plan_uid = UNSET
        else:
            plan_uid = UUID(_plan_uid)

        name = d.pop("name", UNSET)

        host_name = d.pop("hostName", UNSET)

        folder_name = d.pop("folderName", UNSET)

        path = d.pop("path", UNSET)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: Union[Unset, UUID]
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        _restore_session = d.pop("restoreSession", UNSET)
        restore_session: Union[Unset, BackupFailoverPlanRestoreSession]
        if isinstance(_restore_session, Unset):
            restore_session = UNSET
        else:
            restore_session = BackupFailoverPlanRestoreSession.from_dict(_restore_session)

        backup_failover_plan_object = cls(
            instance_uid=instance_uid,
            plan_uid=plan_uid,
            name=name,
            host_name=host_name,
            folder_name=folder_name,
            path=path,
            backup_server_uid=backup_server_uid,
            restore_session=restore_session,
        )

        backup_failover_plan_object.additional_properties = d
        return backup_failover_plan_object

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
