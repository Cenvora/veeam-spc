from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.windows_discovery_rule_method import WindowsDiscoveryRuleMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.discovery_rule_credentials import DiscoveryRuleCredentials
    from ..models.embedded_for_discovery_rule_children_type_0 import EmbeddedForDiscoveryRuleChildrenType0
    from ..models.windows_discovery_rule_deployment_settings import WindowsDiscoveryRuleDeploymentSettings


T = TypeVar("T", bound="WindowsDiscoveryRule")


@_attrs_define
class WindowsDiscoveryRule:
    """
    Attributes:
        access_account (DiscoveryRuleCredentials):
        instance_uid (UUID | Unset): UID assigned to a discovery rule.
        method (WindowsDiscoveryRuleMethod | Unset): Discovery method. Default: WindowsDiscoveryRuleMethod.NETWORKBASED.
        use_master_management_agent_credentials (bool | Unset): Indicates whether Veeam Service Provider Console must
            use master agent credentials to connect discovered computers. Default: True.
        deployment_settings (WindowsDiscoveryRuleDeploymentSettings | Unset):
        field_embedded (EmbeddedForDiscoveryRuleChildrenType0 | None | Unset): Resource representation of the related
            discovery rule entity.
    """

    access_account: DiscoveryRuleCredentials
    instance_uid: UUID | Unset = UNSET
    method: WindowsDiscoveryRuleMethod | Unset = WindowsDiscoveryRuleMethod.NETWORKBASED
    use_master_management_agent_credentials: bool | Unset = True
    deployment_settings: WindowsDiscoveryRuleDeploymentSettings | Unset = UNSET
    field_embedded: EmbeddedForDiscoveryRuleChildrenType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.embedded_for_discovery_rule_children_type_0 import EmbeddedForDiscoveryRuleChildrenType0

        access_account = self.access_account.to_dict()

        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        use_master_management_agent_credentials = self.use_master_management_agent_credentials

        deployment_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deployment_settings, Unset):
            deployment_settings = self.deployment_settings.to_dict()

        field_embedded: dict[str, Any] | None | Unset
        if isinstance(self.field_embedded, Unset):
            field_embedded = UNSET
        elif isinstance(self.field_embedded, EmbeddedForDiscoveryRuleChildrenType0):
            field_embedded = self.field_embedded.to_dict()
        else:
            field_embedded = self.field_embedded

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accessAccount": access_account,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if method is not UNSET:
            field_dict["method"] = method
        if use_master_management_agent_credentials is not UNSET:
            field_dict["useMasterManagementAgentCredentials"] = use_master_management_agent_credentials
        if deployment_settings is not UNSET:
            field_dict["deploymentSettings"] = deployment_settings
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.discovery_rule_credentials import DiscoveryRuleCredentials
        from ..models.embedded_for_discovery_rule_children_type_0 import EmbeddedForDiscoveryRuleChildrenType0
        from ..models.windows_discovery_rule_deployment_settings import WindowsDiscoveryRuleDeploymentSettings

        d = dict(src_dict)
        access_account = DiscoveryRuleCredentials.from_dict(d.pop("accessAccount"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _method = d.pop("method", UNSET)
        method: WindowsDiscoveryRuleMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = WindowsDiscoveryRuleMethod(_method)

        use_master_management_agent_credentials = d.pop("useMasterManagementAgentCredentials", UNSET)

        _deployment_settings = d.pop("deploymentSettings", UNSET)
        deployment_settings: WindowsDiscoveryRuleDeploymentSettings | Unset
        if isinstance(_deployment_settings, Unset):
            deployment_settings = UNSET
        else:
            deployment_settings = WindowsDiscoveryRuleDeploymentSettings.from_dict(_deployment_settings)

        def _parse_field_embedded(data: object) -> EmbeddedForDiscoveryRuleChildrenType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_embedded_for_discovery_rule_children_type_0 = (
                    EmbeddedForDiscoveryRuleChildrenType0.from_dict(data)
                )

                return componentsschemas_embedded_for_discovery_rule_children_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EmbeddedForDiscoveryRuleChildrenType0 | None | Unset, data)

        field_embedded = _parse_field_embedded(d.pop("_embedded", UNSET))

        windows_discovery_rule = cls(
            access_account=access_account,
            instance_uid=instance_uid,
            method=method,
            use_master_management_agent_credentials=use_master_management_agent_credentials,
            deployment_settings=deployment_settings,
            field_embedded=field_embedded,
        )

        windows_discovery_rule.additional_properties = d
        return windows_discovery_rule

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
