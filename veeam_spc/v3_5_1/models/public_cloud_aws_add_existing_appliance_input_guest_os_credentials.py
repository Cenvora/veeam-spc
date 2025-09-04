from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudAwsAddExistingApplianceInputGuestOsCredentials")


@_attrs_define
class PublicCloudAwsAddExistingApplianceInputGuestOsCredentials:
    """
    Attributes:
        guest_os_credentials_uid (UUID): UID assigned to guest OS credentials record.
        certificate_thumbprint (Union[Unset, str]): Thumbprint of a Veeam Backup for Public Clouds appliance security
            certificate.
    """

    guest_os_credentials_uid: UUID
    certificate_thumbprint: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        guest_os_credentials_uid = str(self.guest_os_credentials_uid)

        certificate_thumbprint = self.certificate_thumbprint

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "guestOsCredentialsUid": guest_os_credentials_uid,
            }
        )
        if certificate_thumbprint is not UNSET:
            field_dict["certificateThumbprint"] = certificate_thumbprint

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        guest_os_credentials_uid = UUID(d.pop("guestOsCredentialsUid"))

        certificate_thumbprint = d.pop("certificateThumbprint", UNSET)

        public_cloud_aws_add_existing_appliance_input_guest_os_credentials = cls(
            guest_os_credentials_uid=guest_os_credentials_uid,
            certificate_thumbprint=certificate_thumbprint,
        )

        public_cloud_aws_add_existing_appliance_input_guest_os_credentials.additional_properties = d
        return public_cloud_aws_add_existing_appliance_input_guest_os_credentials

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
