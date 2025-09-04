from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_agent_settings_bandwidth_speed_limit_unit import BackupAgentSettingsBandwidthSpeedLimitUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupAgentSettings")


@_attrs_define
class BackupAgentSettings:
    """
    Attributes:
        disable_scheduled_backups (bool): Indicates whether a Veeam backup agent job schedule is disabled.
        disable_control_panel_notification (bool): Indicates whether Control Panel notifications.
        disable_backup_over_metered_connection (bool): Indicates whether backup over metered connections is disabled.
            Default: True.
        disable_schedule_wakeup (bool): Indicates whether a scheduled wake up timer is disabled.
        throttle_backup_activity (bool): Indicates whether Veeam backup agent throttles backup activities when system is
            busy. Default: True.
        restrict_vpn_connections (bool): Indicates whether backup over VPN connections is disabled.
        flr_without_admin_privileges_allowed (bool): Indicates whether file-level restore is available to users that do
            not have administrative privileges.
        backup_agent_uid (Union[Unset, UUID]): UID assigned to a Veeam backup agent.
        limit_bandwidth_consumption (Union[Unset, bool]): Indicates whether bandwidth consumption for backup jobs is
            limited. Default: False.
        bandwidth_speed_limit (Union[Unset, int]): Value of maximum speed for transferring backed-up data.
        bandwidth_speed_limit_unit (Union[Unset, BackupAgentSettingsBandwidthSpeedLimitUnit]): Measurement units of
            maximum speed for transferring backed-up data.
    """

    disable_scheduled_backups: bool
    disable_control_panel_notification: bool
    disable_schedule_wakeup: bool
    restrict_vpn_connections: bool
    flr_without_admin_privileges_allowed: bool
    disable_backup_over_metered_connection: bool = True
    throttle_backup_activity: bool = True
    backup_agent_uid: Union[Unset, UUID] = UNSET
    limit_bandwidth_consumption: Union[Unset, bool] = False
    bandwidth_speed_limit: Union[Unset, int] = UNSET
    bandwidth_speed_limit_unit: Union[Unset, BackupAgentSettingsBandwidthSpeedLimitUnit] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disable_scheduled_backups = self.disable_scheduled_backups

        disable_control_panel_notification = self.disable_control_panel_notification

        disable_backup_over_metered_connection = self.disable_backup_over_metered_connection

        disable_schedule_wakeup = self.disable_schedule_wakeup

        throttle_backup_activity = self.throttle_backup_activity

        restrict_vpn_connections = self.restrict_vpn_connections

        flr_without_admin_privileges_allowed = self.flr_without_admin_privileges_allowed

        backup_agent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_agent_uid, Unset):
            backup_agent_uid = str(self.backup_agent_uid)

        limit_bandwidth_consumption = self.limit_bandwidth_consumption

        bandwidth_speed_limit = self.bandwidth_speed_limit

        bandwidth_speed_limit_unit: Union[Unset, str] = UNSET
        if not isinstance(self.bandwidth_speed_limit_unit, Unset):
            bandwidth_speed_limit_unit = self.bandwidth_speed_limit_unit.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "disableScheduledBackups": disable_scheduled_backups,
                "disableControlPanelNotification": disable_control_panel_notification,
                "disableBackupOverMeteredConnection": disable_backup_over_metered_connection,
                "disableScheduleWakeup": disable_schedule_wakeup,
                "throttleBackupActivity": throttle_backup_activity,
                "restrictVpnConnections": restrict_vpn_connections,
                "flrWithoutAdminPrivilegesAllowed": flr_without_admin_privileges_allowed,
            }
        )
        if backup_agent_uid is not UNSET:
            field_dict["backupAgentUid"] = backup_agent_uid
        if limit_bandwidth_consumption is not UNSET:
            field_dict["limitBandwidthConsumption"] = limit_bandwidth_consumption
        if bandwidth_speed_limit is not UNSET:
            field_dict["bandwidthSpeedLimit"] = bandwidth_speed_limit
        if bandwidth_speed_limit_unit is not UNSET:
            field_dict["bandwidthSpeedLimitUnit"] = bandwidth_speed_limit_unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        disable_scheduled_backups = d.pop("disableScheduledBackups")

        disable_control_panel_notification = d.pop("disableControlPanelNotification")

        disable_backup_over_metered_connection = d.pop("disableBackupOverMeteredConnection")

        disable_schedule_wakeup = d.pop("disableScheduleWakeup")

        throttle_backup_activity = d.pop("throttleBackupActivity")

        restrict_vpn_connections = d.pop("restrictVpnConnections")

        flr_without_admin_privileges_allowed = d.pop("flrWithoutAdminPrivilegesAllowed")

        _backup_agent_uid = d.pop("backupAgentUid", UNSET)
        backup_agent_uid: Union[Unset, UUID]
        if isinstance(_backup_agent_uid, Unset):
            backup_agent_uid = UNSET
        else:
            backup_agent_uid = UUID(_backup_agent_uid)

        limit_bandwidth_consumption = d.pop("limitBandwidthConsumption", UNSET)

        bandwidth_speed_limit = d.pop("bandwidthSpeedLimit", UNSET)

        _bandwidth_speed_limit_unit = d.pop("bandwidthSpeedLimitUnit", UNSET)
        bandwidth_speed_limit_unit: Union[Unset, BackupAgentSettingsBandwidthSpeedLimitUnit]
        if isinstance(_bandwidth_speed_limit_unit, Unset):
            bandwidth_speed_limit_unit = UNSET
        else:
            bandwidth_speed_limit_unit = BackupAgentSettingsBandwidthSpeedLimitUnit(_bandwidth_speed_limit_unit)

        backup_agent_settings = cls(
            disable_scheduled_backups=disable_scheduled_backups,
            disable_control_panel_notification=disable_control_panel_notification,
            disable_backup_over_metered_connection=disable_backup_over_metered_connection,
            disable_schedule_wakeup=disable_schedule_wakeup,
            throttle_backup_activity=throttle_backup_activity,
            restrict_vpn_connections=restrict_vpn_connections,
            flr_without_admin_privileges_allowed=flr_without_admin_privileges_allowed,
            backup_agent_uid=backup_agent_uid,
            limit_bandwidth_consumption=limit_bandwidth_consumption,
            bandwidth_speed_limit=bandwidth_speed_limit,
            bandwidth_speed_limit_unit=bandwidth_speed_limit_unit,
        )

        backup_agent_settings.additional_properties = d
        return backup_agent_settings

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
