from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.windows_active_directory_based_discovery_rule_ad_method import (
    WindowsActiveDirectoryBasedDiscoveryRuleAdMethod,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedded_for_windows_discovery_rule_children_type_0 import (
        EmbeddedForWindowsDiscoveryRuleChildrenType0,
    )


T = TypeVar("T", bound="WindowsActiveDirectoryBasedDiscoveryRule")


@_attrs_define
class WindowsActiveDirectoryBasedDiscoveryRule:
    """
    Attributes:
        ad_method (WindowsActiveDirectoryBasedDiscoveryRuleAdMethod): Microsoft Entra ID discovery method.
        instance_uid (UUID | Unset): UID assigned to an Microsoft Entra ID discovery rule.
        custom_query (None | str | Unset): LDAP query that returns a list of computers to scan.
        skip_offline_computers_days (int | None | Unset): Number of days for which offline computers are skipped from
            discovery.
        field_embedded (EmbeddedForWindowsDiscoveryRuleChildrenType0 | None | Unset): Resource representation of the
            related Windows discovery rule entity.
    """

    ad_method: WindowsActiveDirectoryBasedDiscoveryRuleAdMethod
    instance_uid: UUID | Unset = UNSET
    custom_query: None | str | Unset = UNSET
    skip_offline_computers_days: int | None | Unset = UNSET
    field_embedded: EmbeddedForWindowsDiscoveryRuleChildrenType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.embedded_for_windows_discovery_rule_children_type_0 import (
            EmbeddedForWindowsDiscoveryRuleChildrenType0,
        )

        ad_method = self.ad_method.value

        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        custom_query: None | str | Unset
        if isinstance(self.custom_query, Unset):
            custom_query = UNSET
        else:
            custom_query = self.custom_query

        skip_offline_computers_days: int | None | Unset
        if isinstance(self.skip_offline_computers_days, Unset):
            skip_offline_computers_days = UNSET
        else:
            skip_offline_computers_days = self.skip_offline_computers_days

        field_embedded: dict[str, Any] | None | Unset
        if isinstance(self.field_embedded, Unset):
            field_embedded = UNSET
        elif isinstance(self.field_embedded, EmbeddedForWindowsDiscoveryRuleChildrenType0):
            field_embedded = self.field_embedded.to_dict()
        else:
            field_embedded = self.field_embedded

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "adMethod": ad_method,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if custom_query is not UNSET:
            field_dict["customQuery"] = custom_query
        if skip_offline_computers_days is not UNSET:
            field_dict["skipOfflineComputersDays"] = skip_offline_computers_days
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedded_for_windows_discovery_rule_children_type_0 import (
            EmbeddedForWindowsDiscoveryRuleChildrenType0,
        )

        d = dict(src_dict)
        ad_method = WindowsActiveDirectoryBasedDiscoveryRuleAdMethod(d.pop("adMethod"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        def _parse_custom_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_query = _parse_custom_query(d.pop("customQuery", UNSET))

        def _parse_skip_offline_computers_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        skip_offline_computers_days = _parse_skip_offline_computers_days(d.pop("skipOfflineComputersDays", UNSET))

        def _parse_field_embedded(data: object) -> EmbeddedForWindowsDiscoveryRuleChildrenType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_embedded_for_windows_discovery_rule_children_type_0 = (
                    EmbeddedForWindowsDiscoveryRuleChildrenType0.from_dict(data)
                )

                return componentsschemas_embedded_for_windows_discovery_rule_children_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EmbeddedForWindowsDiscoveryRuleChildrenType0 | None | Unset, data)

        field_embedded = _parse_field_embedded(d.pop("_embedded", UNSET))

        windows_active_directory_based_discovery_rule = cls(
            ad_method=ad_method,
            instance_uid=instance_uid,
            custom_query=custom_query,
            skip_offline_computers_days=skip_offline_computers_days,
            field_embedded=field_embedded,
        )

        windows_active_directory_based_discovery_rule.additional_properties = d
        return windows_active_directory_based_discovery_rule

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
