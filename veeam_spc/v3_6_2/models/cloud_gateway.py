from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cloud_gateway_status import CloudGatewayStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudGateway")


@_attrs_define
class CloudGateway:
    """
    Example:
        {'instanceUid': '81536849-36C5-4044-9DC5-D1393062ADA8', 'name': 'BACKUPCGW01', 'backupServerUid':
            'DF997BD3-4AE9-4841-8152-8FF5CC703EAB', 'port': 10001, 'isOutOfDate': False, 'isDisabled': False, 'status':
            'Healthy', 'externalPort': 666, 'externalIp': '10.17.26.1'}

    Attributes:
        instance_uid (UUID | Unset): UID assigned to a cloud gateway.
        name (str | Unset): Name of a cloud gateway.
        backup_server_uid (UUID | Unset): UID assigned to a Veeam Backup & Replication server.
        gateway_pool_uid (None | Unset | UUID): UID assigned to a cloud gateway pool that includes the cloud gateway.
        port (int | Unset): Internal port that is listening to external connections.
        external_port (int | Unset): Port for external connections.
        external_address (str | Unset): IP address or DNS name of a network interface card on a cloud gateway used to
            communicate with tenant Veeam Backup & Replication servers.
            > For cloud gateways with version 12, only the DNS name is returned.
        external_ip_list (list[str] | None | Unset): List of available network interface cards.
        is_out_of_date (bool | Unset): Indicates whether a cloud gateway service is outdated.
        host_uid (UUID | Unset): UID assigned to a server that performs a role of a cloud gateway.
        is_disabled (bool | Unset): Indicates whether a cloud gateway is disabled.
        status (CloudGatewayStatus | Unset): Status of a cloud gateway.
    """

    instance_uid: UUID | Unset = UNSET
    name: str | Unset = UNSET
    backup_server_uid: UUID | Unset = UNSET
    gateway_pool_uid: None | Unset | UUID = UNSET
    port: int | Unset = UNSET
    external_port: int | Unset = UNSET
    external_address: str | Unset = UNSET
    external_ip_list: list[str] | None | Unset = UNSET
    is_out_of_date: bool | Unset = UNSET
    host_uid: UUID | Unset = UNSET
    is_disabled: bool | Unset = UNSET
    status: CloudGatewayStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        backup_server_uid: str | Unset = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        gateway_pool_uid: None | str | Unset
        if isinstance(self.gateway_pool_uid, Unset):
            gateway_pool_uid = UNSET
        elif isinstance(self.gateway_pool_uid, UUID):
            gateway_pool_uid = str(self.gateway_pool_uid)
        else:
            gateway_pool_uid = self.gateway_pool_uid

        port = self.port

        external_port = self.external_port

        external_address = self.external_address

        external_ip_list: list[str] | None | Unset
        if isinstance(self.external_ip_list, Unset):
            external_ip_list = UNSET
        elif isinstance(self.external_ip_list, list):
            external_ip_list = self.external_ip_list

        else:
            external_ip_list = self.external_ip_list

        is_out_of_date = self.is_out_of_date

        host_uid: str | Unset = UNSET
        if not isinstance(self.host_uid, Unset):
            host_uid = str(self.host_uid)

        is_disabled = self.is_disabled

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if name is not UNSET:
            field_dict["name"] = name
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if gateway_pool_uid is not UNSET:
            field_dict["gatewayPoolUid"] = gateway_pool_uid
        if port is not UNSET:
            field_dict["port"] = port
        if external_port is not UNSET:
            field_dict["externalPort"] = external_port
        if external_address is not UNSET:
            field_dict["externalAddress"] = external_address
        if external_ip_list is not UNSET:
            field_dict["externalIpList"] = external_ip_list
        if is_out_of_date is not UNSET:
            field_dict["isOutOfDate"] = is_out_of_date
        if host_uid is not UNSET:
            field_dict["hostUid"] = host_uid
        if is_disabled is not UNSET:
            field_dict["isDisabled"] = is_disabled
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        name = d.pop("name", UNSET)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: UUID | Unset
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        def _parse_gateway_pool_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gateway_pool_uid_type_0 = UUID(data)

                return gateway_pool_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        gateway_pool_uid = _parse_gateway_pool_uid(d.pop("gatewayPoolUid", UNSET))

        port = d.pop("port", UNSET)

        external_port = d.pop("externalPort", UNSET)

        external_address = d.pop("externalAddress", UNSET)

        def _parse_external_ip_list(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                external_ip_list_type_0 = cast(list[str], data)

                return external_ip_list_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        external_ip_list = _parse_external_ip_list(d.pop("externalIpList", UNSET))

        is_out_of_date = d.pop("isOutOfDate", UNSET)

        _host_uid = d.pop("hostUid", UNSET)
        host_uid: UUID | Unset
        if isinstance(_host_uid, Unset):
            host_uid = UNSET
        else:
            host_uid = UUID(_host_uid)

        is_disabled = d.pop("isDisabled", UNSET)

        _status = d.pop("status", UNSET)
        status: CloudGatewayStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CloudGatewayStatus(_status)

        cloud_gateway = cls(
            instance_uid=instance_uid,
            name=name,
            backup_server_uid=backup_server_uid,
            gateway_pool_uid=gateway_pool_uid,
            port=port,
            external_port=external_port,
            external_address=external_address,
            external_ip_list=external_ip_list,
            is_out_of_date=is_out_of_date,
            host_uid=host_uid,
            is_disabled=is_disabled,
            status=status,
        )

        cloud_gateway.additional_properties = d
        return cloud_gateway

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
