from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_wan_accelerator_status import BackupWanAcceleratorStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupWanAccelerator")


@_attrs_define
class BackupWanAccelerator:
    """
    Example:
        {'instanceUid': '7eced22b-5e67-45e1-bc00-37e399903bed', 'name': 'BACKUPWAN01', 'backupServerUid':
            'DF997BD3-4AE9-4841-8152-8FF5CC703EAB'}

    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a WAN accelerator.
        name (Union[Unset, str]): Name of a WAN accelerator.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup & Replication server.
        version (Union[Unset, str]): Version of a WAN accelerator service.
        host_uid (Union[Unset, UUID]): UID assigned to a computer that performs a role of a WAN accelerator.
        host_name (Union[Unset, str]): Name of a computer that performs a role of a WAN accelerator.
        is_out_of_date (Union[Unset, bool]): Indicates whether a WAN accelerator service is outdated.
        status (Union[Unset, BackupWanAcceleratorStatus]): WAN accelerator status.
        is_cloud (Union[Unset, bool]): Indicates whether a WAN accelerator is used in the Veeam Cloud Connect
            infrastructure.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    version: Union[Unset, str] = UNSET
    host_uid: Union[Unset, UUID] = UNSET
    host_name: Union[Unset, str] = UNSET
    is_out_of_date: Union[Unset, bool] = UNSET
    status: Union[Unset, BackupWanAcceleratorStatus] = UNSET
    is_cloud: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        version = self.version

        host_uid: Union[Unset, str] = UNSET
        if not isinstance(self.host_uid, Unset):
            host_uid = str(self.host_uid)

        host_name = self.host_name

        is_out_of_date = self.is_out_of_date

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        is_cloud = self.is_cloud

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if name is not UNSET:
            field_dict["name"] = name
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if version is not UNSET:
            field_dict["version"] = version
        if host_uid is not UNSET:
            field_dict["hostUid"] = host_uid
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if is_out_of_date is not UNSET:
            field_dict["isOutOfDate"] = is_out_of_date
        if status is not UNSET:
            field_dict["status"] = status
        if is_cloud is not UNSET:
            field_dict["isCloud"] = is_cloud

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

        name = d.pop("name", UNSET)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: Union[Unset, UUID]
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        version = d.pop("version", UNSET)

        _host_uid = d.pop("hostUid", UNSET)
        host_uid: Union[Unset, UUID]
        if isinstance(_host_uid, Unset):
            host_uid = UNSET
        else:
            host_uid = UUID(_host_uid)

        host_name = d.pop("hostName", UNSET)

        is_out_of_date = d.pop("isOutOfDate", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BackupWanAcceleratorStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BackupWanAcceleratorStatus(_status)

        is_cloud = d.pop("isCloud", UNSET)

        backup_wan_accelerator = cls(
            instance_uid=instance_uid,
            name=name,
            backup_server_uid=backup_server_uid,
            version=version,
            host_uid=host_uid,
            host_name=host_name,
            is_out_of_date=is_out_of_date,
            status=status,
            is_cloud=is_cloud,
        )

        backup_wan_accelerator.additional_properties = d
        return backup_wan_accelerator

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
