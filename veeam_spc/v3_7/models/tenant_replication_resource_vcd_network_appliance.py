from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.network_appliance_tcp_ip_settings import NetworkApplianceTcpIpSettings


T = TypeVar("T", bound="TenantReplicationResourceVcdNetworkAppliance")


@_attrs_define
class TenantReplicationResourceVcdNetworkAppliance:
    """
    Attributes:
        name (str): Name of a network extension appliance.
        instance_uid (UUID | Unset): UID assigned to a network extension appliance.
        data_center_uid (UUID | Unset): UID assigned to an organization VDC.
        data_center_name (None | str | Unset): Name of an organization VDC.
        tcp_ip_settings (NetworkApplianceTcpIpSettings | Unset):
    """

    name: str
    instance_uid: UUID | Unset = UNSET
    data_center_uid: UUID | Unset = UNSET
    data_center_name: None | str | Unset = UNSET
    tcp_ip_settings: NetworkApplianceTcpIpSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        data_center_uid: str | Unset = UNSET
        if not isinstance(self.data_center_uid, Unset):
            data_center_uid = str(self.data_center_uid)

        data_center_name: None | str | Unset
        if isinstance(self.data_center_name, Unset):
            data_center_name = UNSET
        else:
            data_center_name = self.data_center_name

        tcp_ip_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tcp_ip_settings, Unset):
            tcp_ip_settings = self.tcp_ip_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if data_center_uid is not UNSET:
            field_dict["dataCenterUid"] = data_center_uid
        if data_center_name is not UNSET:
            field_dict["dataCenterName"] = data_center_name
        if tcp_ip_settings is not UNSET:
            field_dict["tcpIpSettings"] = tcp_ip_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_appliance_tcp_ip_settings import NetworkApplianceTcpIpSettings

        d = dict(src_dict)
        name = d.pop("name")

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _data_center_uid = d.pop("dataCenterUid", UNSET)
        data_center_uid: UUID | Unset
        if isinstance(_data_center_uid, Unset):
            data_center_uid = UNSET
        else:
            data_center_uid = UUID(_data_center_uid)

        def _parse_data_center_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_center_name = _parse_data_center_name(d.pop("dataCenterName", UNSET))

        _tcp_ip_settings = d.pop("tcpIpSettings", UNSET)
        tcp_ip_settings: NetworkApplianceTcpIpSettings | Unset
        if isinstance(_tcp_ip_settings, Unset):
            tcp_ip_settings = UNSET
        else:
            tcp_ip_settings = NetworkApplianceTcpIpSettings.from_dict(_tcp_ip_settings)

        tenant_replication_resource_vcd_network_appliance = cls(
            name=name,
            instance_uid=instance_uid,
            data_center_uid=data_center_uid,
            data_center_name=data_center_name,
            tcp_ip_settings=tcp_ip_settings,
        )

        tenant_replication_resource_vcd_network_appliance.additional_properties = d
        return tenant_replication_resource_vcd_network_appliance

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
