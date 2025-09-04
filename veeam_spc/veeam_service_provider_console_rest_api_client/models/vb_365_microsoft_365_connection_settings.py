from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vb_365_microsoft_365_basic_authentication_connection_settings import (
        Vb365Microsoft365BasicAuthenticationConnectionSettings,
    )
    from ..models.vb_365_microsoft_365_modern_app_only_authentication_connection_settings import (
        Vb365Microsoft365ModernAppOnlyAuthenticationConnectionSettings,
    )
    from ..models.vb_365_microsoft_365_modern_authentication_with_legacy_protocols_connection_settings import (
        Vb365Microsoft365ModernAuthenticationWithLegacyProtocolsConnectionSettings,
    )


T = TypeVar("T", bound="Vb365Microsoft365ConnectionSettings")


@_attrs_define
class Vb365Microsoft365ConnectionSettings:
    """
    Attributes:
        modern_app_only_authentication_settings (Union[Unset,
            Vb365Microsoft365ModernAppOnlyAuthenticationConnectionSettings]):
        modern_authentication_with_legacy_protocols_settings (Union[Unset,
            Vb365Microsoft365ModernAuthenticationWithLegacyProtocolsConnectionSettings]):
        basic_authentication_settings (Union[Unset, Vb365Microsoft365BasicAuthenticationConnectionSettings]):
    """

    modern_app_only_authentication_settings: Union[
        Unset, "Vb365Microsoft365ModernAppOnlyAuthenticationConnectionSettings"
    ] = UNSET
    modern_authentication_with_legacy_protocols_settings: Union[
        Unset, "Vb365Microsoft365ModernAuthenticationWithLegacyProtocolsConnectionSettings"
    ] = UNSET
    basic_authentication_settings: Union[Unset, "Vb365Microsoft365BasicAuthenticationConnectionSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        modern_app_only_authentication_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.modern_app_only_authentication_settings, Unset):
            modern_app_only_authentication_settings = self.modern_app_only_authentication_settings.to_dict()

        modern_authentication_with_legacy_protocols_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.modern_authentication_with_legacy_protocols_settings, Unset):
            modern_authentication_with_legacy_protocols_settings = (
                self.modern_authentication_with_legacy_protocols_settings.to_dict()
            )

        basic_authentication_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.basic_authentication_settings, Unset):
            basic_authentication_settings = self.basic_authentication_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if modern_app_only_authentication_settings is not UNSET:
            field_dict["modernAppOnlyAuthenticationSettings"] = modern_app_only_authentication_settings
        if modern_authentication_with_legacy_protocols_settings is not UNSET:
            field_dict["modernAuthenticationWithLegacyProtocolsSettings"] = (
                modern_authentication_with_legacy_protocols_settings
            )
        if basic_authentication_settings is not UNSET:
            field_dict["basicAuthenticationSettings"] = basic_authentication_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vb_365_microsoft_365_basic_authentication_connection_settings import (
            Vb365Microsoft365BasicAuthenticationConnectionSettings,
        )
        from ..models.vb_365_microsoft_365_modern_app_only_authentication_connection_settings import (
            Vb365Microsoft365ModernAppOnlyAuthenticationConnectionSettings,
        )
        from ..models.vb_365_microsoft_365_modern_authentication_with_legacy_protocols_connection_settings import (
            Vb365Microsoft365ModernAuthenticationWithLegacyProtocolsConnectionSettings,
        )

        d = dict(src_dict)
        _modern_app_only_authentication_settings = d.pop("modernAppOnlyAuthenticationSettings", UNSET)
        modern_app_only_authentication_settings: Union[
            Unset, Vb365Microsoft365ModernAppOnlyAuthenticationConnectionSettings
        ]
        if isinstance(_modern_app_only_authentication_settings, Unset):
            modern_app_only_authentication_settings = UNSET
        else:
            modern_app_only_authentication_settings = (
                Vb365Microsoft365ModernAppOnlyAuthenticationConnectionSettings.from_dict(
                    _modern_app_only_authentication_settings
                )
            )

        _modern_authentication_with_legacy_protocols_settings = d.pop(
            "modernAuthenticationWithLegacyProtocolsSettings", UNSET
        )
        modern_authentication_with_legacy_protocols_settings: Union[
            Unset, Vb365Microsoft365ModernAuthenticationWithLegacyProtocolsConnectionSettings
        ]
        if isinstance(_modern_authentication_with_legacy_protocols_settings, Unset):
            modern_authentication_with_legacy_protocols_settings = UNSET
        else:
            modern_authentication_with_legacy_protocols_settings = (
                Vb365Microsoft365ModernAuthenticationWithLegacyProtocolsConnectionSettings.from_dict(
                    _modern_authentication_with_legacy_protocols_settings
                )
            )

        _basic_authentication_settings = d.pop("basicAuthenticationSettings", UNSET)
        basic_authentication_settings: Union[Unset, Vb365Microsoft365BasicAuthenticationConnectionSettings]
        if isinstance(_basic_authentication_settings, Unset):
            basic_authentication_settings = UNSET
        else:
            basic_authentication_settings = Vb365Microsoft365BasicAuthenticationConnectionSettings.from_dict(
                _basic_authentication_settings
            )

        vb_365_microsoft_365_connection_settings = cls(
            modern_app_only_authentication_settings=modern_app_only_authentication_settings,
            modern_authentication_with_legacy_protocols_settings=modern_authentication_with_legacy_protocols_settings,
            basic_authentication_settings=basic_authentication_settings,
        )

        vb_365_microsoft_365_connection_settings.additional_properties = d
        return vb_365_microsoft_365_connection_settings

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
