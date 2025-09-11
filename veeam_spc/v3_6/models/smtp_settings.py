from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.smtp_settings_tls_mode import SmtpSettingsTlsMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.o_auth_2_credential import OAuth2Credential
    from ..models.smtp_settings_password_credential import SmtpSettingsPasswordCredential


T = TypeVar("T", bound="SmtpSettings")


@_attrs_define
class SmtpSettings:
    """
    Attributes:
        server_address (str): SMTP server URI containing protocol, host and port.
        tls_mode (SmtpSettingsTlsMode): Type of secure socket comminucation used to connect to an SMTP server.
        timeout (str): Connection timeout.
        password_credential (Union[Unset, SmtpSettingsPasswordCredential]): Credentials required to access an SMTP
            server.
        o_auth_2_credential (Union[Unset, OAuth2Credential]):
        exclusively_accepted_certificate_hash (Union[Unset, str]): Server X509 certificate hex-encoded hash in the
            `<hash-algorithm>:<hash-hex>` format.
    """

    server_address: str
    tls_mode: SmtpSettingsTlsMode
    timeout: str
    password_credential: Union[Unset, "SmtpSettingsPasswordCredential"] = UNSET
    o_auth_2_credential: Union[Unset, "OAuth2Credential"] = UNSET
    exclusively_accepted_certificate_hash: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_address = self.server_address

        tls_mode = self.tls_mode.value

        timeout = self.timeout

        password_credential: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.password_credential, Unset):
            password_credential = self.password_credential.to_dict()

        o_auth_2_credential: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.o_auth_2_credential, Unset):
            o_auth_2_credential = self.o_auth_2_credential.to_dict()

        exclusively_accepted_certificate_hash = self.exclusively_accepted_certificate_hash

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serverAddress": server_address,
                "tlsMode": tls_mode,
                "timeout": timeout,
            }
        )
        if password_credential is not UNSET:
            field_dict["passwordCredential"] = password_credential
        if o_auth_2_credential is not UNSET:
            field_dict["oAuth2Credential"] = o_auth_2_credential
        if exclusively_accepted_certificate_hash is not UNSET:
            field_dict["exclusivelyAcceptedCertificateHash"] = exclusively_accepted_certificate_hash

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.o_auth_2_credential import OAuth2Credential
        from ..models.smtp_settings_password_credential import SmtpSettingsPasswordCredential

        d = dict(src_dict)
        server_address = d.pop("serverAddress")

        tls_mode = SmtpSettingsTlsMode(d.pop("tlsMode"))

        timeout = d.pop("timeout")

        _password_credential = d.pop("passwordCredential", UNSET)
        password_credential: Union[Unset, SmtpSettingsPasswordCredential]
        if isinstance(_password_credential, Unset):
            password_credential = UNSET
        else:
            password_credential = SmtpSettingsPasswordCredential.from_dict(_password_credential)

        _o_auth_2_credential = d.pop("oAuth2Credential", UNSET)
        o_auth_2_credential: Union[Unset, OAuth2Credential]
        if isinstance(_o_auth_2_credential, Unset):
            o_auth_2_credential = UNSET
        else:
            o_auth_2_credential = OAuth2Credential.from_dict(_o_auth_2_credential)

        exclusively_accepted_certificate_hash = d.pop("exclusivelyAcceptedCertificateHash", UNSET)

        smtp_settings = cls(
            server_address=server_address,
            tls_mode=tls_mode,
            timeout=timeout,
            password_credential=password_credential,
            o_auth_2_credential=o_auth_2_credential,
            exclusively_accepted_certificate_hash=exclusively_accepted_certificate_hash,
        )

        smtp_settings.additional_properties = d
        return smtp_settings

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
