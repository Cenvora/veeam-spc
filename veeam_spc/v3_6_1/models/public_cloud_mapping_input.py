from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PublicCloudMappingInput")


@_attrs_define
class PublicCloudMappingInput:
    """
    Attributes:
        company_uid (UUID): UID assigned to a company.
        guest_os_credentials_uid (UUID): UID assigned to guest OS credentials record.
    """

    company_uid: UUID
    guest_os_credentials_uid: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_uid = str(self.company_uid)

        guest_os_credentials_uid = str(self.guest_os_credentials_uid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyUid": company_uid,
                "guestOsCredentialsUid": guest_os_credentials_uid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_uid = UUID(d.pop("companyUid"))

        guest_os_credentials_uid = UUID(d.pop("guestOsCredentialsUid"))

        public_cloud_mapping_input = cls(
            company_uid=company_uid,
            guest_os_credentials_uid=guest_os_credentials_uid,
        )

        public_cloud_mapping_input.additional_properties = d
        return public_cloud_mapping_input

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
