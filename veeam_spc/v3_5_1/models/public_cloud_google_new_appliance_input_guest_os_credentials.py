from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudGoogleNewApplianceInputGuestOsCredentials")


@_attrs_define
class PublicCloudGoogleNewApplianceInputGuestOsCredentials:
    """
    Attributes:
        guest_os_credentials_uid (UUID): UID assigned to guest OS credentials record.
        time_zone_id (str): ID assigned to a time zone.
        ssh_public_key (Union[Unset, str]): SSH public key.
    """

    guest_os_credentials_uid: UUID
    time_zone_id: str
    ssh_public_key: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        guest_os_credentials_uid = str(self.guest_os_credentials_uid)

        time_zone_id = self.time_zone_id

        ssh_public_key = self.ssh_public_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "guestOsCredentialsUid": guest_os_credentials_uid,
                "timeZoneId": time_zone_id,
            }
        )
        if ssh_public_key is not UNSET:
            field_dict["sshPublicKey"] = ssh_public_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        guest_os_credentials_uid = UUID(d.pop("guestOsCredentialsUid"))

        time_zone_id = d.pop("timeZoneId")

        ssh_public_key = d.pop("sshPublicKey", UNSET)

        public_cloud_google_new_appliance_input_guest_os_credentials = cls(
            guest_os_credentials_uid=guest_os_credentials_uid,
            time_zone_id=time_zone_id,
            ssh_public_key=ssh_public_key,
        )

        public_cloud_google_new_appliance_input_guest_os_credentials.additional_properties = d
        return public_cloud_google_new_appliance_input_guest_os_credentials

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
