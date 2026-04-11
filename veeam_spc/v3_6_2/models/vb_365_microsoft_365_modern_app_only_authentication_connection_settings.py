from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vb_365_microsoft_365_modern_app_only_authentication_exchange_connection_settings import (
        Vb365Microsoft365ModernAppOnlyAuthenticationExchangeConnectionSettings,
    )
    from ..models.vb_365_microsoft_365_modern_app_only_authentication_share_point_connection_settings import (
        Vb365Microsoft365ModernAppOnlyAuthenticationSharePointConnectionSettings,
    )


T = TypeVar("T", bound="Vb365Microsoft365ModernAppOnlyAuthenticationConnectionSettings")


@_attrs_define
class Vb365Microsoft365ModernAppOnlyAuthenticationConnectionSettings:
    """
    Attributes:
        configure_application (bool | None | Unset): Indicates whether Veeam Backup for Microsoft 365 can automatically
            assign the certificate and required permissions to the specified Azure AD application.
            > Required only for existing Azure AD application.
             Default: False.
        user_code (None | str | Unset): Device code.
        new_application_name (None | str | Unset): Name of an Azure AD application.
            > Required only when registering a new Azure AD applications.
        application_id (None | Unset | UUID): UID assigned to the application in Azure AD.
            > Required only for an existing Azure AD application.
        application_certificate (None | str | Unset): SSL certificate for Azure AD application access in the Base64
            format.
        application_certificate_password (None | str | Unset): Password for the SSL certificate.
        application_certificate_thumbprint (str | Unset): Application certificate thumbprint for a Microsoft 365
            organization.
        share_point_settings (Vb365Microsoft365ModernAppOnlyAuthenticationSharePointConnectionSettings | Unset):
        exchange_settings (Vb365Microsoft365ModernAppOnlyAuthenticationExchangeConnectionSettings | Unset):
    """

    configure_application: bool | None | Unset = False
    user_code: None | str | Unset = UNSET
    new_application_name: None | str | Unset = UNSET
    application_id: None | Unset | UUID = UNSET
    application_certificate: None | str | Unset = UNSET
    application_certificate_password: None | str | Unset = UNSET
    application_certificate_thumbprint: str | Unset = UNSET
    share_point_settings: Vb365Microsoft365ModernAppOnlyAuthenticationSharePointConnectionSettings | Unset = UNSET
    exchange_settings: Vb365Microsoft365ModernAppOnlyAuthenticationExchangeConnectionSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configure_application: bool | None | Unset
        if isinstance(self.configure_application, Unset):
            configure_application = UNSET
        else:
            configure_application = self.configure_application

        user_code: None | str | Unset
        if isinstance(self.user_code, Unset):
            user_code = UNSET
        else:
            user_code = self.user_code

        new_application_name: None | str | Unset
        if isinstance(self.new_application_name, Unset):
            new_application_name = UNSET
        else:
            new_application_name = self.new_application_name

        application_id: None | str | Unset
        if isinstance(self.application_id, Unset):
            application_id = UNSET
        elif isinstance(self.application_id, UUID):
            application_id = str(self.application_id)
        else:
            application_id = self.application_id

        application_certificate: None | str | Unset
        if isinstance(self.application_certificate, Unset):
            application_certificate = UNSET
        else:
            application_certificate = self.application_certificate

        application_certificate_password: None | str | Unset
        if isinstance(self.application_certificate_password, Unset):
            application_certificate_password = UNSET
        else:
            application_certificate_password = self.application_certificate_password

        application_certificate_thumbprint = self.application_certificate_thumbprint

        share_point_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.share_point_settings, Unset):
            share_point_settings = self.share_point_settings.to_dict()

        exchange_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.exchange_settings, Unset):
            exchange_settings = self.exchange_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configure_application is not UNSET:
            field_dict["configureApplication"] = configure_application
        if user_code is not UNSET:
            field_dict["userCode"] = user_code
        if new_application_name is not UNSET:
            field_dict["newApplicationName"] = new_application_name
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if application_certificate is not UNSET:
            field_dict["applicationCertificate"] = application_certificate
        if application_certificate_password is not UNSET:
            field_dict["applicationCertificatePassword"] = application_certificate_password
        if application_certificate_thumbprint is not UNSET:
            field_dict["applicationCertificateThumbprint"] = application_certificate_thumbprint
        if share_point_settings is not UNSET:
            field_dict["sharePointSettings"] = share_point_settings
        if exchange_settings is not UNSET:
            field_dict["exchangeSettings"] = exchange_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vb_365_microsoft_365_modern_app_only_authentication_exchange_connection_settings import (
            Vb365Microsoft365ModernAppOnlyAuthenticationExchangeConnectionSettings,
        )
        from ..models.vb_365_microsoft_365_modern_app_only_authentication_share_point_connection_settings import (
            Vb365Microsoft365ModernAppOnlyAuthenticationSharePointConnectionSettings,
        )

        d = dict(src_dict)

        def _parse_configure_application(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        configure_application = _parse_configure_application(d.pop("configureApplication", UNSET))

        def _parse_user_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_code = _parse_user_code(d.pop("userCode", UNSET))

        def _parse_new_application_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_application_name = _parse_new_application_name(d.pop("newApplicationName", UNSET))

        def _parse_application_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                application_id_type_0 = UUID(data)

                return application_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        application_id = _parse_application_id(d.pop("applicationId", UNSET))

        def _parse_application_certificate(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        application_certificate = _parse_application_certificate(d.pop("applicationCertificate", UNSET))

        def _parse_application_certificate_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        application_certificate_password = _parse_application_certificate_password(
            d.pop("applicationCertificatePassword", UNSET)
        )

        application_certificate_thumbprint = d.pop("applicationCertificateThumbprint", UNSET)

        _share_point_settings = d.pop("sharePointSettings", UNSET)
        share_point_settings: Vb365Microsoft365ModernAppOnlyAuthenticationSharePointConnectionSettings | Unset
        if isinstance(_share_point_settings, Unset):
            share_point_settings = UNSET
        else:
            share_point_settings = Vb365Microsoft365ModernAppOnlyAuthenticationSharePointConnectionSettings.from_dict(
                _share_point_settings
            )

        _exchange_settings = d.pop("exchangeSettings", UNSET)
        exchange_settings: Vb365Microsoft365ModernAppOnlyAuthenticationExchangeConnectionSettings | Unset
        if isinstance(_exchange_settings, Unset):
            exchange_settings = UNSET
        else:
            exchange_settings = Vb365Microsoft365ModernAppOnlyAuthenticationExchangeConnectionSettings.from_dict(
                _exchange_settings
            )

        vb_365_microsoft_365_modern_app_only_authentication_connection_settings = cls(
            configure_application=configure_application,
            user_code=user_code,
            new_application_name=new_application_name,
            application_id=application_id,
            application_certificate=application_certificate,
            application_certificate_password=application_certificate_password,
            application_certificate_thumbprint=application_certificate_thumbprint,
            share_point_settings=share_point_settings,
            exchange_settings=exchange_settings,
        )

        vb_365_microsoft_365_modern_app_only_authentication_connection_settings.additional_properties = d
        return vb_365_microsoft_365_modern_app_only_authentication_connection_settings

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
