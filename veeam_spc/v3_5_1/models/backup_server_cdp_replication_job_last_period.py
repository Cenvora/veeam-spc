from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_cdp_replication_job_last_period_bottleneck import (
    BackupServerCdpReplicationJobLastPeriodBottleneck,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerCdpReplicationJobLastPeriod")


@_attrs_define
class BackupServerCdpReplicationJobLastPeriod:
    """
    Attributes:
        success_count (Union[Unset, int]): Number of task sessions completed with the `Success` status.
        warning_count (Union[Unset, int]): Number of task sessions completed with the `Warning` status.
        errors_count (Union[Unset, int]): Number of task sessions completed with the `Error` status.
        average_data (Union[None, Unset, int]): Avarage amount of data processed during the synchronization session, in
            kilobytes.
        maximum_data (Union[None, Unset, int]): Maximum amount of data processed during the synchronization session, in
            kilobytes.
        total_data (Union[None, Unset, int]): Total size of data processed during the synchronization session, in
            kilobytes.
        average_duration (Union[None, Unset, int]): Average duration of a syncronization session, in seconds.
        maximum_duration (Union[None, Unset, int]): Maximum duration of a syncronization session, in seconds.
        sync_interval (Union[None, Unset, int]): Duration of a synchronization session configured in the policy, in
            seconds.
        sla (Union[None, Unset, int]): Percentage of sessions completed within the configured RPO.
        max_delay (Union[None, Unset, int]): Difference between the configured RPO and time required to transfer and
            save data, in seconds.
        bottleneck (Union[Unset, BackupServerCdpReplicationJobLastPeriodBottleneck]): Bottleneck in the data
            transmission process.
    """

    success_count: Union[Unset, int] = UNSET
    warning_count: Union[Unset, int] = UNSET
    errors_count: Union[Unset, int] = UNSET
    average_data: Union[None, Unset, int] = UNSET
    maximum_data: Union[None, Unset, int] = UNSET
    total_data: Union[None, Unset, int] = UNSET
    average_duration: Union[None, Unset, int] = UNSET
    maximum_duration: Union[None, Unset, int] = UNSET
    sync_interval: Union[None, Unset, int] = UNSET
    sla: Union[None, Unset, int] = UNSET
    max_delay: Union[None, Unset, int] = UNSET
    bottleneck: Union[Unset, BackupServerCdpReplicationJobLastPeriodBottleneck] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success_count = self.success_count

        warning_count = self.warning_count

        errors_count = self.errors_count

        average_data: Union[None, Unset, int]
        if isinstance(self.average_data, Unset):
            average_data = UNSET
        else:
            average_data = self.average_data

        maximum_data: Union[None, Unset, int]
        if isinstance(self.maximum_data, Unset):
            maximum_data = UNSET
        else:
            maximum_data = self.maximum_data

        total_data: Union[None, Unset, int]
        if isinstance(self.total_data, Unset):
            total_data = UNSET
        else:
            total_data = self.total_data

        average_duration: Union[None, Unset, int]
        if isinstance(self.average_duration, Unset):
            average_duration = UNSET
        else:
            average_duration = self.average_duration

        maximum_duration: Union[None, Unset, int]
        if isinstance(self.maximum_duration, Unset):
            maximum_duration = UNSET
        else:
            maximum_duration = self.maximum_duration

        sync_interval: Union[None, Unset, int]
        if isinstance(self.sync_interval, Unset):
            sync_interval = UNSET
        else:
            sync_interval = self.sync_interval

        sla: Union[None, Unset, int]
        if isinstance(self.sla, Unset):
            sla = UNSET
        else:
            sla = self.sla

        max_delay: Union[None, Unset, int]
        if isinstance(self.max_delay, Unset):
            max_delay = UNSET
        else:
            max_delay = self.max_delay

        bottleneck: Union[Unset, str] = UNSET
        if not isinstance(self.bottleneck, Unset):
            bottleneck = self.bottleneck.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success_count is not UNSET:
            field_dict["successCount"] = success_count
        if warning_count is not UNSET:
            field_dict["warningCount"] = warning_count
        if errors_count is not UNSET:
            field_dict["errorsCount"] = errors_count
        if average_data is not UNSET:
            field_dict["averageData"] = average_data
        if maximum_data is not UNSET:
            field_dict["maximumData"] = maximum_data
        if total_data is not UNSET:
            field_dict["totalData"] = total_data
        if average_duration is not UNSET:
            field_dict["averageDuration"] = average_duration
        if maximum_duration is not UNSET:
            field_dict["maximumDuration"] = maximum_duration
        if sync_interval is not UNSET:
            field_dict["syncInterval"] = sync_interval
        if sla is not UNSET:
            field_dict["sla"] = sla
        if max_delay is not UNSET:
            field_dict["maxDelay"] = max_delay
        if bottleneck is not UNSET:
            field_dict["bottleneck"] = bottleneck

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success_count = d.pop("successCount", UNSET)

        warning_count = d.pop("warningCount", UNSET)

        errors_count = d.pop("errorsCount", UNSET)

        def _parse_average_data(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        average_data = _parse_average_data(d.pop("averageData", UNSET))

        def _parse_maximum_data(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        maximum_data = _parse_maximum_data(d.pop("maximumData", UNSET))

        def _parse_total_data(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_data = _parse_total_data(d.pop("totalData", UNSET))

        def _parse_average_duration(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        average_duration = _parse_average_duration(d.pop("averageDuration", UNSET))

        def _parse_maximum_duration(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        maximum_duration = _parse_maximum_duration(d.pop("maximumDuration", UNSET))

        def _parse_sync_interval(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        sync_interval = _parse_sync_interval(d.pop("syncInterval", UNSET))

        def _parse_sla(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        sla = _parse_sla(d.pop("sla", UNSET))

        def _parse_max_delay(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_delay = _parse_max_delay(d.pop("maxDelay", UNSET))

        _bottleneck = d.pop("bottleneck", UNSET)
        bottleneck: Union[Unset, BackupServerCdpReplicationJobLastPeriodBottleneck]
        if isinstance(_bottleneck, Unset):
            bottleneck = UNSET
        else:
            bottleneck = BackupServerCdpReplicationJobLastPeriodBottleneck(_bottleneck)

        backup_server_cdp_replication_job_last_period = cls(
            success_count=success_count,
            warning_count=warning_count,
            errors_count=errors_count,
            average_data=average_data,
            maximum_data=maximum_data,
            total_data=total_data,
            average_duration=average_duration,
            maximum_duration=maximum_duration,
            sync_interval=sync_interval,
            sla=sla,
            max_delay=max_delay,
            bottleneck=bottleneck,
        )

        backup_server_cdp_replication_job_last_period.additional_properties = d
        return backup_server_cdp_replication_job_last_period

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
