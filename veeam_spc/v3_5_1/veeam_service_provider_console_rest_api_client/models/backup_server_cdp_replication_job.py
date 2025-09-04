from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_cdp_replication_job_long_term_retention_unit import (
    BackupServerCdpReplicationJobLongTermRetentionUnit,
)
from ..models.backup_server_cdp_replication_job_rpo_unit import BackupServerCdpReplicationJobRpoUnit
from ..models.backup_server_cdp_replication_job_short_term_retention_unit import (
    BackupServerCdpReplicationJobShortTermRetentionUnit,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_cdp_replication_job_last_day import BackupServerCdpReplicationJobLastDay
    from ..models.backup_server_cdp_replication_job_last_period import BackupServerCdpReplicationJobLastPeriod
    from ..models.embedded_for_backup_server_job_children_type_0 import EmbeddedForBackupServerJobChildrenType0


T = TypeVar("T", bound="BackupServerCdpReplicationJob")


@_attrs_define
class BackupServerCdpReplicationJob:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Backup & Replication.
        unique_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Service Provider Console.
        rpo (Union[Unset, int]): RPO value.
        rpo_unit (Union[Unset, BackupServerCdpReplicationJobRpoUnit]): RPO measurement units.
        short_term_retention (Union[Unset, int]): Short-term retention value.
        short_term_retention_unit (Union[Unset, BackupServerCdpReplicationJobShortTermRetentionUnit]): Short-term
            retention measurement units.
        long_term_retention (Union[Unset, int]): Long-term retention value.
        long_term_retention_unit (Union[Unset, BackupServerCdpReplicationJobLongTermRetentionUnit]): Long-term retention
            measurement units.
        field_embedded (Union['EmbeddedForBackupServerJobChildrenType0', None, Unset]): Resource representation of the
            related Veeam Backup & Replication server job entity.
        keep_restore_points_in_days (Union[Unset, int]): Number of days for which long-term retention points must be
            retained.
        source_proxy_auto_detect (Union[Unset, bool]): Indicates whether Veeam Backup & Replication must select a source
            proxy automatically.
        target_proxy_auto_detect (Union[Unset, bool]): Indicates whether Veeam Backup & Replication must select a target
            proxy automatically.
        is_application_aware_enabled (Union[Unset, bool]): Indicates whether the application-aware processing is
            enabled.
        last_period (Union[Unset, BackupServerCdpReplicationJobLastPeriod]):
        last_day (Union[Unset, BackupServerCdpReplicationJobLastDay]):
    """

    instance_uid: Union[Unset, UUID] = UNSET
    unique_uid: Union[Unset, UUID] = UNSET
    rpo: Union[Unset, int] = UNSET
    rpo_unit: Union[Unset, BackupServerCdpReplicationJobRpoUnit] = UNSET
    short_term_retention: Union[Unset, int] = UNSET
    short_term_retention_unit: Union[Unset, BackupServerCdpReplicationJobShortTermRetentionUnit] = UNSET
    long_term_retention: Union[Unset, int] = UNSET
    long_term_retention_unit: Union[Unset, BackupServerCdpReplicationJobLongTermRetentionUnit] = UNSET
    field_embedded: Union["EmbeddedForBackupServerJobChildrenType0", None, Unset] = UNSET
    keep_restore_points_in_days: Union[Unset, int] = UNSET
    source_proxy_auto_detect: Union[Unset, bool] = UNSET
    target_proxy_auto_detect: Union[Unset, bool] = UNSET
    is_application_aware_enabled: Union[Unset, bool] = UNSET
    last_period: Union[Unset, "BackupServerCdpReplicationJobLastPeriod"] = UNSET
    last_day: Union[Unset, "BackupServerCdpReplicationJobLastDay"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.embedded_for_backup_server_job_children_type_0 import EmbeddedForBackupServerJobChildrenType0

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        unique_uid: Union[Unset, str] = UNSET
        if not isinstance(self.unique_uid, Unset):
            unique_uid = str(self.unique_uid)

        rpo = self.rpo

        rpo_unit: Union[Unset, str] = UNSET
        if not isinstance(self.rpo_unit, Unset):
            rpo_unit = self.rpo_unit.value

        short_term_retention = self.short_term_retention

        short_term_retention_unit: Union[Unset, str] = UNSET
        if not isinstance(self.short_term_retention_unit, Unset):
            short_term_retention_unit = self.short_term_retention_unit.value

        long_term_retention = self.long_term_retention

        long_term_retention_unit: Union[Unset, str] = UNSET
        if not isinstance(self.long_term_retention_unit, Unset):
            long_term_retention_unit = self.long_term_retention_unit.value

        field_embedded: Union[None, Unset, dict[str, Any]]
        if isinstance(self.field_embedded, Unset):
            field_embedded = UNSET
        elif isinstance(self.field_embedded, EmbeddedForBackupServerJobChildrenType0):
            field_embedded = self.field_embedded.to_dict()
        else:
            field_embedded = self.field_embedded

        keep_restore_points_in_days = self.keep_restore_points_in_days

        source_proxy_auto_detect = self.source_proxy_auto_detect

        target_proxy_auto_detect = self.target_proxy_auto_detect

        is_application_aware_enabled = self.is_application_aware_enabled

        last_period: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_period, Unset):
            last_period = self.last_period.to_dict()

        last_day: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_day, Unset):
            last_day = self.last_day.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if unique_uid is not UNSET:
            field_dict["uniqueUid"] = unique_uid
        if rpo is not UNSET:
            field_dict["rpo"] = rpo
        if rpo_unit is not UNSET:
            field_dict["rpoUnit"] = rpo_unit
        if short_term_retention is not UNSET:
            field_dict["shortTermRetention"] = short_term_retention
        if short_term_retention_unit is not UNSET:
            field_dict["shortTermRetentionUnit"] = short_term_retention_unit
        if long_term_retention is not UNSET:
            field_dict["longTermRetention"] = long_term_retention
        if long_term_retention_unit is not UNSET:
            field_dict["longTermRetentionUnit"] = long_term_retention_unit
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded
        if keep_restore_points_in_days is not UNSET:
            field_dict["keepRestorePointsInDays"] = keep_restore_points_in_days
        if source_proxy_auto_detect is not UNSET:
            field_dict["sourceProxyAutoDetect"] = source_proxy_auto_detect
        if target_proxy_auto_detect is not UNSET:
            field_dict["targetProxyAutoDetect"] = target_proxy_auto_detect
        if is_application_aware_enabled is not UNSET:
            field_dict["isApplicationAwareEnabled"] = is_application_aware_enabled
        if last_period is not UNSET:
            field_dict["lastPeriod"] = last_period
        if last_day is not UNSET:
            field_dict["lastDay"] = last_day

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_cdp_replication_job_last_day import BackupServerCdpReplicationJobLastDay
        from ..models.backup_server_cdp_replication_job_last_period import BackupServerCdpReplicationJobLastPeriod
        from ..models.embedded_for_backup_server_job_children_type_0 import EmbeddedForBackupServerJobChildrenType0

        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _unique_uid = d.pop("uniqueUid", UNSET)
        unique_uid: Union[Unset, UUID]
        if isinstance(_unique_uid, Unset):
            unique_uid = UNSET
        else:
            unique_uid = UUID(_unique_uid)

        rpo = d.pop("rpo", UNSET)

        _rpo_unit = d.pop("rpoUnit", UNSET)
        rpo_unit: Union[Unset, BackupServerCdpReplicationJobRpoUnit]
        if isinstance(_rpo_unit, Unset):
            rpo_unit = UNSET
        else:
            rpo_unit = BackupServerCdpReplicationJobRpoUnit(_rpo_unit)

        short_term_retention = d.pop("shortTermRetention", UNSET)

        _short_term_retention_unit = d.pop("shortTermRetentionUnit", UNSET)
        short_term_retention_unit: Union[Unset, BackupServerCdpReplicationJobShortTermRetentionUnit]
        if isinstance(_short_term_retention_unit, Unset):
            short_term_retention_unit = UNSET
        else:
            short_term_retention_unit = BackupServerCdpReplicationJobShortTermRetentionUnit(_short_term_retention_unit)

        long_term_retention = d.pop("longTermRetention", UNSET)

        _long_term_retention_unit = d.pop("longTermRetentionUnit", UNSET)
        long_term_retention_unit: Union[Unset, BackupServerCdpReplicationJobLongTermRetentionUnit]
        if isinstance(_long_term_retention_unit, Unset):
            long_term_retention_unit = UNSET
        else:
            long_term_retention_unit = BackupServerCdpReplicationJobLongTermRetentionUnit(_long_term_retention_unit)

        def _parse_field_embedded(data: object) -> Union["EmbeddedForBackupServerJobChildrenType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_embedded_for_backup_server_job_children_type_0 = (
                    EmbeddedForBackupServerJobChildrenType0.from_dict(data)
                )

                return componentsschemas_embedded_for_backup_server_job_children_type_0
            except:  # noqa: E722
                pass
            return cast(Union["EmbeddedForBackupServerJobChildrenType0", None, Unset], data)

        field_embedded = _parse_field_embedded(d.pop("_embedded", UNSET))

        keep_restore_points_in_days = d.pop("keepRestorePointsInDays", UNSET)

        source_proxy_auto_detect = d.pop("sourceProxyAutoDetect", UNSET)

        target_proxy_auto_detect = d.pop("targetProxyAutoDetect", UNSET)

        is_application_aware_enabled = d.pop("isApplicationAwareEnabled", UNSET)

        _last_period = d.pop("lastPeriod", UNSET)
        last_period: Union[Unset, BackupServerCdpReplicationJobLastPeriod]
        if isinstance(_last_period, Unset):
            last_period = UNSET
        else:
            last_period = BackupServerCdpReplicationJobLastPeriod.from_dict(_last_period)

        _last_day = d.pop("lastDay", UNSET)
        last_day: Union[Unset, BackupServerCdpReplicationJobLastDay]
        if isinstance(_last_day, Unset):
            last_day = UNSET
        else:
            last_day = BackupServerCdpReplicationJobLastDay.from_dict(_last_day)

        backup_server_cdp_replication_job = cls(
            instance_uid=instance_uid,
            unique_uid=unique_uid,
            rpo=rpo,
            rpo_unit=rpo_unit,
            short_term_retention=short_term_retention,
            short_term_retention_unit=short_term_retention_unit,
            long_term_retention=long_term_retention,
            long_term_retention_unit=long_term_retention_unit,
            field_embedded=field_embedded,
            keep_restore_points_in_days=keep_restore_points_in_days,
            source_proxy_auto_detect=source_proxy_auto_detect,
            target_proxy_auto_detect=target_proxy_auto_detect,
            is_application_aware_enabled=is_application_aware_enabled,
            last_period=last_period,
            last_day=last_day,
        )

        backup_server_cdp_replication_job.additional_properties = d
        return backup_server_cdp_replication_job

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
