from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.discovery_rule_filter_applications_item import DiscoveryRuleFilterApplicationsItem
from ..models.discovery_rule_filter_os_types_item import DiscoveryRuleFilterOsTypesItem
from ..models.discovery_rule_filter_platforms_item import DiscoveryRuleFilterPlatformsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="DiscoveryRuleFilter")


@_attrs_define
class DiscoveryRuleFilter:
    """
    Attributes:
        exclusion_mask (Union[Unset, list[str]]): Array of applied exclusion masks. For custom discovery rules this
            property is ignored.
        ignore_inaccessible_machine (Union[Unset, bool]): Indicates whether discovery is performed among accessible
            computers only. Default: False.
        os_types (Union[Unset, list[DiscoveryRuleFilterOsTypesItem]]): Type of operating system.
        applications (Union[Unset, list[DiscoveryRuleFilterApplicationsItem]]): Applications that must run on discovered
            computers.
        custom_application (Union[Unset, str]): Name of an application required for the `OtherApp` application type.
            > Available only for Linux computers.
        platforms (Union[Unset, list[DiscoveryRuleFilterPlatformsItem]]): Platforms on which discovered computers must
            run.
    """

    exclusion_mask: Union[Unset, list[str]] = UNSET
    ignore_inaccessible_machine: Union[Unset, bool] = False
    os_types: Union[Unset, list[DiscoveryRuleFilterOsTypesItem]] = UNSET
    applications: Union[Unset, list[DiscoveryRuleFilterApplicationsItem]] = UNSET
    custom_application: Union[Unset, str] = UNSET
    platforms: Union[Unset, list[DiscoveryRuleFilterPlatformsItem]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exclusion_mask: Union[Unset, list[str]] = UNSET
        if not isinstance(self.exclusion_mask, Unset):
            exclusion_mask = self.exclusion_mask

        ignore_inaccessible_machine = self.ignore_inaccessible_machine

        os_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.os_types, Unset):
            os_types = []
            for os_types_item_data in self.os_types:
                os_types_item = os_types_item_data.value
                os_types.append(os_types_item)

        applications: Union[Unset, list[str]] = UNSET
        if not isinstance(self.applications, Unset):
            applications = []
            for applications_item_data in self.applications:
                applications_item = applications_item_data.value
                applications.append(applications_item)

        custom_application = self.custom_application

        platforms: Union[Unset, list[str]] = UNSET
        if not isinstance(self.platforms, Unset):
            platforms = []
            for platforms_item_data in self.platforms:
                platforms_item = platforms_item_data.value
                platforms.append(platforms_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exclusion_mask is not UNSET:
            field_dict["exclusionMask"] = exclusion_mask
        if ignore_inaccessible_machine is not UNSET:
            field_dict["ignoreInaccessibleMachine"] = ignore_inaccessible_machine
        if os_types is not UNSET:
            field_dict["osTypes"] = os_types
        if applications is not UNSET:
            field_dict["applications"] = applications
        if custom_application is not UNSET:
            field_dict["customApplication"] = custom_application
        if platforms is not UNSET:
            field_dict["platforms"] = platforms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exclusion_mask = cast(list[str], d.pop("exclusionMask", UNSET))

        ignore_inaccessible_machine = d.pop("ignoreInaccessibleMachine", UNSET)

        os_types = []
        _os_types = d.pop("osTypes", UNSET)
        for os_types_item_data in _os_types or []:
            os_types_item = DiscoveryRuleFilterOsTypesItem(os_types_item_data)

            os_types.append(os_types_item)

        applications = []
        _applications = d.pop("applications", UNSET)
        for applications_item_data in _applications or []:
            applications_item = DiscoveryRuleFilterApplicationsItem(applications_item_data)

            applications.append(applications_item)

        custom_application = d.pop("customApplication", UNSET)

        platforms = []
        _platforms = d.pop("platforms", UNSET)
        for platforms_item_data in _platforms or []:
            platforms_item = DiscoveryRuleFilterPlatformsItem(platforms_item_data)

            platforms.append(platforms_item)

        discovery_rule_filter = cls(
            exclusion_mask=exclusion_mask,
            ignore_inaccessible_machine=ignore_inaccessible_machine,
            os_types=os_types,
            applications=applications,
            custom_application=custom_application,
            platforms=platforms,
        )

        discovery_rule_filter.additional_properties = d
        return discovery_rule_filter

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
