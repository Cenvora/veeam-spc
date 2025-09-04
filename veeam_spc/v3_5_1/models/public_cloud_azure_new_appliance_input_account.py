from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_azure_environment_id import EAzureEnvironmentId

T = TypeVar("T", bound="PublicCloudAzureNewApplianceInputAccount")


@_attrs_define
class PublicCloudAzureNewApplianceInputAccount:
    """
    Attributes:
        connection_uid (UUID): UID assigned to a Microsoft Azure connection.
        environment (EAzureEnvironmentId): Type of a Microsoft Azure cloud environment.
        resource_group_name (str): Name of a resource group.
        subscription_id (str): ID assigned to a Microsoft Azure subscription.
        data_center_id (str): ID assigned to a Microsoft Azure datacenter.
        account_uid (UUID): UID assigned to an account in Microsoft Azure.
    """

    connection_uid: UUID
    environment: EAzureEnvironmentId
    resource_group_name: str
    subscription_id: str
    data_center_id: str
    account_uid: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_uid = str(self.connection_uid)

        environment = self.environment.value

        resource_group_name = self.resource_group_name

        subscription_id = self.subscription_id

        data_center_id = self.data_center_id

        account_uid = str(self.account_uid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionUid": connection_uid,
                "environment": environment,
                "resourceGroupName": resource_group_name,
                "subscriptionId": subscription_id,
                "dataCenterId": data_center_id,
                "accountUid": account_uid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection_uid = UUID(d.pop("connectionUid"))

        environment = EAzureEnvironmentId(d.pop("environment"))

        resource_group_name = d.pop("resourceGroupName")

        subscription_id = d.pop("subscriptionId")

        data_center_id = d.pop("dataCenterId")

        account_uid = UUID(d.pop("accountUid"))

        public_cloud_azure_new_appliance_input_account = cls(
            connection_uid=connection_uid,
            environment=environment,
            resource_group_name=resource_group_name,
            subscription_id=subscription_id,
            data_center_id=data_center_id,
            account_uid=account_uid,
        )

        public_cloud_azure_new_appliance_input_account.additional_properties = d
        return public_cloud_azure_new_appliance_input_account

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
