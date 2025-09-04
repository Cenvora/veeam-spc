from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerBackupJobLogShippingServers")


@_attrs_define
class BackupServerBackupJobLogShippingServers:
    """Log shipping servers used to transport transaction logs.

    Attributes:
        auto_selection (bool): Indicates whether Veeam Backup & Replication selects an optimal log shipping server
            automatically. Default: False.
        shipping_server_ids (Union[Unset, list[UUID]]): Array of UID assigned to servers used to transport transaction
            logs.
    """

    auto_selection: bool = False
    shipping_server_ids: Union[Unset, list[UUID]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_selection = self.auto_selection

        shipping_server_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.shipping_server_ids, Unset):
            shipping_server_ids = []
            for shipping_server_ids_item_data in self.shipping_server_ids:
                shipping_server_ids_item = str(shipping_server_ids_item_data)
                shipping_server_ids.append(shipping_server_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "autoSelection": auto_selection,
            }
        )
        if shipping_server_ids is not UNSET:
            field_dict["shippingServerIds"] = shipping_server_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_selection = d.pop("autoSelection")

        shipping_server_ids = []
        _shipping_server_ids = d.pop("shippingServerIds", UNSET)
        for shipping_server_ids_item_data in _shipping_server_ids or []:
            shipping_server_ids_item = UUID(shipping_server_ids_item_data)

            shipping_server_ids.append(shipping_server_ids_item)

        backup_server_backup_job_log_shipping_servers = cls(
            auto_selection=auto_selection,
            shipping_server_ids=shipping_server_ids,
        )

        backup_server_backup_job_log_shipping_servers.additional_properties = d
        return backup_server_backup_job_log_shipping_servers

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
