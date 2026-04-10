from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server import BackupServer


T = TypeVar("T", bound="EnterpriseManagerBackupServer")


@_attrs_define
class EnterpriseManagerBackupServer:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup & Replication server.
        address (Union[Unset, str]): DNS name or IP address of a Veeam Backup & Replication server.
        port (Union[Unset, int]): Port used by Veeam Backup Service.
        backup_server (Union[Unset, BackupServer]):  Example: {'instanceUid': 'DF997BD3-4AE9-4841-8152-8FF5CC703EAB',
            'name': 'VBR', 'managementAgentUid': '8BDD0D87-D160-40B5-88D3-E77A6F912AF6', 'version': '9.5.4.1000',
            'installationUid': 'C42C94E9-DB8A-4CF4-AF57-911EFA7FEE87'}.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    address: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    backup_server: Union[Unset, "BackupServer"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        address = self.address

        port = self.port

        backup_server: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.backup_server, Unset):
            backup_server = self.backup_server.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if address is not UNSET:
            field_dict["address"] = address
        if port is not UNSET:
            field_dict["port"] = port
        if backup_server is not UNSET:
            field_dict["backupServer"] = backup_server

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server import BackupServer

        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        address = d.pop("address", UNSET)

        port = d.pop("port", UNSET)

        _backup_server = d.pop("backupServer", UNSET)
        backup_server: Union[Unset, BackupServer]
        if isinstance(_backup_server, Unset):
            backup_server = UNSET
        else:
            backup_server = BackupServer.from_dict(_backup_server)

        enterprise_manager_backup_server = cls(
            instance_uid=instance_uid,
            address=address,
            port=port,
            backup_server=backup_server,
        )

        enterprise_manager_backup_server.additional_properties = d
        return enterprise_manager_backup_server

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
