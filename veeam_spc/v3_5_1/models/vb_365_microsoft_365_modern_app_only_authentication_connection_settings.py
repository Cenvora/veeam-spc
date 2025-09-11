from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
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
        configure_application (Union[Unset, bool]): Indicates whether Veeam Backup for Microsoft 365 can automatically
            assign the certificate and required permissions to the specified Azure AD application.
            > Required only for existing Azure AD application.
             Default: False.
        user_code (Union[Unset, str]): Device code.
        new_application_name (Union[Unset, str]): Name of an Azure AD application.
            > Required only when registering a new Azure AD applications.
        application_id (Union[Unset, UUID]): UID assigned to the application in Azure AD.
            > Required only for an existing Azure AD application.
        application_certificate (Union[Unset, str]): SSL certificate for Azure AD application access in the Base64
            format.
        application_certificate_password (Union[Unset, str]): Password for the SSL certificate.
        application_certificate_thumbprint (Union[Unset, str]): Application certificate thumbprint for a Microsoft 365
            organization.
        share_point_settings (Union[Unset, Vb365Microsoft365ModernAppOnlyAuthenticationSharePointConnectionSettings]):
        exchange_settings (Union[Unset, Vb365Microsoft365ModernAppOnlyAuthenticationExchangeConnectionSettings]):
    """

    configure_application: Union[Unset, bool] = False
    user_code: Union[Unset, str] = UNSET
    new_application_name: Union[Unset, str] = UNSET
    application_id: Union[Unset, UUID] = UNSET
    application_certificate: Union[Unset, str] = UNSET
    application_certificate_password: Union[Unset, str] = UNSET
    application_certificate_thumbprint: Union[Unset, str] = UNSET
    share_point_settings: Union[Unset, "Vb365Microsoft365ModernAppOnlyAuthenticationSharePointConnectionSettings"] = (
        UNSET
    )
    exchange_settings: Union[Unset, "Vb365Microsoft365ModernAppOnlyAuthenticationExchangeConnectionSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configure_application = self.configure_application

        user_code = self.user_code

        new_application_name = self.new_application_name

        application_id: Union[Unset, str] = UNSET
        if not isinstance(self.application_id, Unset):
            application_id = str(self.application_id)

        application_certificate = self.application_certificate

        application_certificate_password = self.application_certificate_password

        application_certificate_thumbprint = self.application_certificate_thumbprint

        share_point_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.share_point_settings, Unset):
            share_point_settings = self.share_point_settings.to_dict()

        exchange_settings: Union[Unset, dict[str, Any]] = UNSET
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
        configure_application = d.pop("configureApplication", UNSET)

        user_code = d.pop("userCode", UNSET)

        new_application_name = d.pop("newApplicationName", UNSET)

        _application_id = d.pop("applicationId", UNSET)
        application_id: Union[Unset, UUID]
        if isinstance(_application_id, Unset):
            application_id = UNSET
        else:
            application_id = UUID(_application_id)

        application_certificate = d.pop("applicationCertificate", UNSET)

        application_certificate_password = d.pop("applicationCertificatePassword", UNSET)

        application_certificate_thumbprint = d.pop("applicationCertificateThumbprint", UNSET)

        _share_point_settings = d.pop("sharePointSettings", UNSET)
        share_point_settings: Union[Unset, Vb365Microsoft365ModernAppOnlyAuthenticationSharePointConnectionSettings]
        if isinstance(_share_point_settings, Unset):
            share_point_settings = UNSET
        else:
            share_point_settings = Vb365Microsoft365ModernAppOnlyAuthenticationSharePointConnectionSettings.from_dict(
                _share_point_settings
            )

        _exchange_settings = d.pop("exchangeSettings", UNSET)
        exchange_settings: Union[Unset, Vb365Microsoft365ModernAppOnlyAuthenticationExchangeConnectionSettings]
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
