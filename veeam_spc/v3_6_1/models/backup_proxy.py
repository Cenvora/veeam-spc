from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_proxy_status import BackupProxyStatus
from ..models.backup_proxy_type import BackupProxyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupProxy")


@_attrs_define
class BackupProxy:
    """
    Example:
        {'instanceUid': '6062568E-F90F-4702-8151-CBE3CE2A8C10', 'name': 'BACKUPPRX01', 'version': '9.5.4.2000',
            'backupServerUid': 'DF997BD3-4AE9-4841-8152-8FF5CC703EAB', 'isOutOfDate': False, 'isDisabled': False, 'status':
            'Healthy', 'type': 'vSphere'}

    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a backup proxy.
        name (Union[Unset, str]): Name of a backup proxy.
        version (Union[Unset, str]): Version of a backup proxy service.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup & Replication server.
        is_out_of_date (Union[Unset, bool]): Indicates whether a backup proxy service is outdated.
        is_disabled (Union[Unset, bool]): Indicates whether a backup proxy is disabled.
        host_uid (Union[Unset, UUID]): UID assigned to a server that performs a role of a backup proxy.
        host_name (Union[Unset, str]): Computer name of a server that performs a role of a backup proxy.
        status (Union[Unset, BackupProxyStatus]): Backup proxy status.
        type_ (Union[Unset, BackupProxyType]): Type of a backup proxy.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    is_out_of_date: Union[Unset, bool] = UNSET
    is_disabled: Union[Unset, bool] = UNSET
    host_uid: Union[Unset, UUID] = UNSET
    host_name: Union[Unset, str] = UNSET
    status: Union[Unset, BackupProxyStatus] = UNSET
    type_: Union[Unset, BackupProxyType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        version = self.version

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        is_out_of_date = self.is_out_of_date

        is_disabled = self.is_disabled

        host_uid: Union[Unset, str] = UNSET
        if not isinstance(self.host_uid, Unset):
            host_uid = str(self.host_uid)

        host_name = self.host_name

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if is_out_of_date is not UNSET:
            field_dict["isOutOfDate"] = is_out_of_date
        if is_disabled is not UNSET:
            field_dict["isDisabled"] = is_disabled
        if host_uid is not UNSET:
            field_dict["hostUid"] = host_uid
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_

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

        version = d.pop("version", UNSET)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: Union[Unset, UUID]
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        is_out_of_date = d.pop("isOutOfDate", UNSET)

        is_disabled = d.pop("isDisabled", UNSET)

        _host_uid = d.pop("hostUid", UNSET)
        host_uid: Union[Unset, UUID]
        if isinstance(_host_uid, Unset):
            host_uid = UNSET
        else:
            host_uid = UUID(_host_uid)

        host_name = d.pop("hostName", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BackupProxyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BackupProxyStatus(_status)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, BackupProxyType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BackupProxyType(_type_)

        backup_proxy = cls(
            instance_uid=instance_uid,
            name=name,
            version=version,
            backup_server_uid=backup_server_uid,
            is_out_of_date=is_out_of_date,
            is_disabled=is_disabled,
            host_uid=host_uid,
            host_name=host_name,
            status=status,
            type_=type_,
        )

        backup_proxy.additional_properties = d
        return backup_proxy

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
