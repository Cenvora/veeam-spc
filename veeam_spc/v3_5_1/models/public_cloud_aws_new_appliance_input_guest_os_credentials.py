from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PublicCloudAwsNewApplianceInputGuestOsCredentials")


@_attrs_define
class PublicCloudAwsNewApplianceInputGuestOsCredentials:
    """
    Attributes:
        guest_os_credentials_uid (UUID): UID assigned to guest OS credentials record.
        key_pair_name (str): Name of a key pair.
        time_zone_id (str): ID assigned to a time zone.
    """

    guest_os_credentials_uid: UUID
    key_pair_name: str
    time_zone_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        guest_os_credentials_uid = str(self.guest_os_credentials_uid)

        key_pair_name = self.key_pair_name

        time_zone_id = self.time_zone_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "guestOsCredentialsUid": guest_os_credentials_uid,
                "keyPairName": key_pair_name,
                "timeZoneId": time_zone_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        guest_os_credentials_uid = UUID(d.pop("guestOsCredentialsUid"))

        key_pair_name = d.pop("keyPairName")

        time_zone_id = d.pop("timeZoneId")

        public_cloud_aws_new_appliance_input_guest_os_credentials = cls(
            guest_os_credentials_uid=guest_os_credentials_uid,
            key_pair_name=key_pair_name,
            time_zone_id=time_zone_id,
        )

        public_cloud_aws_new_appliance_input_guest_os_credentials.additional_properties = d
        return public_cloud_aws_new_appliance_input_guest_os_credentials

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
