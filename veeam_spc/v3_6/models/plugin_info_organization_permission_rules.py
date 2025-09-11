from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plugin_permission_rule import PluginPermissionRule


T = TypeVar("T", bound="PluginInfoOrganizationPermissionRules")


@_attrs_define
class PluginInfoOrganizationPermissionRules:
    """Plugin access rules configured for organizations.

    Attributes:
        rules (Union[Unset, list['PluginPermissionRule']]): Array of plugin access rules configured for organizations.
        organizations_are_allowed_by_default (Union[Unset, bool]): Indicates whether all other organizations are
            permitted to access plugin by default.
    """

    rules: Union[Unset, list["PluginPermissionRule"]] = UNSET
    organizations_are_allowed_by_default: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()
                rules.append(rules_item)

        organizations_are_allowed_by_default = self.organizations_are_allowed_by_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rules is not UNSET:
            field_dict["rules"] = rules
        if organizations_are_allowed_by_default is not UNSET:
            field_dict["organizationsAreAllowedByDefault"] = organizations_are_allowed_by_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plugin_permission_rule import PluginPermissionRule

        d = dict(src_dict)
        rules = []
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:
            rules_item = PluginPermissionRule.from_dict(rules_item_data)

            rules.append(rules_item)

        organizations_are_allowed_by_default = d.pop("organizationsAreAllowedByDefault", UNSET)

        plugin_info_organization_permission_rules = cls(
            rules=rules,
            organizations_are_allowed_by_default=organizations_are_allowed_by_default,
        )

        plugin_info_organization_permission_rules.additional_properties = d
        return plugin_info_organization_permission_rules

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
