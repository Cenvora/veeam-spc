from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vb_365_microsoft_365_modern_authentication_with_legacy_protocols_common_connection_settings import (
        Vb365Microsoft365ModernAuthenticationWithLegacyProtocolsCommonConnectionSettings,
    )


T = TypeVar("T", bound="Vb365Microsoft365ModernAuthenticationWithLegacyProtocolsConnectionSettings")


@_attrs_define
class Vb365Microsoft365ModernAuthenticationWithLegacyProtocolsConnectionSettings:
    """
    Attributes:
        share_point_settings (Union[Unset,
            Vb365Microsoft365ModernAuthenticationWithLegacyProtocolsCommonConnectionSettings]):
        exchange_settings (Union[Unset,
            Vb365Microsoft365ModernAuthenticationWithLegacyProtocolsCommonConnectionSettings]):
    """

    share_point_settings: Union[
        Unset, "Vb365Microsoft365ModernAuthenticationWithLegacyProtocolsCommonConnectionSettings"
    ] = UNSET
    exchange_settings: Union[
        Unset, "Vb365Microsoft365ModernAuthenticationWithLegacyProtocolsCommonConnectionSettings"
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        share_point_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.share_point_settings, Unset):
            share_point_settings = self.share_point_settings.to_dict()

        exchange_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.exchange_settings, Unset):
            exchange_settings = self.exchange_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if share_point_settings is not UNSET:
            field_dict["sharePointSettings"] = share_point_settings
        if exchange_settings is not UNSET:
            field_dict["exchangeSettings"] = exchange_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vb_365_microsoft_365_modern_authentication_with_legacy_protocols_common_connection_settings import (
            Vb365Microsoft365ModernAuthenticationWithLegacyProtocolsCommonConnectionSettings,
        )

        d = dict(src_dict)
        _share_point_settings = d.pop("sharePointSettings", UNSET)
        share_point_settings: Union[
            Unset, Vb365Microsoft365ModernAuthenticationWithLegacyProtocolsCommonConnectionSettings
        ]
        if isinstance(_share_point_settings, Unset):
            share_point_settings = UNSET
        else:
            share_point_settings = (
                Vb365Microsoft365ModernAuthenticationWithLegacyProtocolsCommonConnectionSettings.from_dict(
                    _share_point_settings
                )
            )

        _exchange_settings = d.pop("exchangeSettings", UNSET)
        exchange_settings: Union[
            Unset, Vb365Microsoft365ModernAuthenticationWithLegacyProtocolsCommonConnectionSettings
        ]
        if isinstance(_exchange_settings, Unset):
            exchange_settings = UNSET
        else:
            exchange_settings = (
                Vb365Microsoft365ModernAuthenticationWithLegacyProtocolsCommonConnectionSettings.from_dict(
                    _exchange_settings
                )
            )

        vb_365_microsoft_365_modern_authentication_with_legacy_protocols_connection_settings = cls(
            share_point_settings=share_point_settings,
            exchange_settings=exchange_settings,
        )

        vb_365_microsoft_365_modern_authentication_with_legacy_protocols_connection_settings.additional_properties = d
        return vb_365_microsoft_365_modern_authentication_with_legacy_protocols_connection_settings

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
