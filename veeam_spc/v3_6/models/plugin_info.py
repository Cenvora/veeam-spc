from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.plugin_feature import PluginFeature
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plugin_info_agent_permission_rules import PluginInfoAgentPermissionRules
    from ..models.plugin_info_organization_permission_rules import PluginInfoOrganizationPermissionRules


T = TypeVar("T", bound="PluginInfo")


@_attrs_define
class PluginInfo:
    """
    Attributes:
        plugin_id (Union[Unset, UUID]): ID assigned to a plugin.
        name (Union[Unset, str]): Name of a plugin.
        icon (Union[Unset, str]): Path to a plugin icon file.
        description (Union[Unset, str]): Description of a plugin.
        version (Union[Unset, str]): Version of a plugin.
        available_versions (Union[Unset, list[str]]): Array of available plugin versions.
        enabled (Union[Unset, bool]): Indicates whether a plugin is enabled.
        has_api_key (Union[Unset, bool]): Indicates whether API key is assigned to a plugin.
        supported_features (Union[Unset, list[PluginFeature]]): Array of supported plugin features.
        agent_permission_rules (Union[Unset, PluginInfoAgentPermissionRules]): Plugin access rules configured for
            management agents.
        organization_permission_rules (Union[Unset, PluginInfoOrganizationPermissionRules]): Plugin access rules
            configured for organizations.
    """

    plugin_id: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    available_versions: Union[Unset, list[str]] = UNSET
    enabled: Union[Unset, bool] = UNSET
    has_api_key: Union[Unset, bool] = UNSET
    supported_features: Union[Unset, list[PluginFeature]] = UNSET
    agent_permission_rules: Union[Unset, "PluginInfoAgentPermissionRules"] = UNSET
    organization_permission_rules: Union[Unset, "PluginInfoOrganizationPermissionRules"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plugin_id: Union[Unset, str] = UNSET
        if not isinstance(self.plugin_id, Unset):
            plugin_id = str(self.plugin_id)

        name = self.name

        icon = self.icon

        description = self.description

        version = self.version

        available_versions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.available_versions, Unset):
            available_versions = self.available_versions

        enabled = self.enabled

        has_api_key = self.has_api_key

        supported_features: Union[Unset, list[str]] = UNSET
        if not isinstance(self.supported_features, Unset):
            supported_features = []
            for supported_features_item_data in self.supported_features:
                supported_features_item = supported_features_item_data.value
                supported_features.append(supported_features_item)

        agent_permission_rules: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.agent_permission_rules, Unset):
            agent_permission_rules = self.agent_permission_rules.to_dict()

        organization_permission_rules: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization_permission_rules, Unset):
            organization_permission_rules = self.organization_permission_rules.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plugin_id is not UNSET:
            field_dict["pluginId"] = plugin_id
        if name is not UNSET:
            field_dict["name"] = name
        if icon is not UNSET:
            field_dict["icon"] = icon
        if description is not UNSET:
            field_dict["description"] = description
        if version is not UNSET:
            field_dict["version"] = version
        if available_versions is not UNSET:
            field_dict["availableVersions"] = available_versions
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if has_api_key is not UNSET:
            field_dict["hasApiKey"] = has_api_key
        if supported_features is not UNSET:
            field_dict["supportedFeatures"] = supported_features
        if agent_permission_rules is not UNSET:
            field_dict["agentPermissionRules"] = agent_permission_rules
        if organization_permission_rules is not UNSET:
            field_dict["organizationPermissionRules"] = organization_permission_rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plugin_info_agent_permission_rules import PluginInfoAgentPermissionRules
        from ..models.plugin_info_organization_permission_rules import PluginInfoOrganizationPermissionRules

        d = dict(src_dict)
        _plugin_id = d.pop("pluginId", UNSET)
        plugin_id: Union[Unset, UUID]
        if isinstance(_plugin_id, Unset):
            plugin_id = UNSET
        else:
            plugin_id = UUID(_plugin_id)

        name = d.pop("name", UNSET)

        icon = d.pop("icon", UNSET)

        description = d.pop("description", UNSET)

        version = d.pop("version", UNSET)

        available_versions = cast(list[str], d.pop("availableVersions", UNSET))

        enabled = d.pop("enabled", UNSET)

        has_api_key = d.pop("hasApiKey", UNSET)

        supported_features = []
        _supported_features = d.pop("supportedFeatures", UNSET)
        for supported_features_item_data in _supported_features or []:
            supported_features_item = PluginFeature(supported_features_item_data)

            supported_features.append(supported_features_item)

        _agent_permission_rules = d.pop("agentPermissionRules", UNSET)
        agent_permission_rules: Union[Unset, PluginInfoAgentPermissionRules]
        if isinstance(_agent_permission_rules, Unset):
            agent_permission_rules = UNSET
        else:
            agent_permission_rules = PluginInfoAgentPermissionRules.from_dict(_agent_permission_rules)

        _organization_permission_rules = d.pop("organizationPermissionRules", UNSET)
        organization_permission_rules: Union[Unset, PluginInfoOrganizationPermissionRules]
        if isinstance(_organization_permission_rules, Unset):
            organization_permission_rules = UNSET
        else:
            organization_permission_rules = PluginInfoOrganizationPermissionRules.from_dict(
                _organization_permission_rules
            )

        plugin_info = cls(
            plugin_id=plugin_id,
            name=name,
            icon=icon,
            description=description,
            version=version,
            available_versions=available_versions,
            enabled=enabled,
            has_api_key=has_api_key,
            supported_features=supported_features,
            agent_permission_rules=agent_permission_rules,
            organization_permission_rules=organization_permission_rules,
        )

        plugin_info.additional_properties = d
        return plugin_info

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
