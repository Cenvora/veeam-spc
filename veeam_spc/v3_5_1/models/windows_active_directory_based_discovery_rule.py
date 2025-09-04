from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.windows_active_directory_based_discovery_rule_ad_method import (
    WindowsActiveDirectoryBasedDiscoveryRuleAdMethod,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedded_for_windows_discovery_rule_children import EmbeddedForWindowsDiscoveryRuleChildren


T = TypeVar("T", bound="WindowsActiveDirectoryBasedDiscoveryRule")


@_attrs_define
class WindowsActiveDirectoryBasedDiscoveryRule:
    """
    Attributes:
        ad_method (WindowsActiveDirectoryBasedDiscoveryRuleAdMethod): Microsoft Entra ID discovery method.
        instance_uid (Union[Unset, UUID]): UID assigned to an Microsoft Entra ID discovery rule.
        custom_query (Union[Unset, str]): LDAP query that returns a list of computers to scan.
        skip_offline_computers_days (Union[Unset, int]): Number of days for which offline computers are skipped from
            discovery.
        field_embedded (Union[Unset, EmbeddedForWindowsDiscoveryRuleChildren]): Resource representation of the related
            Windows discovery rule entity.
    """

    ad_method: WindowsActiveDirectoryBasedDiscoveryRuleAdMethod
    instance_uid: Union[Unset, UUID] = UNSET
    custom_query: Union[Unset, str] = UNSET
    skip_offline_computers_days: Union[Unset, int] = UNSET
    field_embedded: Union[Unset, "EmbeddedForWindowsDiscoveryRuleChildren"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ad_method = self.ad_method.value

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        custom_query = self.custom_query

        skip_offline_computers_days = self.skip_offline_computers_days

        field_embedded: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_embedded, Unset):
            field_embedded = self.field_embedded.to_dict()

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
        from ..models.embedded_for_windows_discovery_rule_children import EmbeddedForWindowsDiscoveryRuleChildren

        d = dict(src_dict)
        ad_method = WindowsActiveDirectoryBasedDiscoveryRuleAdMethod(d.pop("adMethod"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        custom_query = d.pop("customQuery", UNSET)

        skip_offline_computers_days = d.pop("skipOfflineComputersDays", UNSET)

        _field_embedded = d.pop("_embedded", UNSET)
        field_embedded: Union[Unset, EmbeddedForWindowsDiscoveryRuleChildren]
        if isinstance(_field_embedded, Unset):
            field_embedded = UNSET
        else:
            field_embedded = EmbeddedForWindowsDiscoveryRuleChildren.from_dict(_field_embedded)

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
