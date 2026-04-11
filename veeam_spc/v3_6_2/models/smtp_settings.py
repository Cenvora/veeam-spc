from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.smtp_settings_tls_mode import SmtpSettingsTlsMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.o_auth_2_credential import OAuth2Credential
    from ..models.smtp_settings_password_credential_type_0 import SmtpSettingsPasswordCredentialType0


T = TypeVar("T", bound="SmtpSettings")


@_attrs_define
class SmtpSettings:
    """
    Attributes:
        server_address (str): SMTP server URI containing protocol, host and port.
        tls_mode (SmtpSettingsTlsMode): Type of secure socket comminucation used to connect to an SMTP server.
        timeout (str): Connection timeout.
        password_credential (None | SmtpSettingsPasswordCredentialType0 | Unset): Credentials required to access an SMTP
            server.
        o_auth_2_credential (OAuth2Credential | Unset):
        exclusively_accepted_certificate_hash (None | str | Unset): Server X509 certificate hex-encoded hash in the
            `<hash-algorithm>:<hash-hex>` format.
    """

    server_address: str
    tls_mode: SmtpSettingsTlsMode
    timeout: str
    password_credential: None | SmtpSettingsPasswordCredentialType0 | Unset = UNSET
    o_auth_2_credential: OAuth2Credential | Unset = UNSET
    exclusively_accepted_certificate_hash: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.smtp_settings_password_credential_type_0 import SmtpSettingsPasswordCredentialType0

        server_address = self.server_address

        tls_mode = self.tls_mode.value

        timeout = self.timeout

        password_credential: dict[str, Any] | None | Unset
        if isinstance(self.password_credential, Unset):
            password_credential = UNSET
        elif isinstance(self.password_credential, SmtpSettingsPasswordCredentialType0):
            password_credential = self.password_credential.to_dict()
        else:
            password_credential = self.password_credential

        o_auth_2_credential: dict[str, Any] | Unset = UNSET
        if not isinstance(self.o_auth_2_credential, Unset):
            o_auth_2_credential = self.o_auth_2_credential.to_dict()

        exclusively_accepted_certificate_hash: None | str | Unset
        if isinstance(self.exclusively_accepted_certificate_hash, Unset):
            exclusively_accepted_certificate_hash = UNSET
        else:
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
        from ..models.smtp_settings_password_credential_type_0 import SmtpSettingsPasswordCredentialType0

        d = dict(src_dict)
        server_address = d.pop("serverAddress")

        tls_mode = SmtpSettingsTlsMode(d.pop("tlsMode"))

        timeout = d.pop("timeout")

        def _parse_password_credential(data: object) -> None | SmtpSettingsPasswordCredentialType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                password_credential_type_0 = SmtpSettingsPasswordCredentialType0.from_dict(data)

                return password_credential_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SmtpSettingsPasswordCredentialType0 | Unset, data)

        password_credential = _parse_password_credential(d.pop("passwordCredential", UNSET))

        _o_auth_2_credential = d.pop("oAuth2Credential", UNSET)
        o_auth_2_credential: OAuth2Credential | Unset
        if isinstance(_o_auth_2_credential, Unset):
            o_auth_2_credential = UNSET
        else:
            o_auth_2_credential = OAuth2Credential.from_dict(_o_auth_2_credential)

        def _parse_exclusively_accepted_certificate_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exclusively_accepted_certificate_hash = _parse_exclusively_accepted_certificate_hash(
            d.pop("exclusivelyAcceptedCertificateHash", UNSET)
        )

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
