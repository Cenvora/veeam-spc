from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.public_cloud_appliance_connection_validation_error_type import (
    PublicCloudApplianceConnectionValidationErrorType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.certificate import Certificate


T = TypeVar("T", bound="PublicCloudApplianceConnectionValidationResult")


@_attrs_define
class PublicCloudApplianceConnectionValidationResult:
    """
    Attributes:
        error_type (PublicCloudApplianceConnectionValidationErrorType): Type of a Veeam Backup for Public Clouds
            appliance connection error.
        certificate_thumbprint (str): Thumbprint of a Veeam Backup for Public Clouds appliance security certificate.
        error_message (Union[Unset, str]): Error message for failed Veeam Backup for Public Clouds appliance connection.
        certificate (Union[Unset, Certificate]):
    """

    error_type: PublicCloudApplianceConnectionValidationErrorType
    certificate_thumbprint: str
    error_message: Union[Unset, str] = UNSET
    certificate: Union[Unset, "Certificate"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_type = self.error_type.value

        certificate_thumbprint = self.certificate_thumbprint

        error_message = self.error_message

        certificate: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.certificate, Unset):
            certificate = self.certificate.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "errorType": error_type,
                "certificateThumbprint": certificate_thumbprint,
            }
        )
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if certificate is not UNSET:
            field_dict["certificate"] = certificate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.certificate import Certificate

        d = dict(src_dict)
        error_type = PublicCloudApplianceConnectionValidationErrorType(d.pop("errorType"))

        certificate_thumbprint = d.pop("certificateThumbprint")

        error_message = d.pop("errorMessage", UNSET)

        _certificate = d.pop("certificate", UNSET)
        certificate: Union[Unset, Certificate]
        if isinstance(_certificate, Unset):
            certificate = UNSET
        else:
            certificate = Certificate.from_dict(_certificate)

        public_cloud_appliance_connection_validation_result = cls(
            error_type=error_type,
            certificate_thumbprint=certificate_thumbprint,
            error_message=error_message,
            certificate=certificate,
        )

        public_cloud_appliance_connection_validation_result.additional_properties = d
        return public_cloud_appliance_connection_validation_result

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
