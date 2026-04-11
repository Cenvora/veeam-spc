from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_repository_connection_type import BackupServerRepositoryConnectionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerObjectStorageConnection")


@_attrs_define
class BackupServerObjectStorageConnection:
    """
    Attributes:
        connection_type (BackupServerRepositoryConnectionType):
        gateway_server_ids (list[UUID] | None | Unset): Array of gateway server IDs. The property has the `null` value,
            if the `connectionType` property has the `Direct` value.
    """

    connection_type: BackupServerRepositoryConnectionType
    gateway_server_ids: list[UUID] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_type = self.connection_type.value

        gateway_server_ids: list[str] | None | Unset
        if isinstance(self.gateway_server_ids, Unset):
            gateway_server_ids = UNSET
        elif isinstance(self.gateway_server_ids, list):
            gateway_server_ids = []
            for gateway_server_ids_type_0_item_data in self.gateway_server_ids:
                gateway_server_ids_type_0_item = str(gateway_server_ids_type_0_item_data)
                gateway_server_ids.append(gateway_server_ids_type_0_item)

        else:
            gateway_server_ids = self.gateway_server_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionType": connection_type,
            }
        )
        if gateway_server_ids is not UNSET:
            field_dict["gatewayServerIds"] = gateway_server_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection_type = BackupServerRepositoryConnectionType(d.pop("connectionType"))

        def _parse_gateway_server_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                gateway_server_ids_type_0 = []
                _gateway_server_ids_type_0 = data
                for gateway_server_ids_type_0_item_data in _gateway_server_ids_type_0:
                    gateway_server_ids_type_0_item = UUID(gateway_server_ids_type_0_item_data)

                    gateway_server_ids_type_0.append(gateway_server_ids_type_0_item)

                return gateway_server_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        gateway_server_ids = _parse_gateway_server_ids(d.pop("gatewayServerIds", UNSET))

        backup_server_object_storage_connection = cls(
            connection_type=connection_type,
            gateway_server_ids=gateway_server_ids,
        )

        backup_server_object_storage_connection.additional_properties = d
        return backup_server_object_storage_connection

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
