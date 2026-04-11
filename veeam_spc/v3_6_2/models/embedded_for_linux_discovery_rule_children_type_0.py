from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.discovery_rule import DiscoveryRule
    from ..models.linux_discovery_rule import LinuxDiscoveryRule


T = TypeVar("T", bound="EmbeddedForLinuxDiscoveryRuleChildrenType0")


@_attrs_define
class EmbeddedForLinuxDiscoveryRuleChildrenType0:
    """Resource representation of the related Linux discovery rule entity.

    Attributes:
        discovery_rule (DiscoveryRule | Unset):
        linux_discovery_rule (LinuxDiscoveryRule | Unset):
    """

    discovery_rule: DiscoveryRule | Unset = UNSET
    linux_discovery_rule: LinuxDiscoveryRule | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        discovery_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.discovery_rule, Unset):
            discovery_rule = self.discovery_rule.to_dict()

        linux_discovery_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.linux_discovery_rule, Unset):
            linux_discovery_rule = self.linux_discovery_rule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if discovery_rule is not UNSET:
            field_dict["discoveryRule"] = discovery_rule
        if linux_discovery_rule is not UNSET:
            field_dict["linuxDiscoveryRule"] = linux_discovery_rule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.discovery_rule import DiscoveryRule
        from ..models.linux_discovery_rule import LinuxDiscoveryRule

        d = dict(src_dict)
        _discovery_rule = d.pop("discoveryRule", UNSET)
        discovery_rule: DiscoveryRule | Unset
        if isinstance(_discovery_rule, Unset):
            discovery_rule = UNSET
        else:
            discovery_rule = DiscoveryRule.from_dict(_discovery_rule)

        _linux_discovery_rule = d.pop("linuxDiscoveryRule", UNSET)
        linux_discovery_rule: LinuxDiscoveryRule | Unset
        if isinstance(_linux_discovery_rule, Unset):
            linux_discovery_rule = UNSET
        else:
            linux_discovery_rule = LinuxDiscoveryRule.from_dict(_linux_discovery_rule)

        embedded_for_linux_discovery_rule_children_type_0 = cls(
            discovery_rule=discovery_rule,
            linux_discovery_rule=linux_discovery_rule,
        )

        embedded_for_linux_discovery_rule_children_type_0.additional_properties = d
        return embedded_for_linux_discovery_rule_children_type_0

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
