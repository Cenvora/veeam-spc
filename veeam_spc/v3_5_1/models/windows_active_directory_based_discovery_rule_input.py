from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.windows_active_directory_based_discovery_rule_input_ad_method import (
    WindowsActiveDirectoryBasedDiscoveryRuleInputAdMethod,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.discovery_rule_credentials import DiscoveryRuleCredentials
    from ..models.discovery_rule_filter import DiscoveryRuleFilter
    from ..models.discovery_rule_notification_settings import DiscoveryRuleNotificationSettings
    from ..models.discovery_rule_schedule_settings import DiscoveryRuleScheduleSettings
    from ..models.windows_discovery_rule_deployment_settings import WindowsDiscoveryRuleDeploymentSettings


T = TypeVar("T", bound="WindowsActiveDirectoryBasedDiscoveryRuleInput")


@_attrs_define
class WindowsActiveDirectoryBasedDiscoveryRuleInput:
    """
    Attributes:
        name (str): Name of an Microsoft Entra ID discovery rule.
        master_agent_uid (UUID): UID assigned to a master agent.
        ad_method (WindowsActiveDirectoryBasedDiscoveryRuleInputAdMethod): Microsoft Entra ID discovery method.
        access_account (DiscoveryRuleCredentials):
        skip_offline_computers_days (Union[Unset, int]): Number of days for which offline computers are skipped from
            discovery.
        custom_query (Union[Unset, str]): LDAP query that returns a list of computers to scan.
        use_master_management_agent_credentials (Union[Unset, bool]): Indicates whether credentials specified in the
            master management agent configuration must be used. Default: True.
        filter_ (Union[Unset, DiscoveryRuleFilter]):
        notification_settings (Union[Unset, DiscoveryRuleNotificationSettings]):  Example: {'isEnabled': True,
            'scheduleType': 'Days', 'scheduleTime': '12:30', 'scheduleDay': 'Sunday', 'to': 'administrator@vac.com',
            'subject': 'VSPC Discovery Results', 'notifyOnTheFirstRun': False}.
        deployment_settings (Union[Unset, WindowsDiscoveryRuleDeploymentSettings]):
        schedule_settings (Union[Unset, DiscoveryRuleScheduleSettings]):
    """

    name: str
    master_agent_uid: UUID
    ad_method: WindowsActiveDirectoryBasedDiscoveryRuleInputAdMethod
    access_account: "DiscoveryRuleCredentials"
    skip_offline_computers_days: Union[Unset, int] = UNSET
    custom_query: Union[Unset, str] = UNSET
    use_master_management_agent_credentials: Union[Unset, bool] = True
    filter_: Union[Unset, "DiscoveryRuleFilter"] = UNSET
    notification_settings: Union[Unset, "DiscoveryRuleNotificationSettings"] = UNSET
    deployment_settings: Union[Unset, "WindowsDiscoveryRuleDeploymentSettings"] = UNSET
    schedule_settings: Union[Unset, "DiscoveryRuleScheduleSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        master_agent_uid = str(self.master_agent_uid)

        ad_method = self.ad_method.value

        access_account = self.access_account.to_dict()

        skip_offline_computers_days = self.skip_offline_computers_days

        custom_query = self.custom_query

        use_master_management_agent_credentials = self.use_master_management_agent_credentials

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
                "adMethod": ad_method,
                "accessAccount": access_account,
            }
        )
        if skip_offline_computers_days is not UNSET:
            field_dict["skipOfflineComputersDays"] = skip_offline_computers_days
        if custom_query is not UNSET:
            field_dict["customQuery"] = custom_query
        if use_master_management_agent_credentials is not UNSET:
            field_dict["useMasterManagementAgentCredentials"] = use_master_management_agent_credentials
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
        from ..models.discovery_rule_credentials import DiscoveryRuleCredentials
        from ..models.discovery_rule_filter import DiscoveryRuleFilter
        from ..models.discovery_rule_notification_settings import DiscoveryRuleNotificationSettings
        from ..models.discovery_rule_schedule_settings import DiscoveryRuleScheduleSettings
        from ..models.windows_discovery_rule_deployment_settings import WindowsDiscoveryRuleDeploymentSettings

        d = dict(src_dict)
        name = d.pop("name")

        master_agent_uid = UUID(d.pop("masterAgentUid"))

        ad_method = WindowsActiveDirectoryBasedDiscoveryRuleInputAdMethod(d.pop("adMethod"))

        access_account = DiscoveryRuleCredentials.from_dict(d.pop("accessAccount"))

        skip_offline_computers_days = d.pop("skipOfflineComputersDays", UNSET)

        custom_query = d.pop("customQuery", UNSET)

        use_master_management_agent_credentials = d.pop("useMasterManagementAgentCredentials", UNSET)

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
        deployment_settings: Union[Unset, WindowsDiscoveryRuleDeploymentSettings]
        if isinstance(_deployment_settings, Unset):
            deployment_settings = UNSET
        else:
            deployment_settings = WindowsDiscoveryRuleDeploymentSettings.from_dict(_deployment_settings)

        _schedule_settings = d.pop("scheduleSettings", UNSET)
        schedule_settings: Union[Unset, DiscoveryRuleScheduleSettings]
        if isinstance(_schedule_settings, Unset):
            schedule_settings = UNSET
        else:
            schedule_settings = DiscoveryRuleScheduleSettings.from_dict(_schedule_settings)

        windows_active_directory_based_discovery_rule_input = cls(
            name=name,
            master_agent_uid=master_agent_uid,
            ad_method=ad_method,
            access_account=access_account,
            skip_offline_computers_days=skip_offline_computers_days,
            custom_query=custom_query,
            use_master_management_agent_credentials=use_master_management_agent_credentials,
            filter_=filter_,
            notification_settings=notification_settings,
            deployment_settings=deployment_settings,
            schedule_settings=schedule_settings,
        )

        windows_active_directory_based_discovery_rule_input.additional_properties = d
        return windows_active_directory_based_discovery_rule_input

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
