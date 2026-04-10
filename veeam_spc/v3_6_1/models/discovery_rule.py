import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.discovery_rule_status import DiscoveryRuleStatus
from ..models.discovery_rule_system_type import DiscoveryRuleSystemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.discovery_rule_filter import DiscoveryRuleFilter
    from ..models.discovery_rule_notification_settings import DiscoveryRuleNotificationSettings
    from ..models.discovery_rule_schedule_settings import DiscoveryRuleScheduleSettings


T = TypeVar("T", bound="DiscoveryRule")


@_attrs_define
class DiscoveryRule:
    """
    Attributes:
        name (str): Name of a discovery rule
        master_agent_uid (UUID): UID assigned to a master agent.
        instance_uid (Union[Unset, UUID]): UID assigned to a discovery rule.
        location_uid (Union[Unset, UUID]): UID assigned to a location for which a discovery rule is configured.
        company_uid (Union[Unset, UUID]): UID assigned to a company for which a discovery rule is configured.
        system_type (Union[Unset, DiscoveryRuleSystemType]): Type of guest OS.
        status (Union[Unset, DiscoveryRuleStatus]): Current status of a discovery rule.
        last_run (Union[None, Unset, datetime.datetime]): Date and time of the latest discovery session.
        filter_ (Union[Unset, DiscoveryRuleFilter]):
        notification_settings (Union[Unset, DiscoveryRuleNotificationSettings]):  Example: {'isEnabled': True,
            'scheduleType': 'Days', 'scheduleTime': '12:30', 'scheduleDay': 'Sunday', 'to': 'administrator@vac.com',
            'subject': 'VSPC Discovery Results', 'notifyOnTheFirstRun': False}.
        schedule_settings (Union[Unset, DiscoveryRuleScheduleSettings]):
        total_computers_count (Union[Unset, int]): Number of discovered computers.
        online_computers_count (Union[Unset, int]): Number of online computers.
        offline_computers_count (Union[Unset, int]): Number of offline computers.
    """

    name: str
    master_agent_uid: UUID
    instance_uid: Union[Unset, UUID] = UNSET
    location_uid: Union[Unset, UUID] = UNSET
    company_uid: Union[Unset, UUID] = UNSET
    system_type: Union[Unset, DiscoveryRuleSystemType] = UNSET
    status: Union[Unset, DiscoveryRuleStatus] = UNSET
    last_run: Union[None, Unset, datetime.datetime] = UNSET
    filter_: Union[Unset, "DiscoveryRuleFilter"] = UNSET
    notification_settings: Union[Unset, "DiscoveryRuleNotificationSettings"] = UNSET
    schedule_settings: Union[Unset, "DiscoveryRuleScheduleSettings"] = UNSET
    total_computers_count: Union[Unset, int] = UNSET
    online_computers_count: Union[Unset, int] = UNSET
    offline_computers_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        master_agent_uid = str(self.master_agent_uid)

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        location_uid: Union[Unset, str] = UNSET
        if not isinstance(self.location_uid, Unset):
            location_uid = str(self.location_uid)

        company_uid: Union[Unset, str] = UNSET
        if not isinstance(self.company_uid, Unset):
            company_uid = str(self.company_uid)

        system_type: Union[Unset, str] = UNSET
        if not isinstance(self.system_type, Unset):
            system_type = self.system_type.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        last_run: Union[None, Unset, str]
        if isinstance(self.last_run, Unset):
            last_run = UNSET
        elif isinstance(self.last_run, datetime.datetime):
            last_run = self.last_run.isoformat()
        else:
            last_run = self.last_run

        filter_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        notification_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.notification_settings, Unset):
            notification_settings = self.notification_settings.to_dict()

        schedule_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schedule_settings, Unset):
            schedule_settings = self.schedule_settings.to_dict()

        total_computers_count = self.total_computers_count

        online_computers_count = self.online_computers_count

        offline_computers_count = self.offline_computers_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "masterAgentUid": master_agent_uid,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if location_uid is not UNSET:
            field_dict["locationUid"] = location_uid
        if company_uid is not UNSET:
            field_dict["companyUid"] = company_uid
        if system_type is not UNSET:
            field_dict["systemType"] = system_type
        if status is not UNSET:
            field_dict["status"] = status
        if last_run is not UNSET:
            field_dict["lastRun"] = last_run
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if notification_settings is not UNSET:
            field_dict["notificationSettings"] = notification_settings
        if schedule_settings is not UNSET:
            field_dict["scheduleSettings"] = schedule_settings
        if total_computers_count is not UNSET:
            field_dict["totalComputersCount"] = total_computers_count
        if online_computers_count is not UNSET:
            field_dict["onlineComputersCount"] = online_computers_count
        if offline_computers_count is not UNSET:
            field_dict["offlineComputersCount"] = offline_computers_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.discovery_rule_filter import DiscoveryRuleFilter
        from ..models.discovery_rule_notification_settings import DiscoveryRuleNotificationSettings
        from ..models.discovery_rule_schedule_settings import DiscoveryRuleScheduleSettings

        d = dict(src_dict)
        name = d.pop("name")

        master_agent_uid = UUID(d.pop("masterAgentUid"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _location_uid = d.pop("locationUid", UNSET)
        location_uid: Union[Unset, UUID]
        if isinstance(_location_uid, Unset):
            location_uid = UNSET
        else:
            location_uid = UUID(_location_uid)

        _company_uid = d.pop("companyUid", UNSET)
        company_uid: Union[Unset, UUID]
        if isinstance(_company_uid, Unset):
            company_uid = UNSET
        else:
            company_uid = UUID(_company_uid)

        _system_type = d.pop("systemType", UNSET)
        system_type: Union[Unset, DiscoveryRuleSystemType]
        if isinstance(_system_type, Unset):
            system_type = UNSET
        else:
            system_type = DiscoveryRuleSystemType(_system_type)

        _status = d.pop("status", UNSET)
        status: Union[Unset, DiscoveryRuleStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DiscoveryRuleStatus(_status)

        def _parse_last_run(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_run_type_0 = isoparse(data)

                return last_run_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_run = _parse_last_run(d.pop("lastRun", UNSET))

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

        _schedule_settings = d.pop("scheduleSettings", UNSET)
        schedule_settings: Union[Unset, DiscoveryRuleScheduleSettings]
        if isinstance(_schedule_settings, Unset):
            schedule_settings = UNSET
        else:
            schedule_settings = DiscoveryRuleScheduleSettings.from_dict(_schedule_settings)

        total_computers_count = d.pop("totalComputersCount", UNSET)

        online_computers_count = d.pop("onlineComputersCount", UNSET)

        offline_computers_count = d.pop("offlineComputersCount", UNSET)

        discovery_rule = cls(
            name=name,
            master_agent_uid=master_agent_uid,
            instance_uid=instance_uid,
            location_uid=location_uid,
            company_uid=company_uid,
            system_type=system_type,
            status=status,
            last_run=last_run,
            filter_=filter_,
            notification_settings=notification_settings,
            schedule_settings=schedule_settings,
            total_computers_count=total_computers_count,
            online_computers_count=online_computers_count,
            offline_computers_count=offline_computers_count,
        )

        discovery_rule.additional_properties = d
        return discovery_rule

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
