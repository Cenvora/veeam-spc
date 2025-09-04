import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="SmtpSettingsType0ServerCertificateType0")


@_attrs_define
class SmtpSettingsType0ServerCertificateType0:
    """Server X509 certificate information.

    Attributes:
        friendly_name (str): Friendly name of a certificate.
        subject_name (str): Name of a certificate subject.
        issuer_name (str): Name of a certificate issuer.
        not_after (datetime.date): Expiration date of a certificate.
        not_before (datetime.date): Effective date of a certificate.
        serial_number (str): Serial number of a certificate.
        signature_algorithm (str): Signature algorithm of a certificate.
        hash_ (str): Certificate hex-encoded hash in the `<hash-algorithm>:<hash-hex>` format.
        is_valid (bool): Indicates whether a certificate is valid.
    """

    friendly_name: str
    subject_name: str
    issuer_name: str
    not_after: datetime.date
    not_before: datetime.date
    serial_number: str
    signature_algorithm: str
    hash_: str
    is_valid: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        friendly_name = self.friendly_name

        subject_name = self.subject_name

        issuer_name = self.issuer_name

        not_after = self.not_after.isoformat()

        not_before = self.not_before.isoformat()

        serial_number = self.serial_number

        signature_algorithm = self.signature_algorithm

        hash_ = self.hash_

        is_valid = self.is_valid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "friendlyName": friendly_name,
                "subjectName": subject_name,
                "issuerName": issuer_name,
                "notAfter": not_after,
                "notBefore": not_before,
                "serialNumber": serial_number,
                "signatureAlgorithm": signature_algorithm,
                "hash": hash_,
                "isValid": is_valid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        friendly_name = d.pop("friendlyName")

        subject_name = d.pop("subjectName")

        issuer_name = d.pop("issuerName")

        not_after = isoparse(d.pop("notAfter")).date()

        not_before = isoparse(d.pop("notBefore")).date()

        serial_number = d.pop("serialNumber")

        signature_algorithm = d.pop("signatureAlgorithm")

        hash_ = d.pop("hash")

        is_valid = d.pop("isValid")

        smtp_settings_type_0_server_certificate_type_0 = cls(
            friendly_name=friendly_name,
            subject_name=subject_name,
            issuer_name=issuer_name,
            not_after=not_after,
            not_before=not_before,
            serial_number=serial_number,
            signature_algorithm=signature_algorithm,
            hash_=hash_,
            is_valid=is_valid,
        )

        smtp_settings_type_0_server_certificate_type_0.additional_properties = d
        return smtp_settings_type_0_server_certificate_type_0

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
