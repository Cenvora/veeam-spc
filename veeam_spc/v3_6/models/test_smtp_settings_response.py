from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.test_smtp_settings_response_result import TestSmtpSettingsResponseResult
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.response_error import ResponseError
    from ..models.smtp_server_certificate_info import SmtpServerCertificateInfo
    from ..models.smtp_settings import SmtpSettings


T = TypeVar("T", bound="TestSmtpSettingsResponse")


@_attrs_define
class TestSmtpSettingsResponse:
    """
    Attributes:
        result (TestSmtpSettingsResponseResult):
        smtp_settings (Union[Unset, SmtpSettings]):
        server_certificate (Union[Unset, SmtpServerCertificateInfo]): Server X509 certificate information.
        error (Union[Unset, ResponseError]):
    """

    result: TestSmtpSettingsResponseResult
    smtp_settings: Union[Unset, "SmtpSettings"] = UNSET
    server_certificate: Union[Unset, "SmtpServerCertificateInfo"] = UNSET
    error: Union[Unset, "ResponseError"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        result = self.result.value

        smtp_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.smtp_settings, Unset):
            smtp_settings = self.smtp_settings.to_dict()

        server_certificate: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.server_certificate, Unset):
            server_certificate = self.server_certificate.to_dict()

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
        from ..models.smtp_server_certificate_info import SmtpServerCertificateInfo
        from ..models.smtp_settings import SmtpSettings

        d = dict(src_dict)
        result = TestSmtpSettingsResponseResult(d.pop("result"))

        _smtp_settings = d.pop("smtpSettings", UNSET)
        smtp_settings: Union[Unset, SmtpSettings]
        if isinstance(_smtp_settings, Unset):
            smtp_settings = UNSET
        else:
            smtp_settings = SmtpSettings.from_dict(_smtp_settings)

        _server_certificate = d.pop("serverCertificate", UNSET)
        server_certificate: Union[Unset, SmtpServerCertificateInfo]
        if isinstance(_server_certificate, Unset):
            server_certificate = UNSET
        else:
            server_certificate = SmtpServerCertificateInfo.from_dict(_server_certificate)

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
