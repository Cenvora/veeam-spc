from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.linux_discovery_rule_method import LinuxDiscoveryRuleMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedded_for_discovery_rule_children_type_0 import EmbeddedForDiscoveryRuleChildrenType0
    from ..models.linux_discovery_credentials import LinuxDiscoveryCredentials
    from ..models.linux_discovery_rule_deployment_settings import LinuxDiscoveryRuleDeploymentSettings


T = TypeVar("T", bound="LinuxDiscoveryRule")


@_attrs_define
class LinuxDiscoveryRule:
    """
    Attributes:
        credentials (list['LinuxDiscoveryCredentials']): Credentials required to access discovered computers.
        instance_uid (Union[Unset, UUID]): UID assigned to a discovery rule.
        method (Union[Unset, LinuxDiscoveryRuleMethod]): Discovery method. Default:
            LinuxDiscoveryRuleMethod.NETWORKBASED.
        deployment_settings (Union[Unset, LinuxDiscoveryRuleDeploymentSettings]):
        field_embedded (Union['EmbeddedForDiscoveryRuleChildrenType0', None, Unset]): Resource representation of the
            related discovery rule entity.
    """

    credentials: list["LinuxDiscoveryCredentials"]
    instance_uid: Union[Unset, UUID] = UNSET
    method: Union[Unset, LinuxDiscoveryRuleMethod] = LinuxDiscoveryRuleMethod.NETWORKBASED
    deployment_settings: Union[Unset, "LinuxDiscoveryRuleDeploymentSettings"] = UNSET
    field_embedded: Union["EmbeddedForDiscoveryRuleChildrenType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.embedded_for_discovery_rule_children_type_0 import EmbeddedForDiscoveryRuleChildrenType0

        credentials = []
        for credentials_item_data in self.credentials:
            credentials_item = credentials_item_data.to_dict()
            credentials.append(credentials_item)

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        method: Union[Unset, str] = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        deployment_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.deployment_settings, Unset):
            deployment_settings = self.deployment_settings.to_dict()

        field_embedded: Union[None, Unset, dict[str, Any]]
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
                "credentials": credentials,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if method is not UNSET:
            field_dict["method"] = method
        if deployment_settings is not UNSET:
            field_dict["deploymentSettings"] = deployment_settings
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedded_for_discovery_rule_children_type_0 import EmbeddedForDiscoveryRuleChildrenType0
        from ..models.linux_discovery_credentials import LinuxDiscoveryCredentials
        from ..models.linux_discovery_rule_deployment_settings import LinuxDiscoveryRuleDeploymentSettings

        d = dict(src_dict)
        credentials = []
        _credentials = d.pop("credentials")
        for credentials_item_data in _credentials:
            credentials_item = LinuxDiscoveryCredentials.from_dict(credentials_item_data)

            credentials.append(credentials_item)

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _method = d.pop("method", UNSET)
        method: Union[Unset, LinuxDiscoveryRuleMethod]
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = LinuxDiscoveryRuleMethod(_method)

        _deployment_settings = d.pop("deploymentSettings", UNSET)
        deployment_settings: Union[Unset, LinuxDiscoveryRuleDeploymentSettings]
        if isinstance(_deployment_settings, Unset):
            deployment_settings = UNSET
        else:
            deployment_settings = LinuxDiscoveryRuleDeploymentSettings.from_dict(_deployment_settings)

        def _parse_field_embedded(data: object) -> Union["EmbeddedForDiscoveryRuleChildrenType0", None, Unset]:
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
            except:  # noqa: E722
                pass
            return cast(Union["EmbeddedForDiscoveryRuleChildrenType0", None, Unset], data)

        field_embedded = _parse_field_embedded(d.pop("_embedded", UNSET))

        linux_discovery_rule = cls(
            credentials=credentials,
            instance_uid=instance_uid,
            method=method,
            deployment_settings=deployment_settings,
            field_embedded=field_embedded,
        )

        linux_discovery_rule.additional_properties = d
        return linux_discovery_rule

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
