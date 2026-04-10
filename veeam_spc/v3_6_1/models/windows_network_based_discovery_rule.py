from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.discovery_rule_network import DiscoveryRuleNetwork
    from ..models.embedded_for_windows_discovery_rule_children_type_0 import (
        EmbeddedForWindowsDiscoveryRuleChildrenType0,
    )


T = TypeVar("T", bound="WindowsNetworkBasedDiscoveryRule")


@_attrs_define
class WindowsNetworkBasedDiscoveryRule:
    """
    Attributes:
        networks (list['DiscoveryRuleNetwork']): Network settings.
        instance_uid (Union[Unset, UUID]): UID assigned to a network-based discovery rule.
        field_embedded (Union['EmbeddedForWindowsDiscoveryRuleChildrenType0', None, Unset]): Resource representation of
            the related Windows discovery rule entity.
    """

    networks: list["DiscoveryRuleNetwork"]
    instance_uid: Union[Unset, UUID] = UNSET
    field_embedded: Union["EmbeddedForWindowsDiscoveryRuleChildrenType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.embedded_for_windows_discovery_rule_children_type_0 import (
            EmbeddedForWindowsDiscoveryRuleChildrenType0,
        )

        networks = []
        for networks_item_data in self.networks:
            networks_item = networks_item_data.to_dict()
            networks.append(networks_item)

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        field_embedded: Union[None, Unset, dict[str, Any]]
        if isinstance(self.field_embedded, Unset):
            field_embedded = UNSET
        elif isinstance(self.field_embedded, EmbeddedForWindowsDiscoveryRuleChildrenType0):
            field_embedded = self.field_embedded.to_dict()
        else:
            field_embedded = self.field_embedded

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "networks": networks,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.discovery_rule_network import DiscoveryRuleNetwork
        from ..models.embedded_for_windows_discovery_rule_children_type_0 import (
            EmbeddedForWindowsDiscoveryRuleChildrenType0,
        )

        d = dict(src_dict)
        networks = []
        _networks = d.pop("networks")
        for networks_item_data in _networks:
            networks_item = DiscoveryRuleNetwork.from_dict(networks_item_data)

            networks.append(networks_item)

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        def _parse_field_embedded(data: object) -> Union["EmbeddedForWindowsDiscoveryRuleChildrenType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_embedded_for_windows_discovery_rule_children_type_0 = (
                    EmbeddedForWindowsDiscoveryRuleChildrenType0.from_dict(data)
                )

                return componentsschemas_embedded_for_windows_discovery_rule_children_type_0
            except:  # noqa: E722
                pass
            return cast(Union["EmbeddedForWindowsDiscoveryRuleChildrenType0", None, Unset], data)

        field_embedded = _parse_field_embedded(d.pop("_embedded", UNSET))

        windows_network_based_discovery_rule = cls(
            networks=networks,
            instance_uid=instance_uid,
            field_embedded=field_embedded,
        )

        windows_network_based_discovery_rule.additional_properties = d
        return windows_network_based_discovery_rule

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
