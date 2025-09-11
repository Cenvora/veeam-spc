from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.network_appliance_tcp_ip_settings import NetworkApplianceTcpIpSettings


T = TypeVar("T", bound="TenantReplicationResourceNetworkAppliance")


@_attrs_define
class TenantReplicationResourceNetworkAppliance:
    """
    Attributes:
        name (str): Name of a network extension appliance.
        instance_uid (Union[Unset, UUID]): UID assigned to a network extension appliance.
        hardware_plan_uid (Union[Unset, UUID]): UID assigned to a hardware plan.
        host_name (Union[Unset, str]): Name of a host on which network extension appliance is deployed.
        root_host_name (Union[Unset, str]): Name of a root host on which network extension appliance is deployed.
        external_network_name (Union[Unset, str]): Name of an external production network.
        tcp_ip_settings (Union[Unset, NetworkApplianceTcpIpSettings]):
    """

    name: str
    instance_uid: Union[Unset, UUID] = UNSET
    hardware_plan_uid: Union[Unset, UUID] = UNSET
    host_name: Union[Unset, str] = UNSET
    root_host_name: Union[Unset, str] = UNSET
    external_network_name: Union[Unset, str] = UNSET
    tcp_ip_settings: Union[Unset, "NetworkApplianceTcpIpSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        hardware_plan_uid: Union[Unset, str] = UNSET
        if not isinstance(self.hardware_plan_uid, Unset):
            hardware_plan_uid = str(self.hardware_plan_uid)

        host_name = self.host_name

        root_host_name = self.root_host_name

        external_network_name = self.external_network_name

        tcp_ip_settings: Union[Unset, dict[str, Any]] = UNSET
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
        if hardware_plan_uid is not UNSET:
            field_dict["hardwarePlanUid"] = hardware_plan_uid
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if root_host_name is not UNSET:
            field_dict["rootHostName"] = root_host_name
        if external_network_name is not UNSET:
            field_dict["externalNetworkName"] = external_network_name
        if tcp_ip_settings is not UNSET:
            field_dict["tcpIpSettings"] = tcp_ip_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_appliance_tcp_ip_settings import NetworkApplianceTcpIpSettings

        d = dict(src_dict)
        name = d.pop("name")

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _hardware_plan_uid = d.pop("hardwarePlanUid", UNSET)
        hardware_plan_uid: Union[Unset, UUID]
        if isinstance(_hardware_plan_uid, Unset):
            hardware_plan_uid = UNSET
        else:
            hardware_plan_uid = UUID(_hardware_plan_uid)

        host_name = d.pop("hostName", UNSET)

        root_host_name = d.pop("rootHostName", UNSET)

        external_network_name = d.pop("externalNetworkName", UNSET)

        _tcp_ip_settings = d.pop("tcpIpSettings", UNSET)
        tcp_ip_settings: Union[Unset, NetworkApplianceTcpIpSettings]
        if isinstance(_tcp_ip_settings, Unset):
            tcp_ip_settings = UNSET
        else:
            tcp_ip_settings = NetworkApplianceTcpIpSettings.from_dict(_tcp_ip_settings)

        tenant_replication_resource_network_appliance = cls(
            name=name,
            instance_uid=instance_uid,
            hardware_plan_uid=hardware_plan_uid,
            host_name=host_name,
            root_host_name=root_host_name,
            external_network_name=external_network_name,
            tcp_ip_settings=tcp_ip_settings,
        )

        tenant_replication_resource_network_appliance.additional_properties = d
        return tenant_replication_resource_network_appliance

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
