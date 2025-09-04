from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365Microsoft365ModernAppOnlyAuthenticationSharePointConnectionSettings")


@_attrs_define
class Vb365Microsoft365ModernAppOnlyAuthenticationSharePointConnectionSettings:
    """
    Attributes:
        share_point_save_all_web_parts (Union[Unset, bool]): Indicates whether the export mode for SharePoint Web Parts
            must be changed to back up a customized content of Microsoft SharePoint Online sites. Default: False.
        office_organization_name (Union[None, Unset, str]): Name of a Microsoft SharePoint Online organization in the
            following format: `<name>.onmicrosoft.com`.
            > Required only for an existing Azure AD application.
    """

    share_point_save_all_web_parts: Union[Unset, bool] = False
    office_organization_name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        share_point_save_all_web_parts = self.share_point_save_all_web_parts

        office_organization_name: Union[None, Unset, str]
        if isinstance(self.office_organization_name, Unset):
            office_organization_name = UNSET
        else:
            office_organization_name = self.office_organization_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if share_point_save_all_web_parts is not UNSET:
            field_dict["sharePointSaveAllWebParts"] = share_point_save_all_web_parts
        if office_organization_name is not UNSET:
            field_dict["officeOrganizationName"] = office_organization_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        share_point_save_all_web_parts = d.pop("sharePointSaveAllWebParts", UNSET)

        def _parse_office_organization_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        office_organization_name = _parse_office_organization_name(d.pop("officeOrganizationName", UNSET))

        vb_365_microsoft_365_modern_app_only_authentication_share_point_connection_settings = cls(
            share_point_save_all_web_parts=share_point_save_all_web_parts,
            office_organization_name=office_organization_name,
        )

        vb_365_microsoft_365_modern_app_only_authentication_share_point_connection_settings.additional_properties = d
        return vb_365_microsoft_365_modern_app_only_authentication_share_point_connection_settings

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
