from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_cdp_replication_job_last_day_bottleneck import (
    BackupServerCdpReplicationJobLastDayBottleneck,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerCdpReplicationJobLastDay")


@_attrs_define
class BackupServerCdpReplicationJobLastDay:
    """
    Attributes:
        success_count (int | Unset): Number of task sessions that have completed with the `Success` status.
        warning_count (int | Unset): Number of task sessions that have completed with the `Warning` status.
        errors_count (int | Unset): Number of task sessions that have completed with the `Error` status.
        total_size (int | None | Unset): Total size of the processed data, in kilobytes.
        read_data (int | None | Unset): Amount of data read from the datastore prior to applying compression and
            deduplication, in kilobytes.
        transferred_data (int | None | Unset): Amount of data transferred from the source proxy to the target proxy, in
            kilobytes.
        sla (int | None | Unset): Percentage of sessions completed within the configured RPO.
        max_delay (int | None | Unset): Difference between the configured RPO and time required to transfer and save
            data.
        bottleneck (BackupServerCdpReplicationJobLastDayBottleneck | Unset): Bottleneck in the data transmission
            process.
    """

    success_count: int | Unset = UNSET
    warning_count: int | Unset = UNSET
    errors_count: int | Unset = UNSET
    total_size: int | None | Unset = UNSET
    read_data: int | None | Unset = UNSET
    transferred_data: int | None | Unset = UNSET
    sla: int | None | Unset = UNSET
    max_delay: int | None | Unset = UNSET
    bottleneck: BackupServerCdpReplicationJobLastDayBottleneck | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success_count = self.success_count

        warning_count = self.warning_count

        errors_count = self.errors_count

        total_size: int | None | Unset
        if isinstance(self.total_size, Unset):
            total_size = UNSET
        else:
            total_size = self.total_size

        read_data: int | None | Unset
        if isinstance(self.read_data, Unset):
            read_data = UNSET
        else:
            read_data = self.read_data

        transferred_data: int | None | Unset
        if isinstance(self.transferred_data, Unset):
            transferred_data = UNSET
        else:
            transferred_data = self.transferred_data

        sla: int | None | Unset
        if isinstance(self.sla, Unset):
            sla = UNSET
        else:
            sla = self.sla

        max_delay: int | None | Unset
        if isinstance(self.max_delay, Unset):
            max_delay = UNSET
        else:
            max_delay = self.max_delay

        bottleneck: str | Unset = UNSET
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
        if total_size is not UNSET:
            field_dict["totalSize"] = total_size
        if read_data is not UNSET:
            field_dict["readData"] = read_data
        if transferred_data is not UNSET:
            field_dict["transferredData"] = transferred_data
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

        def _parse_total_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_size = _parse_total_size(d.pop("totalSize", UNSET))

        def _parse_read_data(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        read_data = _parse_read_data(d.pop("readData", UNSET))

        def _parse_transferred_data(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        transferred_data = _parse_transferred_data(d.pop("transferredData", UNSET))

        def _parse_sla(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sla = _parse_sla(d.pop("sla", UNSET))

        def _parse_max_delay(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_delay = _parse_max_delay(d.pop("maxDelay", UNSET))

        _bottleneck = d.pop("bottleneck", UNSET)
        bottleneck: BackupServerCdpReplicationJobLastDayBottleneck | Unset
        if isinstance(_bottleneck, Unset):
            bottleneck = UNSET
        else:
            bottleneck = BackupServerCdpReplicationJobLastDayBottleneck(_bottleneck)

        backup_server_cdp_replication_job_last_day = cls(
            success_count=success_count,
            warning_count=warning_count,
            errors_count=errors_count,
            total_size=total_size,
            read_data=read_data,
            transferred_data=transferred_data,
            sla=sla,
            max_delay=max_delay,
            bottleneck=bottleneck,
        )

        backup_server_cdp_replication_job_last_day.additional_properties = d
        return backup_server_cdp_replication_job_last_day

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
