from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vb_365_backup_proxy_proxy_type import Vb365BackupProxyProxyType
from ..models.vb_365_backup_proxy_status import Vb365BackupProxyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365BackupProxy")


@_attrs_define
class Vb365BackupProxy:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a backup proxy.
        proxy_type (Union[Unset, Vb365BackupProxyProxyType]): Type of a backup proxy.
        status (Union[Unset, Vb365BackupProxyStatus]): Status of a backup proxy.
        host_name (Union[Unset, str]): Host name of a backup proxy.
        description (Union[Unset, str]): Description of a backup proxy.
        port (Union[Unset, int]): Port that is used to connect to a backup proxy.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    proxy_type: Union[Unset, Vb365BackupProxyProxyType] = UNSET
    status: Union[Unset, Vb365BackupProxyStatus] = UNSET
    host_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        proxy_type: Union[Unset, str] = UNSET
        if not isinstance(self.proxy_type, Unset):
            proxy_type = self.proxy_type.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        host_name = self.host_name

        description = self.description

        port = self.port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if proxy_type is not UNSET:
            field_dict["proxyType"] = proxy_type
        if status is not UNSET:
            field_dict["status"] = status
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if description is not UNSET:
            field_dict["description"] = description
        if port is not UNSET:
            field_dict["port"] = port

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

        _proxy_type = d.pop("proxyType", UNSET)
        proxy_type: Union[Unset, Vb365BackupProxyProxyType]
        if isinstance(_proxy_type, Unset):
            proxy_type = UNSET
        else:
            proxy_type = Vb365BackupProxyProxyType(_proxy_type)

        _status = d.pop("status", UNSET)
        status: Union[Unset, Vb365BackupProxyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = Vb365BackupProxyStatus(_status)

        host_name = d.pop("hostName", UNSET)

        description = d.pop("description", UNSET)

        port = d.pop("port", UNSET)

        vb_365_backup_proxy = cls(
            instance_uid=instance_uid,
            proxy_type=proxy_type,
            status=status,
            host_name=host_name,
            description=description,
            port=port,
        )

        vb_365_backup_proxy.additional_properties = d
        return vb_365_backup_proxy

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
