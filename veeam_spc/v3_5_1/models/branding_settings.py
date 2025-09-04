from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.branding_settings_portal_color_theme import BrandingSettingsPortalColorTheme
from ..types import UNSET, Unset

T = TypeVar("T", bound="BrandingSettings")


@_attrs_define
class BrandingSettings:
    """
    Attributes:
        portal_color_theme (Union[Unset, BrandingSettingsPortalColorTheme]): Interface color scheme. Default:
            BrandingSettingsPortalColorTheme.BLUE.
    """

    portal_color_theme: Union[Unset, BrandingSettingsPortalColorTheme] = BrandingSettingsPortalColorTheme.BLUE
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        portal_color_theme: Union[Unset, str] = UNSET
        if not isinstance(self.portal_color_theme, Unset):
            portal_color_theme = self.portal_color_theme.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if portal_color_theme is not UNSET:
            field_dict["portalColorTheme"] = portal_color_theme

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _portal_color_theme = d.pop("portalColorTheme", UNSET)
        portal_color_theme: Union[Unset, BrandingSettingsPortalColorTheme]
        if isinstance(_portal_color_theme, Unset):
            portal_color_theme = UNSET
        else:
            portal_color_theme = BrandingSettingsPortalColorTheme(_portal_color_theme)

        branding_settings = cls(
            portal_color_theme=portal_color_theme,
        )

        branding_settings.additional_properties = d
        return branding_settings

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
