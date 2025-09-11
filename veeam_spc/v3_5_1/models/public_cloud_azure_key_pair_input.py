from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PublicCloudAzureKeyPairInput")


@_attrs_define
class PublicCloudAzureKeyPairInput:
    """
    Attributes:
        connection_uid (UUID): UID assigned to a Microsoft Azure connection.
        subscription_id (str): ID assigned to a Microsoft Azure subscription.
        data_center_id (str): ID assigned to a Microsoft Azure datacenter.
        resource_group_name (str): Name of a resource group.
        key_pair_name (str): Name of a key pair.
    """

    connection_uid: UUID
    subscription_id: str
    data_center_id: str
    resource_group_name: str
    key_pair_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_uid = str(self.connection_uid)

        subscription_id = self.subscription_id

        data_center_id = self.data_center_id

        resource_group_name = self.resource_group_name

        key_pair_name = self.key_pair_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionUid": connection_uid,
                "subscriptionId": subscription_id,
                "dataCenterId": data_center_id,
                "resourceGroupName": resource_group_name,
                "keyPairName": key_pair_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection_uid = UUID(d.pop("connectionUid"))

        subscription_id = d.pop("subscriptionId")

        data_center_id = d.pop("dataCenterId")

        resource_group_name = d.pop("resourceGroupName")

        key_pair_name = d.pop("keyPairName")

        public_cloud_azure_key_pair_input = cls(
            connection_uid=connection_uid,
            subscription_id=subscription_id,
            data_center_id=data_center_id,
            resource_group_name=resource_group_name,
            key_pair_name=key_pair_name,
        )

        public_cloud_azure_key_pair_input.additional_properties = d
        return public_cloud_azure_key_pair_input

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
