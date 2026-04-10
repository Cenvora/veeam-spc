from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PublicCloudMapping")


@_attrs_define
class PublicCloudMapping:
    """
    Attributes:
        appliance_uid (UUID): UID assigned to a Veeam Backup for Public Clouds appliance.
        company_uid (Union[None, UUID]): UID assigned to a company.
        guest_os_credentials_uid (Union[None, UUID]): UID assigned to guest OS credentials record.
    """

    appliance_uid: UUID
    company_uid: Union[None, UUID]
    guest_os_credentials_uid: Union[None, UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        appliance_uid = str(self.appliance_uid)

        company_uid: Union[None, str]
        if isinstance(self.company_uid, UUID):
            company_uid = str(self.company_uid)
        else:
            company_uid = self.company_uid

        guest_os_credentials_uid: Union[None, str]
        if isinstance(self.guest_os_credentials_uid, UUID):
            guest_os_credentials_uid = str(self.guest_os_credentials_uid)
        else:
            guest_os_credentials_uid = self.guest_os_credentials_uid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applianceUid": appliance_uid,
                "companyUid": company_uid,
                "guestOsCredentialsUid": guest_os_credentials_uid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        appliance_uid = UUID(d.pop("applianceUid"))

        def _parse_company_uid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                company_uid_type_0 = UUID(data)

                return company_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        company_uid = _parse_company_uid(d.pop("companyUid"))

        def _parse_guest_os_credentials_uid(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                guest_os_credentials_uid_type_0 = UUID(data)

                return guest_os_credentials_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        guest_os_credentials_uid = _parse_guest_os_credentials_uid(d.pop("guestOsCredentialsUid"))

        public_cloud_mapping = cls(
            appliance_uid=appliance_uid,
            company_uid=company_uid,
            guest_os_credentials_uid=guest_os_credentials_uid,
        )

        public_cloud_mapping.additional_properties = d
        return public_cloud_mapping

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
