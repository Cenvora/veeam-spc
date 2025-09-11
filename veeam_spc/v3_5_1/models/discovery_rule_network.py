from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.machines_network_trust_options import MachinesNetworkTrustOptions


T = TypeVar("T", bound="DiscoveryRuleNetwork")


@_attrs_define
class DiscoveryRuleNetwork:
    """
    Example:
        {'networkName': 'Production', 'firstIp': '172.17.53.1', 'lastIp': '172.17.53.50'}

    Attributes:
        network_name (str): Name of a network configured in Veeam Service Provider Console.
        first_ip (str): First IP-address in the range set for discovery.
        last_ip (str): Last IP-address in the range set for discovery.
        trust_options (Union[Unset, MachinesNetworkTrustOptions]):
    """

    network_name: str
    first_ip: str
    last_ip: str
    trust_options: Union[Unset, "MachinesNetworkTrustOptions"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network_name = self.network_name

        first_ip = self.first_ip

        last_ip = self.last_ip

        trust_options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.trust_options, Unset):
            trust_options = self.trust_options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "networkName": network_name,
                "firstIp": first_ip,
                "lastIp": last_ip,
            }
        )
        if trust_options is not UNSET:
            field_dict["trustOptions"] = trust_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.machines_network_trust_options import MachinesNetworkTrustOptions

        d = dict(src_dict)
        network_name = d.pop("networkName")

        first_ip = d.pop("firstIp")

        last_ip = d.pop("lastIp")

        _trust_options = d.pop("trustOptions", UNSET)
        trust_options: Union[Unset, MachinesNetworkTrustOptions]
        if isinstance(_trust_options, Unset):
            trust_options = UNSET
        else:
            trust_options = MachinesNetworkTrustOptions.from_dict(_trust_options)

        discovery_rule_network = cls(
            network_name=network_name,
            first_ip=first_ip,
            last_ip=last_ip,
            trust_options=trust_options,
        )

        discovery_rule_network.additional_properties = d
        return discovery_rule_network

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
