from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.test_smtp_settings_response_result import TestSmtpSettingsResponseResult
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.response_error import ResponseError
    from ..models.smtp_server_certificate_info_type_0 import SmtpServerCertificateInfoType0
    from ..models.smtp_settings_type_0 import SmtpSettingsType0


T = TypeVar("T", bound="TestSmtpSettingsResponse")


@_attrs_define
class TestSmtpSettingsResponse:
    """
    Attributes:
        result (TestSmtpSettingsResponseResult):
        smtp_settings (Union['SmtpSettingsType0', None, Unset]):
        server_certificate (Union['SmtpServerCertificateInfoType0', None, Unset]): Server X509 certificate information.
        error (Union[Unset, ResponseError]):
    """

    result: TestSmtpSettingsResponseResult
    smtp_settings: Union["SmtpSettingsType0", None, Unset] = UNSET
    server_certificate: Union["SmtpServerCertificateInfoType0", None, Unset] = UNSET
    error: Union[Unset, "ResponseError"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.smtp_server_certificate_info_type_0 import SmtpServerCertificateInfoType0
        from ..models.smtp_settings_type_0 import SmtpSettingsType0

        result = self.result.value

        smtp_settings: Union[None, Unset, dict[str, Any]]
        if isinstance(self.smtp_settings, Unset):
            smtp_settings = UNSET
        elif isinstance(self.smtp_settings, SmtpSettingsType0):
            smtp_settings = self.smtp_settings.to_dict()
        else:
            smtp_settings = self.smtp_settings

        server_certificate: Union[None, Unset, dict[str, Any]]
        if isinstance(self.server_certificate, Unset):
            server_certificate = UNSET
        elif isinstance(self.server_certificate, SmtpServerCertificateInfoType0):
            server_certificate = self.server_certificate.to_dict()
        else:
            server_certificate = self.server_certificate

        error: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "result": result,
            }
        )
        if smtp_settings is not UNSET:
            field_dict["smtpSettings"] = smtp_settings
        if server_certificate is not UNSET:
            field_dict["serverCertificate"] = server_certificate
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.response_error import ResponseError
        from ..models.smtp_server_certificate_info_type_0 import SmtpServerCertificateInfoType0
        from ..models.smtp_settings_type_0 import SmtpSettingsType0

        d = dict(src_dict)
        result = TestSmtpSettingsResponseResult(d.pop("result"))

        def _parse_smtp_settings(data: object) -> Union["SmtpSettingsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_smtp_settings_type_0 = SmtpSettingsType0.from_dict(data)

                return componentsschemas_smtp_settings_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SmtpSettingsType0", None, Unset], data)

        smtp_settings = _parse_smtp_settings(d.pop("smtpSettings", UNSET))

        def _parse_server_certificate(data: object) -> Union["SmtpServerCertificateInfoType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_smtp_server_certificate_info_type_0 = SmtpServerCertificateInfoType0.from_dict(data)

                return componentsschemas_smtp_server_certificate_info_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SmtpServerCertificateInfoType0", None, Unset], data)

        server_certificate = _parse_server_certificate(d.pop("serverCertificate", UNSET))

        _error = d.pop("error", UNSET)
        error: Union[Unset, ResponseError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = ResponseError.from_dict(_error)

        test_smtp_settings_response = cls(
            result=result,
            smtp_settings=smtp_settings,
            server_certificate=server_certificate,
            error=error,
        )

        test_smtp_settings_response.additional_properties = d
        return test_smtp_settings_response

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
