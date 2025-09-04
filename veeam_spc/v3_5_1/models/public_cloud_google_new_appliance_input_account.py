from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PublicCloudGoogleNewApplianceInputAccount")


@_attrs_define
class PublicCloudGoogleNewApplianceInputAccount:
    """
    Attributes:
        account_uid (UUID): UID assigned to a Google Cloud account.
        data_center_id (str): ID assigned to a Google Cloud datacenter.
        availability_zone_id (str): ID assigned to an availability zone.
    """

    account_uid: UUID
    data_center_id: str
    availability_zone_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_uid = str(self.account_uid)

        data_center_id = self.data_center_id

        availability_zone_id = self.availability_zone_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountUid": account_uid,
                "dataCenterId": data_center_id,
                "availabilityZoneId": availability_zone_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_uid = UUID(d.pop("accountUid"))

        data_center_id = d.pop("dataCenterId")

        availability_zone_id = d.pop("availabilityZoneId")

        public_cloud_google_new_appliance_input_account = cls(
            account_uid=account_uid,
            data_center_id=data_center_id,
            availability_zone_id=availability_zone_id,
        )

        public_cloud_google_new_appliance_input_account.additional_properties = d
        return public_cloud_google_new_appliance_input_account

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
