from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.discovery_rule_filter import DiscoveryRuleFilter
    from ..models.discovery_rule_network import DiscoveryRuleNetwork
    from ..models.discovery_rule_notification_settings import DiscoveryRuleNotificationSettings
    from ..models.discovery_rule_schedule_settings import DiscoveryRuleScheduleSettings
    from ..models.linux_discovery_credentials_input import LinuxDiscoveryCredentialsInput
    from ..models.linux_discovery_rule_deployment_settings import LinuxDiscoveryRuleDeploymentSettings


T = TypeVar("T", bound="LinuxNetworkBasedDiscoveryRuleInput")


@_attrs_define
class LinuxNetworkBasedDiscoveryRuleInput:
    """
    Attributes:
        name (str): Name of a network-based discovery rule.
        master_agent_uid (UUID): UID assigned to a master agent.
        networks (list['DiscoveryRuleNetwork']): Range of IP addresses.
        credentials (list['LinuxDiscoveryCredentialsInput']): Credentials required to access discovered computers.
        filter_ (Union[Unset, DiscoveryRuleFilter]):
        notification_settings (Union[Unset, DiscoveryRuleNotificationSettings]):  Example: {'isEnabled': True,
            'scheduleType': 'Days', 'scheduleTime': '12:30', 'scheduleDay': 'Sunday', 'to': 'administrator@vac.com',
            'subject': 'VSPC Discovery Results', 'notifyOnTheFirstRun': False}.
        deployment_settings (Union[Unset, LinuxDiscoveryRuleDeploymentSettings]):
        schedule_settings (Union[Unset, DiscoveryRuleScheduleSettings]):
    """

    name: str
    master_agent_uid: UUID
    networks: list["DiscoveryRuleNetwork"]
    credentials: list["LinuxDiscoveryCredentialsInput"]
    filter_: Union[Unset, "DiscoveryRuleFilter"] = UNSET
    notification_settings: Union[Unset, "DiscoveryRuleNotificationSettings"] = UNSET
    deployment_settings: Union[Unset, "LinuxDiscoveryRuleDeploymentSettings"] = UNSET
    schedule_settings: Union[Unset, "DiscoveryRuleScheduleSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        master_agent_uid = str(self.master_agent_uid)

        networks = []
        for networks_item_data in self.networks:
            networks_item = networks_item_data.to_dict()
            networks.append(networks_item)

        credentials = []
        for credentials_item_data in self.credentials:
            credentials_item = credentials_item_data.to_dict()
            credentials.append(credentials_item)

        filter_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        notification_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.notification_settings, Unset):
            notification_settings = self.notification_settings.to_dict()

        deployment_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.deployment_settings, Unset):
            deployment_settings = self.deployment_settings.to_dict()

        schedule_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schedule_settings, Unset):
            schedule_settings = self.schedule_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "masterAgentUid": master_agent_uid,
                "networks": networks,
                "credentials": credentials,
            }
        )
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if notification_settings is not UNSET:
            field_dict["notificationSettings"] = notification_settings
        if deployment_settings is not UNSET:
            field_dict["deploymentSettings"] = deployment_settings
        if schedule_settings is not UNSET:
            field_dict["scheduleSettings"] = schedule_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.discovery_rule_filter import DiscoveryRuleFilter
        from ..models.discovery_rule_network import DiscoveryRuleNetwork
        from ..models.discovery_rule_notification_settings import DiscoveryRuleNotificationSettings
        from ..models.discovery_rule_schedule_settings import DiscoveryRuleScheduleSettings
        from ..models.linux_discovery_credentials_input import LinuxDiscoveryCredentialsInput
        from ..models.linux_discovery_rule_deployment_settings import LinuxDiscoveryRuleDeploymentSettings

        d = dict(src_dict)
        name = d.pop("name")

        master_agent_uid = UUID(d.pop("masterAgentUid"))

        networks = []
        _networks = d.pop("networks")
        for networks_item_data in _networks:
            networks_item = DiscoveryRuleNetwork.from_dict(networks_item_data)

            networks.append(networks_item)

        credentials = []
        _credentials = d.pop("credentials")
        for credentials_item_data in _credentials:
            credentials_item = LinuxDiscoveryCredentialsInput.from_dict(credentials_item_data)

            credentials.append(credentials_item)

        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, DiscoveryRuleFilter]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = DiscoveryRuleFilter.from_dict(_filter_)

        _notification_settings = d.pop("notificationSettings", UNSET)
        notification_settings: Union[Unset, DiscoveryRuleNotificationSettings]
        if isinstance(_notification_settings, Unset):
            notification_settings = UNSET
        else:
            notification_settings = DiscoveryRuleNotificationSettings.from_dict(_notification_settings)

        _deployment_settings = d.pop("deploymentSettings", UNSET)
        deployment_settings: Union[Unset, LinuxDiscoveryRuleDeploymentSettings]
        if isinstance(_deployment_settings, Unset):
            deployment_settings = UNSET
        else:
            deployment_settings = LinuxDiscoveryRuleDeploymentSettings.from_dict(_deployment_settings)

        _schedule_settings = d.pop("scheduleSettings", UNSET)
        schedule_settings: Union[Unset, DiscoveryRuleScheduleSettings]
        if isinstance(_schedule_settings, Unset):
            schedule_settings = UNSET
        else:
            schedule_settings = DiscoveryRuleScheduleSettings.from_dict(_schedule_settings)

        linux_network_based_discovery_rule_input = cls(
            name=name,
            master_agent_uid=master_agent_uid,
            networks=networks,
            credentials=credentials,
            filter_=filter_,
            notification_settings=notification_settings,
            deployment_settings=deployment_settings,
            schedule_settings=schedule_settings,
        )

        linux_network_based_discovery_rule_input.additional_properties = d
        return linux_network_based_discovery_rule_input

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
