from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.discovery_rule_filter_applications_type_0_item import DiscoveryRuleFilterApplicationsType0Item
from ..models.discovery_rule_filter_os_types_type_0_item import DiscoveryRuleFilterOsTypesType0Item
from ..models.discovery_rule_filter_platforms_type_0_item import DiscoveryRuleFilterPlatformsType0Item
from ..types import UNSET, Unset

T = TypeVar("T", bound="DiscoveryRuleFilter")


@_attrs_define
class DiscoveryRuleFilter:
    """
    Attributes:
        exclusion_mask (Union[None, Unset, list[str]]): Array of applied exclusion masks. For custom discovery rules
            this property is ignored.
        ignore_inaccessible_machine (Union[Unset, bool]): Indicates whether discovery is performed among accessible
            computers only. Default: False.
        os_types (Union[None, Unset, list[DiscoveryRuleFilterOsTypesType0Item]]): Type of operating system.
        applications (Union[None, Unset, list[DiscoveryRuleFilterApplicationsType0Item]]): Applications that must run on
            discovered computers.
        custom_application (Union[None, Unset, str]): Name of an application required for the `OtherApp` application
            type.
            > Available only for Linux computers.
        platforms (Union[None, Unset, list[DiscoveryRuleFilterPlatformsType0Item]]): Platforms on which discovered
            computers must run.
    """

    exclusion_mask: Union[None, Unset, list[str]] = UNSET
    ignore_inaccessible_machine: Union[Unset, bool] = False
    os_types: Union[None, Unset, list[DiscoveryRuleFilterOsTypesType0Item]] = UNSET
    applications: Union[None, Unset, list[DiscoveryRuleFilterApplicationsType0Item]] = UNSET
    custom_application: Union[None, Unset, str] = UNSET
    platforms: Union[None, Unset, list[DiscoveryRuleFilterPlatformsType0Item]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exclusion_mask: Union[None, Unset, list[str]]
        if isinstance(self.exclusion_mask, Unset):
            exclusion_mask = UNSET
        elif isinstance(self.exclusion_mask, list):
            exclusion_mask = self.exclusion_mask

        else:
            exclusion_mask = self.exclusion_mask

        ignore_inaccessible_machine = self.ignore_inaccessible_machine

        os_types: Union[None, Unset, list[str]]
        if isinstance(self.os_types, Unset):
            os_types = UNSET
        elif isinstance(self.os_types, list):
            os_types = []
            for os_types_type_0_item_data in self.os_types:
                os_types_type_0_item = os_types_type_0_item_data.value
                os_types.append(os_types_type_0_item)

        else:
            os_types = self.os_types

        applications: Union[None, Unset, list[str]]
        if isinstance(self.applications, Unset):
            applications = UNSET
        elif isinstance(self.applications, list):
            applications = []
            for applications_type_0_item_data in self.applications:
                applications_type_0_item = applications_type_0_item_data.value
                applications.append(applications_type_0_item)

        else:
            applications = self.applications

        custom_application: Union[None, Unset, str]
        if isinstance(self.custom_application, Unset):
            custom_application = UNSET
        else:
            custom_application = self.custom_application

        platforms: Union[None, Unset, list[str]]
        if isinstance(self.platforms, Unset):
            platforms = UNSET
        elif isinstance(self.platforms, list):
            platforms = []
            for platforms_type_0_item_data in self.platforms:
                platforms_type_0_item = platforms_type_0_item_data.value
                platforms.append(platforms_type_0_item)

        else:
            platforms = self.platforms

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

        def _parse_exclusion_mask(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclusion_mask_type_0 = cast(list[str], data)

                return exclusion_mask_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        exclusion_mask = _parse_exclusion_mask(d.pop("exclusionMask", UNSET))

        ignore_inaccessible_machine = d.pop("ignoreInaccessibleMachine", UNSET)

        def _parse_os_types(data: object) -> Union[None, Unset, list[DiscoveryRuleFilterOsTypesType0Item]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                os_types_type_0 = []
                _os_types_type_0 = data
                for os_types_type_0_item_data in _os_types_type_0:
                    os_types_type_0_item = DiscoveryRuleFilterOsTypesType0Item(os_types_type_0_item_data)

                    os_types_type_0.append(os_types_type_0_item)

                return os_types_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[DiscoveryRuleFilterOsTypesType0Item]], data)

        os_types = _parse_os_types(d.pop("osTypes", UNSET))

        def _parse_applications(data: object) -> Union[None, Unset, list[DiscoveryRuleFilterApplicationsType0Item]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                applications_type_0 = []
                _applications_type_0 = data
                for applications_type_0_item_data in _applications_type_0:
                    applications_type_0_item = DiscoveryRuleFilterApplicationsType0Item(applications_type_0_item_data)

                    applications_type_0.append(applications_type_0_item)

                return applications_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[DiscoveryRuleFilterApplicationsType0Item]], data)

        applications = _parse_applications(d.pop("applications", UNSET))

        def _parse_custom_application(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        custom_application = _parse_custom_application(d.pop("customApplication", UNSET))

        def _parse_platforms(data: object) -> Union[None, Unset, list[DiscoveryRuleFilterPlatformsType0Item]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                platforms_type_0 = []
                _platforms_type_0 = data
                for platforms_type_0_item_data in _platforms_type_0:
                    platforms_type_0_item = DiscoveryRuleFilterPlatformsType0Item(platforms_type_0_item_data)

                    platforms_type_0.append(platforms_type_0_item)

                return platforms_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[DiscoveryRuleFilterPlatformsType0Item]], data)

        platforms = _parse_platforms(d.pop("platforms", UNSET))

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
