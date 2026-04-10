import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="Certificate")


@_attrs_define
class Certificate:
    """
    Attributes:
        issued_to (str): Subject of a certificate.
        issued_by (str): Certificate issuer.
        friendly_name (str): Certificate friendly name.
        thumbprint (str): Thumbprint.
        serial_number (str): Certificate serial number.
        expiration_date (datetime.datetime): Certificate expiration date.
    """

    issued_to: str
    issued_by: str
    friendly_name: str
    thumbprint: str
    serial_number: str
    expiration_date: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issued_to = self.issued_to

        issued_by = self.issued_by

        friendly_name = self.friendly_name

        thumbprint = self.thumbprint

        serial_number = self.serial_number

        expiration_date = self.expiration_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issuedTo": issued_to,
                "issuedBy": issued_by,
                "friendlyName": friendly_name,
                "thumbprint": thumbprint,
                "serialNumber": serial_number,
                "expirationDate": expiration_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issued_to = d.pop("issuedTo")

        issued_by = d.pop("issuedBy")

        friendly_name = d.pop("friendlyName")

        thumbprint = d.pop("thumbprint")

        serial_number = d.pop("serialNumber")

        expiration_date = isoparse(d.pop("expirationDate"))

        certificate = cls(
            issued_to=issued_to,
            issued_by=issued_by,
            friendly_name=friendly_name,
            thumbprint=thumbprint,
            serial_number=serial_number,
            expiration_date=expiration_date,
        )

        certificate.additional_properties = d
        return certificate

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
