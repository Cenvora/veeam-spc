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
        allow_organization_ids (Union[None, Unset, list[str]]): Array of IDs assigned to organizations that are
            permitted to access plugin.
        deny_organization_ids (Union[None, Unset, list[str]]): Array of IDs assigned to organizations that are not
            permitted to access plugin.
        allow_organizations_by_default (Union[None, Unset, bool]): Defines whether all other organizations are permitted
            to access plugin by default.
            > Provide the `null` value to keep the current settings.
    """

    allow_organization_ids: Union[None, Unset, list[str]] = UNSET
    deny_organization_ids: Union[None, Unset, list[str]] = UNSET
    allow_organizations_by_default: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_organization_ids: Union[None, Unset, list[str]]
        if isinstance(self.allow_organization_ids, Unset):
            allow_organization_ids = UNSET
        elif isinstance(self.allow_organization_ids, list):
            allow_organization_ids = self.allow_organization_ids

        else:
            allow_organization_ids = self.allow_organization_ids

        deny_organization_ids: Union[None, Unset, list[str]]
        if isinstance(self.deny_organization_ids, Unset):
            deny_organization_ids = UNSET
        elif isinstance(self.deny_organization_ids, list):
            deny_organization_ids = self.deny_organization_ids

        else:
            deny_organization_ids = self.deny_organization_ids

        allow_organizations_by_default: Union[None, Unset, bool]
        if isinstance(self.allow_organizations_by_default, Unset):
            allow_organizations_by_default = UNSET
        else:
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

        def _parse_allow_organization_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allow_organization_ids_type_0 = cast(list[str], data)

                return allow_organization_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        allow_organization_ids = _parse_allow_organization_ids(d.pop("allowOrganizationIds", UNSET))

        def _parse_deny_organization_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                deny_organization_ids_type_0 = cast(list[str], data)

                return deny_organization_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        deny_organization_ids = _parse_deny_organization_ids(d.pop("denyOrganizationIds", UNSET))

        def _parse_allow_organizations_by_default(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        allow_organizations_by_default = _parse_allow_organizations_by_default(
            d.pop("allowOrganizationsByDefault", UNSET)
        )

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
