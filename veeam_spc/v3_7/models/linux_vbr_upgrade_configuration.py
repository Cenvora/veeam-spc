from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinuxVbrUpgradeConfiguration")


@_attrs_define
class LinuxVbrUpgradeConfiguration:
    """Configuration for upgrading Veeam Backup & Replication on a Linux server.

    Example:
        {'updateIds': ['3f8a9c41-2d57-4e0b-9a1c-6b2f8d3e7a04', 'c1d4e9b2-7a36-4f81-b5e0-9d2a6c4f1e83'],
            'stopAllActivities': True}

    Attributes:
        update_ids (list[UUID]): List of VeeamUpdater update identifiers to install.
        stop_all_activities (bool | Unset): If `true`, all backup jobs and activities will be terminated before upgrade.
    """

    update_ids: list[UUID]
    stop_all_activities: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        update_ids = []
        for update_ids_item_data in self.update_ids:
            update_ids_item = str(update_ids_item_data)
            update_ids.append(update_ids_item)

        stop_all_activities = self.stop_all_activities

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "updateIds": update_ids,
            }
        )
        if stop_all_activities is not UNSET:
            field_dict["stopAllActivities"] = stop_all_activities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        update_ids = []
        _update_ids = d.pop("updateIds")
        for update_ids_item_data in _update_ids:
            update_ids_item = UUID(update_ids_item_data)

            update_ids.append(update_ids_item)

        stop_all_activities = d.pop("stopAllActivities", UNSET)

        linux_vbr_upgrade_configuration = cls(
            update_ids=update_ids,
            stop_all_activities=stop_all_activities,
        )

        linux_vbr_upgrade_configuration.additional_properties = d
        return linux_vbr_upgrade_configuration

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
