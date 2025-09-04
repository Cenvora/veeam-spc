from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PublicCloudAwsAddExistingApplianceInputAccount")


@_attrs_define
class PublicCloudAwsAddExistingApplianceInputAccount:
    """
    Attributes:
        connection_uid (UUID): UID assigned to an Amazon connection.
        data_center_id (str): ID assigned to an AWS datacenter.
        region_id (str): ID assigned to an AWS region.
        account_uid (UUID): UID assigned to an account in AWS.
    """

    connection_uid: UUID
    data_center_id: str
    region_id: str
    account_uid: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_uid = str(self.connection_uid)

        data_center_id = self.data_center_id

        region_id = self.region_id

        account_uid = str(self.account_uid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionUid": connection_uid,
                "dataCenterId": data_center_id,
                "regionId": region_id,
                "accountUid": account_uid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection_uid = UUID(d.pop("connectionUid"))

        data_center_id = d.pop("dataCenterId")

        region_id = d.pop("regionId")

        account_uid = UUID(d.pop("accountUid"))

        public_cloud_aws_add_existing_appliance_input_account = cls(
            connection_uid=connection_uid,
            data_center_id=data_center_id,
            region_id=region_id,
            account_uid=account_uid,
        )

        public_cloud_aws_add_existing_appliance_input_account.additional_properties = d
        return public_cloud_aws_add_existing_appliance_input_account

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
