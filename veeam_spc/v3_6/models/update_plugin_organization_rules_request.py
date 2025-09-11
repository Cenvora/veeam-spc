from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatePluginOrganizationRulesRequest")


@_attrs_define
class UpdatePluginOrganizationRulesRequest:
    """
    Attributes:
        allow_organization_ids (Union[Unset, list[str]]): Array of IDs assigned to organizations that are permitted to
            access plugin.
        deny_organization_ids (Union[Unset, list[str]]): Array of IDs assigned to organizations that are not permitted
            to access plugin.
        allow_organizations_by_default (Union[Unset, bool]): Defines whether all other organizations are permitted to
            access plugin by default.
            > Provide the `null` value to keep the current settings.
    """

    allow_organization_ids: Union[Unset, list[str]] = UNSET
    deny_organization_ids: Union[Unset, list[str]] = UNSET
    allow_organizations_by_default: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_organization_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allow_organization_ids, Unset):
            allow_organization_ids = self.allow_organization_ids

        deny_organization_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.deny_organization_ids, Unset):
            deny_organization_ids = self.deny_organization_ids

        allow_organizations_by_default = self.allow_organizations_by_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_organization_ids is not UNSET:
            field_dict["allowOrganizationIds"] = allow_organization_ids
        if deny_organization_ids is not UNSET:
            field_dict["denyOrganizationIds"] = deny_organization_ids
        if allow_organizations_by_default is not UNSET:
            field_dict["allowOrganizationsByDefault"] = allow_organizations_by_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_organization_ids = cast(list[str], d.pop("allowOrganizationIds", UNSET))

        deny_organization_ids = cast(list[str], d.pop("denyOrganizationIds", UNSET))

        allow_organizations_by_default = d.pop("allowOrganizationsByDefault", UNSET)

        update_plugin_organization_rules_request = cls(
            allow_organization_ids=allow_organization_ids,
            deny_organization_ids=deny_organization_ids,
            allow_organizations_by_default=allow_organizations_by_default,
        )

        update_plugin_organization_rules_request.additional_properties = d
        return update_plugin_organization_rules_request

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
