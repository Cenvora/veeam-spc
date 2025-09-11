from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerBackupJobGuestInteractionProxiesSettings")


@_attrs_define
class BackupServerBackupJobGuestInteractionProxiesSettings:
    """Interaction proxy settings.

    Attributes:
        auto_selection (bool): Indicates whether Veeam Backup & Replication automatically selects the guest interaction
            proxy.
        proxy_ids (Union[Unset, list[UUID]]): Array of UIDs assigned to servers that you want to use as interaction
            proxies.
    """

    auto_selection: bool
    proxy_ids: Union[Unset, list[UUID]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_selection = self.auto_selection

        proxy_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.proxy_ids, Unset):
            proxy_ids = []
            for proxy_ids_item_data in self.proxy_ids:
                proxy_ids_item = str(proxy_ids_item_data)
                proxy_ids.append(proxy_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "autoSelection": auto_selection,
            }
        )
        if proxy_ids is not UNSET:
            field_dict["proxyIds"] = proxy_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_selection = d.pop("autoSelection")

        proxy_ids = []
        _proxy_ids = d.pop("proxyIds", UNSET)
        for proxy_ids_item_data in _proxy_ids or []:
            proxy_ids_item = UUID(proxy_ids_item_data)

            proxy_ids.append(proxy_ids_item)

        backup_server_backup_job_guest_interaction_proxies_settings = cls(
            auto_selection=auto_selection,
            proxy_ids=proxy_ids,
        )

        backup_server_backup_job_guest_interaction_proxies_settings.additional_properties = d
        return backup_server_backup_job_guest_interaction_proxies_settings

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
