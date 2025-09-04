from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365Microsoft365ModernAuthenticationWithLegacyProtocolsCommonConnectionSettings")


@_attrs_define
class Vb365Microsoft365ModernAuthenticationWithLegacyProtocolsCommonConnectionSettings:
    """
    Attributes:
        account (str): User name of an account with enabled MFA.
        password (str): Password of an account with enabled MFA.
        application_id (UUID): UID assigned to the Azure AD application that is used to access a Microsoft 365
            organization.
        grant_admin_access (Union[Unset, bool]): Indicates whether the `ApplicationImpersonation` role is assigned to an
            account. This role is required to back up Microsoft Exchange Online mailboxes.
            To assign the ApplicationImpersonation role, make sure the account that you use is a member of the Organization
            Management group and has been granted the Role Management role in advance.
             Default: False.
        application_secret (Union[Unset, str]): Application secret for the Azure AD application.
            > Use either `applicationSecret` or `applicationCertificate`.
        application_certificate (Union[Unset, str]): SSL certificate in the Base64 format that is used to access the
            Azure AD application.
            Use either `applicationSecret` or `applicationCertificate`.
        application_certificate_password (Union[Unset, str]): Password for the SSL certificate.
        application_certificate_thumbprint (Union[Unset, str]): Application certificate thumbprint for a Microsoft 365
            organization.
    """

    account: str
    password: str
    application_id: UUID
    grant_admin_access: Union[Unset, bool] = False
    application_secret: Union[Unset, str] = UNSET
    application_certificate: Union[Unset, str] = UNSET
    application_certificate_password: Union[Unset, str] = UNSET
    application_certificate_thumbprint: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account = self.account

        password = self.password

        application_id = str(self.application_id)

        grant_admin_access = self.grant_admin_access

        application_secret = self.application_secret

        application_certificate = self.application_certificate

        application_certificate_password = self.application_certificate_password

        application_certificate_thumbprint = self.application_certificate_thumbprint

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account": account,
                "password": password,
                "applicationId": application_id,
            }
        )
        if grant_admin_access is not UNSET:
            field_dict["grantAdminAccess"] = grant_admin_access
        if application_secret is not UNSET:
            field_dict["applicationSecret"] = application_secret
        if application_certificate is not UNSET:
            field_dict["applicationCertificate"] = application_certificate
        if application_certificate_password is not UNSET:
            field_dict["applicationCertificatePassword"] = application_certificate_password
        if application_certificate_thumbprint is not UNSET:
            field_dict["applicationCertificateThumbprint"] = application_certificate_thumbprint

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account = d.pop("account")

        password = d.pop("password")

        application_id = UUID(d.pop("applicationId"))

        grant_admin_access = d.pop("grantAdminAccess", UNSET)

        application_secret = d.pop("applicationSecret", UNSET)

        application_certificate = d.pop("applicationCertificate", UNSET)

        application_certificate_password = d.pop("applicationCertificatePassword", UNSET)

        application_certificate_thumbprint = d.pop("applicationCertificateThumbprint", UNSET)

        vb_365_microsoft_365_modern_authentication_with_legacy_protocols_common_connection_settings = cls(
            account=account,
            password=password,
            application_id=application_id,
            grant_admin_access=grant_admin_access,
            application_secret=application_secret,
            application_certificate=application_certificate,
            application_certificate_password=application_certificate_password,
            application_certificate_thumbprint=application_certificate_thumbprint,
        )

        vb_365_microsoft_365_modern_authentication_with_legacy_protocols_common_connection_settings.additional_properties = d
        return vb_365_microsoft_365_modern_authentication_with_legacy_protocols_common_connection_settings

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
