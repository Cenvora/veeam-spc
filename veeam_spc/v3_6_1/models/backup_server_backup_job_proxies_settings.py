from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerBackupJobProxiesSettings")


@_attrs_define
class BackupServerBackupJobProxiesSettings:
    """Backup proxy settings.

    Attributes:
        auto_selection (bool): Indicates whether backup proxies are detected and assigned automatically. Default: True.
        proxy_ids (Union[None, Unset, list[UUID]]): Array of UIDs assigned to a backup proxy.
    """

    auto_selection: bool = True
    proxy_ids: Union[None, Unset, list[UUID]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_selection = self.auto_selection

        proxy_ids: Union[None, Unset, list[str]]
        if isinstance(self.proxy_ids, Unset):
            proxy_ids = UNSET
        elif isinstance(self.proxy_ids, list):
            proxy_ids = []
            for proxy_ids_type_0_item_data in self.proxy_ids:
                proxy_ids_type_0_item = str(proxy_ids_type_0_item_data)
                proxy_ids.append(proxy_ids_type_0_item)

        else:
            proxy_ids = self.proxy_ids

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

        def _parse_proxy_ids(data: object) -> Union[None, Unset, list[UUID]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                proxy_ids_type_0 = []
                _proxy_ids_type_0 = data
                for proxy_ids_type_0_item_data in _proxy_ids_type_0:
                    proxy_ids_type_0_item = UUID(proxy_ids_type_0_item_data)

                    proxy_ids_type_0.append(proxy_ids_type_0_item)

                return proxy_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[UUID]], data)

        proxy_ids = _parse_proxy_ids(d.pop("proxyIds", UNSET))

        backup_server_backup_job_proxies_settings = cls(
            auto_selection=auto_selection,
            proxy_ids=proxy_ids,
        )

        backup_server_backup_job_proxies_settings.additional_properties = d
        return backup_server_backup_job_proxies_settings

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
