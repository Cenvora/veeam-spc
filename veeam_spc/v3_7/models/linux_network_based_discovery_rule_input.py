from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
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
    r"""
    Example:
        {'name': 'Complex Linux Network Rule', 'masterAgentUid': 'da463bea-d186-4a14-b809-4aba366b03e8', 'networks':
            [{'networkName': 'netw', 'firstIp': '172.36.48.41', 'lastIp': '172.36.48.41', 'trustOptions': {'trustOption':
            'KnownList', 'knownHostList': 'valNet'}}], 'credentials': [{'username': 'root', 'password': 'Password1',
            'priority': 0, 'description': 'Network-based rule for Linux computers', 'sshPort': 22,
            'elevateAccountPrivileges': True, 'addAccountToSudoersFile': True, 'useSuIfsudoFails': True, 'rootPassword':
            'Password1', 'sshPrivateKey': '-----BEGIN RSA PRIVATE KEY-----
            \nMIIEogIBAAKCAQEArVMvwKOymfth5E0wq38d7svfmLVsVAHtIJYMlJBTx6Y+R2+3\nDcAqVLZG9neFJU2ivudafbZnu1TykuM0sKRXRix+cpMU
            GevoY026m6lo0s7m3ft9\nF5oOrr1LefsSadI7MTRhCPrHBKt+G9taMhovnGHq/8JzUflX2k1v7Sjy+zhJzpGW\nmJckhHZ+Jyd28JCdAWNiSEZg
            oEKGdLBL8/nkEm8Su4SRRKiTxRSbHtof+tUjIdoL\ntmdT9CiYM11eb46GMV8haaDEwpd0pL7iWZfXIo6ZZcKZ60JU70tYmz69JaYfVOLb\nasaI
            3ng22dzmt89Kk4C1i0ueVMH3WE7MvndpzwIBJQKCAQAODantBlqW3Qfv6pU+\nVmo19NrHMU34+Ty9c/Muo+seBo9tk2+1Ab4+OErxY6MDBkt3Qz
            DZwq52+Qy/zTuf\nnp9K4QNVZd8JBUoxkK5D+PqpTwvMzzOn08wAVImURMokQXprxfoHpaFvFNLfqgBk\n7V3OaM3dYssUfAA0S3fHHv7xxijIfW
            /F4EKGk7B1+WX1LIoka4OF3fRtktqlv0xV\nIDG1YqugiwEHL2cxVHmviqJOfP496JKzz9TXS6TMWbRThykQjXf8irOfQsAbjmuO\nFFp+FCK8XI
            TKuS9tBinpKpsUZoLiZ3r+uAO3gVWutdsdrJChYP87+Aaj82PWr+tv\nfSNlAoGBAOynYVyFklx597Yg4jdVg6+TEMlQ8Ga4TK6Iba8NzGPt6qRq
            1UeRninF\ncw7jIVojtqdqzKnnm+d5Ri4tS5rjLJjTwyePpR5HU3mwlDCpaJIS0XUptNOwwqso\n9Y/a92iwzAMA1Z4s3q+ye2tinP0WZb1B7RxM
            jrBNOuswnv3An7BFAoGBALt+eoI1\nNujkC/JXQVYgkkWtJJgu+d314qSate929cW8w37p/OevwcafOlocCvQPGOa7g6XP\nyCtw6CQtv2jbiZ2R
            ddyvTP8kYg71o4MtND5SGiJ+Q2B2PmDbCcPZ5IZ5PyNru6Wj\nClX/bFVh0lszbpWLPKKwdJwhd+d6i3dJewUDAoGBALMW4eUmz5/tmNzanVpOjS
            rr\n1VoTvNgcxGhnPj9Itll1xlLpEBp8CP0EH7g9Lf8GRQkSjQr0dftHBK1StcFR+DxN\nOb0SwiTAWtihTYyb4G6KyAWjBWHtjGXZzpZgg+CFyt
            HXHjKC0ghrZFFDtRKNfWyg\nl8JjcuZISENHY4+YsDJdAoGAfq9niGklGeYxleft4D+FbVlQE8y2qrrlPslmLC3I\nqDNvVcCxzPo20k/pKCDJIX
            H8EYWeI+1CD4OjxWsEyk8lodD8nAe+ZzRCQXWKKDNM\n0Cmi9LYthl27ceAbWtF+u7m1ChhcMaWDhjb2K9pP3MHi72vqsx1H3x2IXiJeO9ez\n/H
            cCgYEAvbcMG79y8Io4lm+c/emqnIPIL0fyrwo7SJ9qdojN63IV3YtQvct+V/Za\nOnLVizuPAye0Bk2qbc4nSt9Jj+E3PrOrZCyEtdQHwT90WM5f
            zb5OOk6sIwMJaajn\nY6mMXL0VW0XYI6PhfFPdwKhi2nPP07VzN302VWxTI3HeNT7Hg6A=\n-----END RSA PRIVATE KEY-----\n',
            'passphrase': '', 'type': 'LinuxCertificate'}], 'filter': {'exclusionMask': [], 'ignoreInaccessibleMachine':
            True, 'osTypes': ['Debian', 'Ubuntu'], 'applications': [], 'customApplication': None, 'platforms':
            ['MicrosoftHyperVandVmWareVSphere', 'Physical']}, 'notificationSettings': {'isEnabled': True, 'scheduleType':
            'Weeks', 'scheduleTime': '05:00', 'weekSettings': {'scheduleDay': 'Monday'}, 'to': 'admin@mycompany.com',
            'subject': 'Linux Discovery', 'notifyOnTheFirstRun': False}, 'deploymentSettings': {'isEnabled': False,
            'backupPolicyUid': None, 'setReadOnlyAccess': True}, 'scheduleSettings': {'scheduleType': 'NotScheduled',
            'timeZone': None, 'dailyScheduleSettings': None, 'monthlyScheduleSettings': None, 'periodicalScheduleSettings':
            None}}

    Attributes:
        name (str): Name of a network-based discovery rule.
        master_agent_uid (UUID): UID assigned to a master agent.
        networks (list[DiscoveryRuleNetwork]): Range of IP addresses.
        credentials (list[LinuxDiscoveryCredentialsInput]): Credentials required to access discovered computers.
        filter_ (DiscoveryRuleFilter | Unset):
        notification_settings (DiscoveryRuleNotificationSettings | Unset):  Example: {'isEnabled': True, 'scheduleType':
            'Days', 'scheduleTime': '12:30', 'scheduleDay': 'Sunday', 'to': 'administrator@vac.com', 'subject': 'VSPC
            Discovery Results', 'notifyOnTheFirstRun': False}.
        deployment_settings (LinuxDiscoveryRuleDeploymentSettings | Unset):
        schedule_settings (DiscoveryRuleScheduleSettings | Unset):
    """

    name: str
    master_agent_uid: UUID
    networks: list[DiscoveryRuleNetwork]
    credentials: list[LinuxDiscoveryCredentialsInput]
    filter_: DiscoveryRuleFilter | Unset = UNSET
    notification_settings: DiscoveryRuleNotificationSettings | Unset = UNSET
    deployment_settings: LinuxDiscoveryRuleDeploymentSettings | Unset = UNSET
    schedule_settings: DiscoveryRuleScheduleSettings | Unset = UNSET
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

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        notification_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notification_settings, Unset):
            notification_settings = self.notification_settings.to_dict()

        deployment_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deployment_settings, Unset):
            deployment_settings = self.deployment_settings.to_dict()

        schedule_settings: dict[str, Any] | Unset = UNSET
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
        filter_: DiscoveryRuleFilter | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = DiscoveryRuleFilter.from_dict(_filter_)

        _notification_settings = d.pop("notificationSettings", UNSET)
        notification_settings: DiscoveryRuleNotificationSettings | Unset
        if isinstance(_notification_settings, Unset):
            notification_settings = UNSET
        else:
            notification_settings = DiscoveryRuleNotificationSettings.from_dict(_notification_settings)

        _deployment_settings = d.pop("deploymentSettings", UNSET)
        deployment_settings: LinuxDiscoveryRuleDeploymentSettings | Unset
        if isinstance(_deployment_settings, Unset):
            deployment_settings = UNSET
        else:
            deployment_settings = LinuxDiscoveryRuleDeploymentSettings.from_dict(_deployment_settings)

        _schedule_settings = d.pop("scheduleSettings", UNSET)
        schedule_settings: DiscoveryRuleScheduleSettings | Unset
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
