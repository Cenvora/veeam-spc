from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.deploy_schedule import DeploySchedule
    from ..models.linux_vbr_upgrade_configuration import LinuxVbrUpgradeConfiguration


T = TypeVar("T", bound="LinuxVbrScheduledUpgradeConfiguration")


@_attrs_define
class LinuxVbrScheduledUpgradeConfiguration:
    """Configuration for scheduling Veeam Backup & Replication on a Linux server upgrade.

    Example:
        {'configuration': {'updateIds': ['7d9f1c2a-3b84-4e5d-9a16-2c8e1f0b4d63',
            'f3a6c10b-58d2-4e71-bc94-0a7e9d23f815'], 'stopAllActivities': True}, 'schedule': {'dateTime':
            '2026-07-14T22:00:00-05:00'}}

    Attributes:
        configuration (LinuxVbrUpgradeConfiguration): Configuration for upgrading Veeam Backup & Replication on a Linux
            server. Example: {'updateIds': ['3f8a9c41-2d57-4e0b-9a1c-6b2f8d3e7a04', 'c1d4e9b2-7a36-4f81-b5e0-9d2a6c4f1e83'],
            'stopAllActivities': True}.
        schedule (DeploySchedule):
    """

    configuration: LinuxVbrUpgradeConfiguration
    schedule: DeploySchedule
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration = self.configuration.to_dict()

        schedule = self.schedule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configuration": configuration,
                "schedule": schedule,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deploy_schedule import DeploySchedule
        from ..models.linux_vbr_upgrade_configuration import LinuxVbrUpgradeConfiguration

        d = dict(src_dict)
        configuration = LinuxVbrUpgradeConfiguration.from_dict(d.pop("configuration"))

        schedule = DeploySchedule.from_dict(d.pop("schedule"))

        linux_vbr_scheduled_upgrade_configuration = cls(
            configuration=configuration,
            schedule=schedule,
        )

        linux_vbr_scheduled_upgrade_configuration.additional_properties = d
        return linux_vbr_scheduled_upgrade_configuration

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
