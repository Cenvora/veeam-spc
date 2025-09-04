from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerBackupJobLogShippingServersType0")


@_attrs_define
class BackupServerBackupJobLogShippingServersType0:
    """Log shipping servers used to transport transaction logs.

    Attributes:
        auto_selection (bool): Indicates whether Veeam Backup & Replication selects an optimal log shipping server
            automatically. Default: False.
        shipping_server_ids (Union[None, Unset, list[UUID]]): Array of UID assigned to servers used to transport
            transaction logs.
    """

    auto_selection: bool = False
    shipping_server_ids: Union[None, Unset, list[UUID]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_selection = self.auto_selection

        shipping_server_ids: Union[None, Unset, list[str]]
        if isinstance(self.shipping_server_ids, Unset):
            shipping_server_ids = UNSET
        elif isinstance(self.shipping_server_ids, list):
            shipping_server_ids = []
            for shipping_server_ids_type_0_item_data in self.shipping_server_ids:
                shipping_server_ids_type_0_item = str(shipping_server_ids_type_0_item_data)
                shipping_server_ids.append(shipping_server_ids_type_0_item)

        else:
            shipping_server_ids = self.shipping_server_ids

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

        def _parse_shipping_server_ids(data: object) -> Union[None, Unset, list[UUID]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                shipping_server_ids_type_0 = []
                _shipping_server_ids_type_0 = data
                for shipping_server_ids_type_0_item_data in _shipping_server_ids_type_0:
                    shipping_server_ids_type_0_item = UUID(shipping_server_ids_type_0_item_data)

                    shipping_server_ids_type_0.append(shipping_server_ids_type_0_item)

                return shipping_server_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[UUID]], data)

        shipping_server_ids = _parse_shipping_server_ids(d.pop("shippingServerIds", UNSET))

        backup_server_backup_job_log_shipping_servers_type_0 = cls(
            auto_selection=auto_selection,
            shipping_server_ids=shipping_server_ids,
        )

        backup_server_backup_job_log_shipping_servers_type_0.additional_properties = d
        return backup_server_backup_job_log_shipping_servers_type_0

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
